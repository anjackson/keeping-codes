---
title: What Do We Need? (part 2)
subtitle: Characterisation & Validation
layout: default
category: What We Need
status: stub
publish: true
---

A while ago...

> JHOVE "approaching the end of its life": sourceforge.net/p/jhove/bugs/5… Makes me wonder about long-term implications for its user community?
> https://twitter.com/bitsgalore/status/382085810796781568

More recently:

My first though was to see if an organisation like OPF would take on stewardship of the code, but a pithy tweet from dericed reminded me that there are some serious problems with our characterisation tools.

Firstly, there are too many of them. In terms of generic characterisation and validation tools, have JHOVE, JHOVE2, NZME and FITS, all of which are solely of interest to the digital preservation community AFAICT. For a small community under financial strain, this is a lot of code to look after. Furthermore, there are various problem with (and incompatabilities between) the various tools.

The problems with JHOVE:
- WELL FORMED v. valid means nothing outside of XML.
- Validation: Fast-Fail versus Lint.
- No apparent identification capability.

JHOVE wishlist
http://fileformats.wordpress.com/2013/02/01/future-jhove/
There are some parts of the PDF/A profile that Jhove do not check. A fact that worry some of our customers. For example “The data within content streams, and therefore the use of operators and the glyph descriptions of embedded fonts.” are not checked.

JHOVE2 sought to resolve some of these issues, but 

JHOVE2, complex Spring, hardcore BDB thing means checksums fail (Tika solved this using a stream), Reinvention of schematron for assertion, aggrefier is insufficient.
I need to know this is half a shape file, not 'unknown'.
"Clumps. Sets of source units that JHOVE2 knows how to characterize as a unit. These 
include GIS shapefiles, which consist of at least 3 files (with .shp, .shx, and .dbf 
extensions) possibly accompanied by other files"
Heavy reflection. Re-invents service/module management I think.
JHOVE2 uses BerkeleyDB JE as its persistence memory manager. = Death on a cluster.
Aggrefier - need to know X should be associated with Y, not 'unknown' if only X or Y is there.
Hooking definitions into code not really that good an idea.


NZME appears to be fine. I've not had much luck using it myself, and if you look at the open source project you'd think it was dead (although it apparently is not). The jFLAC audio format library was no longer being developed...

FITS seems pretty healthy at the moment,


Specialised Tools
-----------------

JHOVE JP2 module versus the jpylyzer stand-alone tool for JP2. Maintaining these tools to cover all fine-grained detail we desire is an awful lot of work. In general, we should probably expect to hand down to stand-alone tools that know even more, rather than re-implement things ourselves.

Apache PDFBox Preflight

HTML?! W3C validator.

Office Dependency Analysis, lost:
http://www.openplanetsfoundation.org/blogs/2012-02-01-dependency-discovery-tool-office-files-code-published
http://www.openplanetsfoundation.org/comment/242#comment-242


Beyond Digital Preservation
---------------------------

The case of PDFBox above hints at a broader truth - that there are other tools in use beyond the digital preservation community that are very similar to what we might want ourselves.

For me, the stand-out example is Apache Tika. It is... They have already been very welcoming of many minor modifications. Of course, our idea preservation tool might not match their use case, but even then we could gain a lot by being aligned. We could re-use the same ID and Parser plugin module system, and so no longer have to maintain our own. If we did set up a 'preservation-flavour' fork of Tika, any particularly useful or mature code may well be possible to contribute back again.

Certainly, the NZME and JHOVE systems are very similar in structure to Tika, and porting those over would be pretty straightforward. JHOVE2 modules a bit more cumbersome, in that they would require a little more work to wrap, but it's entirely possible. 

Like the FITS codebase, the remainder of JHOVE2 is focussed on invoking other tools. FITS attempts to resolve/expose apparent conflicts. These roles would remain unchanged, I imagine, but both could take advantage of Preservation Tika directly instead of wrapping JHOVE(2), NZME and Tika separately.

Personally, I thing the 'combining other tools' part of got JHOVE2 and FITS is very cumbersome. Mostly, I feel this way because Java is a very clunky language to do that kind of thing in - a scripting language like Python would be a much more natural fit. Furthermore, such close binding between the tools means that both JHOVE2 and FITS end up doing a degree of versioned dependency management, where leveraging the package manager of the host platform would be far more elegant. This would be difficult on Windows, but those users might be better supported by some kind of Virtual Machine appliance.

Identification Too
==================

* DROID need to know broken doc, not ???, similar with pdf and html etc.
    * https://twitter.com/britpunk80/status/387919425799606272

The problem with magic
- what the spec says versus what happens. In practice sig may need to account for variations 
- awkward to deal with non ASCII and encoding obscures
- sigs also need weighting which is relative to one another, which is odd in reg context 
- simple magic is often insufficient.
- some formats and versions variants can't be spotted with magic, you end up dropping into more complex schemes, so keeping it together is good

FOURCC

DFJustin
one thing that would be cool to see come out of this effort is some patches to file/libmagic, there is a lot of stuff out there it doesn't recognize
Development plans

RI and format needs

Unusual PDFs/JPEGs, truncated JP2s.
EOF signatures are nearer to validation.
Identification: FP v FN
- http://en.wikipedia.org/wiki/Sensitivity_and_specificity

Also, necessity of multi-pass means disambiguation is the order of the day.
Therefore, 'parent' (conformance heirarchy) relationships are critical to ensuring the right thing happens downstream. otherwise, tools are badly couples. TIFF example
(N puids) child process must declare N puids, but will miss false negatives (at that level of refinement)
One (vaguer) puid, child can declare that one puid.
Stronger e.g. is PDF, you can have a PDF generic sig, and versioned sigs. IF you allow the generic parent, then downstream analysis can cope even when there is a new format.
Strict Conformance Hierarchy would make this clear.


Related: [My quest to learn the Dvorak keyboard layout, the grand finale](http://arstechnica.com/gadgets/2014/04/my-quest-to-learn-the-dvorak-keyboard-layout-the-grand-finale/)

Related: [Misunderstanding Metadata](http://erikpiil.com/2014/07/08/misunderstanding-meta/)


Funding Open Source Tools
=========================

We have open source products, but no open source projects.

Why don't we work together? 

Disagree on architectural or technical issues that make them incompatible.
OR
Not used to pooling development?
OR
Not enough actual development effort, most users are users not devs so 'scratch your own itch' fails?





