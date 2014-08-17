---
title: Archiving the Dynamic Web
layout: default
category: Web Archives
tags: [draft]
publish: true
permalink: /keeping-codes/practice/archiving-the-dynamic-web.html
redirect_from: "/keeping-codes/practice/Archiving%20the%20Dynamic%20Web.html"
---

## Introduction ##
Of the [many challenges facing those of us who attempt to preserve the web](http://blog.dshr.org/2012/05/harvesting-and-preserving-future-web.html), one of the most pressing is the highly dynamic nature of many modern websites. The Wikipedia SOPA blackout banner case study shows how this can prevent both crawling and playback.  That example is bad enough, but unfortunately there are many more cases like this, but where almost all artefacts presented on the page are pulled down dynamically via JavaScript. Occasionally, even relatively simple constructs like conditional comments have caused problems (c.f. gov.uk rendering thread). In general, as the level and dynamic sophistication is increased, our ability to reliably reconstructing the intended interpretation outside the context of a browser becomes more error prone. 

Fortunately, recent web browser developments, and their use on mobile platforms, has lead to some very nice, compact, embeddable rending engines. In particular, the WebKit engine has been very successful, and has lead to a number of embedded forms:

* [WebView](http://docs.oracle.com/javafx/2/api/javafx/scene/web/WebView.html) and [WebEngine](http://docs.oracle.com/javafx/2/api/javafx/scene/web/WebEngine.html) - a WebKit rendering component, originally part of JavaFX but now a standard part of the Java 7 JRE.
* [PhantomJS](http://phantomjs.org/) - a headless WebKit browser with a JavaScript based scripting interface.
* [Ghost.py](http://jeanphix.me/Ghost.py/) - an embedded WebKit browser with a Python interface, that also supports plugins (e.g. Flash).

This kind of tool is often intended to be used to aid development and regression testing for web site generator software, but can also be used to help web archiving. We have been experimenting with PhantomJS, and this document outlines how our crawler architecture might develop over time.

## Architectures ##

### Current Architecture ###

Currently, for every seed, we render the root page via an embedded browser, as outlined below. 

![Asynchronous Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-async.jpeg)

As the crawl proceeds, every time Heritrix3 starts processing a new seed URL, that URL is also POSTed to a RabbitMQ message queue using our [AsynchronousMQExtractor](https://github.com/ukwa/bl-heritrix-modules). An entirely separate [WebTools service](https://github.com/openplanets/wap/tree/master/WebTools
) polls the message queue, and runs a PhantomJS script that collects the URLs of the resources required to perform the rendering. It then saves the rendering as a screenshot, and pushes the list of URLs into Heritrix3's 'action directory', which instruct the crawler to download those URLs promptly. 

This has worked reasonably well, but suffers in a couple of areas.

We treat every known host and every manually annotated URL as a seed, and so around four million URLs will be rendered, out of a total of around 1.3 billion URLs. (TBA Something on tunable rendered fraction). Those four million screenshot processes take some time, and as we are only running one WebTools service at the moment, the time that elapses between the two processes can be rather long. This means the URLs downloaded by Heritrix may not be valid by the time the download is attempted.

A more serious problem is that this approach downloads everything twice, from two independent contexts, with different sessions, user agents, etc. This means that not only are we downloading the same things too often, but that the two sets of required URLs can be inconsistent. In particular, it is common to bundle up CSS files on a per-session basis, and so the list of URLs required to render a page in the embedded browser may not be the same as those in Heritrix3. As Heritrix3 downloads the main page, and the embedded renderer is only used to determine transcluded resources, the composite archive is inconsistent.

### Synchronous Rendering ###
One way to solve the time-lag problem would be by having a larger array of WebView services consuming the message queue. We will probably experiment with that first.

However, it may instead be preferable to bring the two closer together, and perform the rendering synchronously, during the crawl, thus guaranteeing that the results would be as timely as possible.

![Synchronous Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-sync.jpeg)

This architecture would mean that the overall crawl would proceed more slowly, particularly at first. However, based on our experience so far, we do not believe this would be a major problem. The embedded renderers are very efficient, and during the first domain crawl we successfully collected the entire set of asynchronous screenshots long before the crawl drew to a close.

Taking this even further, it would be possible to bring the rendering process right inside Heritrix3.

![Synchronous Embedded Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-sync-embed.jpeg)

Given the existence of the WebEngine component, it should be possible to do this using only pure Java 7 code rather than calling our to PhantomJS. Having said that, one issue with running a full rendering engine is that it exposes the service to possible browser-based exploits. This is not all that likely when running an odd, embedded browser on an non-mainstream platform (ours run on a flavour of Linux), but precautions should still be taken to ensure that the machine can be rebuilt easily if compromised.  Due to the large amount of complex state managed by the current Heritrix3 architecture, this would not be an advisable architecture.

### Army of Ghosts ###
The other problem we mentioned above was that of the doubly-downloaded, inconsistent content. One solution is to send the full request headers to the WebView service, thus ensuring the session and other information are the same. This is a sensible step, but it still seems unsatisfactory that every URL is being downloaded twice. To avoid that, a much larger change to our architecture would be required.

![WARC Writing Proxy](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-writer-proxy.jpeg)

In this scheme, we still use Heritrix3 (essentially as a crawl frontier queue management engine), but the WARC writing (including de-duplication) is all handled via a dedicated proxy (such as [warcprox](https://github.com/internetarchive/warcprox) or [LAP](https://github.com/INA-DLWeb/LiveArchivingProxy)). This architecture is much easier to scale out, e.g. using [SQUID as a load balancer](http://wiki.squid-cache.org/Features/LoadBalance#CARP_:_Cache_Array_Routing_Protocol). 

It also allows us to use a single WARC backend for a wide range of manual or automated archiving processes, and keeps all of the deduplication logic close to the writers and out of the crawlers. (TBA More about how this opens up scaling out on both sides, i.e. army of ghosts)

## Quality Assurance ##

### Crawl-level QA ###

[Monitrix](https://github.com/ukwa/monitrix)

### Near Real-Time Playback QA ###

OpenWayback hooked in to evaluate playback ASAP.

### Preserving the Render ###

Would be good to package the screenshots into WARCs into some standard form. Would also be good to capture the extracted URL lists and the final DOM trees and store those too. This would make it easier to perform QA on future preservation actions.

http://docs.oracle.com/javafx/2/api/javafx/scene/web/WebEngine.html#getDocument()

## The Elastic Crawler ##

To spec.


## Other problems ##

http://www.dlib.org/dlib/november13/kelly/11kelly.html

## Components ##

* Crawl Metadata, User Agent etc.
* Seeds (text file)
* DecideRules
* FrontierPreparer
* QuotaEnforcer
* Canonicalisation
* uriUniqFilter
* IP/Robots.txt info validity/timeout.
* Fetchers
* Extractors
* PeristLog
* FetchHistory
* Sheets
* Our custom stuff, IP sheets etc.
* WARC Writers, disk space monitoring, etc.

Heritrix3 queues, per host.
This enforces delay?
Queue rotation behaviour?

Coping with millions of queues?

* [Kafka can't](http://mail-archives.apache.org/mod_mbox/kafka-users/201310.mbox/%3CCA+Vbu7zMRWuLiVLzC+iAdX+XJUb3xdZHaunxGJzNsC9QwrtYSg@mail.gmail.com%3E)
* [RabbitMQ can](http://lists.rabbitmq.com/pipermail/rabbitmq-discuss/2009-February/003042.html)
* [Kestrel?](https://github.com/twitter/kestrel) which is used with Twitter Storm.

But do we need millions of queues? Do they only exist as a means of helping enforce the crawl rate?

[When taking a snapshot Heritrix renames crawl.log](https://webarchive.jira.com/wiki/display/Heritrix/When+taking+a+snapshot+Heritrix+renames+crawl.log)

[Frontier queue budgets](https://webarchive.jira.com/wiki/display/Heritrix/Frontier+queue+budgets)
[BdbFrontier](https://webarchive.jira.com/wiki/display/Heritrix/BdbFrontier)

SQUID + CARP (Cache Array Routing Protocol) and N * LAP/warcprox
OR
CrawlBolts keep track of proxies via ZK and route on host hash.
IF
This is really necessary? Alternative is simply to store duplicate info in Cassandra.
In principle, the Archiving Proxies could do much of this:
- Crawl-delay
- Retries?
Probably too complex. Perhaps better to have separate CASSANDRA table like:
- ( ((hash), SURT, UUID), WARC-Record-Type, WARC, Offset )
- Use this to decide duplicates, store or write re-visit, etc.

URIs table used for crawl/frontier:
- ( ((host), SURT, crawl_time), URI, hash?)


http://commoncrawl.org/common-crawl-move-to-nutch/
A WARC writer added to Nutch: 
https://github.com/Aloisius/nutch/commit/3ef169ad5402cee35346f566c85c237b5d128495
versus
https://github.com/commoncrawl/commoncrawl-crawler

See also [StormScraper](https://github.com/tjake/stormscraper), and [associated slides](http://www.slideshare.net/tjake/storm-and-cassandra#), e.g. [this topology overview](http://www.slideshare.net/tjake/storm-and-cassandra/30).

Not clear complex features like queue rotation are strictly required. May make more sense to start with something simpler. In fact, it probably makes sense to think a bit more radically about the whole thing, and investigate the possibility of switching over to true 'continuous crawling'.

So, aspects are that e.g. using Storm or similar makes long-running processes easier. Also the need to 'crawl right now' needs to sit alongside the 'has not been crawled since X and is due' and the 'big crawl' more easily.

Balance between the queues and the state (e.g. Cassandra/HBase is less clear now).

* IN: system, high-priority and low-priority queues of URLs.
* SPOUT: Watch the queues, in priority order, occasionally skipping down to avoid total queue backlog.
* DISTRIBUTE: URLs grouped on Host.
* BOLT: Pause based on crawl delay (STATE NEEDED)
    * URL comes in.
    * Look up last known Crawl-Delay and last known crawl timestamp.
    * Wait until time has passed before emitting.
* BOLT: Download resource (embedded browser OR old-style GET):
    * BOLT: Record success in State.
    * BOLT: Append to WARC (if old-style).
    * BOLT: Extract links:
        * BOLT: Check links against State, and DecideRules, and Enqueue if crawl is due.
            * BOLT: Record link discovery in State.


See also

* [AJAX/JavaScript Enabled Parsing with Apache Nutch and Selenium](http://soryy.com/blog/2014/ajax-javascript-enabled-parsing-apache-nutch-selenium/)
    * https://github.com/momer/nutch-selenium-grid-plugin
