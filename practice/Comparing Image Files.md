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

There's a few well-known metrics for this. One of the most ubiquitous is the [Peak Signal-to-Noise Ratio (PSNR)][6], which is relatively simple. More recent metrics include [SSIM][7] and [MSSSIM][8]. The choice of which is important really depends on your context, but in the case of lossless compression, their all pretty much equivalent.  But if you're using lossy compression, accurate evaluate of the difference is critical in order to ensure your decision to deliberately discard a small amount of detail is being implemented accurately.

In terms of implementation, the algorithms are all pretty similar. Go through each pixel, and perhaps each colour channel, and add up the differences.  Take the total, and scale it down in proportion with the size of the image, and you get a stable metric of image quality.

It looks easy, and so the temptation is to just go ahead and build it from scratch.

But it's not easy. It's actually really, really nasty in a very subtle way.

Because, well, sometimes, adding up falls down.


Why Addition Fails
------------------



colourspace kicker



https://github.com/datascience/photohawk

https://github.com/openplanets/planets-suite/blob/master/services/java-se/src/main/java/eu/planets_project/services/java_se/image/JavaImageIOCompare.java#L180

Publicise

https://github.com/ukwa/warc-explorer#wayback-player