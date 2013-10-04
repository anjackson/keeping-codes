---
title: Finding Formats
layout: default
categories: [experiments]
tags: [stub]
publish: false
---

How do I go about hunting down a format I don't understand.

* Search for file extension, sometimes fails (.s5).
* Search for encodings of the first few bytes (worked for some, e.g. s5 etc.)


Case of DAb2/DabF

* Started by this: https://twitter.com/anarchivist/status/383666204369780736
    * "I have a database file from a classic Mac system & I'm trying to figure out the originating software. Type: "DAbF"; creator: "DAb2". Ideas?"
* No FFB, no .ext
    * "Byte 0 is 0x0F, and bytes 1-15 seem to be a last modified date in "MM/DD/YYhh:mmpm" format."
* BUT some OS/system info and image of icon.
    * http://twitpic.com/df5meq
* Random searching for early Mac screens (Google Image Search for 'Mac System 7')
    * https://encrypted.google.com/search?q=system+7&hl=en&source=lnms&tbm=isch&sa=X&ei=LN9GUozfLc-rhAeR-oGgCw&ved=0CAkQ_AUoAQ&biw=1280&bih=679&dpr=1#hl=en&q=mac%20system%207&revid=64016564&tbm=isch&facrc=_&imgdii=_&imgrc=qCj3Ffe6mQ4wiM%3A%3Be63k9sCIhKPacM%3Bhttp%253A%252F%252F25.media.tumblr.com%252Ftumblr_m49x7rTasR1rqafsoo1_1280.png%3Bhttp%253A%252F%252Fmacfloppy.tumblr.com%252F%3B512%3B342
* Found images like this:
    * http://macfloppy.tumblr.com/post/22271289226/the-system-folder-in-system-6-expanded-quite-a-bit
    * Note 'DA Handler'
* Searching for 'apple DA Handler' lead me to this:
    * http://www.mactech.com/articles/mactech/Vol.07/07.07/MultiWindowDA/index.html
    * Icon is very similar, so perhaps a file related to Desk Accessories?
    * http://en.wikipedia.org/wiki/Desk_Accessory#Apple_Macintosh


Aside, while railing down a dead end, learned about unpacking resource forks.

UnRezWack DAbase\ v2.09\ ShareWare -o DAbase
  829  RezWack -d DAbase\ v2.09\ ShareWare -r DAbase\ v2.09\ ShareWare/..namedfork/rsrc -o DAbase.wak
  830  UnRezWack DAbase.wak -o DAbase-wak

 mv DAbase\ v2.09\ ShareWare DAbase
  DeRez DAbase



Format Dynamics

Follow on from Formats over Time?

https://en.wikipedia.org/wiki/Resource_fork as archetypal failure of clever tech due to sharing problems.
