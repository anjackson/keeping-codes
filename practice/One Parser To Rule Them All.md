---
title: One Parser To Rule Them All
subtitle: and in the syntax bind them.
layout: default
categories: [practice]
tags: [stub]
---

All you adorable file format hang wringing people should be aware of this mouse that is an elephant in the distance. 

https://twitter.com/textfiles/status/406868504701587456

[Hammer and Tongs](https://events.ccc.de/congress/2013/wiki/Projects:Hammer_and_Tongs)


Dark_Star
someone (meaning someone with mad MediaWiki skillz  should probably think a bit about templates that can be used to describe file formats. Something like blocks, hexdump-like tables, containers (like for PNG/IFF/RIFF chunks), standards for "word" vs. "uint16" vs. "be_uint16" etc. etc. etc.
20:31
SketchCow
Yes.
20:31
nitro2k01
Yup. I may have opinions on this.

Dark_Star
yeah I imagine that would be bad. isn't there some kind of description language that can be used to describe file formats in a structured way and have that parsed into diagrams automatically?
something like LaTeX for file formats
20:41
chronomex
that is a very old problem
it is a holy grail
20:42
Dark_Star
one could even use that to build a generic converter for those file formats 




BinX, c. 2002?, which seems long gone, [Binary XML](http://www.smos.esa.int/BinaryXML/) continued up to 2005.

http://www.epcc.ed.ac.uk/projects-portfolio/edikt-e-science-data-information-knowledge-transformation

[Are there (have there been) any efforts to create a schema language for arbitrary binary formats?](http://stackoverflow.com/questions/4670555/are-there-have-there-been-any-efforts-to-create-a-schema-language-for-arbitrar)

[My collection](https://www.diigo.com/user/anjacks0n/unparsing)


A Flawed Approach?

The drive being largely aesthetic and novelty. Each of these solves the same problem, but in very different looking ways.

That writing the parser is a one-off cost. It *might* be slightly easier, but it's the maintenance cost that's hard.

Any such framework means you also have to port the framework. A C parser just needs a C compiler. A parser written in a specialist language needs it's compiler porting over first.

XCEL as the apeosis of this, and XML Schema used to describe binary formats in XML and extract the content to another XML format.

False simplicity?

It looks simpler, but is not really general. To cope with any arbitrary format, one must be able to represent the logic of any existing arbitrary parser, and the only way to guarantee this is to use a Turing complete representation. This is fine, as long as understood that it is just another programming language that is well suited to this task, and not some kind of magic bullet.

It is possible to avoid this somewhat by restricting the domain of format to some subset, that can be represented in a strictly regular, declarative language (say). Problem here is that you also have to cope with validation problems and failures. Can your extremely generic system also cope with the common edge cases and format exceptions? You can't satisfy Postel's Law while also keeping this KISS.

Only syntax, no semantics.

The classic PDF example. A simple parser cannot distiguish 'good' and 'bad' PDF encryption. Can't get at the unobfuscated parse tree unless you implement a small part of the PDF standard. Similarly, for the nastier binary formats, simply opening up the parse tree doesn't tell you much. The information is not simply expressed, and you also need to capture the semantics (in the sense of the process that the data is intended to be projected through) to make any sense of it. PDF is an edge case here. You can make nice PDFs with decent text stream, but easy to futz it because it's really a layout language.


Good stuff

It works for programming languages. Backhas-Nur, etc etc.

As long as one accepts that it may not be sufficient, seens as part of the picture, but with dedicated parsers used for validation/complex cases, and only applied to some formal subset.

If all of this effort had been more coherent, it might have worked.

JAXB, Jackson

https://twitter.com/rafeco/status/407580620609818624
It’s easy to make fun of XML, but it was a massive improvement over predecessors like this:
http://www.washingtonpost.com/blogs/wonkblog/wp/2013/10/23/the-health-care-laws-most-important-number-834/

Look at Thrift, etc. Compare against them and make advantages clear.

Focus on maintainability and adoption as well as elegance.
