---
title: Obsolescence in the Web Archive
layout: default
categories: [practice]
tags: [stub]
publish: true
---

Looking for known 'difficult' formats, and breaking it down.

Investigate formats that have been identified as 'difficult' elsewhere. Are they present, what amount, and what can be done?

* Spectrum tape images.
* Difficult formats from NLA: http://www.nla.gov.au/content/preservation-intent-selective-web-harvesting
    * RealMedia (and it's many variations, identification issues)
    * VRML (logical superset option)
    * Shockwave / .dcr
    * Quicktime VR (identification challenge)
* The .pcd from Kodak image CDs to TIF or JPG via ImageMagick.

Linux:
* http://s-macke.github.io/jor1k/


Spectrum
--------

TODO Embed JSMESS, as playback mechanism.
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.tap%22&f[1]=content_ffb%3A%2213000000%22
bugfever.tap works in fuse.
http://jsmess.textfiles.com/
http://web.archive.org/web/19991001051504/http%3A%2F%2Fwkweb1.cableinet.co.uk%3A80%2Fmalkc%2FWheelie.tap
Also
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.sna%22 = 89 SNA
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.tzx%22 = 817 TZX
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.z80%22 = 134 Z80
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.tap%22 = 142 TAP


VRML
----
(vrml/wrl)

TODO Also implement VRML support, combining migration (vrml to x3d, meshlabserver or XSLT based) and emulation (or rather x3d to html+JavaScript)
http://cic.nist.gov/vrml/nistlogo_x3dom.html
Also 
http://www.webarchive.org.uk/aadda-discovery/formats?sort_by=solr_document&sort_order=DESC&f%5B0%5D=content_type_ext%3A%22.wrl%22 > 8000 WRL VRML 1 or 2/97

Shockwave
---------
Shockwave (.dcr)

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.dcr%22 = 7235 .dcr

Needs Shockwave player:
http://www.digitalpreservation.gov/formats/fdd/fdd000130.shtml

http://en.wikipedia.org/wiki/Adobe_Shockwave
 .DCR (Director Compressed Resource) files created using the authoring tool Adobe Director.

http://helpx.adobe.com/director/kb/common-questions-director.html#main_export

Director files are saved with the DIR extension and can be opened and edited on either the Macintosh or Windows platform from within Director. In addition once a file or project has been completed it can be saved as a DXR which is a read-only, uneditable version of the DIR. Director projectors are executable versions of a Director file. Projectors include the Director runtime engine inside and therefore do not require installation of a plug-in. Projectors have the extension EXE on Windows. On Macintosh, projectors have no extension by default. A DCR is a Shockwave version of a DIR published via Director. Director casts can be saved as a regular Director cast, CST, a protected Director cast, CXT, or a Shockwave cast, CCT. In addition Director can export to digital video: MOV on Macintosh and AVI or MOV on Windows computers.

Windows and Mac, still supported.
I installed v12/64it and an example played fine, in Chrome.
Linux:
http://askubuntu.com/questions/48140/compatible-version-of-adobe-shockwave-player
https://help.ubuntu.com/community/Shockwave

Note confusion with DCR

Quicktime VR
------------

http://fileformats.archiveteam.org/wiki/QuickTime#Quicktime_VR

http://192.168.1.206:8990/solr/jisc/select?q=content_type_ext%3A%22.mov%22&wt=xml&indent=true&fl=url&facet=true&facet.field=content_type&facet.mincount=1 = ONLY 8641 .MOV

Really not clear what this could be migrated into.

May be possible to extract and re-export
* http://wiki.panotools.org/QTVR
* https://groups.google.com/forum/#!topic/ptgui/MNOSwDXmdVQ
    * "if you only  own the QTVR  file  than  you have to transform it back to an equirectangular panorama I use for it on Mac the legendary  Cubic Converter"
    * http://wiki.panotools.org/CubicConverter
    * Have to pull from web archive...
    * http://web.archive.org/web/20120324184958/http://www.clickheredesign.com.au/cubicconverter/
* http://www.ptgui.com/

RealAudio & RealMedia
---------------------
(ram/rm/ra)

http://web.archive.org/web/19961101195522/http://netra.creative-labs.co.uk/

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.ra%22

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


Kodak Photo CD
---------------

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


eBooks
------
One (!) .epub, but given the date range...
http://www.acrobat-services.co.uk/drupa2008%20(9-8at14H35).epub




Music Files
-----------
.sib
http://web.archive.org/web/20010608070251/http://www.andys-music.co.uk/sibhtml/firstcontact.htm


SO, things like Music. 
We can support extension based search.
Finale .mus
Sibelius .sub
Music XML .mxl (or full type including schema)
May be possible to search PDF/JPGs by Generator, e.g.
*Finale*
etc.

