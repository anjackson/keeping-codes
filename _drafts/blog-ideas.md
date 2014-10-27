---
title: Blog Ideas
---

## Ideas, briefly:
- Functional Programming Brain Hurt
    - Feels like when I'm solving hand puzzles, or some cryptic crossword clues. I can feel my way to the right answer, but I frankly don't quite understand it until afterwards.
- Maps as metaphors for languages and models.
- flindex: Flat Index
- I have mixed feelings about "The perfect is the enemy of the good." It's true, but I've seen it used to justify very sloppy work.…when the real problem has been that the 'perfected' proposal is simply disconnected from reality, or an excuse not to talk to users, or 
- CDX Dataset
- Finish off half-life 1000 once Solr is fixed. Then BLOG.
- [Domain crawl graphs](https://intranet.bl.uk:8443/confluence/pages/viewpage.action?pageId=139630062)
- CC License adoption
- Don't &lt;blink> -- obsolete elements from the web archives
    - Plus &lt;marquee>  ... ?
- Fashions in Styling, CSS versus &lt;font>
- clear.gif -- tracking images through the web.
- CAPTCHA, see {% include crossref.md page="ukwa-mining-meaning" %}.
- Nanite (what to say?)
- Web archiving RI use case e.g. <http://britishlibrary.typepad.co.uk/webarchive/2011/12/advent-calendar-december-3rd.html>
* Using UKWA to preserve your project.
- Islands in the UK Domain
- <http://www.openplanetsfoundation.org/blogs/2014-03-24-arc-warc-migration-how-deal-de-duplicated-records>
- [This Is For Everyone - (c) All Rights Reserved](http://gty.im/149366163)
- Integrating International Archives
    - DHT+Range Queries, [e.g. ExampleDST.java](https://github.com/tomp2p/TomP2P/blob/master/examples/src/main/java/net/tomp2p/examples/ExampleDST.java)?
 - On The Naming Of Things
 - On Preserving Conversations
   - Blog on HTTP v. HTML
   - Connect to DSHR blog. <http://blog.dshr.org/2010/06/jcdl-2010-keynote.html>
- Software Engineering versus Computer Sciece. CS4SC? Comp-to-Data arc. <http://www.delicious.com/beardedstoat/cs4sc>
- Format Herd Immunity
    - Format obsolescence as disease 
    - We are the immune system 
- Data And Metadata, interpretation difference.
- eBook wars, like early years of DRM music etc.
- Files versus filesystems. Latter obsolete first, former at risk due to persistent ram plus walled gardens.
-  Is ISO Enough? Open standards etc.
- [Endangered Languages -- Scottish Gaelic](http://www.endangeredlanguages.com/lang/3049)
* Characterising Codes
- Beyond OAIS
    - why OAIS is a straight-jacket and limits the care digital media needs.
- Compression Is Not A Significant Property
- Preservation Planning - Baysian versus frequentist... First principles/ab initio or Empirical modelling.
- Simplification pressure? e.g. Markdown or even Wikipedia? REST over SOAP. HTML over PDF? Others?
* BLOG: Building Trust (Format Registries)
* BLOG: Format data model - what is permanent? Why opaque IDs.
* BLOG: The long-tail of formats
* BLOG: Identifying Microsoft formats. Why DROID and File fail. JHOVE2 it. Use those os and office installers or images to make test corpus?
* TODO BLOG: Preserving processes, software and test suites.
- Wikipedia's echo chamber - Deletionists - Self reinforcing etc.
- QA costs and variation - "QA for emulation can be at an environment rather than object level so potentially cheaper" <https://twitter.com/euanc/status/375272042511491072>
- My fathers story - Learning to geek
- Career planning computer - And jobs that didn't exist.


## Fragments

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


### Standards For Fragments

Issue about CITE paper, W3C Fragment effort, and issue about whether the fragment can reference the entity rather than the resource.

<http://www.ariadne.ac.uk/issue67/blackwell-hackneyBlackwell/> <http://www.w3.org/2008/WebVideo/Fragments/>

In particular, if we wish the fragment identifiers to be insulated from some details., i.e. fractions used be CITE rather than pixels, we need to get that in the standard? It does % for spatial dimensions, so is that okay? is that precise enough? What if we want to point at something really small? How many SigFig.


### Cargo Cult Standards

p.s. and if I anyone starts writing yet another standalone identifier, provenance or metadata standard from scratch, I will come around to your house, take away your computer, and replace it with a Chrome tablet so you always have to GOOGLE IT FIRST. :-)

Every time you start writing a new standalone metadata standard from scratch, God kills a kitten. Please make it stop.


### Letters to my son

- Plans for digital preservation
- Scaleability from the low side, to contrast with BL scale later.
- A business opportunity?
- Costs manageable via scale?


### Coding at Scale

Scaling Issues: File numbers

* DROID file handles
* Results, all in memory, JHOVE v Tika.
* Also, Tika at scale issue, where keeping the same class was building up RAM? Need to reinstanciate to make things stop going OOM and/or running OOFileHandles. (???)

Scaling issues: File size, 
Aggressive random-access-file opening:
https://github.com/openplanets/droid/commit/2c9f9b1a86e3fd219ecc8b8ed4cde0b81cfe2057

If you want to really optimise this thing, it should be possible to do all this (including checksum calculation) while only streaming over the whole input stream once. I've been trying to do that in our web archive indexer (which also incorporates the Nanite tool) with some success, but gracefully handling large files is not proving easy when some tools (e.g. DROID, PDFBox Preflight) tend to assume that you have a random access file and can flip to the end of the bitstream and back easily.

### Iteration

* http://rkroundtable.org/2014/06/30/contexts-connections-access-the-glorious-possibilities-of-getting-it-all-wrong/
* http://blog.codinghorror.com/quantity-always-trumps-quality/


Knowing first is impossible
"Need to be very *very* clear about what is to be preserved before developing tools"
<https://twitter.com/mopennock/status/375271606085378048>


 -    - [http://gamearchitect.net/Articles/SoftwareIsHard.html][3] 
   - [http://www.codinghorror.com/blog/2006/04/best-practices-and-puffer-fish.html][4] 
   - [http://www.webarchive.org.uk/wayback/archive/20121225045735/http://www.jisc.ac.uk/events/2010/07/jif10/virtualgoodybag/understandingsustainability.aspx][5] 


### Programmer versus car mechanic

http://www.codinghorror.com/blog/2012/05/please-dont-learn-to-code.html
http://www.codinghorror.com/blog/2012/05/so-you-want-to-be-a-programmer.html
programming versus writing, not all of us need to be novelists.



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



