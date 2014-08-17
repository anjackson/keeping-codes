---
title:  Comparing Image Files
layout: default
category: Images
tags: [outline]
publish: true
---

So, you're performing image conversions, say [TIFF-to-JPEG2000][1]. For large collections (e.g. [JP2K@Wellcome][9]), this is a computationally intensive and long-winded process. How do you check if it all went okay?

Well, you can run [JHOVE][2] or [jpylyzer][3] on the output, and that'll tell you if it's well-formed. But it doesn't look at the data, and [subtly malformed files might get past them][4]. Validation can catch many errors, but it can't catch them all (and [they've been missed before][5]). This is particularly challenging if you're using one of the lossy modes of the JP2 format in order to save on storage cost, and what to check that the degree of loss is acceptable.

So, to be really, totally, completely sure about what you've lost, the only option is to save the JP2 out to disk, and then load it back in again along with the source image, and then go through each one and compare them, pixel by pixel. 


Comparison Metrics
------------------

There's a few well-known metrics for this. One of the most ubiquitous is the [Peak Signal-to-Noise Ratio (PSNR)][6], which is relatively simple. More recent metrics include [SSIM][7] and [MS-SSIM][8], which are intended to be more sensitive to changes a human observer would consider _significant_. The choice of which algorithm to employ really depends on your context. In the case of lossless compression, they're all pretty much equivalent, and you may as well use the simplest one (of the three mentioned above, that would be PSNR).  But if you're using lossy compression, appropriate evaluate of the difference is critical in order to ensure your decision to deliberately discard a small amount of detail is being implemented accurately.=


Adding Up
---------

In terms of implementation, the algorithms are all pretty similar. Go through each pixel, get the colour of that pixel from each image, and for each colour channel add up the difference, multiplied by itself - the sum of the squares.  Then, take the total, and scale it down in proportion with the size of the image and number of colour channels, and there's your metric of image quality.

It looks easy, and so the temptation is to just go ahead and build it from scratch. [I did this myself during the PLANETS project][10], partially because I couldn't find a suitable Java implementation. Developing my own version revealed a number of other subtlies, so I wanted to check against an existing implementation in order to test whether I was doing things right. I chose to use ImageMagick's compare, and ran the same pair of test images through both.

And I couldn't get it to work. I got _roughly_ the right answer, but instead of (say) 44.233 dB, I'd get 44.231 dB. Not a big difference, but enough to unnerve. If I didn't understand where that discrepancy came from, how could I trust the results in general? 

I eventually tracked down the problem, and it turned out that adding up those differences isn't as easy as I though. It's actually really quite nasty in a very subtle way. Because sometimes, adding up falls down.


Rounding Down
-------------

The process of adding up those small difference means we are performing many millions of additions. When processing digitised images, it is not unusual to need to process images over 20 mega-pixels in size. For greyscale images, that means 20 million additions, and for colour images this can mean 60 million addition operations.

The problem was that, without really thinking about it, I'd chosen to use a double precision floating-point variable to hold my total. This seems like a good idea, but [floating-point have a number of well-documented subtleties][11] which I'd neglected to consider (which is pretty embarrassing given I've taught this to Masters students before!).

15–17 significant decimal digits precision

I really don't understand why this didn't work! It should be integers!

AH, did the squaring introduce an error?! Or was it actually underflow, due to sum-of-squares exceeding 10^15?

SO, cannot reproduce the original error, but it seems it must NOT have been due to rounding, but due to the algorithm not being correct. Oh.

1/((2^53)/(16*16*6567*9055))*6567*9055

1/((2^53)/(4*4*6567*9055/2))*6567*9055

So, adding very large numbers, so at say an average difference of 4, the average rounding error will be about 5.28148059e-8, i.e only one part in about 20 million. BUT this rounding error happens 60 million times, which leads to a significant underestimation of the total. Quite how the errors add up can be rather subtle, and depend on the nature of the distribution, but they can mean (for example) that only large errors are counted, and large numbers of small differences are ignored.

https://github.com/datascience/photohawk

https://github.com/datascience/photohawk/blob/master/photohawk-image-evaluator/src/main/java/at/ac/tuwien/photohawk/evaluation/operation/metric/MSEMetric.java#L83

https://github.com/openplanets/planets-suite/blob/master/services/java-se/src/main/java/eu/planets_project/services/java_se/image/JavaImageIOCompare.java#L180

colourspace kicker

Publicise. I couldn't find a Java version, so perhaps if I publicise this version, anyone wanting to do the same can learn from my mistakes.


[1]: http://wiki.opf-labs.org/display/SP/SO31+Preservation+Grade+TIFF+to+JPEG2000+Migration
[2]: http://sourceforge.net/projects/jhove/
[3]: http://openplanetsfoundation.org/software/jpylyzer
[4]: ../experiments/Understanding%20Tools%20and%20Formats%20Via%20Bitwise%20Analysis.html
[5]: http://www.atlasofdigitaldamages.info/v1/migration-issues/migration-tiff-to-jpeg2000/
[6]: https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
[7]: https://en.wikipedia.org/wiki/SSIM
[8]: http://tdistler.com/iqa/algorithms.html
[9]: http://jpeg2000wellcomelibrary.blogspot.co.uk/
[10]: https://github.com/openplanets/planets-suite/blob/master/services/java-se/src/main/java/eu/planets_project/services/java_se/image/JavaImageIOCompare.java
[11]: http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
