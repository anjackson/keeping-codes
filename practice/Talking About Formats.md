---
title: Talking About Formats
layout: default
categories: [practice]
tags: [stub]
publish: true
permalink: /practice/talking-about-formats.html
---

In digital preservation, at the most basic level, we need to be able to associate digital resources with the software that is required to make the content accessible. Most commonly, this is achieve by identifying the format of a bitstream. Therefore, we need to be able to clearly and unambiguously talk about formats, and we must endeavour to ensure that this clarity persists over time.

Talking In PRONOM
-----------------

There are a few different formal frameworks for talking about formats, but the most well-known and well-respected one specifically aimed at digital preservation is PRONOM. But the interesting thing about PRONOM is that it is, in a sense, only half the language we need. We do get an explicit enumeration of 'nouns', but the 'grammar' that controls how those nouns should be applied is not explicitly defined.

At first, this looks straight-forward. When running the DROID command-line tool, the result of the identification is reported as in the 'Format' column. Similarly, in PREMIS, PRONOM format identifiers (PUIDs) are used to declare the &lt;premis:format> for a given bitstream. In summary, we might say our 'grammar' is simply:

    <bitstream> .hasFormat. <PUID>

All well and good.

Until you hit the edge cases.

### Multiple Matches ###

The first one that many of us have experience is when DROID can't give a single definitive answer, but instead returns multiple matching PUID. For example, until fairly recently, DROID new about TIFF versions 3, 4, 5 and 6, but could not distinguish between then, so when passed a TIFF, it returned them all. At this point, our initial grammar becomes ambiguous, because:

    <bitstream> .hasFormat. <fmt/7>
    <bitstream> .hasFormat. <fmt/8>
    <bitstream> .hasFormat. <fmt/9>
    <bitstream> .hasFormat. <fmt/10>

could be taken to mean either of:

    <bitstream> .hasFormat. ( <fmt/7> AND <fmt/8> AND <fmt/9> AND <fmt/10> )
    <bitstream> .hasFormat. ( <fmt/7> OR <fmt/8> OR <fmt/9> OR <fmt/10> )

In the context of the above discussion, we know that DROID cannot distinguish the distinct TIFF versions, so we know that the latter ('OR') is the case. However, it is easy to imagine cases where 'AND' might be useful. For example, a GeoTIFF is also a TIFF, and a DOCX is also a ZIP, and many file formats can also be interpreted as plain text. 


### Has Format? ###

However, there is another issue with using multiple results in this way. The implication of the .hasFormat. relationship is that this is a statement of an attribute of the bitstream. But while DROID is uncertain, the bitstream itself can definitely only be encoded in one version. If it's using TIFF 6 features, it is not a TIFF 3,
therefore the assertion that the bitstream .hasFormat. TIFF 3 is simply wrong. But if it is only using TIFF 3 features, then it can reasonably be said to be TIFF 3 AND 4 AND 5 AND 6, because each successive TIFF format was a superset of the previous version.

(NOTE I'm ignoring proprietary/odd tags right now, maybe add them in later).

Similarly, certain bitstreams can carefully constructed to be interpreted as multiple, unrelated formats. See PDF/JPG/etc example. 

This is not to say that .hasFormat. is necessarily bad - it may work well enough and it certainly covers the majority of cases. But if we stick to that notation, we will need to accept that it is an approximation and there will be some cases we simply can't capture.


### Beyond The Bitstream ###

[Should there be a Pronom ID for unidentifiable/unidentified?](http://qanda.digipres.org/181/should-there-be-pronom-id-for-unidentifiable-unidentified)

### Scaling Up ###

Note problem of limited PRONOM format language expressivity. .format.is versus expressions via mime type eg charset, encoding, codecs, versions


Extended MIME Types
-------------------

http://wiki.whatwg.org/wiki/Video_type_parameters
codecs
e.g. Quicktime VR example file = [ video/quicktime; codecs="cvid, pano" ]

version field already in use, e.g. Firefox Java plugins.

file extension based types already in use, e.g. Firefox: application/x-extension-EXT

We can add application/x-pronom-fmt-99, say.

### Combining MIME with PRONOM


### Hierarchy & Ambiguity


### Talking about Software


Conclusions
-----------

[What is a file format?](http://qanda.digipres.org/38/what-is-a-file-format)
