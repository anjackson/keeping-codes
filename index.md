---
title:  Keeping Codes
layout: default
---

This is a collection of notes on digital preservation.

* Fundamentals
    * [Communicating With The Future](fundamentals/Communicating With The Future.html)
* Practice
    * [Sustainable Access for the UK Web Archive](practice/UKWA Sustainable Access.html)
    * [Characterising Software and Dependencies](practice/Characterising Software and Dependencies.html)
* Case Studies
    * [BBC Micro Data Recovery](case-studies/BBC Micro Data Recovery.html)
    * [Characterising PDF Documents](case-studies/Characterising PDFs.html)
    * [Archiving Wikipedia During the SOPA Blackout](case-studies/Wikipedia SOPA.html)


Planning - top down worse than stakeholder engagement. CI versus an initio. Separate choices - strategy versus implementation. 
Significant properties - content properties not relevant. Dependency analysis and critical characterisation role. For content, in future, eye of stakeholder means users should be able to express format preference.
- SOPA Blackout Wikipedia Homepage
Format analysis - cf versions don't matter, features do.
Modelling - oais is clumsy, arbitrary boundary, not user centered
RI - best stuff done outside of the iPres community
Trust models omitted - trust is social
Threat models uncertain?
Pull in requirements and issues, AIT stuff.
Pull in Monitrix, BDT, IMAQA, WAT Mining


Keeping Codes
=============

Inclusive definition of digital preservation 
Ensuring reuse

It's not the digital that's the problem
Directly.
It just makes new machines easy


On Preservation Strategies
--------------------------
The early computers had little or no permanence. 
Tape, pushing memory to disk.
Early persistence and communication, Yellow Pages listings in computer magazines.
That the road to perpetuity is made of daily steps.
That we should understand how preservation is done, right now, on a day-to-day, week-to-week, year-to-year level, because the only way to reach out across centuries is by changing the day-to-day.

This is not a digital object
File bitstream resource-content
They are the first step to presrvation
Persistant state


- The First Preservation Action: Save As...
- Map to Shannon
-- Coding theorem as Zeroth Law of Digital Preservation

On Systems
----------

- The Stack
- Migrations And Emulations
- Choosing the performances: wikipedia black out case study
* The Performance Spectrum, just the one.
** http://notepad.benfinoradin.info/2012/08/28/take-a-picture/
- The Stack and The Continuum
-- Continuity versus archaeology
-- The experience versus the potential
-- Broadcast to narrowcast - no longer a property of the medium.
- An instance of a performance to all performances.
- Strategies are where you draw the migration bubble on the stack.
-- Standards Reliance is the implied default.
-- Also, migrate to supported environment is a double bubble.
Rothenberg Vernacular (Middle english example ) is about perception side.
o-ring data is about the extrapolation, not the data. very different major migration loss.
Rotherberg vernacular extraction example, cut-paste from emulator, is a migration.
Backwards compatible, new versions run old stuff. Breaks in this, e.g. deprecation, are the issue.
REF that high-change-freq. chart from last years iPres.

That all digital objects are processes, and that the artefact is an analogue relic.

That the difficulties in preserving access to digital media arise primarily because the access the item is mediated, not because they are digital. The same can be said of needing a speaker of an obscure language to understand a book. You can either keep the language alive (emulation), or translate the book (migration).

That RI is of two kinds:
1. Performance RI, that is the information required to reconstruct a particular interpretation of a digital artefact, i.e. to regenerate a signal to be interpreted by an actor outside the system. e.g. rendering a PDF.
2. Perception/Understanding/ RI, that is any futher information required to support the actor in understanding the preserved signal.

That actor-RI is subjective. It's consqeuences aare tjhat is should be layered rather that designed up-front, and turns into educational resources if you wait long enough

IMPORTANT: Identifiers and distinguishing 'this version created the item' from 'this is the intended interpretation'. e.g. DOC is tricky here, as writer version confused with reader version?

Format specs must be implemented to come alive, and it is the processes that implement the specs that are definitive.

In truth, every so-called digital object is a process, not state. The illusion of stillness has taken years to create, but is a kindly lie.

 digital preservation for years. The most common 'preservation action' is porting. Calling it 'source code migration' underplays its importance.
 
 
http://unsustainableideas.wordpress.com/2012/07/03/solve-file-format-problem/#respond
There is an issue about scope, and relation to other data stores, but I think you've jumped ahead too quickly. The problem is clearly stated: Make is possible to get the data out and re-use it. The solution will be whatever it takes to do that. Therefore, documentation, software and specification are liable to be in scope, but everything else will be driven by necessity. For me, the main attraction of this approach is that it will concentrate on whatever it takes to make it work, i.e. collect the data then model it flexibly. Not 


On Format
---------

-Herd Immunity
-- Format obsolescence as disease 
-- We are the immune system 
- The First Preservation Strategy: Format...
- Data And Metadata, interpretation difference.
- eBook wars, like early years of DRM music etc.
- files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
-  Is ISO Enough? Open standards etc.
- http://www.endangeredlanguages.com/lang/3049

A format is a social convention for exchanging data.
A format is a way of grouping documents that share some features.

Perhaps the difference here is whether we are trying to document all possible 'strains' of a format, or whether we are just trying to find what format(s) the item is consistent with, e.g. in order to pass the item on for deeper inspection. Or in other words, are we defining format by implementation (software) and context or by specification?


On Theory
---------

- The zeroth law of digital preservation
- Beyond the zeroth law: compression and RI
Other: false positive scaling problem http://mobile.theverge.com/2012/10/28/3567048/carnegie-mellon-video-surveillance-action-recognition
- Trust http://en.wikipedia.org/wiki/Source_criticism
- Bitwiser
- Preservation Planning - Baysian versus frequentist... First principles/ab initio or Empirical modelling.
- Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?




Insignificant properties
------------------------

- Significant Property Schemes 
-- Sig prop breakdown
-- Compression Is Not A Significant Property

Well, this cuts to the heart of the matter that I've had so much trouble trying to express. Well, here goes...

So, the premise is that we shall judge the reproduction of some performance, whether emulated of via migration, by using some formal scheme to capture and compare the 'significant properties' of the two performances. I have three issues with this. Firstly, I'm not sure we should be the people who get to decide what is 'significant'. Secondly, I believe this approach is both extremely difficult (as Euan points out) and unnecessary - i.e, that when we do want to evaluate a reproduction we don't need to create a special new 'preservation language' to make it work. However, I'll leave those for another time, because my third problem goes much deeper.

I'll start to pick this apart using a really simple example - ASCII. To render ASCII, we must implement a process: if the byte value is 0x61, plot a glyph that look like 'a' and move to the next spot. Capturing the contextual information this depends on, the mapping table and the glyphs, is not sufficient to reproduce this. The rendering is fundamentally a process, a projection, a computation, not static information. The process can be written down, but this is just migrating it to another language, and if you use prose will need to be re-implemented in order to interpret and make use of it.  We always end up implementing or porting software - the documentation of the rendering is just helping us get it right.

Unfortunately, in general, the properties of a rendering process cannot be captured by a simple document compose of prose and declarative data. The only unambiguous language one can use to describe any process a performance may contain is a Turing complete language. Any Turing complete language will suffice, but any language less powerful than that (e.g. the kind of simple declarative data structures we often prefer, or something like boolean logic) will not be able to capture everything we may want to preserve. Thus, if preserving general processes means we are required to preserve one or more Turing-complete formal languages, we are preserving software, by definition. 

Having said that, we could choose to preserve only data in formats that a simpler, e.g. regular languages.


I believe there are absolutely no cases where this can be truly avoided. You're just flattening to a simpler process (e.g. ASCII) and moving the rest of the interpretation out to the user.

The fundamental problem with a system based on significant property schemes is that, in general, most digital object data does not specify properties in a way that maps cleanly to the performance, and indeed could never do so. In the general case, a performance is fundamentally a process, a sequence of states, and the bitstream you load just starts you off in the right place. When you try to capture the properties of performances, you must be able to cope with the fact that the performance may be generated from the data, rather than being 'merely presenting' the data. The necessity to be able to describe any possible performance means that our 'significant property' language must be powerful enough to explain what the generated performance may be. The only formal languages that are capable of capturing any possible performance are those that are Turing complete, i.e. programming languages. Therefore, the only *general* way to capture the 'significant properties' of any possible format we may come across is as software. In the baldest terms, PDF is only  unambiguously defined by it's reference implementation, Adobe Reader.


What we can choose to do, however, is to select some common formats that we believe will act as sufficient substitutes and invest more in supporting those. For example, if Excel becomes problematic, users may prefer to have plain text CSV of the data rather than nothing at all, or having to manually dig around in an emulator. Practically, this means that where we are sure there is value in it, we will support formats that allow us to get that data to our users directly. But to cover the general cases, where we are not yet sure of the value, the best we can do is preserve the software associated with the data, so that some future user can dig out the value. Ideally, if we capture the source code and associated documentation around that software, we increase the chances of this working. 

 
Firstly, I have an issue around who defines what the 'essence' is. I'm not convinced it should be us. As the purpose of a format is to persist a performance, the only safe assumption is that all of those properties are significant. Anything else is predijucing the future, which is fine, as long as your use case is clear, but if we have the chance I would like to put that choice in the hands of our readers and users as soon as possible. But that just a problem with the 'significant' part. I also have issues with the 'properties' part.

One part of the problem with properties is that, when it can work, it has tended to lead to a kind of catch 22. We want to used significant properties to evaluate a migration from one format to another, and this has been taken to mean that we must define some kind of significant property scheme that can be used to capture some or all of the properties of both formats. However, as I argued above, each such property scheme is nothing more than yet another format. i.e. we are judging a migration from format A to format B, but expressing the transformation in terms of a special 'preservation format C'. In some cases, this can be made to work. The problem, however, is the amount of work it involves. It means having one 'super-set' format that is capable of expressing all the potentially 'significant' properties of all the formats you might want to migrate between. This is an immense amount of work, and a keeping such a system up to date would be a huge burden on the preservation community.  Worst of all, even when this approach can me made to work, it is not necessary to create a special preservation 'super format' to do it - there are other ways to judge a migration. I'll leave describing them to some future post, because even that is not the real problem.

Catch 22

---
Papers

Testbed future 

Gaming named entities for extraction from the historical archive.

Poor mans technology watch

Recent opf post and older wap one on RI
A new collection? Computing history collection? Computing Reference? 

Hard disk quality risks
Losing half the array 
CDROM of health data
Advice for public sector TNA?

