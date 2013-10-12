---
title: What Do We Need
layout: default
categories: [practice]
tags: [stub]
---

The Registries We Need
======================

To go through

http://notepad.benfinoradin.info/2013/09/12/it-takes-a-village-to-save-a-hard-drive/

and other stories

And do consider what we truly need from our registries. What is achievable? What is helpful?

--
Now, go through and read it one more time, and think about how such a registry could actually have helped. What would it need to include?
--
Could it really replace the expertise of those five (or so) people? Or should its purpose be to capture and link what they have achieved?
--
Is the answer really in building registries? Or is it better to run more XFR STNs and help document and preserve what they do?
--
http://www.openplanetsfoundation.org/blogs/2013-09-13-registries-we-need
--

Could some research project, with some model knocked up to cover a vast problem space by some young researcher with very little experience actually doing digital preservation, ever, in any way, be expected to be sufficient expressive to cover this stuff?

Could any ontology or taxonomy ever be sophisticated enough to capture this process in a re-usable way? Even if that is possible, is the investment required to make it so even vagualy feasible?

---

And even if we could afford it, could we do it when we strip the heart out of it.

---

So, in that particular case, they need nothing. Their were people to ask. (loss sources, e.g. experience).

So, instead we can help preserve what they did. They started doing that anyway. We can do two things.  

1. Give it permanence.

2. Link it.

The latter is where the real added value might lie, linking it up, making it discoverable. How do we ensure anyone else who spots that port can find this story? How do we link these things.

This is just like authors and authority files. The purpose of which is not to stamp out ambiguity but to manage it. To collect aliases, and pick a preferred name, so that these stories can be brought together.

Who is actually doing digital preservation? And who of those is actually using or generating RepInfo as part of their job?

---
 
http://unsustainableideas.wordpress.com/2012/07/03/solve-file-format-problem/#respond
There is an issue about scope, and relation to other data stores, but I think you've jumped ahead too quickly. The problem is clearly stated: Make is possible to get the data out and re-use it. The solution will be whatever it takes to do that. Therefore, documentation, software and specification are liable to be in scope, but everything else will be driven by necessity. For me, the main attraction of this approach is that it will concentrate on whatever it takes to make it work, i.e. collect the data then model it flexibly. Not 

---

Software
--------

#JHOVE "approaching the end of its life": sourceforge.net/p/jhove/bugs/5… Makes me wonder about long-term implications for its user community?
https://twitter.com/bitsgalore/status/382085810796781568

OpenWayback

Talking About Formats
---------------------
Note problem of limited PRONOM format language expressivity. .format.is versus expressions via mime type eg charset, encoding, codecs, versions

### Extended MIME Types

http://wiki.whatwg.org/wiki/Video_type_parameters
codecs
e.g. Quicktime VR example file = [ video/quicktime; codecs="cvid, pano" ]

---

Poor mans technology watch

* RI - best stuff done outside of the iPres community. Largely due to lack of resources, rather than goodwill or skills.

That Endangerment Survey
------------------------

Accidentally submitted for form early.
Didn't understand the language about 'the factor'.
'Information become inaccessible.'
Features versus formats.
Accompanying documentation did not make the 'factor' thing clear.

The Tools We Need
=================

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

Aggrefier - need to know X should be associated with Y, not 'unknown' if only X or Y is there.

Format registry should ideally enumerate all distinct 'strains' - i.e. all implementations in all contexts. This is far too large a job to be required up-front. We need a way of recording format definitions that we can refine over time, to finer and finder granularity, but with as little unconsustentyly as possible. Accept we will make mistakes, but it should be possible to bake the granularity in so that later identifications are mostly consistent.
e.g. 
* application/octet-stream
* application/x-ext-jpg OR application/octet-stream; ext=jpg
* image/jpeg
* image/jpeg; v=1.01
* image/jpeg; v=1.01; xmp.creatorTool=adobe-photoshop-10.0;
* image/jpeg; v=1.01; xmp.creatorTool=adobe-photoshop-10.0; env=technical-environment-21

Validation: Fast-Fail versus Lint

Office Dependency Analysis, lost:
http://www.openplanetsfoundation.org/blogs/2012-02-01-dependency-discovery-tool-office-files-code-published
http://www.openplanetsfoundation.org/comment/242#comment-242


JHOVE wishlist
http://fileformats.wordpress.com/2013/02/01/future-jhove/
There are some parts of the PDF/A profile that Jhove do not check. A fact that worry some of our customers. For example “The data within content streams, and therefore the use of operators and the glyph descriptions of embedded fonts.” are not checked.


JHOVE2, complex Spring, hardcore BDB thing means checksums fail (Tika solved this using a stream), Reinvention of schematron for assertion, aggrefier is insufficient.
I need to know this is half a shape file, not 'unknown'.
"Clumps. Sets of source units that JHOVE2 knows how to characterize as a unit. These 
include GIS shapefiles, which consist of at least 3 files (with .shp, .shx, and .dbf 
extensions) possibly accompanied by other files"
Heavy reflection. Re-invents service/module management I think.
JHOVE2 uses BerkeleyDB JE as its persistence memory manager. = Death on a cluster.



