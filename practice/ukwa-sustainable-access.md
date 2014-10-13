---
title: UKWA Sustainable Access Plan
layout: default
category: Web Archives
status: stub
tags: ["Requirements for Tools"]
---

> The themes of the 2014 TPDL/JCDL combined conference will follow the theme of ‘preserving the past - finding the future’. Digital collections face two major challenges: organising and conserving material across time, and enabling users to discover the material they need in increasingly large collections. In terms of ‘preserving the past’, example issues include the demands of digitisation of physical materials, the digital preservation of material so it remains acessible, and the systematic classification and indexation of large collections across social and technological change.
>
> In contrast, when ‘finding the future’, sophisticated discovery tools, effective library policies, support for linked data, and supporting the user’s interpretaton and analysis of content are examples of the key challenges that face the communities of DL practitioners and researchers.
> 
> The conference welcomes internationally leading insights into both research problems and practical complexities. Contributions from digital humanities, digital preservation, hypertext and information retrieval researchers are as much a vital part of the digital library community’s interests as core DL research, and submissions on these and other related topics are strongly encouraged.
>
> <small>[Digital Libraries 2014 - Call for papers](http://dl2014.org/cfp.html)</small>

Introduction
------------

We have stuff, we've started collecting LOTS of stuff. We need to understand how to preserve it, and how to ensure it will be useful. We can do this by using historical archives and exploring how they might be exploited, and looking for examples for preservation problems. We can use that research strand to inform our production services.

Preserving the past to understand the future

Starting with search
--------------------

The need for full-text search is critical - you cannot preserve access to what you cannot find. Therefore, the ability to find the content of interest is a critical first step both to access and preservation. The traditional web archive playback mechanism, the Wayback Machine, focusses on replay of individual web resource over time, but you need to know the URL. The problem is that often you don't always know the URL. Either it has been lost already (?), or c.f. that social media example where links are known but died before preservation but may be held elsewhere.

Beyond that, we would like to support many more modes of discovery than this. Some of this is at the resource level, but looking beyond the individual resources, like indexing the links in pages in order to expose incoming links. Or looking for similar content, perhaps containing copies of other resources, etc. *Flesh this out*.

Then, at the whole collection level, we want to be able to support Google Books style NGram queries, exposing longitudinal trends both in terms of content and composition of the web archive.

In short, we want to know what's important, what content people care about, and use that to drive which preservation problems we try to deal with. The discovery process is where we start.

Indexing 
--------

In order to create a full-text index, we must extract a textual representation of every single resource.

I'm not sure it's reasonable to expect what is appropriate for the Internet Archive's web archive to be appropriate elsewhere. For example, when accessing the content, the archive's visitors are expected to come to the Wayback Machine armed with the URL of the site they want. They look up the URL, choose the date, and download the items they want, and the interpretation of the content is left entirely to them. Very little metadata is required for discovery, and the IA only need to support access at the protocol level (HTTP has been pretty stable so far).

I think the web archive is quite exceptional in this regard and that, in order to be enable their users to discover and use their collections effectively, most other institutions will have to understand how to interpret their content. For example, to support full-text search, some sort of transformation to plain text is required. One must choose therefore choose whether to make this text version an archival artefact (which assumes it could never be improved), or whether to support the software required to re-parse the original items in order to be able to generate new indexes in the future. Similarly, 


Piggyback Preservation Risk Scanning
------------------------------------

Given we are attempting to extract plain text from every resource, therefore visiting every byte, we have an excellent opportunity to piggyback on this process. Given that the indexing process is largely I/O driven, i.e. that reading the source files and writing the indexes are the time-consuming parts, the additional overhead of adding a bit more intelligence to the processing is minimal.

For example, format identification is already a required step - no software component can attempt to reliably extract the full text from a resource without first knowing what format the resource is it. It is a simple matter to ensure that the result of this initial identification is recorded.

Learning from research
----------------------

### Dealing with duplication

Messy, interpretation issues.

### Improving crawlers

Rendering for dependencies,


See also

[Good practice in preservation webharvests, David Pearson (NLA), Peter McKinney (NLNZ), Prepared for the Preservation Working Group of IIPC](https://docs.google.com/document/d/1UPQ4uIfaUA20nYxtwmTkx15iNRYVY4FOJBZS1Fg0RCk)


Outline of talk for IIPC GA 2014
================================

WebARTist is very similar.

Pages in.
Pages in archive but not 'intentional' (in seed list).
Pages not archived but known.

Using anchor text to infer content of unarchived documents.



Preservation Stuff
------------------

Knowledge bases
(manually constructed)
- Historical environments over time, drawl from partners.
- Risks for web archives. From NLA 2009. Likelyhood? Severity? Mitigation.
    - Add to Wikipedia? Maybe not due to the tags etc.
    - Bibliography, could be a Zotero group, say.
    - c.f. The Web Archive Bibliography. Expansive overview of the field.
    - Three bibliographies and a database?
    - This would be a good hackathon thing, to push this forward.
- Environment submission
- OldApps are friendly, so we should follow up.


Jun 5,
Jul 17,

...

Difficult Formats
- VRML1
- MP4

Future Standards:
* Screenshotting the domain crawl. PLUS on-ready DOM.
* Roger's cool fragment screenshots.
* Video stuff?

SCAPE:
* Nanite
* DRMLint to Flint, as more general that just DRM, but focussed on dependencies.
    * Embedded/linked JavaScript, missing fonts in PDF, etc.
* Pageylyzer, for visual and/or structural comparisons of web pages: http://openplanets.github.io/pagelyzer/
* ToMaR
* DRMLint/Flint - assess files against a format policy (i.e. checking for javascript, missing fonts etc. in PDFs)
* xcorrsound, pagelyzer, jpylyzer, and a few Apache Tika improvements.
* Interject
* They are at DL2014 in London.

There might be an interest in ToMaR (http://openplanets.github.io/ToMaR/). This is a tool which wraps command line tools for easier execution on a Hadoop cluster.
Sven has put together a demo which uses it to run FITS over a WARC file and import into the SCAPE C3PO profiling tool (http://peshkira.github.io/c3po/). See Sven’s blog post: http://openplanetsfoundation.org/blogs/2013-12-16-web-archive-fits-characterisation-using-tomar
(I don’t know if Sven will be there?!)

Alan Akbik (TUB) has continued his work on Text Mining/Information Extraction (I think the tool used to be called KrakeN, but as I understand it, this work has moved on since then. There’s an online information extraction system available: http://lucene.textmining.tu-berlin.de/ and a blog post about it here:
http://www.openplanetsfoundation.org/blogs/2014-04-03-web-scale-data-mining-digital-preservation

SCAPE (jointly with APARSEN) have also got a workshop at the DL conference (http://www.dl2014.org/) where there will be a panel discussion followed by a number of demos related to the tools and services SCAPE have produced. Still awaiting confirmation on the date SCAPE will be there (the proposed date is the 8th, but this may change), but the conference is 8-12th Sept in London.

Joachim has suggested Barbara Sierman may also be at the IIPC conference (for whatever working group she’s involved in) and was (allegedly) planning to mention SCAPE. We have some SCAPE flyers around specific tools; hopefully Barbara will be taking some of those with her too.

Other than the things that Peter has mentioned I don’t have much to add.  DRMLint will be changing names to Flint soon, to reflect how it can also assess files against a format policy (i.e. checking for javascript, missing fonts etc in PDFS).  I am working on Geospatial files and will add them in to Flint eventually, reusing the infrastructure.  We are aiming to publish up to date source and have a web demonstrator of it up soon (on http://scape.opf-labs.org) (and maybe a blog post)

It’s testing validity of GML and NTF files.  They’re just format modules in a forked DRMLint so they should slot into Flint fairly well (or in a separate repo, pulling in bits from FLInt).

http://sourceforge.net/projects/officeddt/ could 


OpenWayback
===========

How contributions model should work.


Paper on LDWA
=============
- oais as rep model not digital preservation
- Js  stuff
- Storage scaling 
- Characterisation as core problem
- Silly restrictions
- User feedback to judge SIG prop
- Reindexing as bau, hence cluster but any performing chechsumming store could piggyback 
- Linear implied discovery model of oais as painfully wrong
- Catalogue data as derivative data plus annotations
Loop of evaluation at dip stage to PACT preservation actions
Actually linked to stakeholders rather than lone decision maker
Cost rise over time plateau's at 'complete reverse engineering'? Or infinite because of what you are forced to guess
Instead of guessing what they'll need, collect evidence to validate the approach.
Web archive to keep thumbnails, screenshots, Dom trees? Render traces?

Services - can we make these services sustainable:
- Bookmarks
- Curation of the web
- Annotations
- Page change notifications, a la https://visualping.io/ https://monitorbook.com/

