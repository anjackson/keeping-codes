---
title:  On Web Archiving
layout: default
categories: [practice]
tags: [stub]
publish: false
---

Content and Conversations: The Evolution of Web Archiving
---------------------------------------------------------

Building on http://blogs.loc.gov/digitalpreservation/2013/11/anatomy-of-a-web-archive/
BUT focusing on not simply that this is additional WARC data, but that preserving the headers is preserving a conversation. It is not merely and transport, etc. Early systems PANDAS HTTPTrack etc. focus on web as a mere transport, resulting in a collection of files. However, really, it is a protocol, and to capture everything that protocol can do, without prejuding the content, you need to preserve the conversation.

ARC does this by preserving the response headers, which sometimes are the only source of interpretive/contextual data. Simplest, this might be date stamps, but even the format may only be declared there (ascii encoding). etc.

WARC takes this a step further. Each record is wrapped in additional WARC headers to help preserve contextual information about the collection process and the integrity of the content. Moreover, it also allows us to preserve the request that elicited the response, and so allows us to understand what features of the request may have influence the response (e.g. user agent mobile sites, cookies logins, referrer google-search, etc.).

See also https://etherpad.mozilla.org/uadetection-usecases https://wiki.mozilla.org/UA/UseCases

Now, Accept-Language, there's a good one.

By preserving the conversation, we can ensure the fidelity of the process of playing that content back.

This is not sufficient - although we can preserve whatever conversation occurs, in order to allow a future user to explore a long-disappeared site, we need to accurately simulate the user process now. As web sites become increasingly interactive, this means we need more sophisticated crawlers (using embedded browser) to execute the JavaScript and capture the conversations behind each page. Similarly, our playback infrastructure needs to grow in order to allow this dynamic behaviour to be rendered reliably. OpenWayback.


Features
--------
Features not Properties.
http://www.evolutionoftheweb.com/?hl=en-gb#/evolution/day
Features over time, by browser, lovely.

Notes on Web Archiving
----------------------

* Introduction and basic processes.
    * Somewhat disconnected from process/user-simulation.
* Web Use and Web Studies
    * i.e. use cases for web archives
* Selection for Web Archives
    * Policy and process, would be good to compare pre/post LD and annotation model.
* Copying Websites
    * Some technical detail on server/translation/client archiving (c.f. process preservation.)
    * Somewhat disconnected, again.
* Hidden Web
    * The continuum of sophistication of user simulation is not explicit.
    * Somewhat disconnected, again.
* Access and Finding Aids
    * i.e. Discovery
* Mining Web Collection
    * i.e. more use cases
* Long-term preservation of web content.
    * Somewhat vague and OAIS focussed.
    * Very woolly on use of migration/emulation terms, and on how to integrate migrations.
    * No actual examples of obsolescence.
    * Note also that if you are not charged with access to a given resource, you may still be charged with it being discoverable, both via search and via linkage (in and out context).
* Large and small case studies with details.

Ideas
* Not at all user focussed beyond the use-cases.
* Does not make it clear that we are archiving a conversation, not resources. (may need to review to be sure, but the PANDAS->to->WARC story is not told AFAICT).
* Does not make it clear that the crawler is future user simulation.
* Separation of long and short term preservation is somewhat artificial - the current re-writing etc. is a preservation action. Lots happening already.
* A focus on annotation may help continuity of across the scales of selective to domain harvesting.
* No Memento, either as migration technology or more importantly, global, integrated discovery.
