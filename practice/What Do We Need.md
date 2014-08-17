---
title: What Do We Need
layout: default
category: Requirments
tags: [stub]
---

The Registries We Need
======================

To go through

http://notepad.benfinoradin.info/2013/09/12/it-takes-a-village-to-save-a-hard-drive/

and other stories

And do consider what we truly need from our registries. What is achievable? What is helpful?


Now, go through and read it one more time, and think about how such a registry could actually have helped. What would it need to include?

Could it really replace the expertise of those five (or so) people? Or should its purpose be to capture and link what they have achieved?

Is the answer really in building registries? Or is it better to run more XFR STNs and help document and preserve what they do?

http://www.openplanetsfoundation.org/blogs/2013-09-13-registries-we-need


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
I like this scenario, but I think we need to dig a little deeper and if you'll forgive me I'll play Devil's Advocate to do so.

You mention a format I'd never heard of ('Inset PIX'), so I go to Google and get straight to this excellent detailed summary (http://netghost.narod.ru/gff/graphics/summary/inset.htm) - job done, right? Does that mean that, as long as the web, plus Google, is everything we need? 

The scenario you outline seems to be a process that a person would go through, rather than anything automated, so why do we need a data model? What is the advantage of putting all this effort into normalising the data if everyone just wants to read the Wikipedia page?
---
 
http://unsustainableideas.wordpress.com/2012/07/03/solve-file-format-problem/#respond
There is an issue about scope, and relation to other data stores, but I think you've jumped ahead too quickly. The problem is clearly stated: Make is possible to get the data out and re-use it. The solution will be whatever it takes to do that. Therefore, documentation, software and specification are liable to be in scope, but everything else will be driven by necessity. For me, the main attraction of this approach is that it will concentrate on whatever it takes to make it work, i.e. collect the data then model it flexibly. Not 

Mismatch risk. 
Separate RI, Implementations, Specifications, Properties etc.
Format as a superset of multiple definitions
BySpec.
AsImplemented
IdentifiedByMIME
IdentifiedByExt
IdentifiedByMagic?

Wikipedia integration?
http://en.wikipedia.org/wiki/Wikipedia:WikiProject_Computing
Task force? Or
http://en.wikipedia.org/wiki/Wikipedia:WikiProject_Software

http://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view
http://en.wikipedia.org/wiki/Wikipedia:Verifiability
http://en.wikipedia.org/wiki/Wikipedia:No_original_research
http://en.wikipedia.org/wiki/Wikipedia:Notability

We will want to cover long tail. I'm concerned that we'll only get the main ones in.

Rather, I think a simple system that brings the sources together is the right thing for now, while we work on NPVO, V. This will involve to OR. N will have to be judged in collaboration, as will the steps necessary to turn this info into a Source.  Really, a route into PRONOM is the way here. Trust processes again.

http://en.wikipedia.org/wiki/Template:Infobox_file_format

http://www.mediawiki.org/wiki/Manual:Parameters_to_Special:Export
http://en.wikipedia.org/wiki/Special:Export/Portable_Document_Format
http://www.bbc.co.uk/nature/life/Southern_right_whale
http://dbpedia.org/page/Tagged_Image_File_Format
http://en.wikipedia.org/wiki/TIFF
http://www.nationalarchives.gov.uk/pronom/fmt/353.xml
http://en.wikipedia.org/wiki/Wikipedia:Creating_a_bot

http://en.wikibooks.org/wiki/Choosing_The_Right_File_Format
http://en.wikiversity.org/wiki/Digital_Libraries/File_formats,_transformation,_migration

In part, I think it's because we're not quite sure what we need. But frankly, I think we're going to have to start trying to collect the data in order to work that out.

I think a bigger barrier is the lack of a coherent social structure to ensure the longevity of the information, and the associated uncertainty over where to put our effort. I think many of us are willing to contribute information, but we need a forum where the information can be rapidly 
 overall information flow is critical, in that the contributors must have some assurance that their contirbutions will matter, will persist. e.g. end up in PRONOM.


The primary value we have added appears to come from the DROID tool using the identification information in PRONOM to spot different versions of specified formats. Once that is done, most users I have observed go from there, onto Google, and generally end up on Wikipedia.

Maybe that's not such a bad thing. 

Info

It needs to support the kinds of information we need to exchange: about file formats; about software applications and technical environments, and how they relate to file formats; and institutional preferences/policy about file formats and technical environments.
http://www.openplanetsfoundation.org/blogs/2011-07-21-registry-guidelines-answers

Suggested initial information to cover: 
• Signatures for identifying formats using tools like DROID and Fido. 
• Information on which software can read which formats 
• Information on the dependencies of that software (‘technical environment’) 
• Significant properties/characteristics of files in a particular format? 
• Which tools can successfully identify a format 
• Which tools can successfully validate a format 
• Documentation or specifications of formats 
Is it also desirable to publish ‘policy’ information as well as the above ‘factual’ information? 
By policy information, we mean the choices of an individual organization for questions such 
as: 
• Preferred identification tool 
• Preferred characterisation tool per format 
• Policies around conversion of certain formats into other formats for preservation or 
access and the preferred tools to carry out such conversions 
Representation information registry providers do not need to publish all of this information – 
any subset of it can still be valuable.
http://www.openplanetsfoundation.org/system/files/Guidelines_for_representation_information_publishing V0.1.pdf

http://www.digitalpreservation.gov/formats/fdd/fdd000022.shtml



---

Software
--------

> JHOVE "approaching the end of its life": sourceforge.net/p/jhove/bugs/5… Makes me wonder about long-term implications for its user community?
> https://twitter.com/bitsgalore/status/382085810796781568

OpenWayback

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

Fundamentally, the things we can identify clearly as formats, and so much of the content of PRONOM, is inherently reasonably stable. Selection/collection bias. The really 'at risk' stuff is rarer, or more rarefied, and is not even in the list.

See also [File Format Action Plans](http://blogs.loc.gov/digitalpreservation/2014/01/file-format-action-plans-in-theory-and-practice/).

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

## Talking about formats
Maybe we should concentrate on managing suitably unambiguous identifiers for different formats, and just contribute to Wikipedia to make sure those identifiers are embedded alongside more descriptive details and explanations. With so many registries so poorly filled, we must either start explicitly allocating resources to help fill them (instead of designing new ones), or face the fact that we need the help of the wider community and pitch in with Wikipedia. Who better to review and build trust in those pages than us? And where better to place that information in order to ensure it will be maintained for the foreseeable future and is likely to be archived in perpetuity?

My preferred proposal is that we design new data fields for Wikipedia, and create a QA process that looks at all the format records and checks if these fields e

Will the necessity of 'no primary research' kill it? Or are we just documenting what is held elsewhere?

### GRAMMAR 

In part, this problem arises because there is no specification to any grammar by which these symbols (identifiers) that PRONOM mints may be combined. Due to the way the word format is commonly used, one usually ends up with a simple grammar along the lines of "(resource) . hasFormat . PUID:fmt/44".
 
Unfortunately, we often need a way of saying that a resource appears to conform to one or more specifications. For example, PRONOM also contains character coding identifiers, e.g. chr/1 for Unicode UTF-8. How are we supposed to combine these identifiers to state things like 'this document is UTF-8 that conforms to the XML 1.0 standard'? The MIME type scheme handles this kind of combination much more elegantly, e.g. 'text/xml; charset="utf-8"', but neither really captures the fact that UTF-8 is also a format in it's own right.

cTrue. Maybe we need .nearlyConformsTo. or .parseableAs. as well?

----
Archiving Reference Implementations and Standards...
http://digitalcuration.blogspot.com/2008/03/legacy-document-formats.html
PRONOM Update Form:
http://www.nationalarchives.gov.uk/contact/contactform.asp?id=13

<Format> .createdBy. <Application> .conformsTo. <Spec>
Where <Application> is made up of particular <Software> in a particular <Environment>.

 <resource> .conformsTo. <PDF-1.4> .accordingTo. <JHOVE2>
 <resource> .conformsTo. <PDF-A> .accordingTo. <XXX>
 <PDF-A> .isSpecialisationOf. <PDF-1.4>
 <resource> .createdBy. <AdobeReader>
 <resource> .hasExtension. "pdf"

 

Underlying this is my own dissatisfaction with the opacity of PUIDs. Why do we have to put up with using fmt/xx when what we we want to say is fmt/PDF/1.4? I realise that this arises because of the concern that any information encoded in the identifier may turn out to be wrong, but what on earth does it mean to mint a permanent identifier for a record when every single aspect of that record is permitted to change? If we don't know which fields uniquely define a format, how do we know when a new one comes along?

Using a PRONOM ID, as they stand, allows you to make assertions like This-File . Has-Format . PUID:fmt/44. 

Similarly, whether internal or external signatures are authoritative or ambiguous depends heavily on context, and it is not clear whether it is even sensible to try and make permanent identifiers for such things.

c.f. HTML data versus behaviour definition argument
http://lists.w3.org/Archives/Public/public-html/2008Nov/0248.html
http://lists.w3.org/Archives/Public/public-html/2007Nov/0444.html
http://en.wikipedia.org/wiki/WHATWG

See also MIME Type Problem and difference from our needs (descriptive, no behaviours)
http://annevankesteren.nl/2006/11/text-xml
http://tools.ietf.org/html/draft-murata-kohn-lilley-xml-03#page-7
text/xml is deprecated, is this a mismatch, or are we wrong? All combinatory schemes have this problem? Or does it only arise because it gives XML etc two declarations and it is not clear which is authoritative? PRoblem is, we still need to know how to respond to identifiers, so using identifiers brings us to the same problem? What about ZIP/ODF style combinations?

## Validation: Fast-Fail versus Lint

###Office Dependency Analysis, lost:
http://www.openplanetsfoundation.org/blogs/2012-02-01-dependency-discovery-tool-office-files-code-published
http://www.openplanetsfoundation.org/comment/242#comment-242


### JHOVE wishlist
http://fileformats.wordpress.com/2013/02/01/future-jhove/
There are some parts of the PDF/A profile that Jhove do not check. A fact that worry some of our customers. For example “The data within content streams, and therefore the use of operators and the glyph descriptions of embedded fonts.” are not checked.


JHOVE2, complex Spring, hardcore BDB thing means checksums fail (Tika solved this using a stream), Reinvention of schematron for assertion, aggrefier is insufficient.
I need to know this is half a shape file, not 'unknown'.
"Clumps. Sets of source units that JHOVE2 knows how to characterize as a unit. These 
include GIS shapefiles, which consist of at least 3 files (with .shp, .shx, and .dbf 
extensions) possibly accompanied by other files"
Heavy reflection. Re-invents service/module management I think.
JHOVE2 uses BerkeleyDB JE as its persistence memory manager. = Death on a cluster.



