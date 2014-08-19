---
title: User-Driven Digital Preservation
layout: default
categories: ["Web Archives", blog]
tags: [complete]
publish: false
---

First published at

---

When we archive the web, we want to do our best to ensure that future generations will be able to access the content we have preserved.  This isn't only a matter of keeping the digital files safe and ensuring they don't get damaged. We also need to worry about the software that is required in order to access those resources. 

For many years, the spectre of obsolescence and the ensuing [digital dark age](http://en.wikipedia.org/wiki/Digital_Dark_Age) drove much of the research into digital preservation. However, even back in 2006, [Chris Rusbridge was arguing that this concern was overblown](http://www.ariadne.ac.uk/issue46/rusbridge#File_formats_become_obsolete_very_rapidly_Excuse_me...), and [since at least 2007](http://blog.dshr.org/2007/04/format-obsolescence-scenarios.html), [David Rosenthal](http://blog.dshr.org/) has been arguing that [this kind of obsolescence is no longer credible](http://blog.dshr.org/2010/11/half-life-of-digital-formats.html).

The current consensus among those who care for content seems to have largely (but not universally) shifted away from perceiving obsolescence as the main risk we face. Many of us expect the vast majority of our content to remain accessible for at least one or two decades, and any attempt to predict the future beyond the next twenty years should be taken with a large pinch of salt. In the meantime, we are likely to face much more basic issues concerning the economics of storage, and concerning the need to adopt scalable collection management techniques to ensure the content we have remains safe, discoverable, and is accompanied by the contextual information it depends upon.

This is not to say obsolescence is no risk at all, but rather that the scale of the problem is uncertain. Therefore, in order to know how best to take care of our digital history, we need to find ways of gathering more evidence about this issue. 

One aspect of this is to analyse the content we have, and try to understand how it has changed over time. Examples of this kind of work include our paper on [Formats Over Time](http://arxiv.org/abs/1210.1714) ([more here](http://www.webarchive.org.uk/ukwa/visualisation/ukwa.ds.2/fmt)), and more recent work on embedding this kind of preservation analysis in our [full-text indexing processes](https://github.com/ukwa/webarchive-discovery) so we can [explore these issues more readily](http://britishlibrary.typepad.co.uk/webarchive/2014/07/how-much-of-the-uk-html-is-valid.html).

But studying the content can only tell you half the story - for the other half, we need to work out what we mean by obsolescence. 

If there is an open source implementation of a given format, then we might say that format cannot be obsolete. But if 99.9% of the visitors to the web archive are not aware of that fact (and even if they were, would not be able to compile and build the software in order to access the content), is that really an accurate statement?  If the members of our [designated community](http://en.wikipedia.org/wiki/Designated_Community) can't open it, then it's obsolete, whether or not someone somewhere has all the time, skills and resources needed to make it work. 

Obsolescence is a [user experience problem](http://en.wikipedia.org/wiki/User_experience) that ends with frustration. So how can we better understand the needs and capabilities of our users, to enable them to help drive the digital preservation process?

To this end, and working with [the SCAPE Project](http://www.scape-project.eu/), we have built a prototype service that is designed to help us find the content that users are having difficulties with, and where possible, to provide alternative ways of accessing that content. This prototype service, called [Interject](http://www.webarchive.org.uk/interject/), demonstrates how a mixture of feedback systems and preservation actions can be smoothly integrated into the search infrastructure of the UK Web Archive, by acting as an 'access helper' for end users.

For example, if you go to our [historical search prototype](http://www.webarchive.org.uk/aadda-discovery/) and [look for a specific file called 'lostcave.z80'](http://www.webarchive.org.uk/aadda-discovery/search?text=lostcave.z80&sort_by=solr_document&sort_order=ASC&f[0]=content_type_norm%3A%22other%22) you'll see the Internet Archive has a number of copies of this old ZX Spectrum game but, unless you have an emulator to hand, you won't be able to use them. However, if you click 'Use our access helper', the Interject service will [inspect the resource](http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19981207063144/http://www.zenn.demon.co.uk:80/com/reviews/games/Lostcave.z80), summarise what we understand about it, and where possible offer transformed versions of that resource. In the case of 'lostcave.z80', this includes a [full browser-based emulation](http://www.webarchive.org.uk/interject/view/action%2Fjsspeccy/http://web.archive.org/web/19981207063144/http://www.zenn.demon.co.uk:80/com/reviews/games/Lostcave.z80) so that you can actually play the game yourself. (Note that this example was partially inspired by [the excellent work on browser-based emulated access being carried out by the Internet Archive](http://blog.archive.org/2013/12/31/still-life-with-emulator-the-jsmess-faq/)). 

The Interject service can offer a range of transformation options for a given format. For example, instead of running the emulator in your browser, the service can spin up an emulator in the background, take a screenshot, and then deliver that image back to the you, like this:

![Lost Cave (dynamically generated screenshot)](http://www.webarchive.org.uk/interject/action/qaop/http://web.archive.org/web/19981207063144/http://www.zenn.demon.co.uk:80/com/reviews/games/Lostcave.z80)

These simple screenshots are not quite as impressive as the multi-frame GIFs created by [Jason Scott's Screen Shotgun](http://ascii.textfiles.com/archives/4306), but they do illustrate the potential a simple web API that transforms content on demand. 

As the available development time was relatively short, we were only able to add support for a few 'difficult' formats.
For example, the [X BitMap](http://en.wikipedia.org/wiki/X_BitMap) image format was the [first image format on the web](http://1997.webhistory.org/www.lists/www-talk.1993q1/0182.html). However, despite this early and important role this format (and the related [X PixMap](http://en.wikipedia.org/wiki/X_PixMap) format for colour images) are not as widely support today and so may require format conversion in order to enable access. Fortunately, there are a number of open source projects that support these formats, and Interject makes them easy to use. See for example [image.xbm](http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19961102050932/http://vulture.dcs.king.ac.uk:80/icons/image.xbm), [xterm-linux.xpm](http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19971121061547/http://wwwcache.rl.ac.uk:80/CDROM/docs/linux-2.0.30/xterm-linux.xpm) and [this embedded equation image](http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19990128151646/http://www.alcd.soton.ac.uk:80/~dder/bugs/_8917_tex2html_wrap1129.xbm) shown below as a more modern [PNG](http://en.wikipedia.org/wiki/Portable_Network_Graphics): 

![XBM rendered as PNG](http://www.webarchive.org.uk/interject/action/commons-imaging-conversion/http://web.archive.org/web/19990128151646/http://www.alcd.soton.ac.uk:80/~dder/bugs/_8917_tex2html_wrap1129.xbm)

We also added support for [VRML1 and VRML97](http://en.wikipedia.org/wiki/VRML), two early web-based formats for 3D environments that required a browser plugin to explore. Those plugins are not available for modern browsers, and the formats have been superseded by the [X3D format](http://en.wikipedia.org/wiki/X3D). Unfortunately these formats are not backward compatible with each other, and tool support for VRML1 is quite limited. However, we were able to find suitable tools for all three formats, and using Interject, we are able to take [a VRML1 file](http://www.webarchive.org.uk/interject/inspect/http://web.archive.org/web/19961031121001/http://watt.ccir.ed.ac.uk:80/projects/vrml/penguin1.wrl), and then combine a two format conversions ([VRML1-to-VRML97](http://www.webarchive.org.uk/interject/inspect/http://www.webarchive.org.uk/interject/action/vrml1to97/http://web.archive.org/web/19961031121001/http://watt.ccir.ed.ac.uk:80/projects/vrml/penguin1.wrl) and [VMLR97-to-X3D](http://www.webarchive.org.uk/interject/inspect/http://www.webarchive.org.uk/interject/action/vrml97toX3D/http://www.webarchive.org.uk/interject/action/vrml1to97/http://web.archive.org/web/19961031121001/http://watt.ccir.ed.ac.uk:80/projects/vrml/penguin1.wrl)) before passing the result to a browser-based X3D renderer, [like this](http://www.webarchive.org.uk/interject/view/action%2Fx3dom/http://www.webarchive.org.uk/interject/action/vrml97toX3D/http://www.webarchive.org.uk/interject/action/vrml1to97/http://web.archive.org/web/19961031121001/http://watt.ccir.ed.ac.uk:80/projects/vrml/penguin1.wrl). 

Each format we decide to support adds an additional development and maintenance burden, and so it is not clear how sustainable this approach will be in the long term. This is one of the reasons why [Interject is open source](https://github.com/ukwa/interject), and we would be very happy to receive ideas or contributions from other individuals and organisations. 

But even with a limited number of transformation services, the core of this idea is to find ways to listen to our users, so we have some chance of finding out what content is 'obsolete' to them. By listening when they ask for help, and by allowing our visitors to decide between the available options, the real needs of our designated communities can be expressed directly to us and so taken into account as part of the preservation planning process.




