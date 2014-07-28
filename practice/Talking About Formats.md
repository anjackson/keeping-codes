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

There are a few different formal frameworks for talking about formats, but the most well-known and well-respected one intended for digital preservation is PRONOM. But the interesting thing about PRONOM is that it is, in a sense, only half the language we need. It gives us an explicit enumeration of 'nouns', i.e. format definitions, but the 'grammar' that controls how those nouns should be applied is not explicitly defined.

At first, however, this looks straight-forward. When running the DROID command-line tool, the result of the identification is reported as in the 'Format' column. Similarly, in PREMIS, PRONOM format identifiers (PUIDs) are used to declare the &lt;premis:format> for a given bitstream. In summary, if we might say our 'grammar' is simply:

    <bitstream> .hasFormat. <PUID>

All well and good.

Until you hit the edge cases.

### Multiple Matches ###

The most common edge case, which many of us have experience, is when DROID can't give a single definitive answer, but instead returns multiple matching PUIDs. For example, until fairly recently, PRONOM knew about TIFF versions [3](http://apps.nationalarchives.gov.uk/pronom/fmt/7), [4](http://apps.nationalarchives.gov.uk/pronom/fmt/8), [5](http://apps.nationalarchives.gov.uk/pronom/fmt/9) and [6](http://apps.nationalarchives.gov.uk/pronom/fmt/10), but DROID could not distinguish between then, so when passed a TIFF, it returned them all. At this point, our initial grammar becomes ambiguous, because:

    <bitstream> .hasFormat. <fmt/7>
    <bitstream> .hasFormat. <fmt/8>
    <bitstream> .hasFormat. <fmt/9>
    <bitstream> .hasFormat. <fmt/10>

could be taken to mean either of:

    <bitstream> .hasFormat.
        ( <fmt/7> AND <fmt/8> AND <fmt/9> AND <fmt/10> )

    <bitstream> .hasFormat. 
        ( <fmt/7> OR <fmt/8> OR <fmt/9> OR <fmt/10> )

In the context of the above discussion, we know that DROID cannot distinguish the distinct TIFF versions, so we might assume that the latter ('OR') is the case. However, it is easy to imagine cases where 'AND' might be useful. For example, a GeoTIFF is also a TIFF, and a DOCX is also a ZIP, and many file formats can also be interpreted as plain text.  Unless we extend the grammar, we cannot distinguish between these two cases.

This way of handling similar formats caused a lot of confusion, and so in in [2010 (see release 51)](http://www.nationalarchives.gov.uk/aboutapps/pronom/release-notes.xml) the decision was taken to create a new generic [TIFF PUID](http://apps.nationalarchives.gov.uk/pronom/fmt/353), and to deprecate the separate identifiers so that DROID would return only the new PUID. However, the deprecation of PUIDs that have already been applied to many thousands of digital objects also [caused some consternation ](http://www.openplanetsfoundation.org/blogs/2011-08-28-fmt-78910) [^1].

### Has Format? ###

Unfortunately, this decision to allow multiple matches also leads to deeper problems concerning the semantics of the `.hasFormat.` assertion. The implication of the .hasFormat. relationship is that this is a statement of an attribute of the bitstream. But while DROID may be uncertain, the bitstream itself can definitely only be encoded in one version of a format, which may or may not be compatible with other version. 

For example, if a bitstream uses TIFF 6 features, it is not a TIFF 3, therefore the assertion that the bitstream `.hasFormat.` TIFF 3 is simply wrong. But if it is only using TIFF 3 features, then it can reasonably be said to be TIFF 3 AND 4 AND 5 AND 6, because each successive TIFF format was a superset of the previous version. In short, the .hasFormat. approach cannot distinguish between DROID's uncertainty and format compatibility. 


### Polyglots ###

The notion of format compatibility can be stretched even further by trying to describe [polyglots](http://en.wikipedia.org/wiki/Polyglot_%28computing%29): bitstreams that are simultaneously interpretable as two or more distinct formats. Polyglots are most commonly designed to be interpreted as more than one programming language, but the concept is easily extended to binary data formats (sometimes referred to as "binary polyglots").

Examples include [this HTML file, which transcludes a copy of itself when rendered, but interpreted as a JPEG](http://lcamtuf.coredump.cx/squirrel/) (see [this discussion for more information](http://stackoverflow.com/questions/11587119/is-this-a-web-page-or-an-image)), and [this collection of carefully constructed polyglots](https://code.google.com/p/corkami/wiki/mix). The latter collection includes three files that are valid Windows, Linux and OS X binaries respectively, but where each of those binary executables is also a working PDF document, a Java Jar file (Zip + Class + manifest), and a HTML + JavaScript file. 


### Non-format Identifiers ###

There are also a number of other situations and classes of digital resource that we can come across during identification, and it is reasonable to ask whether a suitable format language should cover these. 

For example, a recent posting to the [digital preservation Q&A site](http://qanda.digipres.org/) explored whether there [should there be a PRONOM ID for unidentifiable/unidentified?](http://qanda.digipres.org/181/should-there-be-pronom-id-for-unidentifiable-unidentified). As I stated in my answer to that question, there are a number of states beyond just 'unidentified' that it may be worth minting identifiers for, so we can talk about them. They include:

* Folders
* Empty files
* [Soft/symbolic links](http://en.wikipedia.org/wiki/Symbolic_link) 
* [Hard links](http://en.wikipedia.org/wiki/Hard_link)
* Various classes of [block device](http://en.wikipedia.org/wiki/Device_file)

The other answers to that question make it clear that the solution employed by PRONOM and DROID is to add a separate field for each case of interest -- the PUIDs are only to be applied to bitstreams of non-zero length, while additional data fields are used to record whether something is a folder, or to record the length of the bitstream. 

This is, of course, a perfectly reasonable approach. However, if we could design a format language that subsumes these additional fields into a single consistent explicit form, it will make it easier to communicate and preserve that information. 


### Comparing & Describing Tools ###

There are a range of tools that perform format identification, and it is very useful to be able to compare the results from different tools in order to work out how best to exploit or combine them. However, as only DROID uses PUIDs, we need a more general language in order to enable us to directly compare the results of different tools.

Similarly, we would like to be able to document which tools can read or write different formats. A richer format language would make it easier to describe tools and processes and make them discoverable.


### Scaling Up ###

PRONOM's [PUIDs](http://www.nationalarchives.gov.uk/aboutapps/pronom/pdf/pronom_unique_identifier_scheme.pdf) are defined as a linear sequence of distinct identifiers, where each one must be manually created and assigned as new formats are identified, according to a [careful development process](http://www.nationalarchives.gov.uk/documents/information-management/pronom-file-signature-research.pdf). This provides a strong basis for formal identification, the architectural design of the identifiers and the process by which they are 'minted' can act as a bottleneck.

Firstly, this design means that if we restrict ourselves to using only PUIDs, we cannot talk about a format until a PUID has been minted for it. This may seem insurmountable, but in fact identifier schemes are often user-extensible. Windows developers are free to create new file extension associations, OS X developers are free to [declare new Uniform Type Identifiers](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_declare/understand_utis_declare.html#//apple_ref/doc/uid/TP40001319-CH204-SW1), and Internet Media Types provide [three different extension mechanisms](http://en.wikipedia.org/wiki/Internet_media_type#Vendor_tree).

Of course, it is perfectly reasonable not to mint permanent identifiers in these cases, but by embedding PUIDs in a more general format language we allow for a smooth transition to using formal permanent identifiers.

The second and more serious scaling issue for PUIDs is how we handle combinations of different aspects of format. If we take a MP4 video as an example, we know that just calling it an MP4 does not really tell us enough to interpret the object as MP4 is a container format. An MP4 can have any number of audio and video streams, each using one of a range of distinct codecs. If we imagine attempting to mint a separate PUID for every possible combination of codecs and streams, we would require a potentially massive number of distinct records, accelerating exponentially with the number of distinct encoding options. 

The case of text encodings is similar - creating distinct identifiers for each possible encoding for every plain text format would require many thousands of PUIDs. Given that PRONOM has a separate identifier sequence for character sets (e.g. [UTF-8 is chr/1](http://apps.nationalarchives.gov.uk/pronom/chr/1)) it would seem that the PRONOM designers recognised this issue, but the `chr/XXX` identifier namespace is not well known and the grammar by which these were intended to be combined with the format identifiers is not clear.


A Extensible Format Identification Scheme
-----------------------------------------

A number of the issues outlined above have been raised previously, along with proposals for possible solutions. They have generally taken the form of entirely new format registry designs and implementations, built by independent groups and then presented to the wider digital preservation community.  None, so far, have succeeded.

The reasons for this are not clear, but I would propose that one important omission has been the failure to adequately investigate who the actual users are. Critically, it has not been clear who will be spending their time filling these registries


Based on the issues identified above,  embed PRONOM in a language, but without cloning it, etc.

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

Current Implementation
----------------------

Link to Nanite

Issues
------

This is not to say that using `.hasFormat.` is necessarily a bad idea -- it certainly covers the majority of cases and so may be good enough. But if we stick to that notation, we will need to accept that it is an approximation and there will be some cases we simply can't capture.


[What is a file format?](http://qanda.digipres.org/38/what-is-a-file-format)

### Mixed Format Files ###

Despite their rather extreme nature, polyglots are not the most difficult to describe formats we might try to encompass with out format language.
HTML with JavaScript, etc.

Link to software feature dependency.

<!--
(NOTE I'm ignoring proprietary/odd tags right now, maybe add them in later).
-->


Footnotes
---------

[^1]: Some of the people involved in the discussions around this issue refer to it light-heartedly as "the TIFF tiff".
