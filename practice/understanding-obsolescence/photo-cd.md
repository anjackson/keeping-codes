---
title: Kodak Photo CD
subtitle: .pcd
layout: default
category: Formats
status: stub
publish: true
---


* The .pcd from Kodak image CDs to TIF or JPG via ImageMagick.

Not many, if any.

http://192.168.1.206:8990/solr/jisc/select?q=content_type_ext%3A%22.pcd%22&wt=xml&indent=true

Three hits, only one a Kodak PCD
http://www-uxsup.csx.cam.ac.uk:80/netdoc/rfc/img0069.pcd
Identified as audio/mpeg by Tika, but ID ok with fffile.

opf:Downloads andy$ tika -m img0069.pcd 
Content-Length: 1048321
Content-Type: audio/mpeg
channels: 2
resourceName: img0069.pcd
samplerate: 48000
version: MPEG 3 Layer I Version 1
xmpDM:audioChannelType: Stereo
xmpDM:audioCompressor: MP3
xmpDM:audioSampleRate: 48000

c.f. http://siarchives.si.edu/blog/importance-original