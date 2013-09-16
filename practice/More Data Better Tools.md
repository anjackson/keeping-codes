---
title: More Data, Better Tools
layout: default
---

We use Web Archive data to drive tool development.


Extended MIME Types
-------------------

http://wiki.whatwg.org/wiki/Video_type_parameters
codecs
e.g. Quicktime VR example file = [ video/quicktime; codecs="cvid, pano" ]


N.B. JISC: generator: 1,515,845
1,730,222
2,519,052
1,389,879
Now up to (on one core) 2,519,198
ACTUALLY 12,749,373

4,894,079 -> 318,824,400

http://192.168.45.10:8983/solr/aadda-discovery
http://192.168.1.152:8983/solr/jisc

Investigate formats

* Spectrum tape images.
* Difficult formats from NLA: http://www.nla.gov.au/content/preservation-intent-selective-web-harvesting
    * RealMedia (and it's many variations, identification issues)
    * VRML (logical superset option)
    * Shockwave / .dcr
    * Quicktime VR (identification challenge)
* The .pcd from Kodak image CDs to TIF or JPG via ImageMagick.



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

PCD
---

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

Mining for Signatures
---------------------
Starting with unidentified formats: http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type%3A%22application/octet-stream%22, we can script a series of queries for different extensions that attempt to build plausible signatures for each, based on the FFB. 

application/octet-stream: 146,541
null: 351,779 almost all OLE2 with a few ZIP.

11109 .s5, with P%000010 or L%000010 as FFB
5302 .ipx, with very similar FFB, sb%xx01/2/6
4394 .nwc, all with '[Not' with a few '[NWZ' FFB (http://www.noteworthysoftware.com/player/)
3822 .dbf, with mostly 'OPLD' FFB and some other similar binary ones.
2482 .adx, with largely no FFB?

### Psion 5 ###
Starting at 'application/octet-stream' the most common unknown extension was .s5 - this had consistent magic (two FFB variants).
* [psiconv](http://software.frodo.looijaard.name/psiconv/) may be able to extract info/text.
* [s5 Header Format](http://software.frodo.looijaard.name/psiconv/formats/Header_Section.html#Header Section)


Parse Error Analysis
====================

http://192.168.1.206:8990/solr/#/jisc/schema-browser?field=parse_error


Fuzzy Hash Analysis
===================

Need to show
* different content making the same hash?
* degree of change of a site over time, e.g. homepages.
* finding similar content across domains?

http://commons.apache.org/proper/commons-lang/javadocs/api-3.1/org/apache/commons/lang3/StringUtils.html#getLevenshteinDistance%28java.lang.CharSequence,%20java.lang.CharSequence,%20int%29

Data in warc-discovery/analysis-tools

www.york.ac.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.york.ac.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.amazon.co.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.amazon.co.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.bbc.co.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.bbc.co.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true

www.wales.gov.uk
http://192.168.1.206:8990/solr/jisc/select?q=url%3A%22http%3A%2F%2Fwww.wales.gov.uk%3A80%2F%22&sort=crawl_date+asc&rows=50&fl=ssdeep_hash_bs_*%2Ccrawl_date&wt=xml&indent=true


Works well for catching small changes in wales and york.  However, need to compare it with raw crypto hash of payload to see if the fuzzy has an advantage.

Case for the others is less clear, partially due to gaps in the record. Really need diffs/overlaps next to change graph.

Could also experiment with profiling location of edits to determine if changes are at top or bottom of the page.

 
