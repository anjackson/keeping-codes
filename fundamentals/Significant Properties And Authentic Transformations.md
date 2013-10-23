---
title:  Significant Properties And Authentic Transformations
layout: default
categories: [fundamentals]
tags: [outline]
---

* Significant properties - content properties not relevant. Dependency analysis and critical characterisation role. For content, in future, eye of stakeholder means users should be able to express format preference.

No date, Prismatic Error
http://www.dailymail.co.uk/news/article-107412/The-Queen-Mother-dies.html

So, I think this is a long-winded way of saying that the Intellectual Object, essence, etc. does not exist, which dovetails with that other paper recently about digital object identity.

'Nothing is the same as something else': significant properties and notions of identity and originality


Insignificant properties
------------------------

- Significant Property Schemes 
    - Sig prop breakdown
    - Compression Is Not A Significant Property

Well, this cuts to the heart of the matter that I've had so much trouble trying to express. Well, here goes...

So, the premise is that we shall judge the reproduction of some performance, whether emulated of via migration, by using some formal scheme to capture and compare the 'significant properties' of the two performances. I have three issues with this. Firstly, I'm not sure we should be the people who get to decide what is 'significant'. Secondly, I believe this approach is both extremely difficult (as Euan points out) and unnecessary - i.e, that when we do want to evaluate a reproduction we don't need to create a special new 'preservation language' to make it work. However, I'll leave those for another time, because my third problem goes much deeper.

I'll start to pick this apart using a really simple example - ASCII. To render ASCII, we must implement a process: if the byte value is 0x61, plot a glyph that look like 'a' and move to the next spot. Capturing the contextual information this depends on, the mapping table and the glyphs, is not sufficient to reproduce this. The rendering is fundamentally a process, a projection, a computation, not static information. The process can be written down, but this is just migrating it to another language, and if you use prose will need to be re-implemented in order to interpret and make use of it.  We always end up implementing or porting software - the documentation of the rendering is just helping us get it right.

Unfortunately, in general, the properties of a rendering process cannot be captured by a simple document compose of prose and declarative data. The only unambiguous language one can use to describe any process a performance may contain is a Turing complete language. Any Turing complete language will suffice, but any language less powerful than that (e.g. the kind of simple declarative data structures we often prefer, or something like boolean logic) will not be able to capture everything we may want to preserve. Thus, if preserving general processes means we are required to preserve one or more Turing-complete formal languages, we are preserving software, by definition. 

Having said that, we could choose to preserve only data in formats that a simpler, e.g. regular languages.


I believe there are absolutely no cases where this can be truly avoided. You're just flattening to a simpler process (e.g. ASCII) and moving the rest of the interpretation out to the user.

The fundamental problem with a system based on significant property schemes is that, in general, most digital object data does not specify properties in a way that maps cleanly to the performance, and indeed could never do so. In the general case, a performance is fundamentally a process, a sequence of states, and the bitstream you load just starts you off in the right place. When you try to capture the properties of performances, you must be able to cope with the fact that the performance may be generated from the data, rather than being 'merely presenting' the data. The necessity to be able to describe any possible performance means that our 'significant property' language must be powerful enough to explain what the generated performance may be. The only formal languages that are capable of capturing any possible performance are those that are Turing complete, i.e. programming languages. Therefore, the only *general* way to capture the 'significant properties' of any possible format we may come across is as software. In the baldest terms, PDF is only  unambiguously defined by it's reference implementation, Adobe Reader.


What we can choose to do, however, is to select some common formats that we believe will act as sufficient substitutes and invest more in supporting those. For example, if Excel becomes problematic, users may prefer to have plain text CSV of the data rather than nothing at all, or having to manually dig around in an emulator. Practically, this means that where we are sure there is value in it, we will support formats that allow us to get that data to our users directly. But to cover the general cases, where we are not yet sure of the value, the best we can do is preserve the software associated with the data, so that some future user can dig out the value. Ideally, if we capture the source code and associated documentation around that software, we increase the chances of this working. 

 
Firstly, I have an issue around who defines what the 'essence' is. I'm not convinced it should be us. As the purpose of a format is to persist a performance, the only safe assumption is that all of those properties are significant. Anything else is predijucing the future, which is fine, as long as your use case is clear, but if we have the chance I would like to put that choice in the hands of our readers and users as soon as possible. But that just a problem with the 'significant' part. I also have issues with the 'properties' part.

One part of the problem with properties is that, when it can work, it has tended to lead to a kind of catch 22. We want to used significant properties to evaluate a migration from one format to another, and this has been taken to mean that we must define some kind of significant property scheme that can be used to capture some or all of the properties of both formats. However, as I argued above, each such property scheme is nothing more than yet another format. i.e. we are judging a migration from format A to format B, but expressing the transformation in terms of a special 'preservation format C'. In some cases, this can be made to work. The problem, however, is the amount of work it involves. It means having one 'super-set' format that is capable of expressing all the potentially 'significant' properties of all the formats you might want to migrate between. This is an immense amount of work, and a keeping such a system up to date would be a huge burden on the preservation community.  Worst of all, even when this approach can me made to work, it is not necessary to create a special preservation 'super format' to do it - there are other ways to judge a migration. I'll leave describing them to some future post, because even that is not the real problem.

Catch 22

---

### 1. Introduction

Abstract problem. Equiv to normalisation to preservation format. If
concrete, superset problem and encoding problem too. Huge amount of
work, so use an open format instead. Digital object types as format
collectons, but only limited data is truely the same, if any. If
abstract then need to capture relationships and map between then.
Unfortunately ontologies are not Turing complete, so will not cover all
possibilities. Or treat common as simple and look only at gaps between
formats? This whole approach encourages the focus to lie on the
deconstrucuon of the content. Worse still, many properties lie in
surprising places, and really we are wanting statements about access .
Preservation actions need qa properties, eg comparative properties like
psnr. Focus on loss directly, rather than deconstructing the content.
Can use abstract form, eg a footnote is broken, which is useful without
being a burden. Othecs more useful, Fingerprints and other aggregates.
Dependency analysis. PDF Rare use case spotting and other profile
compliance cases. Tiff and jp2 cases. Pdfa too?

Planets testbed and intellectual characteristics, worse than the xcl
superset approach as expressed in plain English and thus ambiguous and
poor coverage. Tending to be couched in the language of the performance.
Enforced extraction of properties for later comparison and evaluation.
Cite code4lib.
---
title: Significant Properties & Authentic Transformations
layout: default
categories: [fundamentals]
---


Plato mixes format choice and implementation aspects into one compromise
process.

Compression Encryption Implicit interpretation config or defaults, eg
encoding, colourspace Performance Resource dependencies, fonts, network,

* Note that TB and PC are using ’digital object type’ to mean VERY different things.
* e.g. how to document the context of a performance (technical enviroment properties).
* e.g. what are the properties of preservation services that are of interest.
* http://www.planets-project.eu/private/pages/wiki/index.php/List\_of\_Digital\_Object\_Types\_and\_their\_Associated\_Properties
* http://www.significantproperties.org.uk/

http://www.nytimes.com/2002/08/29/technology/what-s-next-a-universal-tool-to-rescue-old-files-from-obsolescence.html?scp=18&sq=%22digital+archiving%22&st=nyt

....

The Testbed’s ‘Intellectual Properties’ are proving diffficult to
define, in particular it is not clear how to relate that concept to the
measurable properties that can be determined by users or by using
characterisation tools. Here, I am aiming to clarify what these ideas
mean, and how we might proceed.

[A summary of conclusions might be included here.]

Need to read:

Data Without Meaning: Establishing the Significant Properties of Digital
Research

http://www.ijdc.net/index.php/ijdc/article/view/110

InSPECT Reports

http://www.significantproperties.org.uk/

http://www.significantproperties.org.uk/inspect-framework.html

et al

Author and/or User testing is key to managing lossy QA.

#### 1.1 Digital Object Properties

http://www.webarchive.org.uk/wayback/archive/20050410120000/http://www.leeds.ac.uk/cedars/guideto/dpstrategies/dpstrategies.html

Identification of the underlying astract form, an “abstract model of the
data that preserves all the necessary properties of the data”, Note also
that significant properties is confused, as must eval to choose UAF, but
are funciton of UAF. Also, noted as subjective, which contradicts the
hope:

“For a complex digital object the above discussion implies a lot of
effort in deducing significant properties. However, it is our
expectation, that this analysis can often be carried out for a whole
class of objects (e.g. Word4Windows files), and the preservation of a
newly arrived digital object in such a format merely reuses the
analysis, even to the point that the representation net will already
exist, and creating the representation information for the new object
only involves pointing to the pre-existing net.”

From the Testbed deliverable TB/3 - D2, we see that the intention of,
for example, a migration experiment, is to test how well the migration
preserves the ‘Intellectual Properties’ of the appropriate type of
digital object, which are intended to be defined in such a way as to
transcend file format:

“So, we will need a list of all intellectual characteristics, or
properties, per digital object type. This list should contain properties
that have to do with the ‘intellectual’ qualities of a digital object
type and not with the file format.”

This appears to be compatible with the definition of ‘Significant
Properties’ used by the InSPECT project:

“Significant properties are those aspects of the digital object which
must be preserved over time in order for the digital object to remain
accessible and meaningful.”, “The essence of a performance can be
defined in terms of a set of measurable properties, which must be
preserved.”

Of course, by introducing the word ‘significant’, we expose the
potential ambiguity over what ‘significant’ means. For example, Margaret
Hedstrom, Project Director of CAMiLEON, has provided that project’s
definition of the term:

“those properties of digital objects that affect their quality,
usability, rendering, and behaviour.”\
[Hedstrom and Lee, p. 218] (M. Hedstrom and C.A. Lee, “Significant
properties of digital objects: definitions, applications, implications”,
Proceedings of the DLM-Forum 2002, at
http://ec.europa.eu/transparency/archival\_policy/dlm\_forum/doc/dlm-proceed2002.pdf)

This very broad definition clearly encompasses anything that affects the
performace, in sharp contrast to the notions of ‘essential’ properties
implied by the InSPECT definition. Futhermore, defining the ‘essence’ of
an object, in the sense of choosing which properties are ‘significant’
and should be preserved, is exercising a value judgement and depends
upon the preservation context. In the Testbed context, we are not
attempting to choose which properties are preserved, but instead to
determine how different preservation actions affect the ‘intellectual
properties’ of different digital objects.

Metadata is also data.

Naming of properties must distinguish what they are, and what they are
for. Information/Explicit/Content properties, Loaded/Parsed/Promised
proeprties, Projected/Performed/Rendered properties. Former in the
language of a format, mid in a language that spans formats, latter in
the language of the techinical environment? Significant, diagnostic,
characteristic, etc are the what-for.

NOTE that Archivematica’s Sig Char are actually encoding properties, as
they would be the same for large numbers of items - they do not capture
the ’uniqueness’ of the performance that a given file promises.

#### 1.2 Evaluation via Comparing Properties

This notion of intellectual properties also implies a particular mode of
investigation. The Testbed design has assumed that we wish to take some
digital objects and extract their properties, and use those properties
to examine the different preservation actions. For example, we may run a
range of migrations from the source format to a range of candidate
target formats, and compare the properties drawn from the source object
with those drawn from the target objects. This is not the only potential
mode of operation, and we will return to this issue later.

[A figure would work well here.]

[Could use a neat word for this mode of operation.]

### 2 The Problems with Properties

The distinction between the ‘affective’ properties of Hedstrom and the
Testbed’s ‘intellectual’ properties reveals a widespread conceptual
confusion about what ‘digital object property’ means. The term property
implies ownership, but it is not always clear if we are talking about
‘properties of a digital object’ or ‘properties of the performance of a
digital object’. Without suitable qualification, the term ‘property’
could mean an intrinsic asset of the digital object itself, or could be
a statement about a performance of that object.

Although the digital object defines its performance, that performance is
also a product of the software and the technical enviroment the software
is executing in, including the operating system, hardware and so on.
This process can be broken down into two stages. First, the software
parses the digital object, separating the container (standard file
headers, syntactic structure and so on) from the content (the data and
any embedded metadata). This parsing process takes the ’frozen’ digital
object and builds the live, in-memory version, out of which the
performance can be projected. Secondly, the rendering stage takes the
in-memory information content and presents it to the user, and may allow
the user to interact with it, via the computer peripherals. Thus, the
rendering procedure always depends upon the technical environment as
well as the software.

Clearly, therefore, the information in the digital objects defines the
‘unique’ aspects of the performance, while other aspects of the
performance that are common to all digital objects of that format will
be implicit, or rather inherited from the software and techincal
enviroment. Indeed, the entire purpose of the digital object is to
describe that which uniquely defines the performance, out of all
possible performances supported by that format. Therefore, if we
consider the ‘significant properties’ as defined by Hedstrom, the whole
digital object should always be preserved as every byte of the digital
object should have the potential to affect the performance - even any
embedded metadata can usually become part of the performance, because
the user can use the rendering software to inspect that data too. In
this formulation, every single byte is essential, either for defining
the performance or for defining the syntactic structure that permits the
performance to be stored as a file.

Furthermore, to re-construct the performance, we must also store the
software that parses and renders objects of that format, or at least
store any documentation that specifies how these processes should be
performed. Such a file format specification defines a ‘type’ of digital
objects, and is a statement of the essential properties that must be
maintained across technical environments in order for a digital object
of that type (format) to maintain an authentic performance. The file
format specification defines the peformance properties in terms of a set
of information properties, and how these information properties can be
stored in a digital object of that ‘type’. A particular digital object
holds values for the information properties, and thus defines a
particular performance.

#### 2.1 Characterising Performances

During a performance, we can attempt to capture aspects of the
experience by measuring properties derived from the rendered form,
either manually or via a software agent. When attempting to preserve the
‘intellectual properties’ of a digital object, we are actually referring
to the preservation of these ‘performance properties’, as opposed to the
‘information properties’ that are actually held in the digital object
itself. However, it is not clear how to define these properties, as by
stripping away the dependance upon ‘format’ we also strip away the usual
‘languages’ by which we might describe a performance.

To bridge this gap, the notion of ‘characterisation’ of digital objects
has been invented. Based on the available information concerning the
digital object format, the characterisation process re-uses or
re-implements the object parser, allowing the content to be extracted
and re-expressed as a set of explicit information properties. These
properties can be combined with the specification of the rendering
process, in order to predict the preformance properties that the object
promises. The predicted performance properties do not in general pertain
to any particular techincal environment, or at least if significant
variations are expected across platforms then the characterisation
process with make these variations explicit. These predictions combine
the properties defined in the specification with the values provided in
the digital object in order to describe the performance or performances
in potentia. This process can never fully account for all possible
variations in technical environment, but nevertheless represents a clear
statement of the intended interpretation.

Break down the performance.

The Persistant, The Performance, The Perception.

The Performance: Load, Parse, Process, Render, Project, Listen (Load,
Parse, ...)

1.  (Persist: Encode, Store.)

#### 2.2 The Trancendence Fallacy

We have posed ourselves the problem of defining a set of performance
properties that can fully describes the intellectual content of the
performace of a digital object, in a way that does not depend on the
format of that object. This implies that we should be able to extract
the same properties from different digital objects and express the
values of those properties in some common, concrete, unambigious
representation. This has proved to be rather difficult and to explain
why, it is important to understand that while it is easy to define
concepts that transcend file format, it is rather more difficult to
assign values to those concepts.

Being this concrete forces you to choose a true representation, that is
a model and an encoding.

For example, if you allow an ‘image’ type to include both vector and
raster images, then there are NO measurable properties that are common
to all formats and therefore no measurable properties that can be
associated with an ’image’ digital object type. e.g. you could define an
’image’ property called ’width’, but the /precise/ meaning, including
units and computable values depends on both the file format and the
rendering context (print or screen), the latter of which renders the
experimental results subjective unless the rendering context is more
tightly controlled. What does it mean to manually measure the width of
an image? Do I hold a ruler up to the screen? Do you want that in inches
or pixels? Is the DPI obvious, or context-dependent? Chould I inspect
the binary myself using some other tool? How do I record the method I
used? To summarise, you can define concepts for intellectual properties
that transcend file format, but you can only measure values of
properties that exist in (performances of) file formats.

THE ADOBE IMAGING MODEL separates graphics (the specification of shapes
and colors) from rendering (controlling a raster output device).
http://www.adobe.com/devnet/pdf/pdf\_reference\_archive.html

The HTML visual formatting model.
\<http://www.w3.org/TR/CSS21/visuren.html\>

We cannot divorce the precise conceptual definition of a property from
the techical representation of it, because we cannot make any use of any
information that is not expressed in some symbolic form, whether it is
plain English or a binary-encoded number, or whatever. That is what
information is - you cannot represent the value of a property without
choosing a representation for that value. To ’measure’ a property is to
assign a value to a specific concept, and to record and present this
value, a concrete carrier for it must be chosen, even if it is only a
plain ASCII string.

Different ’values’ definitions of the same concept are meaningless,
because the different is alsways systematic. Not a subjective thing.

’Intellectual properties’ are not measurable in general, and do not
generally transcend file format. Some properties may do so, but these
will always be a subset of the properties in files.

You can map between models and representations, one-to-one, but not ‘up’
to one model that works for all other models.

Returning to the point, we are not arguing that this is not achievable
due to some technical ‘difficulty’ that might one day be overcome.
Indeed, neither are we arguing that there are no concepts that transcend
file format. The issue arises when one wishes to associate measured
values with those concepts. When you wish to record or otherwise
communicate a particular value associated with a chosen concept, you
cannot do without also choosing a concrete symbolic representation for
that value. Therefore, we have now had to choose not just the
‘intellectual’ properties, but also concrete representations for the
values for those properties, in order that they might be measured and
compared. Furthermore, in order to be useful, these properties must
cover a significant proportion of the ‘performance’ of a digital object,
otherwise we cannot argue that the performance has been retained if the
properties are preserved. As we have been forced to be so specific and
thorough, we have ended up creating a conceptual framework that is, I
think, formally identical to another conceptual framework that already
exists: the notion of ‘file format’. The PDF specification is the
definition of the ‘intellectual properties’ of a digital object of type
‘PDF’, and the file itself contains the values of those properties that
define the performance.

Conceptual ’tags’ can trancend the implementation, but a value of that
property cannot. Format features. Width

Web archiving design history, a design anti-pattern? Needs a good
reference.

Automated language analysis, e.g. Ugaritic, and what is required to make
this work.

#### 2.3 The Nature Of Characterisation

This idea is central to understanding how XCL and other characterisation
tools work. When we extract the values of properties, we are actually
just re-expressing the contents of the binary file in a new, more
accessible form - indeed in a new digital object format that reflects
the performance that the binary file promises. That is, in essence, what
an XCDL file is. Please note not about automatability really, but about
measurablility in general. This is not actually about automatability,
but about whether a property is reproducibly measurable. If we are not
reasonably careful about how we design our measurable properties, hidden
factors may irrevocably garble the results. Use XCL because automatic
properties really are measurable.

XCDL works by re-encoding file data in a common form that is text-based
and therefore accessible. the list of properties for each type covers
all props, and the comparable ones are a sub-set in general.

Indeed, property super-sets do not in general exist, and may change
overtime, therefore ontology should express properties that are common
to different formats, and not supersets all children of which use those
properties, and this will fail in general. It’s more like tagging that
heirarchy. Heirarchies are brittle to growth. See image case.

Different formats contain information requried for rendering, encoding
in some specific form. There is not ’a property’ that is the same in
both, except when trivally true. There may be properties in one that can
be mapped to the other, i.e. the information content may be conserved.
But neither representation is primary, they are just two encodings
related by some computational process (lossless/lossy,
reversible/irreversible). i.e. that a computational mapping exists is
the only statement that then contain ’the same information’ that we can
automate.

Property super-sets and algorithmically-related representations. That
Diagram Idea.

Implicit properties too.

e.g. imageWidth (pixels) is shared between all bitmap formats, but is
not a ’super’. imageWidth in vector is different, and can only be
related to the bitmap one via DPI value and a computation.

CApturing the performance in a new representation is the very hard work.
a pitcure says a thousand words.

PDF standard is a statement of Sig Prop of PDF.

Note that ’font size’ is an almost useless property.

### 3 Redefining Properties

In general, it is also suggested that we change methodology. As no
’super types’just different representations, this suggests we look at
mappings between individual representations, and not an up-to-props
mode.

Beyond that, how can we proceed? Most appropriate approach depends on
circumstances.

#### 3.1 Define ’Essential’ Formats

We can keep the notion, and work hard to define the essence, describe a
performace, but this is equivalent to choosing or creating a format.
Normalisation.

If one can successfully re-express the ‘essence’ of a digital object in
some set of properties, and store those, there is no longer any need to
store the original object, as any other properties held there are, by
our own definition, non-essential. It does not matter whether these
properties were measured automatically or by hand, by simply defining
what is ‘essence’ of an object means, i.e. the properties and their
values, we have built a new digital carrier for our content. Therefore,
by defining a set of concrete, measurable properties associated with a
digital object ‘type’, we are effectively defining a new digital object
format. In this sense, characterisation is simply a ‘special case’ of
migration.

To choose the essence, canonicalise, is equivalent to choosing a format,
normalise. The differnece is that the sec of the performance is a loose
and local thing, not a tight and global thing like a PDF can be.

Or, to put that another way, if you want a concrete representation of
the concept of a ’document’, perhaps you should just choose one of the
existing ones (e.g. ODF) and work out which properties are important to
you. The alternative is to spend your time building up a concrete
’document’ type, but this appears to be formally equivalent to creating
your own unique document file format, one that no-one else supports or
even knows about.

Allow loss of the rest.

—-

Keep it abstract Abstract properties most useful ay the format class
level for choosing between formats. Eg essential dimensions. You can’t
be a png or gif without L2, gif can and video must do L2T, audio is T,
etc. These are dimensions of performance! Less clear otherwise, e.g.
Where does text fit in. Colorspace and other calibration data? Dpi?
Dimensions of data might work here, as in D2+C for images, D for text
and audio, but different projectors in each case. How does PDF fit in.
Each page is T given the performance, so like a movie? Ah, video is D2T2
because of audio track, PDF is D2T. Both are L2T in performance. Add
sensory dimensions? Video is SH, PDF is ST(H) as can do sound.
Sight/visual, smell/Olfactory, Hearing/auditory, touch/tactile?,
taste/?, others. PDF and gif are L2(T), but are D2(T) and D(T) although
T is not quite what I mean. So an image, L2:S, should only be mapped
into other LL:S forms? L and L3 meaningless? 3d film is 2LLT:va. Keep it
real Fine-grained mappings also useful. E.g. Tiff res to jp2 res? But
just related fields? Stay in language of format but define identifiers
for info based on spec, reusing the language. Then relate them. Still
not at instance level, but a spec for implement. May work best as a
corpus. Note that JHOVE and other tools can be confusing, because it’s
not always clear if they are using the language of the format, the
language of standard, of their own. i.e. when fields are derived rather
than reported.

Performed, Projected, versus Parsed. Printed parse is content
projection. NISO MIX are projected properties or rather migrated to
metadata model.

Use the peripheral bottleneck as the description layer. Screen,
Loudspeaker, keyboard, mouse, etc and describe performance in those
terms. Very small variation at this level? Keyboards? Speaker systems?

Why is the parse required. Explore why memory dumps are unreliable.
Serialisation helps isolate from artifacts (ie format is the sig props
of performance, again)

#### 3.2 Focus On Information Content

We can discard the notion of ‘intellectual properties’ as concrete,
measurable entities, and instead treat them as conceptual ‘tags’ that
can be used to group related information properties. In this case, we
leave the definition of the performace in the specifications and
software, and focus on preserving the performance-defining information
held within digital objects.

Format features. abstract tags can be used to inficate that image
formats are related, but not used to re-encode the data without creating
a new format. So, building Representation Information can be done in
terms of format features. Common traits can be implemented as tags, and
used to determine/discover potential migration pathways that are of
interest. However, the potential for loss can only be understood by
direct comparison between two concrete formats, and the actual loss can
only be evaluated in the context of the comparison of the initial and
final object. That may be, in part, achieved by measuring ’significant’
properties of each and comparing them, but that is not sufficient to
ensure the process worked unless the property system is as complex as
the sum of the two formats.

Any more than a painting can be separated from its medium... well, less
so, but still.

##### 3.2.1 Evaluating Migration Pathways

Therefore, Logical Information Superset is the migration that makes
sense. Migration across forms of representation is the tricky
one.Comparing File Formats

Logical Information Superset is a useful idea, and applies to the
different versions of some formats. Across formats, this can be tested
using the shoygun, up to a point.

carl fleischhauer image conversion work?

Theoretically Authentic Pathways logical information superset.e.g.
PDF1.4 covers all in PDF1.3 and by inspecting standards you can tell all
info can be translated/moved without loss. Relation to PDF/A is
different. Requires precise ident scheme for standards (i.e. PRONOM not
MIME types). Useful.

Verified Authentic Migrations tools seen to deal with the potential
authentic pathways.

#### 3.3 Focus On Critial Properties

We can limit scope, and specify a subset of preformance that are of
particular interest, and manage translation between representations.

Focus on aspects that require attention

OR on ’tell-tale property’ measurments that would indicate a range of
failures. e.g. page number.

Or, we can deliberately introduce ambiguosity, so that our ’intellectual
properties’ act to ’summarise’ the detailed performance properties.

These last two are of interest here, but how do we determine where to
focus our attention, and where to safely introduce ambiguity?

We would also like the language of these properties to be reasonably
formal and consistent, so that the algorithmically predicted properties
can be held alongside manually measured values.

##### 3.3.1 Evaluating Performances

Useful subset of properties that are common/translatable.

SEPARATE: Related formats that we know how to map between, easier to
deal with by direct comparison.

When wishing to compare different binary carriers, it is of course
necessary to know how to compare the properties we have extracted. The
fact that the values of properties cannot transcend their carrier form
has an important consequence here. Different formats can employ
different binary forms for related properties, and these properties
cannot be reliably extracted to a single, shared form. For example, a
JPEG and a PNG may use different models of colour space (YCbCr and RBG),
and as there is no such thing as a ’super colour space’, any embedded
colour profiles must be extracted as distinct properties, not as
different values of a single property. This is why only a sub-set of the
image properties extracted by the XCL tools can be compared directly,
the others are captured by properties the presence of which depends upon
the format under consideration. It can be no other way.

Indeed, in the general case, the each property in one format may be
expressed using the values one or more different properties in some
other format. The automated comparison currently concentrates on those
properties that /are/ shared between different formats, but in general
the properties of different formats are related by a computational
process (algorithm) that depends on how those properties are expressed
within the source and target formats. For example, if in one format the
decimal number 0.1 is stored as a string, and in another it is stored as
a binary number, then there is no way to trans

i.e. not that F\*F complexity, as always examining one-to-one mapping.

statements about the performance that must be maintained in order for
the object to be considered authentic

Augment by explicitly noting implicit properties, like ’needs
transparency’, or moreover, ’dependencies’.

Dependency analysis is really key, what s/w and other resources (keys)
are needed to render it. Format is a way of managing dependency, and so
embedded formats are important. etc.

Record requirements for objects in the language of the performance.

i.e we have the language of the format (info content), and the language
of the performance (interpretation) as distinct, concrete concepts.
Other abstract models muddle formats, or mix the language of the two.
What about comparing objects in the same ColourSpace? this is a middle
road, constructing a proxy for the performance and comparing the objects
in that artificial setting.

##### 3.3.2 Subjectivity Versus Objectivity

Properties of comparison are different, but can sometimes be constructed
from properties of instances.

e.g. trying to unambigiously enumerate the font spec for a complex
document is very difficult, and is essentially equivalent to
re-implementing a significant chunk of the PDF standard in plain
english.

However, statements of comparison, like ’were the font sizes preserved
between X and Y’ are entirely tractable. By focussing on the
differences, we can identify the acceptable losses even when the
properties in each format are not easy to capture.

Does this transformation preserve the semantics?

Does this transformation preserve the visual appearance?

You can choose how deep to go.

May also include statements about the /perception/ of the performance of
a digital object.

BUT only rendering has the answer. We have limited control over the
render stack, but this can be improved.

Subjective and perception issues.

For example, if people misunderstand what we mean in our property
definitions, we will not get stable ’averages’ that mean anything. If we
allow people to submit ’width’ however they like, we will just get a
meaningless jumble of results. Recording the fact that you used Adobe
Acrobat won’t solve that problem.

Asking people to record the ’font-size’ of the ’text’ is meaningless
unless we also supply a way of addressing fragments of content, and even
then can be very difficult to determine (what on earth does ’font-size’
mean if the object is actually a bitmap?).

There are no subjective statements to be made about the content of a
digital object - it is just bits and bytes. There should be no
subjective statement to be made about the way in which those bytes are
used to construct a performance, as this is done using a deterministic
computational process. At this level, the main issue is that different
technical environments may produce different performances from the same
source object, but this is not what ’subjective’ means.

Subjective statements can only be made about our /perception/ of the
performance, not about the actual contents of the actual file or the
process that interpreted it. The original Testbed plan was to allow
users to record their perceptions of the performance of different types
of digital object, but the focus of the characterisation work has been
on the information contained in different formats of digital object, and
what that information implies about the performance.

Comparison is a separate issue. It is meaningful to ask for a subjective
judgement about whether the noise introduced by compression is
acceptable, but getting the person to evaluate the noise-level in the
pre/post migration files is unlikely to be as effective as getting them
to say whether they think the two compare well.

There is no fundemental problem with collecting ’subjective’ judgements,
but the framework in which we hold these results should be compatible
with the automatic work.

Subjective questions are a very bad idea. Subjective answers are just
fine.

##### 3.3.3 Managing Ambiguity

Some ambiguity is okay, but how to capture that? How to join with the
Information Properties.

Subjective measurements.

Rotheburg properties and problems,

content, context (metadata), appearance (e.g. layout, colour), behaviour
(e.g. interaction, functionality) and structure (e.g. pagination,
sections).

Useless, as really about perception?

Statements about the performance, rather than capturing the performance.

Evaluating Preservation Actions

We can’t create formats that /completely/ describe performances, because
that’s crazy hard and never transcends format.

If we define properties that do transcend format, there is always some
’value judgement’ in choosing which are of interest, and in choosing the
representation there is also some potential for loss.

So, how to do it. Can we home in on the critial issues without having to
capture all this complexity.

File format is promise of a performance that transcends the render
stack.

properties that belong to the ’image’ property type, not a digital
object type?

#### 3.4 Promises, Statements & Tests

I have a simple question. I have a text. I want to preserve its
paragraphs. I try migrations to different file formats with different
tools. I want to compare the outcomes. so the objcet peroprtiy is relted
to objcet type, not file format. I look at the outcomes and say
"similar", or "quite similar"etc

[12:26:37] Maurice van den Dobbelsteen: or I do automated conversion
first and the rest subjcetively/manually

[12:27:17] Andrew N. Jackson: hm, good example. you see, to the tech
eye, the whole thing looks a bit skewed [12:27:52] Andrew N. Jackson: do
you mean ’preseve the semantic concept of paragraphs’ or ’generate
something that appears to look the same’ [12:27:59] Maurice van den
Dobbelsteen: the latter

Our central problem is that we do not know how to relate the performance
properties to the measurable properties.

This is compounded by the difficulty that some ’performance’ properties
may become measurable is we can find an algorithm for it.

The aim of the standard is then to become the statement of the
performance properties, i.e. how to generate the experience from the
data. i.e. enough information to be able to write an implementation,
and/or an actual reference implementation. Can be ’test-oriented’ like
ACID3.

The concept of ’Word Count’ is a good example of a ’Document’ property
that could benefit from more clear definition, e.g. clarifying the way
symbols, abbreviations and acronyms are handled. It is, of course, not
necessarily possible to extract the word count from video, audio or
raster carriers, and it may not even be possible to reliably extract the
value of this property from document formats without also specifying the
precise algorithm used to generate it (which may itself depend on the
carrier format). In this case, it may be better to consider the
’intellectual property’ as a /tag/ associated with a number of concrete
property definitions, rather than an actual concrete concept in it’s own
right. I suspect this may be the case in general.

Manageble, narrow focus, e.g. describing the performance of static
images. For example, a potentially useful property would be
IsAlphaChannelInUse, or HasTransparentRegions, which would be true or
false, and should be possible to define for all image types but which is
NOT an explict property of the digital object content, but is a
statement about the result of the rendering. Nevertheless, this concept
does not really transcend file format, and should not be presented when
it is not applicable (e.g. when using JPEG, which has no alpha channel).

functional testing for digital objects? Like Selenium, ACID3, but for
the experience. A document testing framework..

The choice of statements is a value judgement, given that we cannot
cover everything.

Specify what must not be lost, instead of enumerating what must be kept.

MeasurementType - human, or code agent, methodology or algorithm, etc

A language for statements about the performance.

A way of capturing dependencies.

### 4 Quality Assurance Methods

#### 4.1 Acceptance Testing

Preservation Planning : ’Transparency must be maintained’, logic like IF
’myfile’ has ’alphaChannelInUse’ then output format must
’haveAlphaChannel’. This is not the Testbed use case.

Statements that may be of use: ’hasAlphaChannel’ (can we tell when we
can ask?) ’isAlphaChannelInUse’

So, ’was transparency preserved’ is a fact about image migration that
can be computationally determined, i.e. a statement on the comparison of
two images. Property ’extractAlphaChannel’ may be comparable, but
clumsy. Must extract to super-set.

#### 4.2 Corpora

What, then, do Corpora mean? Have to be careful in the Migration case.

Manual verified corpora are useful, e.g. isotar, jhove.

What does in mean when no tool can be trusted, because we can’t manually
inspect everything? e.g. xcl corpus.

### 5 Other Material

Assuming we can store them... Challenge of preserving access

The challenge of describing the performances of digital objects.

Importance of QA, and of automation. [CITEs]

The curators want to express their preservation needs, but to be
reliable, unambiguous, and therefore automatable in princpile, require
the tech version to be linked to high-level.
