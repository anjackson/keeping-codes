---
title: UKWA Sustainable Access Plan
layout: default
categories: [practice]
tags: [stub]
---

> The themes of the 2014 TPDL/JCDL combined conference will follow the theme of ‘preserving the past - finding the future’. Digital collections face two major challenges: organising and conserving material across time, and enabling users to discover the material they need in increasingly large collections. In terms of ‘preserving the past’, example issues include the demands of digitisation of physical materials, the digital preservation of material so it remains acessible, and the systematic classification and indexation of large collections across social and technological change.
>
> In contrast, when ‘finding the future’, sophisticated discovery tools, effective library policies, support for linked data, and supporting the user’s interpretaton and analysis of content are examples of the key challenges that face the communities of DL practitioners and researchers.
> 
> The conference welcomes internationally leading insights into both research problems and practical complexities. Contributions from digital humanities, digital preservation, hypertext and information retrieval researchers are as much a vital part of the digital library community’s interests as core DL research, and submissions on these and other related topics are strongly encouraged.
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