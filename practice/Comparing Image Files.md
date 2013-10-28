---
title:  Comparing Image Files
layout: default
categories: [practice]
tags: [stub]
published: false
---

So, you're performing image conversions, say [TIFF-to-JPEG2000][1]. How do you check if it all went ok?

Well, you can run [JHOVE][2] or [jpylyzer][3] on the output, and that'll tell you if it's well-formed. But it doesn't look at the data, and [subtly malformed files might get past them][4]. Validation can catch many errors, but it can't catch them all (and they've [been missed before][5]).

So, to be really, totally, completely sure you've not lost anything, the only option is to save the JP2 out to disk, and then load it back in again along with the source image, and then go through each one and compare them, pixel by pixel.


Comparison Metrics
------------------

There's a few well-known metrics for this. One of the most ubiquitous is the [Peak Signal-to-Noise Ratio (PSNR)][6], which is relatively simple. More recent metrics include [SSIM][7] and [MSSSIM][8]. The choice of which is important really depends on your context, but in the case of lossless compression, their all pretty much equivalent.  But if you're using lossy compression, accurate evaluate of the difference is critical in order to ensure your decision to deliberately discard a small amount of detail is being implemented accurately.

In terms of implementation, the algorithms are all pretty similar. Go through each pixel, and perhaps each colour channel, and add up the difference multiplied by itself - the sum of the squared.  Then, take the total, and scale it down in proportion with the size of the image, and you get a stable metric of image quality.

It looks easy, and so the temptation is to just go ahead and build it from scratch. I did this, partially because no Java version, but there are a number of other subtlies, so I wanted to check against an existing implementation, like ImageMagick's compare.

And I couldn't get it to work. I got roughly the right answer, but instead of (say) 44.233 dB, I'd get 44.231 dB. Not a bit difference, but enough to unnerve. If I didn't understand where that error came from, how could I trust the results in general? 

I eventually tracked it down, and it turned out that adding up those differences isn't as easy as I though. It's actually really quite nasty in a very subtle way.

Because sometimes, adding up falls down.


Why Addition Fails
------------------

round-off error

60 MP image. Squaring the error.

1/((2^53)/(16*16*6567*9055))*6567*9055

1/((2^53)/(4*4*6567*9055/2))*6567*9055

So, adding very large numbers, so at say an average difference of 4, the average rounding error will be about 5.28148059e-8, i.e only one part in about 20 million. BUT this rounding error happens 60 million times, which leads to a significant underestimation of the total. Quite how the errors add up can be rather subtle, and depend on the nature of the distribution, but they can mean (for example) that only large errors are counted, and large numbers of small differences are ignored.

https://github.com/datascience/photohawk

https://github.com/openplanets/planets-suite/blob/master/services/java-se/src/main/java/eu/planets_project/services/java_se/image/JavaImageIOCompare.java#L180

colourspace kicker

Publicise. I couldn't find a Java version, so perhaps if I publicise this version, anyone wanting to do the same can learn from my mistakes.

https://github.com/ukwa/warc-explorer#wayback-player

[1]: 
[2]:
[3]: 
[4]: ../experiments/Understanding%20Tools%20and%20Formats%20Via%20Bitwise%20Analysis.html
