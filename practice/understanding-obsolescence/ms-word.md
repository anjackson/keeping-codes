---
title: MS Word
subtitle: .doc
layout: default
category: Formats
status: stub
publish: true
---

### Pre-1995 ###
Difficult to identify...

These are only identified by Tika, but may be down to file extension.
http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19961029183743/http://tornado.badc.rl.ac.uk:80/data/aase/document/readme.doc
http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19961029183904/http://tornado.badc.rl.ac.uk:80/data/aase2/document/contact.doc

DROID spots only this V6 one?
http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19961101023442/http://zeus.codex.co.uk:80/sem-demo/semwebpl.doc

Hm, first two may be text, this looks more likely:

http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_type_ext%3A%22.doc%22&f[1]=content_ffb%3A%22fe370023%22
Based in part on example from 
http://fileformats.archiveteam.org/wiki/DOC
http://msxnet.org/word2rtf/formats/ffh-dosword5#16.1

Based on that, e.g. 0x31be0000
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_ffb%3A%2231be0000%22

Similarly for v 6.0: 6031* not many, just one, but appears to be malformed HTML?
"all full-saved Word documents begin with 0x6031, 0x000, 0xAB00"
http://www.webarchive.org.uk/aadda-discovery/formats?f[0]=content_ffb%3A6031*

A range of FFB popular combos that remains unclassified. eg. %FE7%00# and related that may be early Word documents.
File says they are MSOffice, but they upset Tika rather badly.
Droid says: application/msword; version=5.0

### DOCX ###
* https://twitter.com/euanc/status/482526239140626433

