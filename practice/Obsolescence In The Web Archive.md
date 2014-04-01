---
title: Obsolescence in the Web Archive
layout: default
categories: [practice]
tags: [stub]
publish: true
---

Looking for known 'difficult' formats, and breaking it down.

Of course, programming languages are often more highly version dependant (Python 3, Perl 6). But also difficult to spot, and not really the kind of thing where we'd transform on access.

Investigate formats that have been identified as 'difficult' elsewhere. Are they present, what amount, and what can be done?

* Spectrum tape images.
* Difficult formats from NLA: http://www.nla.gov.au/content/preservation-intent-selective-web-harvesting
    * RealMedia (and it's many variations, identification issues)
    * VRML (logical superset option, identification gap, version issues)
    * Shockwave / .dcr
    * Quicktime VR (identification challenge)
* The .pcd from Kodak image CDs to TIF or JPG via ImageMagick.

See also http://rhizome.org/editorial/2014/feb/10/authenticity-access-digital-preservation-geocities/

There is a story: 
> "Adoption of XHTML on the web was essentially zero, except for those who were starting from XML to begin with."
> <small>http://www.slideshare.net/cavlec/the-sad-saga-of-xhtml-or-what-happens-when-markup-geeks-get-arrogant</small>

Linux:
* http://s-macke.github.io/jor1k/

Interjection: http://www.webarchive.org.uk/interject/

Start here: http://www.dlib.org/dlib/january05/rosenthal/01rosenthal.html

[Deploying webp](http://www.igvita.com/2013/05/01/deploying-webp-via-accept-content-negotiation/) is similar, but still server-driven.

But add concept of agent-driven negociation. Turns out interjection is already in the spec.

* [RFC 2616: 300 Multiple Choices](https://tools.ietf.org/html/rfc2616#section-10.3.1) for redirect-based interaction.
* Fleshed out in [RFC 2295: 8.3 Alternates](http://tools.ietf.org/html/rfc2295#section-8.3)
    * [RFC 2295: 5.3 Source quality](http://tools.ietf.org/html/rfc2295#section-5.3)
    * Has explicit modes for "server chose this alternative" and "here's a list of alternatives" (200 TCN: choice, 300 TCN: list)
    * Even a rich and extensible 'feature' negotiation system, which links nicely to my concerns of features being more important than format version.
    * If Accepted formats are not available, use this with response code 406 Not Available

* See also [Mozilla Developer Network: Content negotiation](https://developer.mozilla.org/en-US/docs/Content_negotiation?redirect=no)

* See too ['Reactive' content negotiation: Empirical evidence that its status should be reconsidered in HTTPbis](http://www.ltg.ed.ac.uk/~ht/reactive_conneg.html)
> it calls "proactive negotiation" (formerly "server-driven negotiation"), but it intensifies its description of these from "disadvantages" to "serious disadvantages".

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

Cleaner to just use the FFB:
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_ffb%3A%222356524d%22

ID tools need to cover 1.0 versus 2.0. And then Interject needs to cope with 1.0 and all I can find is a Windows binary.

A list here, mostly dead:
http://www.web3d.org/pipermail/x3d-public_web3d.org/2012-February/001923.html

This dodgy thing seems to be the only option: http://www.interocitors.com/polyhedra/vr1tovr2/index.html

Other resources:

http://www.subdude-site.com/WebPages_Local/RefInfo/Computer/Linux/LinuxGuidesByBlaze/apps3Dtools/3D_viewers-converters/3D_vrml1_and_vrml2_notes.htm

This seems to be a good converter (Windows only AFAICT)
http://merlin.fit.vutbr.cz/wiki/index.php?title=Open_Inventor_Tools

VRML Plugin and Browser Detector
http://cic.nist.gov/vrml/vbdetect.html

http://www.cortona3d.com/cortona3dviewer

EXCELLENT:
http://castle-engine.sourceforge.net/view3dscene.php#section_converting


http://www.xj3d.org/tutorials/basic_applet.html


http://www.web3d.org/wiki/index.php/Player_support_for_X3D_components

http://www.subdude-site.com/WebPages_Local/RefInfo/Computer/Linux/LinuxGuidesByBlaze/apps3Dtools/3D_viewers-converters/3D_vrml1_and_vrml2_notes.htm

DROID distinguishes 1/97 (fmt/93 and fmt/94), but does not identify x3d.
Tika only knows VRML extension (not even that?!), but can be taught all.

VRML1 to VRML97
* http://www.cs.princeton.edu/~min/meshconv/

VRML97 to X3D
* http://www.x3dom.org/?page_id=532 etc. /Applications/Instant\ Player.app/Contents/MacOS/aopt --help
    * /Applications/Instant\ Player.app/Contents/MacOS/aopt -i penguin4.wrl -x penguin5-aopt.x3d
    * Works but proprietary and no commercial use allowed.
* meshlabserver.exe -i <wrl file> -o <x3d file> (no colour, just the mesh, it seems)
* Blender, c.f. http://auxmem.com/2012/01/24/convert-3ds-files-to-obj-with-blender/ script created and works.
* http://ovrt.nist.gov/v2_x3d.html seems to work and is simpler to integrate.

X3D to HTML
* X3DOM looks like a fairly simple wrap. http://www.x3dom.org/
* See http://x3dom.org/x3dom/example/blenderExport/horse-inline.html for an example of pulling in the X3D via URL

X3D to PNG
* http://castle-engine.sourceforge.net/view3dscene.php#section_screenshot
    * view3dscene my_model.wrl --screenshot 0 output.png
* http://www.niallmoody.com/heilan/
* http://libx3d.sourceforge.net/ 

Blender can't load VRML1, view3dscence can't convert, apparently (at least from CLI?)

Uh-oh, VRML can haz hyperlinks, of course, so https://twitter.com/archivetype/status/429004845102944256

So, maybe tweak so they are subtypes of text/plain and allow the text to be indexed?
Nah, it's only c. 10,000 so pull them out and look for links via WWWAnchor/Anchor.
- http://www.sv.vt.edu/classes/vrml/NCSA_VRML_Tutorial/examples/ThreeSpheresURL.wrl.txt
- http://graphcomp.com/info/specs/sgi/vrml/spec/part1/nodesRef.html#Anchor

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

c.f. http://siarchives.si.edu/blog/importance-original

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


WMF
---
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_full%3A%22application/x-msmetafile%22

9911 ish.

https://code.google.com/p/wmf2svg/

http://wvware.sourceforge.net/libwmf.html

https://en.wikipedia.org/wiki/Windows_Metafile

By Volume
---------
text/html (256325571) 
image/jpeg (14535000) 
image/gif (12793957) 
application/xhtml+xml (5558036) 
application/pdf (1587549) 
text/html\ (1064468) 
text/plain (871652) 
application/xml (438235) 
null (351819) 
image/png (331226) 
application/x-shockwave-flash (310464) 
text/htm (198320) 
application/octet-stream (146581) 
audio/x-pn-realaudio (146551) 
text-html (103136) 
application/rss+xml (88736) 
Mime-Type (70472) 
application/zip (67022) 
audio/mpeg (52611) 
application/x-dosexec (45544) 
application/x-gzip (41907) 
image/vnd.microsoft.icon (37987) 
text/xml (36627) 
application/rtf (34915) 
text/html charset=windows-1251 (32285) 
Office Supplies (29056) 
audio/midi (28669) 
application/postscript (27871) 
image/x-ms-bmp (27328) 
video/x-ms-wmv (23883) 
text/javascript (22523) 
text/xhtml (20133) 
application/x-msdownload (19115) 
text/html, charset=iso-8859-1 (18717) 
application/rdf+xml (17717) 
audio/x-ms-wax (16725) 
audio/x-wav (15722) 
application/x-javascript (13106) 
message/rfc822 (12054) 
image/x-xbitmap (10902) 
text/css (10839) 
audio/x-ms-wma (10349) 
application/x-msmetafile (9921) 
terxt/html (9365) 
application/java-vm (9325) 
application/atom+xml (8910) 
application/x-tex (8909) 
text/html charset=iso-8859-1 (8533) 
video/mpeg (8530) 
model/vrml (8489)

Quite a lot of MIDI
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22audio/midi%22
1996 example, Flip Player ok but QuickTime and VLC not.
Same for most recent example.
VLC can be modified to support it https://wiki.videolan.org/Midi
Server-side would be a lot easier.

https://github.com/beschulz/wav2png


Buggy Tika: 
http://web.archive.org/web/20020916061744/http://www.agentblonde.fsnet.co.uk:80/sounds/razorsedgev.wax

SO. wax not marked as isSpecializationOf in Tika sig file, so identification fails and text/plain wins.

coda
----

Realistic examples, high-value but high-risk.

http://arstechnica.com/apple/2011/07/does-apple-still-care-about-creative-pros/ Legacy file support.
c.f. audio master tool plugins.

"webring" when did new sites stop happening?

