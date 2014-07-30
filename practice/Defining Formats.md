---
title: Defining Format
layout: default
categories: [practice]
tags: [stub]
publish: true
permalink: "defining-format.html"
---

> __GOAL__
>
> The aim of this document is to unify the various meanings of format, from high-level specification down to data transmission protocols like LOAD and SAVE (see e.g. [ZX Spectrum tape format](http://www.zxshed.co.uk/sinclairfaq/index.php5?title=TAP_format)).
> 


Introduction
------------

The idea of a digital data format is recognised as a crucial component in our effort to ensure we can preserve access to digital resources over time. Therefore, given it's central role in digital preservation, it is perhaps surprising that we do not share a consistent and complete definition of what format actually means[^1]. This lack of consensus is reflected in the answers this question on the [DP Q&A](http://qanda.digipres.org/) site from 2014: [What is a file format?](http://qanda.digipres.org/38/what-is-a-file-format)

At the time of writing, the answers to that question include or link to nine definitions of format. The more formal definitions tend to focus on format rather literally, as the structure of the bitstream, but some of the others make no mention of internal structure at all. Instead, the other definitions tend to define format as a method or convention. My contention is that, despite the dominance of the *format-as-structure* view, the *format-as-convention* approach is the key to bringing all these definitions together into a coherent whole. 

If we consider formats to serve as social conventions, or more precisely, as communication protocols, we can build a base definition that covers all cases:

> A format is a protocol designed to allow the persistence and transmission of the run-time state of computer software.

This definition starts with the 'why', with what formats are used for, rather than the 'what' because the 'what' depends on the context. But by considering how to achieve the 'why' in different contexts, the other other definitions of format can be brought into the fold. This definition also indicates the nature of that context -- it's all about the software. 


Protocols
---------

Data structures and the software that can read or write them are closely intertwined, and at a fundamental level, software defines the form and nature of those data structures in a way no mere documentation can ever match. But the full protocols that enable the use of those data structures are more reliant on the wider software and hardware environment. 

### Early Formats ###

Use ZX Spectrum tape format as an example, minimal variations of interpretation, payload very close to the hardware.

### Format Identifiers ###

Modern operating systems and networks want to support the use of a wide range of data and software, and do not wish to impose any kind of limits on what formats are supported. Therefore, they all provide ways of creating identifiers that act as links between the data and the software that understands it. This allows the system to manage the links without understanding the details.

The most common convention for linking format and software is the filename extension. It is endemic to modern computing[^2], and all major operating systems contain some kind of local registry that allows software applications to inform the operating system (and so the user) about the formats it supports. This simple protocol means that when as a user creates a new digital resource, the software they are using is able to save their work to disk in a way that ensure that file can be re-opened at a later date.
<!-- (lots of underlying stuff there about filesystems, persistence, etc.) -->

Prior to OS X, the Macintosh operating system used [Creator Codes](http://en.wikipedia.org/wiki/Creator_code) rather than file extensions (see also [Apple's old reference material](http://support.apple.com/kb/TA25699?viewlocale=en_US). However, since then, file extensions have been integrated into Apple's new file type identification system, the [Uniform Type Identifiers](http://en.wikipedia.org/wiki/Uniform_Type_Identifier). In this more general framework, file extensions are still used to determine format by default, but this can be overridden on a per-file basis, and applications can register the actions they support at various levels of the format [conformance hierarchy](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_conc/understand_utis_conc.html#//apple_ref/doc/uid/TP40001319-CH202-BCGJGJGA).

Out of the context of individual operating systems, perhaps the most widely used and well known format protocol is the MIME type system used by [email](http://en.wikipedia.org/wiki/MIME) and then [HTTP](http://www.w3.org/Protocols/rfc2616/rfc2616.html) (e.g. [the `Content-Type` header](http://www.w3.org/Protocols/rfc1341/4_Content-Type.html)) as the more generalised [Internet Media Types](http://en.wikipedia.org/wiki/Internet_media_type). In this case, the [IANA](http://www.iana.org/) maintain [a registry of media types](http://www.iana.org/assignments/media-types/media-types.xhtml), and coordinate the standardisation of new identifiers. The specification also includes a number of extension points for formats that do not require full standardisation. These identifiers are then used by various clients and servers to declare the type of content, and also to support more sophisticated operations like [content negotiation](http://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html).


### Magic Numbers ###

All these protocols necessarily rely on external factors for the persistence of these identifiers. File extensions (and any similar format information) are held as metadata on the filesystem, and for HTTP the `Content-Type` is in it's own header. This means this information can be lost or changed, accidentally or deliberately. User's might remove or change file extensions, or a server might be mis-configured to sent the wrong headers.

To cope with this eventuality, there is an extremely common and long-standing convention for software to embed some kind of signature in the bytestreams it creates, so that it can recognise it's own data even when the contextual information has been lost. This is often done by using a special sequence of bytes at the start of the file, chosen so as to be unlikely to be used for anything else[^3].  This kind of special flags for identifying binary sequences have [a long history](http://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_number_origin), and are commonly known as *"magic numbers"*.


* Expansion of load/save as a sub-protocol.
    - These conventions reflect the internal protocol in effect 
* Overview of the components of the protocol.
    - Linking bytestreams with the software that understands them, and vice versa (magic).
* How formats grow (structure and expansion)
* How formats have been shaped by wider environment:
    - device independence
    - Single Software, Single Platform
    - Multiple Software, Single Platform
    - Multiple Software, Multiple Platforms
    - Designing For The Future


- Formal Specification
- Standardisation

But these are exactly how formats evolve in order to ensure preservation.

That format survey, 20 years because these are the mature formats


Breaking Protocol
-----------------

If we define formats in terms of their idealised form, as outlined in their specification with information models etc. we underestimate the complexity.

Crucially, Conventions can be broken.

Software read and write are always different.

Coping with being software, each one a coiled spring, 


### Coping with failed conventions ###

.conformsTo. versus distinctions like

- created by (`xmp:CreatorTool` from the [Extensible Metadata Platform (XMP) Schema](http://www.exiv2.org/tags-xmp-xmp.html), and also the `xmpMM:History` `softwareAgent` from the [XMP Media Management Schema](http://www.exiv2.org/tags-xmp-xmpMM.html))
- created for - formatted for target software
- created according to - formatted for a common specification 


### Dialects ###

c.f. CSV, TIFF proprietary tags.


Are we really going to capture the history of a format. Look what's involved.
[MP3: The Meaning of a Format](http://www.dukeupress.edu/MP3/)


What Digital Preservation Needs
-------------------------------

The fundamental goal is software dependency analysis. We need to know what software we need to access the file, but we may only have the bytestream and some metadata to go on.

Identifying Formats is one tactic for understanding software dependencies, but it is just the means, and not really an end in itself.


### Exploiting Magic ###

Similarly, even where there is not a formalised header, there is often some kind of distinctive structure as a consequence of the fundamental structure and needs of the software that operates on those bytestreams, and so it is usually possible to invent an appropriate *signature* for identifying any bytestream format. 

Bytestream identification tools like DROID aggregate and exploit these so called *'magic numbers'* in order to make intelligent guesses about what software a bytestream requires. By combining external information (like file extensions) with  internal signatures like these, identification tools can reliably identify large numbers of formats.

#### Combining extensions with first bytes ####

... that thing.

http://www.webarchive.org.uk/aadda-discovery/formats?sort_by=solr_document&sort_order=ASC&f[0]=content_type_ext%3A%22.ppp%22&f[1]=content_ffb%3A%22d0cf11e0%22

### Associating Software With Formats ###

We also want to formats that depend on software

PRONOM also contains [a list of software](http://apps.nationalarchives.gov.uk/PRONOM/Software/proSoftwareSearch.aspx?status=listReport) and [associated vendors](http://apps.nationalarchives.gov.uk/PRONOM/Vendor/proVendorSearch.aspx?status=listReport), but mapped in at the format level rather than the instance



## Mixed Format Files ##

Despite their rather extreme nature, polyglots are not the most difficult to describe formats we might try to encompass with out format language.
HTML with JavaScript, etc.

Link to software feature dependency.




[^1]: You think 'format' is bad. 'Digital object' is much, much worse, but we'll come to that later.
[^2]: I should really try to add some kind of historical context here. When were file extensions first used, and so on.
[^3]: As for file extensions, is no central authority for allocating these identifiers, but as they are generally at least four characters long, collisions have been rare so far. Having said that, it is perhaps unsurprising that the length of these byte sequences has grown over time[^4].
[^4]: [citation needed!] -- I should probably use the PRONOM data to verify that!
