---
title: Defining Format
layout: default
category: "Format"
status: stub
publish: false
---

> __GOAL__
>
> The aim of this document is to unify the various meanings of format, from high-level specification down to data transmission protocols like LOAD and SAVE (see e.g. [ZX Spectrum tape format](http://www.zxshed.co.uk/sinclairfaq/index.php5?title=TAP_format)).
> 

> "This is all getting quite ontological. Is there an ultimate truth of formats?"
> https://twitter.com/digitalfay/status/519280317421461504


To Read
* <http://www.nybooks.com/blogs/nyrblog/2014/oct/21/escape-microsoft-word/>
* <https://themanual.org/read/issues/4/paul-ford/article>
* <http://www.digitalmeetsculture.net/article/focal-internationals-basic-guide-to-wrappers-files-and-formats/>

Format research notes, note that format version may refer to source/target s.w. rather than actual format version.

Introduction
------------

The idea of a digital data format is recognised as a crucial component in our effort to ensure we can preserve access to digital resources over time. Therefore, given it's central role in digital preservation, it is perhaps surprising that we do not share a consistent and complete definition of what format actually means[^1]. This lack of consensus is reflected in the answers this question on the [DP Q&A](http://qanda.digipres.org/) site from 2014: [What is a file format?](http://qanda.digipres.org/38/what-is-a-file-format)

At the time of writing, the answers to that question include or link to twelve definitions of format, which can be broadly grouped as follows:

1. *format-as-structure*
    * "A set of syntactic and semantic rules for mapping between an information model and a serialized bit stream." From JHOVE2, via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=123#a123)
    * "The internal structure and encoding of a digital object, which allows it to be processed, or to be rendered in human-accessible form." from PRONOM, via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=123#a123)
    * "File formats encode information into a form which can only be processed and rendered comprehensible by very specific combinations of hardware and software." from [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=103#a103)
    * "The organization of data within digital objects, usually designed to facilitate the storage, retrieval, processing, presentation and/or transmission of the data by software" from [INTERPARES](http://www.interpares.org/ip2/display_file.cfm?doc=ip2_glossary.pdf&%E2%81%9ECFID=1791938&CFTOKEN=29367639), via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=123#a123)
    * "Packages of information that can be stored as data files or sent via network as data streams (aka bitstreams, byte streams)." from [LoC](http://www.digitalpreservation.gov/formats/intro/format_eval_rel.shtml), via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=123#a123) 
    * "A byte-serialized encoding of an information model." from [the GDFR Ontology](http://web.archive.org/web/20110721203408/http://www.gdfr.info/docs/Ontology-v1-2003-03-10.pdf)
2. *format-as-structural-convention*
    * "A file format is a method of storing digital information in a computer file, allowing its later use by computer systems or people." from PRONOM, via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=94#a94)
    * "Set of structural conventions that define a wrapper, formatted data, and embedded metadata, and that can be followed to represent images, audiovisual waveforms, texts, etc., in a digital object. The wrapper component on its own is often colloquially called a file format." from FADGI, via [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=123#a123)
3. *format-as-chaos* (or rather *format-as-broken-conventions*)
    * "I would suggest that there is no good answer to this question, as much as we all would like there to be one. A "file format" can be defined by many things and can have a range of purposes." from [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=104#a104)
4. *format-as-software-behaviour*
    * "'saved as' file format [versus] 'open as' file format" from [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=44#a44)
5. *format-as-identifer*
    * "From my experience, the many people distinguish formats based on extensions. This means that people will distinguish a TSV from a CSV, but not an Excel ODS from an OpenOffice ODS or a PDF 1.3 from a PDF/A3." from [this answer](http://qanda.digipres.org/38/what-is-a-file-format?show=44#a44)
    * "Whatever The National Archive's DROID tool identifies?" from [the original question](http://qanda.digipres.org/38/what-is-a-file-format)

The first two groups contain quite formal definitions, and tend to focus on format quite literally, as the structure of the bitstream. Those in the second group also emphasis the fact that these structures reflect social conventions around the use of data. The third group also focuses on the nature of formats as social conventions, if in rather despairing tones. However, it is not immediately clear how to square them with the last two groups, focusing on software and identifiers.

Fortunately, it is possible to bring all of these definitions together in a form  [that is agnostic towards the preservation strategy](http://qanda.digipres.org/38/what-is-a-file-format?show=65#c65), and the perspective of *format-as-convention* is the key.


Format As Protocol
------------------

If we consider formats to serve as social conventions, or more precisely, as communication protocols, we can propose a definition of the form:

> A format is a protocol designed to allow the persistence and transmission of the run-time state of computer software.

This definition starts with the 'why', i.e. with the purpose of formats, rather than the 'what', because the 'what' depends on the context. But by considering how to achieve the 'why' in different contexts, the other definitions of format can be brought into the fold. This definition also indicates the nature of that context -- it's all about the software. 




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

To cope with this eventuality, there is an extremely common and long-standing convention for software to embed some kind of signature in the bytestreams it creates, so that it can recognise it's own data even when the contextual information has been lost. This is often done by using a special sequence of bytes at the start of the file, chosen so as to be unlikely to be used for anything else[^3].  This kind of special flags for identifying binary sequences are a kind of [in-band signalling](http://en.wikipedia.org/wiki/In-band_signaling), have [a long history](http://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_number_origin), and are commonly known as *"magic numbers"*.


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


[from FADGI, who make a break down digital resources as wrapper, bitstream, and metadata, and prefer to call only the former the format.]

Postel's Daemon
---------------

If we define formats in terms of their idealised form, as outlined in their specification with information models etc. we underestimate the complexity.

Crucially, Conventions can be broken. http://www.robweir.com/blog/2009/05/update-on-odf-spreadsheet-interoperability.html

Software read and write are always different.

Coping with being software, each one a coiled spring, 


### Coping with failed conventions ###

.conformsTo. versus distinctions like

- created by (`xmp:CreatorTool` from the [Extensible Metadata Platform (XMP) Schema](http://www.exiv2.org/tags-xmp-xmp.html), and also the `xmpMM:History` `softwareAgent` from the [XMP Media Management Schema](http://www.exiv2.org/tags-xmp-xmpMM.html))
- created for - formatted for target software
- created according to - formatted for a common specification 


### Dialects ###

c.f. CSV, TIFF proprietary tags.



Surveying Digital Resources
---------------------------


Data structures and the software that can read or write them are closely intertwined, and at a fundamental level, software defines the form and nature of those data structures in a way no mere documentation can ever match. But the full protocols that enable the use of those data structures are more reliant on the wider software and hardware environment. 

Are we really going to capture the history of a format. Look what's involved.
[MP3: The Meaning of a Format](http://www.dukeupress.edu/MP3/)

### Dependency Analysis ###

The fundamental goal is software dependency analysis. We need to know what software we need to access the file, but we may only have the bytestream and some metadata to go on.

Identifying Formats is one tactic for understanding software dependencies, but it is just the means, and not really an end in itself.

Postel's Law should probably get a nod at some point.

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

## NOTES

Bitstream, software association first.
Bitstream ensemble can depend on minutiae, so we can't get it right from the start. But we can split the tree as we need.

The bit streams we see depend only on the creation process. 
We can keep 'how does Y cope' separate.

Links to significant properties and format equivalence.
Crucially the right metrics for migration cannot be defined ahead of time, because they depend on the target format.


[^1]: You think 'format' is bad. 'Digital object' is much, much worse, but we'll come to that later.
[^2]: I should really try to add some kind of historical context here. When were file extensions first used, and so on.
[^3]: As for file extensions, is no central authority for allocating these identifiers, but as they are generally at least four characters long, collisions have been rare so far. Having said that, it is perhaps unsurprising that the length of these byte sequences has grown over time ([citation needed!] -- I should probably use the PRONOM data to verify that!)
