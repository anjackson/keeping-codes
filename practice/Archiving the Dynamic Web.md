---
title: Archiving the Dynamic Web
layout: default
categories: [practice]
tags: [outline]
publish: true
---

## Introduction ##

## Architectures ##

### Current Architecture ###

![Asynchronous Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-async.jpeg)

H3 + PhantomJS via RabbitMQ 

https://github.com/ukwa/bl-heritrix-modules

https://github.com/openplanets/wap/tree/master/WebTools


### Synchronous Rendering ###

![Synchronous Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-sync.jpeg)

H3 + PhantomJS realtime (or near realtime) with the right Cookies.

![Synchronous Embedded Rendering](https://raw.github.com/anjackson/keeping-codes/gh-pages/practice/images/crawler-sync-embed.jpeg)


### Army of Ghosts ###

H3 or other browsers or manual users.

Load-balancing proxy, warcprox/LAP, local or shared deduplication,

## Quality Assurance ##

### Crawl-level QA ###

### Near Real-Time Playback QA ###

### Preserving the Render ###

Would be good to package the screenshots into WARCs into some standard form. Would also be good to capture the extracted URL lists and the final DOM trees and store those too. This would make it easier to perform QA on future preservation actions.

