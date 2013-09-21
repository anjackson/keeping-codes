---
title: Understanding Tools & Formats Via Bitwise Analysis
layout: default
categories: [experiments]
tags: [complete]
publish: true
---

Recently, at the [SPRUCEdp Unified Characterisation Hackathon][3], I [presented some early work][4] on using bitwise analysis of digital resources to better understand how software tools operate upon them. [A recent blog post on a similar piece of work by Jay Gattuso of NZNL][5] reminded me that I had not yet had a chance to write up what I've found so far. This document outlines the approach and initial results, showing how the bit-level sensitivity of various JP2 tools can be effectively mapped and compared.


Bitwise Analysis
----------------

At heart, the approach is a very simple brute-force analysis: we systematically flip each and every bit in a source bitstream and observe whether any given software process notices the change. This allows us to build up a map of how the data the the tool interact.

For example, to look at JPEG2000 tools, we first need to create a small test image, such as this 16px square fragment of a photograph:

{% include figure.html src="images/bitwiser/16px-photo.png" alt="The source image." %}

We then convert it to the format of interest, [JP2][2] (via [PPM][1] using ImageMagick, and then through Kakadu).

If we just look at the raw byte values, generating an image of the data inside the JP2 file, we get the figure shown below.

{% include figure.html src="images/bitwiser/fig-bm-original.png" alt="Bitwise map of the source data file." %}

This simple visualisation reveals clear 'quiet' and 'noisy' areas. For a compressed format, we can be fairly certain that the high-entropy 'noisy' region corresponds to the compressed image data, and the 'quiet' areas correspond to file structural information and metadata. But we can go further than this, using this little image to compare JPEG 2000 tools while also learn about the structure of the bitstream.

Taking [_JHOVE_][9] as an example, we could start by wrapping it up a script that takes our test file as input, and extracts the 'is Valid' result from _JHOVE_'s output. This output becomes our 'ground truth' for this experiment.

We then perform the bitwise analysis. That is we go through the entire file, byte by byte, and within each byte, bit by bit. We flip each bit in turn, and for each one, we re-run the _JHOVE_ on the modified file, and observe if the output from _JHOVE_ changes. Then we flip the bit back and move on to the next one.

For each byte, we note which bits modified the result, and which did not, and convert that to a greyscale pixel value for that part of the datafile, which indicates how sensitive the validation process was to that byte. This builds up a map of the data, indicating how sensitive that software process was to each part of the file. By convention, white is used to indicated completely insensitive areas, whereas black means even a single bit-flip would have been noticed.

Clearly, if a given bit-flip modifies the output, then the tool is sensitive to that bit. However the reverse case, where a bit-flip does not modify the output, does not necessarily prove the bit was ignored - it is also possible that the bit was sentiently repaired. In other words, the gaps in the maps reveal the location of data that is either ignored or trivially redundant. Therefore, wherever possible, tools should be configured to report any 'quirks' that they compensate for, rather than silently fix errors (which is good practice anyway). 

This procedure can be repeated for multiple tools, and the sensitivity maps compared.


Characterisation
----------------

First, I looked at identification and characterisation tools, as shown below:

{% include figure.html src="images/bitwiser/fig-bm-chartools.png" alt="Bitwise map of characterisation tool sensitivity." %}

For the _file_ tool, which only performs identification, we can clearly see that it is only sensitive to the JPEG 2000 'magic number' at the start of the file, and the remainder of the file is ignored completely. Note that _DROID_ uses the same signature information, so can be expected to give the same result. However, we were not able to test as _DROID_ does not lend itself to being run repeatedly from the command line.

The other tools clearly perform deeper analyses. The next most sensitive one, [_jp2StructCheck_][6], was the predecessor of [_Jpylyzer_][7], and although clearly more sensitive than _file_, the sensitivity map is consistent with a basic structural analysis. On the other hand, whicle the [_exiftool_][8] metadata extractor is much more sensitive to the file header, if does not inspect any other parts of the file at all. 

Both _Jyplyzer_ and _JHOVE_ are sensitive to changes in much more of the file - the advances made by _Jpylyzer_ over _jp2StructCheck_ are particularly striking. Interestingly, full _JHOVE_ characterisation is sensitive to significantly more of the file than _Jpylyzer_, but appears to ignore parts of the file that _Jpylyzer_ covers. None of these tools appear to be sensitive to much of the latter half of the file.


Validation
----------

Here, we focussed on the validation tools, and instead of using the whole characterisation output as 'ground truth', we just extract the 'is Valid' result and compare that. Therefore, these maps show which parts of the JP2 appear to be validateable, not just extractable. For example, if there is a comment in the file, the characterisation process may notice that modifying it changes the text, but may not know whether comment is valid or not.

{% include figure.html src="images/bitwiser/fig-bm-validtools.png" alt="Bitwise map of validation tool sensitivity." %}

We can see minor differences between _JHOVE_ versions, indicating how this approach could be used to complement regression testing. More interestingly, it is clear that _Jpylyzer_ is much more discerning than _JHOVE_ in this regard. Many of the JP2 that _JHOVE_ would pass as 'valid' are determined to be invalid by _Jpylyzer_, indicating that it performs a more rigorous validation process.


Rendering
---------

Judging by the results, it seems that none of the tools considered above are able analyse or validate the actual compressed image data. We have seen the analysis of the file structure and the metadata, but to learn more, there is no alternative but to use an actual JP2 decompresser to convert the image to a different format, and check if any resulting image is modified when we flip the bits.

{% include figure.html src="images/bitwiser/fig-bm-rendertools.png" alt="Bitwise map of rendering tool sensitivity." %}

This shows that _OpenJpeg_, _ImageMagick (JasPer)_, and _Kakadu_ are all highly sensitive to the image data, but ignore changes to significant fractions of the header data that the characterisation tool did cover. This suggest that the best validation strategy may be to combine _Jpylyzer_ and a JP2 decompresser, in order to maximise coverage of the image data and metadata.  _Kakadu_ appears to be the most sensitive renderer, although it is a close call, and the maps within the image data are very similar. Note that the small amounts of 'ignored' data in the image payload may  correspond to errors that were noticed but were silently corrected.


Conclusions
-----------

On it's own, this approach provides an interesting way to understand bitstreams and compare tools, although it would benefit from additional development to make it easier to compare and combine the sensitivity maps. Furthermore, the understanding of the bitstream itself can be deepened by monitoring the output of the tool more closely. For example, when working with characterisation tools, we can see directly if the bit we just flipped modified a comment, a colour-space, or some other data or metadata the tool is capable of exposing. A relatively simple user interface could user this approach to create an engaging way to explore bitstream data formats interactively.

These techniques could also form the basis of a sophisticated preservation tool regression testing and comparison system, which has the distinct advantage of having to invest very little knowledge up-front about the format itself. We only need to define the output of interest for a given tool or set of tools, and can put a range of different bitstreams through them in order to learn more about both. In essence, we trust the software to inform us about the format, and this can be used to kick-start the more traditional approach of documenting formats and creating format test suites.

As indicated above, one limitation of this approach is that redundant data cannot be distinguished from ignored data. However, we can start to compensated for this by learning more about the format and comparing the available tools. In this experiment, it seems likely that the majority of the 'insensitive' data really is simply ignored, but further research would be required to come up with ways of understanding how to verify whether that is truly the case.

However, the main limitation of this approach is the high volumes of computation time needed for such intensive processing. Even for this very small 773 byte test file, each bitwise analysis involves running each tool 6184 times. This took around an hour of computation, although of course this depends on the nature tool (for example, Java tools tend to be slower than C tools). Further research could determine whether full byte-flips are an acceptable alternative to flipping each byte individually, although even then, the approach is only likely to be possible for smaller files. However, the success of the approach does not depend on the size of the files, but rather on the degree to which the input files cover the features available in a given format. Further research, perhaps similar to [this][10], could also look at ways of analysing and mapping out the software as well as the input data.

The source code and example data used in this experiment are available [here on GitHub][11].

[1]: images/bitwiser/16px-photo-png-im.ppm
[2]: images/bitwiser/16px-photo-png-im-ppm-kdu.jp2
[3]: http://wiki.opf-labs.org/display/SPR/SPRUCE+Hackathon+Leeds,+Unified+Characterisation
[4]: http://www.slideshare.net/andrewnjackson/unified-characterisation-please
[5]: http://www.openplanetsfoundation.org/blogs/2013-02-14-exploring-impact-flipped-bits
[6]: https://github.com/bitsgalore/jp2StructCheck
[7]: http://openplanetsfoundation.org/software/jpylyzer
[8]: http://www.sno.phy.queensu.ca/~phil/exiftool/
[9]: http://jhove.sourceforge.net/
[10]: https://code.google.com/p/imagetestsuite/wiki/AboutTestSuite
[11]: https://github.com/openplanets/bitwiser

