---
title: On Compression of Digitized Material
layout: default
categories: [practice]
tags: [stub]
---

Tiff/Zip

Additional confusion, due to range of options, e.g. TIFF ZIP compression option, which is entirely separate from the notion of putting TIFs in a ZIP file.

https://twitter.com/benosteen/status/382469918270435328

You should have checksums and backups anyway, so why is a rare bit-flip worth the >30% increase in cost of storage? 
Add in zip's internal per-file CRC32 hash (weak but workable), and tampering/bit-flipping is trivial to spot.



http://www.pixmonix.com/myths/myth-TIFF-files-are-better.php

If you are doing extensive editing of your images that may require repeated opening, editing and resaving, you should work in a format that is lossless. However, most people don't need this, at least when working with images that Pixmonix returns after scanning your slides or negatives.

... 

File Size. The files are significantly larger than a very high quality JPEG for most images. For example, a 2000 PPI scan of 35mm film results in a TIFF file that is approximately 16MB in size. For most images, the resulting high-quality, full-sized JPEG files are 4-8MB. For 4000 PPI scans, TIFF files are approximately 60MB; full-sized JPEG files are 10-15MB. These smaller files are much easier to use. They take less disk space for stoarge (and backup) and open much more quickly in any program making use of the images.

