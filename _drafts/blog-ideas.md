---
title: Blog Ideas
---

## One Liners

Wikipedia's echo chamber - Deletionists - Self reinforcing etc.

<http://gty.im/149366163>

<https://intranet.bl.uk:8443/confluence/pages/viewpage.action?pageId=139630062>

Preserve the Mona Lisa by duplication? Delete the original?

* Using UKWA to preserve your project.
- Format Herd Immunity
    - Format obsolescence as disease 
    - We are the immune system 
- Data And Metadata, interpretation difference.
- eBook wars, like early years of DRM music etc.
- files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
-  Is ISO Enough? Open standards etc.
- <http://www.endangeredlanguages.com/lang/3049>
* Characterising Codes
- Interject
- Script tags over time and Umbra etc.
- Clever screen/div shots and DOMs thing.
- Forms and Scripts
- CC License adoption
- Fashions in Styling
- Don't <blink> (and other obsolete ones)
- UK domain islands.
- Web archiving RI use case e.g. http://britishlibrary.typepad.co.uk/webarchive/2011/12/advent-calendar-december-3rd.html
- clear.gif
- <http://www.openplanetsfoundation.org/blogs/2014-03-24-arc-warc-migration-how-deal-de-duplicated-records>

- Beyond OAIS
    - why OAIS is a straight-jacket and limits the care digital media needs.
- Digital Preservation Software's Usability Problem
    - Based on https://twitter.com/benfinoradin/status/490166741855506432
- What's wrong with PRONOM
    - Lack of parent-child relationships: http://www.openplanetsfoundation.org/blogs/2011-08-28-fmt-78910
    - Close ties to DROID
    - Vague definition of format. OOXML Strict/Transitional? Creating software version or version or intended software version. No link to SW. Most records nearly empty, so it's just the signature and a couple of strings.
    - Poor community sourcing tools.
    - No separation of signatures and identifiers.
    - Opaque management decisions.
    - Too many false negatives:
      - Partially validates content
      - Truncated JP2s or PDFs.
    - lowerPriorityThan is hard to tune with weak signatures. Global priority is easier and simpler.
    - No text/plain heuristic.
    - Encourages use of a insufficiently expressive format language.
- Unpopular opinions about format registries
    - The 'magic numbers' do not belong in there. (Magic is not just Magic, and is contextual)
    - Linked Data brings little to the table. (also a magic-composition problem (see above))
    - The contents of PRONOM do not belong in there. (you just gave yourself a data synchronisation problem)
- OR Focus on what I'm doing instead. Data mining approach, comparing engines, and auto-sig etc.
- Compression Is Not A Significant Property
- Defining Format
    - c.f. That Q&A item.
- Preservation Planning - Baysian versus frequentist... First principles/ab initio or Empirical modelling.
- eBook wars, like early years of DRM music etc.
- files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
- Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?
* Is ISO Enough? Open standards etc.
* Stack Overflow for Digital Curation
* Trust http://en.wikipedia.org/wiki/Source_criticism
* The Performance Spectrum, just the one.
** http://notepad.benfinoradin.info/2012/08/28/take-a-picture/

http://www.endangeredlanguages.com/lang/3049

Writing:
programming versus car mechanic
http://www.codinghorror.com/blog/2012/05/please-dont-learn-to-code.html
http://www.codinghorror.com/blog/2012/05/so-you-want-to-be-a-programmer.html
programming versus writing, not all of us need to be novelists.


TODO BLOG: Paying for Open Source ('pro', license, support, pooled)
TODO BLOG: Preserving processes, software and test suites.

Time travel
- Passive history is needed too.

Knowing first is impossible
"Need to be very *very* clear about what is to be preserved before developing tools"
https://twitter.com/mopennock/status/375271606085378048

QA costs and variation
"QA for emulation can be at an environment rather than object level so potentially cheaper"
https://twitter.com/euanc/status/375272042511491072

Letters to my son
- Plans for digital preservation
- Scaleability from the low side, to contrast with BL scale later.
- A business opportunity?
- Costs manageable via scale?

My fathers story
- Learning to geek

Career planning computer
- And jobs that didn't exist.

Vendors, communities and trust
-The enthusilasts will be the ones who save us, who are right no biolding the towers flog tepees gain information that thefuure will need to reconstruct t IRS past.
- Also, many institutions hands are tied by the law or he fear of it. The enthusiatst carry on, generally safe from prosecution while non commercial. 
- So how do we trust them? How do we build this expertise into our systems
- Earlier
- A comment by a sceneor manager made me realise that, as things are now, vendor onsolcsnce is a real risk. The only route to establishing a access system relies on extren vendrs. 
- I took it for granted that an institution like the bl would maintain the people it needs to undrstans it's own content. Surely no memory institution could expect to function without the people and code that embody the undrstansibg? We could not function without staff that understand paper, why should digital be different?
- Economics, skills, etc
- But also, contractual approach 
- or at least the wider comm


### 2012, the year DP jumped the shark
- Rothenberg arguing dp should outline its society by design - long now
- Rosenthal's straw man
- HTML as rothenbergs types
- Still apparently arguing Migration v Emulation, more straw men
- Unproven strategies taught?
- Hopelessly overambitious levels of preservation, most folks need reasons to get off the bottom rung.

### The Fourth Age Of Cataloguing ###
0. Books on shelves. locations in head.
1. Card catalogue of physical items
2. Online card catalogue OPAC of physical items
3. Online catalogue of digitised physical items
4. Online catalogue of born digital material.

We have been here before... [Google Directory No Longer](http://www.seroundtable.com/google-directory-gone-13731.html)

### On Format Languages ###
http://www.nationalarchives.gov.uk/PRONOM/Format/proFormatSearch.aspx?status=detailReport&id=1160&strPageToDisplay=summary
I understand the desire to focus PRONOM development on creating signatures, and I realise that keeping the references up to date would be a lot of work. However, I worry that signatures alone are not enough, because without the references, I don't think it's clear what is actually being identified. Without reference to any version of the ISO spec., or indeed MS Office, what does it mean to identify a file as 'Open Office XML' fmt/412? That kind of fine-grained identification is critically important if you wish to really understand the preservation issues around OOXML, because on the strict form has transparent semantics and can be considered preservation friendly. The transitional form is full of opaque semantics like 'render this paragraph like Word95 does'.

Except, actually, right now, it doesn't matter, because as far as I know there is no generally available software that implements OOXML Strict (I think only the latest Office betas do so). So right now, the ambiguity in the PRONOM definition is harmless, and getting into the details is pretty much a waste of time. If you just need to ID files right now, it works just fine.

http://www.zdnet.com/office-to-finally-fully-support-odf-open-xml-and-pdf-formats-7000002696/

Except, except, when the new versions arrive, and the various formats start to get supported to varying degrees, and the standard keep moving and 

Also, it's worth noting that the Open Digital Formats Registry idea is quite close to the Registry Ecosystem idea outline here (http://www.openplanetsfoundation.org/blogs/2011-02-15-file-format-registry-report-released). I used to be quite skeptical about this idea, but I've come around to it (http://www.openplanetsfoundation.org/blogs/2012-07-06-biodiversity-and-registry-ecosystem).

----

BLOG: Vendor Obsolescence, IE6, SilverLight, Flash?
http://blog.colbyrabideau.com/post/8317497197/i-dont-know-how-to-ie6
http://arstechnica.com/microsoft/news/2010/11/silverlight-html5-and-microsofts-opaque-development-strategy.ars
http://www.guardian.co.uk/technology/2011/jun/14/microsoft-windows-8-developers
http://www.zdnet.com/blog/microsoft/microsoft-needs-to-tell-windows-8-developers-now-about-jupiter-and-silverlight/9608
http://www.theregister.co.uk/2011/06/06/windows_tablets_without_silverlight_dot_net/


--- 

BLOG: Re-inventing the wheel (to be changed)
Issue about CITE paper, W3C Fragment effort, and issue about whether the fragment can reference the entity rather than the resource.

http://www.ariadne.ac.uk/issue67/blackwell-hackneyBlackwell/
http://www.w3.org/2008/WebVideo/Fragments/

In particular, if we wish the fragment identifiers to be insulated from some details., i.e. fractions used be CITE rather than pixels, we need to get that in the standard? It does % for spatial dimensions, so is that okay? is that precise enough? What if we want to point at something really small? How many SigFig.


---
Cargo Cult Standards

p.s. and if I anyone starts writing yet another standalone identifier, provenance or metadata standard from scratch, I will come around to your house, take away your computer, and replace it with a Chrome tablet so you always have to GOOGLE IT FIRST. :-)

Every time you start writing a new standalone metadata standard from scratch, God kills a kitten. Please make it stop.

---
BLOG: IT's not that cheap or easy - BBC Archive/Shutdown issue
http://www.wired.co.uk/news/archive/2011-02/11/bbc-torrent-archive-websites
http://www.webcitation.org/60lBTX2oN

---
BLOG: Cargo Cult Standards
BLOG: SCAPE and OPF
BLOG: Deconstructing the Planets Testbed
BLOG: Building Trust
BLOG: Format data model - what is permanent? Why opaque IDs.
BLOG: The long-tail of formats
BLOG: Identifying Microsoft formats. Why DROID and File fail. JHOVE2 it. Use those os and office installers or images to make test corpus?
BLOG/PAPER: Compression & Entropy

Full decomposition of Identification and RI?

RI - IDs - (identify) - TestFiles - (create) - Software - (implements) - RI
RI - (validate) - Testfiles

So, Fido etc manage identifiers, and link to RI about formats.
Identifiers also come with test documents, which describe the SW that created them.
RI has unique IDs and links to information about SW.
RI includes specifications that Validators validate objects against.

---

I'm not sure it's reasonable to expect what is appropriate for the Internet Archive's web archive to be appropriate elsewhere. For example, when accessing the content, the archive's visitors are expected to come to the Wayback Machine armed with the URL of the site they want. They look up the URL, choose the date, and download the items they want, and the interpretation of the content is left entirely to them. Very little metadata is required for discovery, and the IA only need to support access at the protocol level (HTTP has been pretty stable so far).

I think the web archive is quite exceptional in this regard and that, in order to be enable their users to discover and use their collections effectively, most other institutions will have to understand how to interpret their content. For example, to support full-text search, some sort of transformation to plain text is required. One must choose therefore choose whether to make this text version an archival artefact (which assumes it could never be improved), or whether to support the software required to re-parse the original items in order to be able to generate new indexes in the future. Similarly, 

NOTE: DHT+Range Queries?

https://github.com/tomp2p/TomP2P/blob/master/examples/src/main/java/net/tomp2p/examples/ExampleDST.java

---

Misc. Blog Ideas
 - Format features for standards. Eg mime type embed. 
 - Why open? Other issues than code.
 - Comms not content.
 - OPF: How to join in... (also collect stuff from SF TRAC wiki)
 -    - [https://sourceforge.net/apps/trac/planets-suite/][1]  
 - OPF: Reponse to Planets Testbed Review
 -    - In reponse to [http://e-records.chrisprom.com/?p=1183][2]  
 - OPF:  The need for a roadmap.
 -    - [http://gamearchitect.net/Articles/SoftwareIsHard.html][3] 
   - [http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html][4] 
   - [http://www.jisc.ac.uk/events/2010/07/jif10/virtualgoodybag/understandingsustainability.aspx][5] 
 - OPF: Blog on other systems and similarities:[][6] 
 -    - [http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx][7] 
   - Each has a plug-in architecture, each has a new GUI, need to share....
   - [http://inkdroid.org/journal/2010/08/24/notes-on-retooling-libraries/][8] 

 - Blog idea: THE ROBOT[][9] 
 -    - [http://www.youtube.com/my_videos][10] 
   - [http://www.youtube.com/watch?v=3L44R9FJ-9U][11] 
 - On The Naming Of Things
 - On Preserving Conversations
 -    - Blog on HTTP v. HTML
   - Connect to DSHR blog. [http://blog.dshr.org/2010/06/jcdl-2010-keynote.html][12]  

  - Software Engineering versus Computer Sciece. CS4SC? Comp-to-Data arc.
http://www.delicious.com/beardedstoat/cs4sc

Coding at Scale
---------------

Scaling Issues: File numbers

* DROID file handles
* Results, all in memory, JHOVE v Tika.
* Also, Tika at scale issue, where keeping the same class was building up RAM? Need to reinstanciate to make things stop going OOM and/or running OOFileHandles. (???)

Scaling issues: File size, 
Aggressive random-access-file opening:
https://github.com/openplanets/droid/commit/2c9f9b1a86e3fd219ecc8b8ed4cde0b81cfe2057

If you want to really optimise this thing, it should be possible to do all this (including checksum calculation) while only streaming over the whole input stream once. I've been trying to do that in our web archive indexer (which also incorporates the Nanite tool) with some success, but gracefully handling large files is not proving easy when some tools (e.g. DROID, PDFBox Preflight) tend to assume that you have a random access file and can flip to the end of the bitstream and back easily.


Iteration
---------

* http://rkroundtable.org/2014/06/30/contexts-connections-access-the-glorious-possibilities-of-getting-it-all-wrong/
* http://blog.codinghorror.com/quantity-always-trumps-quality/




  [1]: https://sourceforge.net/apps/trac/planets-suite/
  [2]: http://e-records.chrisprom.com/?p=1183
  [3]: http://gamearchitect.net/Articles/SoftwareIsHard.html
  [4]: http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html
  [5]: http://www.jisc.ac.uk/events/2010/07/jif10/virtualgoodybag/understandingsustainability.aspx
  [6]: http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html
  [7]: http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx
  [8]: http://inkdroid.org/journal/2010/08/24/notes-on-retooling-libraries/
  [9]: http://www.naa.gov.au/records-management/secure-and-store/e-preservation/at-naa/software.aspx
  [10]: http://www.youtube.com/my_videos
  [11]: http://www.youtube.com/watch?v=3L44R9FJ-9U
  [12]: http://blog.dshr.org/2010/06/jcdl-2010-keynote.html
  [13]: http://blogs.ecs.soton.ac.uk/keepit/2010/08/23/keepit-course-3-describing-significant-characteristics-and-recording-provenance/
  [14]: http://digital-scholarship.org/dcpb/dcpb.htm
  [15]: http://lists.ala.org/wws/arc/digipres/2010-08/msg00007.html
  [16]: http://www.digitalpreservation.gov/ndsa/
  [17]: http://www.digitalpreservation.gov/ndsa/
  [18]: http://www.software.ac.uk/SustainingSoftware.html
  [19]: http://www.culturegrid.org.uk/
  [20]: https://sourceforge.net/mail/admin/list_subscribers.php?group_id=265364&amp;group_list_id=68391&amp;func=display



