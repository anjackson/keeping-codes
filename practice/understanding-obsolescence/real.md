---
title: RealAudio & RealMedia
subtitle: .ra .ram .rm
layout: default
category: Web Archives
status: stub
publish: true
---

Found in NLA, enquote?
RealMedia (and it's many variations, identification issues)

* http://web.archive.org/web/19961101195522/http://netra.creative-labs.co.uk/
* http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.ra%22

And RealAudio (early versions) and RealMedia (later versions)
FFB = .ra%FD for early versions.
1801 .ra http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.ra%22
audio/x-pn-realaudio; version=2.0 (1204)
application/vnd.rn-realmedia (268)
audio/x-pn-realaudio; version=1.0 (139)
124 .ra with audio/x-pn-realaudio; version=1.0
130 .ra with audio/x-pn-realaudio but no payload.
FFB .ra%FD (1343) .RMF (268) pnm: (39) rtsp (12)

For .rm: 
application/vnd.rn-realmedia (8094) Apply application/vnd.rn-realmedia filter
audio/x-pn-realaudio (6109)
FFB .RMF (8077), rtsp (6178)


For these, it seems ffmpeg can convert, so on the fly access is possible.

    $ ffmpeg -i roar.rm -f wav test.wav
    $ cat in | ffmpeg -i - -f wav > out
