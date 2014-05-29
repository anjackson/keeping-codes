---
title: The Format Registry Landscape
subtitle: The roles they play, and opportunities they provide.
layout: default
categories: [practice]
tags: [stub]
publish: false
---

Introduction
------------

What problem are we solving? Linking bitstreams to software.


The Registries
--------------

### IANA

http://www.iana.org/assignments/media-types/media-types.xhtml

### Windows Registry

### NSRL

### SWID Tags

A standard, rather than a registry.

http://tagvault.org/swid-tags/


The Opportunities
-----------------

### Data mining

### Comparison

### Collaboration

### Think Bigger

IANA, WikiData

https://www.mediawiki.org/wiki/Wikidata_Toolkit


So, my broadest definition of a file format does like this:

    A format is a protocol designed to allow the persistence and transmission of the run-time state of computer software.


Notes on the NZNL presentation
-------------------------------

Points:

The format model will be 'wrong' - it will need to change, by consensus.

If this is about automation? Then be clear that you are making software - and the registry is a means to that end.

No-one knows what they need from a DPTR, it seems.

Collection Management:
- "Critical to day to day business." NZNL.
- "Want to understand the objects at a deep level."
- "It's not some weird PDF, it's just a collection item."
- Thing about barriers. If they can't GitHub, are they happy to crack open a hex editor? What do you mean by a deep level?
- Is this a broad audience or a very technical audience.
- "Industrial Management & Preservation" - scale implies automation?

Goals:
- Format-level risk management - Grand.
- HW/SW Dependencies.
- Media Carriers.

- Characterisation
- Risk analysis
- Preservation Action, pathways etc. (Also interested in providing these to users, c.f. /interject/).

Actually about tool support.

I do not care about validation, except where it can be considered a reliable signal for likely access issues.

Note identification varies
- HTML, e.g. signatures competition, heuristics, bias.

Central store of knowledge - I'm happier with links, you only really need to aggregate actionable data.
I agree pinning "war stories" together against tools or formats will be a good idea.

Changing the day-to-day workflow of tens of people worldwide? Hundreds? This is hard, but who are your users again?

Please share case studies and user stories, and please form a user group of people who would self-identify as the users in your user stories.

Waterfall danger.
It's not iterative or agile if the user stories are fixed and were developed behind closed doors.

Where does trust come from. I'd rather that you did not say 'Will provide trustworthy data' because that's too vague. For some, it seems, trust is primarily about provenance. Your model, that Community peer review will lead to more trustworthy data, is much stronger.

Much of this is linking existing information and commenting on it, but much is new research. Who will be doing this?

IMPORT is BAD unless the source is DEAD.

I prefer an integration model. Pull in the data, and only link against it, and use it to bring related data together and 

Not convinced that RISK IS LOCAL, or rather, it's only local if you don't have an international community of expertise and experience to tap into.

Oddly, signatures are local, and that's why they should be OOS.

How to resolve conflicts, with a worked example, e.g. the TIF-tiff, how would this have worked before and after that change?

I prefer: pool under identifiers, expose the differences, change the data sources. Again, that part is NOT an API and NOT automatic.

There are many different 'unix' registries. I assume you mean file versions? Note that Debian, OS X etc. Magdirs all vary slightly. It's a world of pain. Either we totally fix that one, or we just link.

- ID/RI separation
- PRONOM Conflict Resolution
- 'Confronted this earlier', SDB ???
- What are you going to automate? Be specific! Start with DRM or PDF risks or something.
- PRONOM validates.
- PDF engineerd so they don't need that history.
- IANA, w3c 

Everything the MVP really needs can be done with flat files on GitHub.

We want an automated service.
BUT
This is a peer-review system, that's not something we can automate.
THESE
Surely we publish, we don't run off live.

This is essentially software.
SO, what is the QA/testing phase?

No mention of data-mining sources, combination, etc.
NSRL
Collection mining for software and formats.

Recommendation: Push the identification process out of scope, including most of PRONOM. PRONOM is basically an identification stack, with very little additional information about the formats.

Magic is contextual. Do we record what we think the X it.

TRiD and JHOVE lone developers. JHOVE maintenance is not R&D, it's just maintenance. Deprecation of adaptors between JHOVE 1 and 2 should not have happened? So make one. What's stopping you or us? Also for tool developers? How, and who?

Adobe don't have the back-catalogue of versions of PDF. No formal structure for them to understand the history of PDF. So, they don't need it. PDF is one of the tightest forward/backward compatible formats there is. You can be *almost* sure that an old PDF will look the same because of the format design. So, then, the question is, how to we allow that to be verified?

Otherwise, what do you mean by history? Is it something you can capture? What's the scope?

William's point about a range of services is not necessarily sound. Range of identification tools is fine, but a mess of separate RI stacks is not worthwhile.

What stops us from actually collaborating? e.g. why didn't your Virus WARC make it into the UKWA warc corpus?
* https://twitter.com/NDHA_NZ/status/389930412639653888
* https://github.com/jayGattusoNLNZ/DigitalPreservationNZ

What is the activation barrier? We've had the same with CRISP, UDFR, etc. Few contribute, so it really can't be that critical right?


Alternative forms:
- A journal.
- A dashboard.

CC-BY or DEAD.

Membership-based model proposed.

e.g. https://tools.ietf.org/html/rfc3236#section-8
Accept: application/xhtml+xml;
        profile="http://www.w3.org/TR/xhtml-basic/xhtml-basic10.dtd"

Format specs. are social norms guidelines. Grammar textbooks.
Want to describe/glob files.
You are defining formats using whatever available spec as the baseline. Strains.
Implementations.

Specification has Implementations (which might have formats).
Composition, brings together Aspects from outside Specifications. Variants. Unclassified variants.

I have two perspectives, the bit-space and the show-space.

Write/Read separation is not clear.

> "Great news! @OpenJPEG in the process of becoming official reference software for JPEG 2000 Part 1 http://tinyurl.com/qxs2fyc"
> <small><a href="https://twitter.com/openjpeg/status/420187947153899520">@OpenJPEG</a></small>

Test formats:
- DRM
- OOXML strict/transitional.
- ePub including 'obfuscated' fonts.
- A truncated PDF.
- Half a two-part resource.
- RAM image formats
- wget 1.14 GZipped WARCs.
- WordStar - tiny traces left. What more do we need? http://fileformats.archiveteam.org/wiki/WordStar
- JP2 - jpylyzer profile validation workflow.
- HTML, especially the current HTML5/w3c/WHATWG situation. http://fileformats.archiveteam.org/wiki/HTML#Specs

Two specs, no spec.
One spec, interpreted differently.
Two specs, identical interpretations of different structures.
Error handling

Pick something really solid that's an actual risk, like PDF/A violations as risks, or perhaps just the presence of DRM, and sketch the whole thing out around it.

Source http://www.dpconline.org/newsroom/latest-news/1141-future-of-technical-registry-services-feb-2014

PDF/A-3 Risks...
http://blogs.loc.gov/digitalpreservation/2014/02/new-ndsa-report-the-benefits-and-risks-of-the-pdfa-3-file-format-for-archival-institutions/

Completely unaware of http://gator1355.hostgator.com/~iipc/pwg/risks.php, but that's going public soon.

http://www.keep-totem.co.uk/ is basically empty.


Tensions
- Automated and industrial, or peer-review.
- Technical or broad user base.
- If it's so obviously a win, why isn't it happening already. Why aren't you working in the open so you can be found?

Format model does not appear to separate syntax from semantics, i.e. aspects/features are both an encoding and an interpretation. Not sure this is drawn out.

Are we really going to capture the history of a format. Look what's involved.
[MP3: The Meaning of a Format](http://www.dukeupress.edu/MP3/)
