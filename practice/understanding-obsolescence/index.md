---
title: Understanding Obsolescence
subtitle: In the Web Archive
layout: default
category: Web Archives
status: stub
publish: true
---

Introduction
------------

The goal is to looking for 'difficult' formats, formats that might be considered obsolete, and to dig deeper into what that means by examining some real examples. In particular, I want to understand how the affects the UK Web Archive -  are these formats present, how many are they, and what can be done?

Despite format obsolescences role as the long-standing bogeyman of digital preservation, modern examples of obsolescence seem few and far between, and the phenomenon itself seems poorly understood. TBA DSHR call, and current responses. TBA links to issues about what formats mean and what obsolescece means and whether it really occurs at all.

However, some have produced reports on formats that have presented challenges for access. The NLA has produced a summary of access concerns from their web archive [here](http://www.nla.gov.au/content/preservation-intent-selective-web-harvesting). The paper [Creating Preservation-Ready Web Resources (Smith08)][Smith08] also contains some examples of formats that rely on a range of access mechanisms (browser support, plugins, application software, etc.).

Here, I look at those formats, and also at others I've uncovered while exploring the UK Web Archive historical holdings, and attempt to document the access issues around each. 


---

So, I'm flattered that my Formats Over Time paper is mentioned in the File Format Action Plan part of the agenda, and I would also like to see more of that kind of information being made available. Therefore, my idea of an File Format Action Plan would include quite a lot of context as well as the proposed action(s). e.g.

* Set the context, e.g. how the particular format sits with respect to the overall format profile of the collection.
* Describe the problem, i.e. the nature and severity of the obsolescence including how you know it is causing problems with access.
* Description of the action options considered.
* Description of how the possible options have been evaluated, and how you will know the access problems have been resolved.
* Chosen action and details of it's implementation.

However, it's worth noting that 

Formats Found
-------------

* [VRML](vrml.html)
* [RealAudio & RealMedia](real.html)
* [Shockwave](shockwave.html)
* [Quicktime VR](quicktime-vr.html)
* [IPIX](ipix/)
* [Geometric description language](gsm.html)[^1]
* [DICOM Medical Imaging](dicom.html)[^1]
* [TIFF & XIF](tiffs.html)[^1]
* [PDF & FDF](pdfs.html)[^1]
* [Spectrum Snapshots & Tapes](spectrum.html)
* [Others](misc.html)
* [AppleWorks](appleworks.html)
* [eBooks](ebooks.html)
* [Lotus 1-2-3](lotus-1-2-3.html)
* [MIDI](midi.html)
* [MS Word](ms-word.html)
* [Quattro Pro](quattro-pro.html)
* [Serif PagePlus](serif-pageplus.html)
* [Sheet music](sheet-music.html)
* [Windows MetaFile](wmf.html)
* [Lotus 1-2-3](wordperfect.html)
* [WordStar](wordstar.html)

Notes
-----

Realistic examples, high-value but high-risk.

http://arstechnica.com/apple/2011/07/does-apple-still-care-about-creative-pros/ Legacy file support.
c.f. audio master tool plugins.

See also https://twitter.com/nonwrestler/status/524868838966308864

"webring" when did new sites stop happening?

Programming languages are often more highly version dependant (Python 3, Perl 6). But also difficult to spot, and not really the kind of thing where we'd transform on access.


See also http://rhizome.org/editorial/2014/feb/10/authenticity-access-digital-preservation-geocities/

Side note on format dynamics, e.g. PS v PDF and turing completeness makes consistent implementation verifiable in principle?

> "Parsimonious Preservation – (another) different approach to digital information management"
> http://www.thegreatbear.net/audio-transfer/parsimonious-preservation-approaches-information-management/#comment-12540

> "If you work in digital preservation then the term ‘significant properties’ will no doubt be familiar to you. The concept has been viewed as a hindrance due to being shrouded by foggy terminology, as well as a distinct impossibility because of the diversity of digital objects in the world which, like their analogue counterparts, cannot be universally generalised or reduced to a series of measurable characteristics."
>
> http://www.thegreatbear.net/audio-transfer/significant-properties-technical-challenges-digital-preservation/


> "Determining the significant properties of a digital object has been touted as a means to ensure a digital object’s authenticity over time (Heslop, Davis, & Wilson, 2002). The appraisal process should include a consideration of a digital object’s essential attributes (Webb, 2003, p. 72), because they are indelibly linked to the asset’s value (Blue Ribbon Task Force, 2010, p. 21) and meaning over time (Heslop et al., 2002, p. 14). Notably, an understanding of the core features of a digital asset may aid media managers to choose an appropriate metadata schema (Hedstrom, Lee, Olson, & Lampe, 2006). - See more at: http://www.tameyourassets.com/what-are-significant-properties/#sthash.1NONPa8x.dpuf"
>
> http://www.tameyourassets.com/what-are-significant-properties/

There is a story: 
> "Adoption of XHTML on the web was essentially zero, except for those who were starting from XML to begin with."
> <small>http://www.slideshare.net/cavlec/the-sad-saga-of-xhtml-or-what-happens-when-markup-geeks-get-arrogant</small>


Linux:

* http://s-macke.github.io/jor1k/


> Do I know any blender folks? I have a blender 2.4 "game", and I need some help porting it to newer versions. I can pay.
> https://twitter.com/adamwwolf/status/532172039302680576


Interjection 
------------

Start here: [Transparent Format Migration of Preserved Web Content](http://www.dlib.org/dlib/january05/rosenthal/01rosenthal.html)

Contrast with [Studies on the scalability of web preservation](http://purl.pt/24107/1/iPres2013_PDF/Studies%20on%20the%20scalability%20of%20web%20preservation.pdf) - which seems to do everything at index time and proposed rebuilding the WARCs.

http://www.webarchive.org.uk/interject/

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

Formats By Volume
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



[Smith08]: http://www.dlib.org/dlib/january08/smith/01smith.html

[^1]: Formats from [Creating Preservation-Ready Web Resources](http://www.dlib.org/dlib/january08/smith/01smith.html)
