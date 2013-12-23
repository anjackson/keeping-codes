---
title: Communicating with the Future
layout: default
categories: [fundamentals]
tags: [outline]
permalink: communicating-with-the-future.html
---

"Digital Preservation is access, in the future." - David Brunton

https://twitter.com/nlagovau/status/407324307182714880


This series of short posts explores the consequences of a single assertion: that information science and communication theory form the fundamental basis of digital preservation. 

A number of authors have noted that digital preservation involves ensuring we can communicate with the future [TBA], and have explored preservation issues from that perspective. But this is more than just an illuminating point of view, and the current literature has neglected to address the relationship between digital preservation and the well-established field of communication theory. Indeed, any 'theory of digital preservation' must be consistent with established principles of information science.

By treating communication theory as our starting point, we can trace out the beginnings of such a theory. On the way, we can explore the relationship between digital and analogue signals, and the ways in which the limits of computability place limits on what we can knowingly preserve. We can outline the relationship between signals and noise, and from there start to see the relationships between compressibility, artificial intelligence, and representation information. We will examine some of the ways in which current digital preservation practices and built on algorithms and processes that have their roots in information science and on a continuum of engineering practices, extending from the shortest to the longest time scales.

To begin this journey, we must start by defining [the Zeroth Law of Digital Preservation](The Zeroth Law of Digital Preservation.html).

The Zeroth Law of Digital Preservation
--------------------------------------

In the field of [thermodynamics][1], there was a law so obvious, so taken for granted, that no-one even realised it could be considered a law. The notion of thermal equilibrium - roughly speaking, the notion that a 'temperature' could be defined at all - was so fundamental that it simply assumed without question. Later, if became clear that the first, second and third laws of thermodynamics were not strictly consistent unless this axiom was added. The primacy of this assumption was recognised formally by calling it the [zeroth law of thermodynamics][2].

I believe that the field of digital preservation has followed a similar path, and that the mathematical theory of communication that began with [Claude Shannon's][3] [seminal work from the 1948][4] is so fundamental to every single digital preservation system and concept we have been using. In short, that Shannon's [noisy-channel coding theorem][5] should be considered our Zeroth Law.


Set the scene, describe source coding theorem, and describe our 'channels'. 

...

Source coding theorem as backbone of what we already used, lead into what it tells us about preserving information if we consider a format migration 'channel'.

But this applies to everything - even the 'discrete' form applies as much to text and morse code as it does to WAV files and HTTP. So, [what's so special about digital preservation?](What is Special About Digital Preservation.html).



What's So Special About Digital Preservation?
---

It's not the digital that's the problem
Directly.
It just makes new machines easy.

OR

Software is the only thing that distinguishes 'digital preservation' from any other discrete, symbolic communcation system (from Morse Code to the written word).


Something about computing and green and brown field development. 
Moving into cities built on cities.

Broadcast to narrowcast - no longer a property of the medium.

Then point out that that the other part of the theoretical underpinnings is that the comms is done using computers, so that Turing applies, etc. Refer to Validation page.

So, the critical thing is the Turing machine, and practically, this means software is at the heart of it. 

Expression, manifestation, inflation, reification, actualisation, act.
No word in any glossary for this, the run-time representation of the digital object.

---
LINK TO von Neumann Machines
----
The important of the von Neumann architecture. The separate of data and code underpinning the entire concept of data that can be separated and made portable etc.

Also, this is archetypical of the engineering decisions that underly the technologies we are attempting to preserve. That understanding the technology is one part, but understanding use, adoption, is critical to understanding preservation.

But separable code and data is only the beginning. The buildings of our software machines have already discovered that raw machine code and binary data and not necessarily the best way of maintaining access, even to their own systems. To understand that, we need to dip into another part of information theory - formal languages.

--- 
LINK TO Code as Communication
---
Describe the interpretation v. representation problem again. It is possible to do absolutely anything with a computer using only machine code, but it has not proved a easily interpretable construct. Cray and his toggle switches. The engineers sought a middle ground, a language precise enough to be turned into machine code, but approachable enough that the meaning of the program might be understood. i.e. there is a communication story here, with the source code communicating a slightly different set of things, with some room for error. 

Define the formal languages, describe the Chomsky heirarchy briefly, to refer back to in a subsequent section.

Also, what about persisting the state of the programs, which is where we get interesting.

Also sufficiently isolated from technical details, vector of cross-platform comms. It is in this context that the first digital 'formats' start to appear [citation needed what about physical digital formats?]

The Digital Object Dichotomy
----------------------------

Outline the fundemental confusions that arise from two distinct conceptions - bitstream and performance. The truth is inbetween, as both are projections of the true object, the bytes in flight.

The Stack

That all digital objects are processes, and that the artefact is an analogue relic.

In truth, every so-called digital object is a process, not state. The illusion of stillness has taken years to create, but is a kindly lie.

Bytes in flight. etc.


The First Preservation Action: Save As...
-----------------------------------------

The early computers had little or no permanence. 
Tape, pushing memory to disk.
Early persistence and communication, Yellow Pages listings in computer magazines.
That the road to perpetuity is made of daily steps.
That we should understand how preservation is done, right now, on a day-to-day, week-to-week, year-to-year level, because the only way to reach out across centuries is by changing the day-to-day.

This is not a digital object
File bitstream resource-content
They are the first step to presrvation
Persistant state


LINK TO [Codes](codes.html) ??? (Chomsky) 
No, not yet.


### Edit notes

So, this section lays basic theoretical groundwork, and touch upon all the main existing areas that will be referenced elsewhere. It starts with introducing Shannon, and ends by describing basic bitstream-based persistence in those terms.

Follow-on sections break this down:
- Codes, i.e. Chomsky heirarchy and its applications.
- Siginificant Properties paradox and resolution (possibly part of the above).
- Validation and the Halting Problem.
- Entropy, Compression and RI

Illustrative Asides:
- Press Any Key
- What Are We Editing

Dealing with Value
- Not A Science
- Making Plans
- Never Alone (social aspect)


[1]: https://en.wikipedia.org/wiki/Book:Thermodynamics
[2]: https://en.wikipedia.org/wiki/Zeroth_law_of_thermodynamics
[3]: https://en.wikipedia.org/wiki/Claude_Shannon
[4]: https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication
[5]: https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem

