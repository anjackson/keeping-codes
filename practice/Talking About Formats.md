---
title: Talking About Formats
layout: default
categories: [practice]
tags: [outline]
publish: true
permalink: /practice/talking-about-formats.html
---

In digital preservation, at the most basic level, we need to be able to associate digital resources with the software that is required to make the content accessible. Most commonly, this is achieve by identifying the format of a bitstream. Therefore, we need to be able to clearly and unambiguously talk about formats, and we must endeavour to ensure that this clarity persists over time.

Talking In PRONOM
-----------------

There are a few different formal frameworks for talking about formats, but the most well-known and well-respected one intended for digital preservation is PRONOM. But the interesting thing about PRONOM is that it is, in a sense, only half the language we need. We do get an explicit enumeration of 'nouns', i.e. format definitions, but the 'grammar' that controls how those nouns should be applied is not explicitly defined.

At first, however, this looks straight-forward. When running the DROID command-line tool, the result of the identification is reported as in the 'Format' column. Similarly, in PREMIS, PRONOM format identifiers (PUIDs) are used to declare the &lt;premis:format> for a given bitstream. In summary, if we might say our 'grammar' is simply:

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

This way of handling similar formats often caused a lot of confusion, and so in the case of TIFF, the decision was taken to create a new generic TIFF PUID, and to deprecate the separate identifiers. However, the deprecation of PUIDs that have already been applied to many thousands of digital objects also [caused some consternation](http://www.openplanetsfoundation.org/blogs/2011-08-28-fmt-78910) [^1].

### Has Format? ###

However, there is another issue with using multiple results in this way. The implication of the .hasFormat. relationship is that this is a statement of an attribute of the bitstream. But while DROID is uncertain, the bitstream itself can definitely only be encoded in one version. If it's using TIFF 6 features, it is not a TIFF 3, therefore the assertion that the bitstream .hasFormat. TIFF 3 is simply wrong. But if it is only using TIFF 3 features, then it can reasonably be said to be TIFF 3 AND 4 AND 5 AND 6, because each successive TIFF format was a superset of the previous version.

(NOTE I'm ignoring proprietary/odd tags right now, maybe add them in later).

Similarly, certain bitstreams can carefully constructed to be interpreted as multiple, unrelated formats. See PDF/JPG/etc example. 

This is not to say that .hasFormat. is necessarily bad - it may work well enough and it certainly covers the majority of cases. But if we stick to that notation, we will need to accept that it is an approximation and there will be some cases we simply can't capture.


### Non-formats ###

There are also a number of other situations and classes of digital resource that we can come across during identification, and it is reasonable to ask whether a suitable format language should cover these. See for example this recent posting to the digital preservation Q&A site: [Should there be a PRONOM ID for unidentifiable/unidentified?](http://qanda.digipres.org/181/should-there-be-pronom-id-for-unidentifiable-unidentified)

As I stated in my answer to that question, there are a number of states beyond just 'unidentified' that it may be worth minting identifiers for, so we can talk about them. They include:

* Folders
* Empty files
* [Soft/symbolic links](http://en.wikipedia.org/wiki/Symbolic_link) 
* [Hard links](http://en.wikipedia.org/wiki/Hard_link)
* Various classes of [block device](http://en.wikipedia.org/wiki/Device_file)

The other answers to that question make it clear that the solution employed by PRONOM and DROID is to add a separate field for each case of interest. The PUIDs are only to be applied to bitstreams of non-zero length, while additional data fields are used to record whether something is a folder, or to record the length of the bitstream.

This is, of course, a perfectly reasonable approach. However, if we could design a format language that subsumes these additional fields into a single consistent explicit form, it will make it easier to communicate and preserve that information. 

### Comparing & Describing Tools ###

There are a range of tools that preform format identification, and it is very useful to be able to compare the results from different tools in order to work out how best to exploit or combine them. However, as only DROID uses PUIDs, see need a more general language in order to enable us to directly compare the results of different tools.

Similarly, we would like to be able to document which tools can read or write different formats. A richer format language would make it easier to describe tools and processes and make them discoverable.

### Scaling Up ###

Note problem of limited PRONOM format language expressivity. .format.is versus expressions via mime type eg charset, encoding, codecs, versions

Combinations. PRONOM has chr/1 identifiers, e.g. [UTF-8 is chr/1](http://apps.nationalarchives.gov.uk/pronom/chr/1)

Formats not yet in PRONOM.

A Extensible Format Identification Scheme
-----------------------------------------

To embed PRONOM in a language, but without cloning it, etc.

Not necessarily preservation language, but a lingua franca for the medium term. However, given results change, etc.

https://github.com/openplanets/scape-toolspecs

### Resolving The TIFF Troubles ###

Subclasses a.k.a Conformance Heirarchy. no need to deprecate

### The MIME Info Specification ###

http://www.freedesktop.org/wiki/Specifications/shared-mime-info-spec/

http://standards.freedesktop.org/shared-mime-info-spec/shared-mime-info-spec-latest.html#subclassing

### Extended MIME Types ###

http://wiki.whatwg.org/wiki/Video_type_parameters
codecs
e.g. Quicktime VR example file = [ video/quicktime; codecs="cvid, pano" ]

version field already in use, e.g. Firefox Java plugins.

file extension based types already in use, e.g. Firefox: application/x-extension-EXT

We can add application/x-pronom-fmt-99, say.

### Building on PRONOM ###

### Hierarchy & Ambiguity ###

Above in the tree is AND, below is OR.

### Formats With No PUID ###

That formats can be identified by EXT or new Version without significant risk in the medium term, so we can talk about new (or newly discovered) formats without waiting for PRONOM to mint an ID before we can say anything.

### Dialects ###

c.f. CSV

### Describing & Comparing Tools ###

This

### Associating Software With Formats ###

We also want to formats that depend on software

http://apps.nationalarchives.gov.uk/PRONOM/Software/proSoftwareSearch.aspx?status=listReport

http://apps.nationalarchives.gov.uk/PRONOM/Vendor/proVendorSearch.aspx?status=listReport


Issues
------

[What is a file format?](http://qanda.digipres.org/38/what-is-a-file-format)


[^1]: Some of the people involved in the discussions around this issue refer to it light-heartedly as "the TIFF tiff".
