---
title:  What Are We Editing?
layout: default
categories: [fundamentals]
status: stub
published: false
---

Documents, Abstract and Immutable?
----------------------------------

In [this paper][1], Allen and Wickett starts with an abstract model of an XML String and then based on this Platonic perspective then go on to assert that all Strings are immutable, and that the Document Cannot Be Edited.

Which is fine, for those of you using a document authoring system composed of mathematical constructs. Unfortunately, on my current budget, I am restricted to using electronic computers that aim to implement an approximation to those mathematical ideals. My computer does not belong only to Turing, but also von Neumann, and many thousands of other engineers and technicians involved in the evolution of the laptop in front of me.

As you can probably tell from my tone, this kind of paper bothers me. Such broad statements feel, to me, like the worst kind of artificial controversy, declaring numerous entirely functional concepts as problematic because they don't fit the authors' assumptions.

Given their assumptions, their conclusions may well be perfectly valid, but if you want to tell stories about the world, you have to test those assumptions against it.

This falls into a class of arguments that all jar with me because they appear to deny the materiality of digital media. Various arguments appear, floating on an air of abstracted understanding. How can we tell them apart, if they don't agree on their terms - not even on the 'digital object' itself! 

But how can they agree on terms without relating them to the world we experience, and how can the terms be related to the real world other than by seeking our more concrete definitions of the process and functioning of real computer systems?

All of the notes in this collection are, to some extend, an attempt to address this apparent lack of coherence with a solid grounding in realistic systems. To that end, I though it would be interesting to pick apart what really happens when you edit a document.


The Verona Sentence
-------------------

The original paper give the example of a simple sentence:

> I remember Verona.

...which is then edited to read:

> I remember, but dimly, Verona.

...so, what happened in between?

Well, the short version is, 'it depends'.  Precisely what happens when a document is edited depends on a lot of details concerning the software and hardware state of the machine. However, under some reasonable assumptions, we can make some progress.


Editable Representations
------------------------

So, lets assume that the editor has just loaded a text file containing the string '_I remember Verona._' into a simple text editor. 

The main thing we need to know about that editor in order to proceed is how it relates to the text file. Most text editors will process the file as a linear bitstream and convert the whole thing into an in-memory representation of that document. For example, most Java programs that load 8-bit text files actually store the string values in 16-bit memory structures (i.e. and implementation of UTF-16). Of course, this can cause issues for large files that won't fit in RAM, but it's a reasonable assumption for this example.

So the file has been loaded, and the in memory representation is in place. But we can't interact with it directly. If we are going to edit that sentence, we need to place our cursor between just after "remember", but where's the cursor?

The answer, of course is that there is _another_ representation of that data structure - one that we can see and use to guide our actions. The in-memory data structure may be in charge, but some kind of projection is needed, subservient but crucial.

In almost every computer system, this is achieved by having another in-memory data structure that describes the image to be presented on the screen and which is (more or less) directly projected through the physical pixels of our screens.

Two 'objects'. The representation and the projection. Working in a cycle of with the user feedback from the keyboard, mouse, and so on, in an ongoing process that maintains the illusion of a document.

So, what happens when you edit the document? The key press is received, the text editor is informed, the in-memory representation is modified, the projection is updated. Rinse and repeat, and the edit is complete.

In truth, in this moment, there is no 'digital object' as it is most commonly defined (e.g. OAIS). There is no file or bitstream for this newly edited, unsaved document. The in-memory data structure itself is only implicitly defined - the software and the data complicit and entwined in the mind of the machine. The individual components will be strewn haphazardly across the address space of the computer, existing only in vulnerable, volatile RAM.


The Concrete and the Abstract
-----------------------------

It's not like the mathematical entity. Finite. Mutable. etc.

XML case no different.
XML document into their favourite XML editor, and that this is a 'native XML editor' (like [Altova][2], say) rather than simple an text editor that knows a lot about XML (like [Oxygen][3]). Th

Does this matter? If we want to be able to describe when things go wrong, when the distance between the mathematical representation and the implementation falls wide, then we need to understand.

Deeper Still
------------

While the in-memory representation is at the heart of this issue, the outline above is still an extremely simplified version of what's going on. If you want to understand what *really* happens when edit a document, you have to start by understanding what happens when you [press any key][4]

[Renear, Allen H., and Karen M. Wickett. “Documents Cannot Be Edited.” Presented at Balisage: The Markup Conference 2009, Montréal, Canada, August 11 - 14, 2009. In Proceedings of Balisage: The Markup Conference 2009. Balisage Series on Markup Technologies, vol. 3 (2009). doi:10.4242/BalisageVol3.Renear01.][1]

[1]: http://www.balisage.net/Proceedings/vol3/html/Renear01/BalisageVol3-Renear01.html
[2]: http://www.altova.com/xml-editor/
[3]: http://www.oxygenxml.com/
[4]: Press+Any+Key.html

