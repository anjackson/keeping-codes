---
title: Understanding Tools & Formats Via Bitwise Analysis
layout: default
categories: [experiments]
publish: true
---

Recently, at the [SPRUCEdp Unified Characterisation Hackathon][3], I [presented some early work][4] on using bitwise analysis of digital resources to better understand how software tools operate upon them. [A recent blog post][5] reminded me that I had not yet publicised the results more widely. This document outlines the approach and my initial results, showing how the bit-level sensitivity of various JP2 tools can be effectively mapped and compared.


Bitwise Analysis
----------------

At heart, the approach is a very simple brute-force analysis: we systematically flip each and every bit in a source bitstream and observe whether any given software process notices the change. This allows us to build up a map of how the data the the tool interact.

So, to look at JPEG2000 tools, we first need to create a small test image, such as this 16px square fragment of a photograph:

{% include figure.html src="images/bitwiser/16px-photo.png" alt="The source image." %}

First, we convert it to the format of interest, [JP2][2] (via [PPM][1] using ImageMagick, and then through Kakadu). If we just look at the raw byte values, generating an image of the data inside the file, we get the figure shown below.

{% include figure.html src="images/bitwiser/fig-bm-original.png" alt="Bitwise map of the source data file." %}

This simple visualisation reveals clear 'quiet' and 'noisy' areas. For a compressed format, we can be fairly certain that the high-entropy 'noisy' region corresponds to the compressed image data, and the 'quiet' area to file structural information and metadata. But we can go further than this, using this little image to compare JPEG 2000 tools and learn about the structure of the bistream.

Taking [JHOVE][9] as an example, we could start by wrapping it up a script that take our test file as input, and extracts the 'is Valid' result from JHOVE's output. This output becomes our 'ground truth' for this experiment.

We then perform the bitwise analysis. That is we go through the entire file, byte by byte, and within each byte, bit by bit. We flip each bit in turn, and for each one, we re-run the JHOVE on the modified file, and observe if the output from JHOVE changes. Then we flip the bit back and move on to the next one.

For each byte, we note which bits modified the result, and which did not, and convert that to a greyscale pixel value for that part of the datafile, which indicates how sensitive the validation process was to that byte. This builds up a map of the data, indicating how sensitive that software process was to each part of the file. By convention, we use black to mean completely insensitive areas, whereas white mean even a single bit-flip would have been noticed.

Clearly, if a given bit-flip modifies the output, then the tool is sensitive to that bit. However, it should be pointed out that the reverse case, where a bit-flip does not modify the output, does not necessarily prove the bit was ignored because it is also possible that the bit was sliently repaired. Therefore, wherever possible, tools should be configured to report and 'quirks' that they compensate for (which is good practice anyway). Therefore, the gaps in the maps reveal the location of data that is either ignored, or trivially redundant.

This procedure can be repeated for multiple tools, and the sensitivity maps compared.


Characterisation
----------------

First, we looked at identification and characterisation tools, as shown below:

{% include figure.html src="images/bitwiser/fig-bm-chartools.png" alt="Bitwise map of characterisation tool sensitivity." %}

For the file tool, which only performs identification, we can clearly see that it is only sensitive to the JPEG 2000 'magic number' at the start of the file. Note that DROID uses the same signature, so can be expected to give similar results. However, we were not able to test as DROID does not lend itself to being run repeatedly from the command line.

The other tools perform deeper analysis. The next most sensitive one, [jp2StructCheck][6], was the predecessor of [Jpylyzer][7], and although clearly more sensitive that file, the fact that it only checks high-level features can be clearly seen. The [exiftool][8] metadata extractor is clearly much more sensitive to the file header, but does not inspect any other parts of the file. The advances made by Jpylyzer over jp2StructCheck are clearly visible. Interestingly, full JHOVE characterisation is sensitive to significantly more of the file than Jpylyzer, but appears to ignore parts of the file that the Jpylyzer covers.


Validation
----------

Here, we focussed on the validation tools, and instead of using the whole charactersation output as 'ground truth', we just extract the 'is Valid' result and compare that. Therefore, these maps show which parts of the JP2 appear to be validatable, not just extractable. i.e. if there is a comment in the file, the characterisation process may notice that modifying it changes the text, but may not know whether comment is valid or not.

{% include figure.html src="images/bitwiser/fig-bm-validtools.png" alt="Bitwise map of validation tool sensitivity." %}

Here we can see minor differences between JHOVE versions, indicating how this approach could be used to complement regression testing. More interestingly, it is clear that Jpylyzer is much more descerning that JHOVE in this regard. Many of the JP2 that JHOVE would pass as 'valid' are determined to be invalid by Jpylyzer, indicating that it performs a more rigourous validation process.

Rendering
---------

Judging by the above images, it is clear that none of the tools considered so far can do much to analyse the actual compressed image payload. We have seen the analysis of the file structure and the metadata, but to earn more, there is no alternative but to use an actual JP2 decompresser to convert the image to a different format, and check if that output works and if any resulting image is modified when we flip the bits.

{% include figure.html src="images/bitwiser/fig-bm-rendertools.png" alt="Bitwise map of rendering tool sensitivity." %}

This shows that OpenJpeg, ImageMagick (JasPer), and Kakadu are all highly sensitive to the image data, but ignore changes to significant fractions of the header data that the characterisation tools covered. Kakadu appears to be the most sensitive, although it is a close call, and the maps within the image data are very similar. Note that the small amounts of 'ignored' data in the image payload may well correspond to errors that were noticed but were silently corrected.

Conclusions
-----------

On it's own, this approach provides an interesting way to understand bitstreams and compare tools. The understanding of the bitstream iself can be further deepend by monitoring the output of the tool more closely. For example, when working with characterisation tools, we can see directly if the bit we just flipped modified a comment, a colour-space, or some other data or metadata the tool is capable of exposing.

Combining these approaches also allows for a sophisticated tool regression testing and comparison system, which has the distinct advantage of having to invest very little knowledge up-front about the format itself. We only need to define the output of interest for a given tool or set of tools, and can put a range of different bitstreams through them in order to learn more about both. This nicely complements the more traditional approach of documenting formats and creating format test suites.

The main limitations are firstly that redundant data cannot be distiguished from ignored data, and secondly the resources needed for such intensive processing. The former can be compensated for somewhat by learning more about and comparing the available tools that act on the same format. In this experiment, it seems likely that the majority of the ignored data really is simply ignored, but futher research would be required to come up with ways of understanding and overcoming this limitation. (MC)

The intensive processing required is more difficult to avoid. Further research could determine whether full byte-flips are an acceptable alternative to flipping each byte individually, but even then, this approach is only likely to be possible for fairly small files. However, the success of the approach does not depend on the size of the files, but rather on the degree to which the test files cover the features available in a given format. Further research, perhaps similar to [this][10], could also look at ways of analysing and mapping out the software itself.


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
