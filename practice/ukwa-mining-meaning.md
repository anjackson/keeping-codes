---
title: Mining For Meaning
subtitle: Lessons Learned From Data-Mining The UK Web Archive
layout: default
categories: Web Archives
status: stub
---

# Strands

* Breadth of user needs.  ‘I know exactly what I want’ is not representative of most of our users. They generally start with one question and then it shifts and changes under them as they get used to the nature of the archive and the search capabilities.
* A new mode Information Retrieval. Our users are not only looking for specific documents, so the usual framing of IR ‘information needs’ does not fit here.
* User-led search configuration. Related to the previous point. Empowerment an choice over black-boxes.
* Danger of assumptions over data, use of random sample to fight against it.
* Danger of https://en.wikipedia.org/wiki/Hindsight_bias ?

http://historyonics.blogspot.fr/2014/11/big-data-small-data-and-meaning_9.html

# Abstract 

At the UK Web Archive, we have been working with historians of modern history or order to understand how best to help them explore and exploit the JISC UK Web Domain Dataset (1996-2013). This large collection, some 57TB of compressed ARC and WARC files containing about four billion resources, presents a major challenge to our standard discovery mechanisms. This is further complicated by the fact that our researchers need to learn how to approach the data just as much as we need to learn how best to expose the data to them.

Our iterative strategy has been based on using data-mining techniques to populate a large, richly-faceted fulltext search index. This provides a performant platform from which the use of terms can be tracked page-by-page, while supporting complex facets which allow us to provide additional metadata and contextual information and that enable our researchers to slice and dice the dataset into more manageable pieces. For example, by storing the crawl date in the index, we can slice the data by time-frame, and therefore study how the usage of terms (and indeed any other facets) shift and change over time. Both the indexing methodology and the user interface have been developed under an 'agile' approach, using real researcher feedback to help steer the development of this system.

That process has taught us a lot about how to cope with the scale of the data, but more importantly, it has led to significant changes not only in the way we index, but even in the way we harvest the web. Working closely with historians has emphasised the need to collect contextual information about the crawl and the content in order to ensure that researchers can get what they need from our archives. In this paper, we will present lessons we have learned so far, and present our vision for the future.


* [Tuesday 4 November – Interrogating the archived UK web: Historians and Social Scientists Research Experiences](http://ihrdighist.blogs.sas.ac.uk/2014/10/28/tuesday-4-november-interrogating-the-archived-uk-web-historians-and-social-scientists-research-experiences/)
* [Interrogating the Archived UK Web – postscript](http://ihrdighist.blogs.sas.ac.uk/2014/11/06/interrogating-the-archived-uk-web-postscript/)
* [Big Data, Small Data and Meaning](http://archiveshub.ac.uk/blog/2014/11/big-data-small-data-and-meaning/)
* [Big Data, Small Data and Meaning](http://historyonics.blogspot.co.uk/2014/11/big-data-small-data-and-meaning_9.html)
* [Big Data for Dead People: Digital Readings and the Conundrums of Positivism](http://historyonics.blogspot.co.uk/2013/12/big-data-for-dead-people-digital.html)
* [Web Archives as Big Data, 3 December 2014](https://gist.github.com/drjwbaker/3bce1164a1834785ab7a)

General IR Stuff
* http://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html
* 

Biases and correctives. Normalisation strategies, c.f. Google Books, etc.

RCT?

[A Distinction worth Exploring: “Archives” and “Digital Historical Representations”](http://www.archivesnext.com/?p=3645)

Statistics and issues
* https://news.ycombinator.com/item?id=7287665
* [Biblio bizarre: who publishes in Google Books](http://sappingattention.blogspot.co.uk/2014/04/biblio-bizarre-who-publishes-in-google.html)
* [the meaning of statistics and digital humanities](http://lab.softwarestudies.com/2012/11/the-meaning-of-statistics-and-digital.html)

[Operationalizing and the Natural Sciences](http://www.scottbot.net/HIAL/?p=40224)
https://en.wikipedia.org/wiki/Intersubjective_verifiability

[Lessons from science part the third: why we do what we do](http://cradledincaricature.com/2014/03/12/lessons-from-science-part-the-third-why-we-do-what-we-do/)

[Digital history and the death of quant](http://britishlibrary.typepad.co.uk/digital-scholarship/2014/04/digital-history-and-the-death-of-quant.html)

>
>
> Humanistic thinking does not proceed by experiments that yield results; it is a matter of mental experiences, provoked by works of art and history, that expand the range of one’s understanding and sympathy.
> 
> This is why the best humanistic scholarship is creative, more akin to poetry and fiction than to chemistry or physics: it draws not just on a body of knowledge, though knowledge is indispensable, but on a scholar’s imagination and sense of reality.
>
> http://www.newrepublic.com/article/117428/limits-digital-humanities-adam-kirsch
>

> http://text-patterns.thenewatlantis.com/2014/05/my-response-to-adam-kirsch.html

> http://www.matthewjockers.net/2014/05/07/so-what/

> 
> [What Is "Digital Humanities," and Why Are They Saying Such Terrible Things about It?](http://mkirschenbaum.files.wordpress.com/2014/04/dhterriblethingskirschenbaum.pdf)

When making statements about the world, experimental evidence is how you raise mere consensus to something approaching truth.

when I doubt there's any consensus on the "Humanities".

Almost as much fun as all that malarky about defining "Digital Humanities".
Somehow with the implication that if you can't define it you shouldn't be taken seriously.

Outline
=======

* Two-fold challenges:
    * Indexing large collections
    * Suitable for analytics
* Indexing strategies:
    * Indexing into HDFS
    * Handling deduplication.
 * Preservation Features
    * Format and risk scanning included.
 * c.f. Sustainable Access writing.

Future work, timeline reconstruction. Missing 3xx, 4xx, 5xx, DNS FAIL, transient crawler errors, etc.

Information Retrival Models
===========================

Two modes of use. 

* Traditional IR case, where we are looking for a particular resource or small set of resources to examine in detail.
* Analytical/Evidential IR case, where we wish to say something about the entire dataset, and are really trying to infer something about the population that created the information, rather than the information itself.


Genre
-----
* http://tedunderwood.com/2014/12/29/how-to-find-english-language-fiction-poetry-and-drama-in-hathitrust/
* Genre in web archives
* NOT "<genre> -'Web site'; supplied by system" from http://lcweb2.loc.gov/diglib/lcwa/html/lcwa-techinfo.html
* [Common Criteria for Genre Classification: Annotation and Granularity](http://ceur-ws.org/Vol-205/paper9.pdf)
    * [Web Genres for Download](http://www.nltg.brighton.ac.uk/home/Marina.Santini/#Download)

Twisted Timelines
=================

Looking up phrases.

Captcha
-------

 * http://web.archive.org/web/20030110182448/http://news.bbc.co.uk:80/1/hi/technology/2635855.stm
 * http://web.archive.org/web/20030123152944/http://www.computing.co.uk:80/News/1137729 (earliest publication date)
 * http://web.archive.org/web/20030208002757/http://www.chrisjames.co.uk:80/cj/contents/pages/cat_techie.php
 * http://web.archive.org/web/20021229115410/http://www.theregister.co.uk/content/6/28694.html

Tracing Sources & Twists
------------------------
 * http://downtrend.com/71superb/professor-called-racist-for-correcting-black-students-grammar-and-punctuation/
 * No 'sort by crawl date', makes tracing to source harder.
 * https://www.insidehighered.com/news/2013/11/25/ucla-grad-students-stage-sit-during-class-protest-what-they-see-racially-hostile
     * https://www.insidehighered.com/news/2013/11/25/ucla-grad-students-stage-sit-during-class-protest-what-they-see-racially-hostile#comment-1138447698
 * http://dailybruin.com/2013/11/20/submission-moore-hall-sit-in-addressing-discrimination-lacked-open-tolerant-spirit/
 * Can we do more to trace to source? Not just crawl date, but metadata, links, etc.?

Also

 * [Chillax](http://web.archive.org/web/19991002215401/http://members.tripod.co.uk:80/Chimwemwe/)
 * information superhighway
 * web 2.0
 * cyberspace
 * world wide web
 * the web
 * chav (Peak Chav c. 2005)
 * al queda
 * guest book, hit counter?
 * etc...


 As Natalia Cecire mentions, when critiquing the masculine DH metaphors of “building” and “mining” and digging,”

    “the field might look very different if dominant metaphors for ‘doing’ digital humanities research included weaving, cooking, knitting, and raising or nurturing.”

Curation's second death
=======================

[What Could Curation Possibly Mean?](http://blogs.loc.gov/digitalpreservation/2014/03/what-could-curation-possibly-mean/)

Curation has died before, on the web. Story of DMOZ and Google (and indeed Yahoo).

* [https://wiki.digitalmethods.net/Dmi/DemiseDirectory](The Demise of the Directory: Web librarian work removed in Google)
* [see also](http://blogoscoped.com/archive/2006-04-21-n63.html)
* [Yahoo killing off Yahoo after 20 years of hierarchical organization](http://arstechnica.com/information-technology/2014/09/yahoo-killing-off-yahoo-after-20-years-of-hierarchical-organization/)
* [Metadata Quality, Completeness, and Minimally Viable Records](http://vphill.com/journal/post/4075)

Spam problem.

But how do we know the algorithm is enough. Need humans to ensure value is reflected, and to try and address any gaps.

Curation is no longer absolute - no longer an attempt to tag and categorise into some universal ontology. Powered by social media constructs, curation now means a million tiny cliques of consensus. This may seem a backward step, but this loosely-coupled arrangement allows any real consensus to emerge at it's natural scale. EXAMPLES.

Rather like a folksonomy versus an ontology. All 'top down' ontologies requires consensus first, and although this might lead to a 'cleaner' data set, this also holds back adoption and growth and sets a high bar for communication and consensus-building. The 'bottom up' taxonomies like those on Flickr allow consensus to emerge more naturally, but also exposes conflict and inconsistency.

Some parallel to one-way web links versus two-way ones, which required consensus between two parties to be formed before a link could be established.

And so, where this consensus might apply to you, this allows search engines to augment their 'universal' full-text search and bring in results and rankings based on the value that others have implied through their acts of curation. It is not yet clear how well this will actually work in practice, but this seems to be the vision of the search engine giants.

As an aside, I suspect that this is why Google (among others) are so keen on authentic identities on the web. By trying to keep the social networks free of the false accounts that are the usual tool of spammers or trolls, they are attempting to prevent the arms race that has dogged them this far.

 is that the authentic opinions of individuals building things on the web will 


Libraries and the web: 
- https://coffeecode.net/archives/301-Library-catalogues-and-HTTP-status-codes.html


Link Dynamics
- [Where do bloggers blog? Platform transitions within the historical Dutch blogosphere | Weltevrede | First Monday](http://firstmonday.org/ojs/index.php/fm/article/view/3775/3142)

Data Mining Methodology
-----------------------
The emphasis on big data and statistical analysis in cultural and social contexts makes me uneasy. There is no 'noise' in humanities data sets. There are only silenced voices.
The direct adoption of big data/statistical methods makes me uneasy. There is no 'noise' in humanities data. There are only silenced voices.

Other: false positive scaling problem http://mobile.theverge.com/2012/10/28/3567048/carnegie-mellon-video-surveillance-action-recognition

- Every data point is a thought, a mind, etc
- Those future users who will, with tears in there eyes, click Save As...
- Publishers memory to truly a national memory. Our people's memory
- Archives of emotion

Mining For Meaning: Methodologies for meaningful data mining of web archives. 


