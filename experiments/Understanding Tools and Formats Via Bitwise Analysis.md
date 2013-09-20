---
title: Understanding Tools & Formats Via Bitwise Analysis
layout: default
categories: [experiments]
publish: true
---

Recently, at the [SPRUCEdp Unified Characterisation Hackathon][3], I [presented some early work][4] on using bitwise analysis of digital resources to better understand how software tools operate upon them. [A recent blog post][5] reminded me that I had not yet publicised the results more widely. This document outlines the approach and my initial results, showing how the bit-level sensitivity of various JP2 tools can be effectively mapped and compared.


Bitwise Analysis
----------------

At heart, the approach is a very simple brute-force analysis. Imagine we take some test image, such as this small fragment of a photograph.

{% include figure.html src="images/bitwiser/16px-photo.png" alt="The source image." %}

First, we convert it to the format of interest, [JP2][2] (via [PPM][1] using ImageMagick, and then through Kakadu). Looking at the byte values, and generating an image of the data inside the file, we get the figure shown below, with clear 'quiet' and 'noisy' areas. For a compressed format, we can be fairly certain that the high-entropy 'noisy' region corresponds to the compressed image data, and the 'quiet' area to file structural information and metadata.

{% include figure.html src="images/bitwiser/fig-bm-original.png" alt="Bitwise map of the source data file." %}


But this small file can allow us to go further than this, and be used to map out the data and compare JPEG 2000 tools in much more detail.

Taking JHOVE as an example, we start by wrapping it up a script that take our test file as input, and extracts the 'is Valid' result from JHOVE's output. This output becomes our 'ground truth' for this experiment.

We then being the brute-force bitwise analysis. That is we go through the entire file, byte by byte, and within each byte, bit by bit. We flip each bit in turn, and for each one, we re-run the JHOVE on the modified file, and observe if the output from JHOVE changes. Then we flip the bit back and move on to the next bit.

For each byte, we note which bits modified the result, and which did not, and convert that to a greyscale pixel value for that part of the datafile, which indicates how sensitive the validation process was to that byte. This builds up a map of the data, indicating how sensitive that software process was to each part of the file. By convention, we use black to mean completely insensitive areas, whereas white mean even a single bit-flip would have been noticed.

This procedure can be repeated for multiple tools, and the sensitivity maps compared.

NOTE silent fixing cannot be seen.

Characterisation
----------------

First, we looked at identification and characterisation tools, as shown below:

{% include figure.html src="images/bitwiser/fig-bm-chartools.png" alt="Bitwise map of characterisation tool sensitivity." %}

For the file tool, which only performs identification, we can clearly see that it is only sensitive to the JPEG 2000 'magic number' at the start of the file. (Note, does DROID use an EOF marker?).

The other tools perform deeper analysis. The next most sensitive one, jp2StructCheck, was the predecessor of jpylyzer, and although clearly more sensitive that file, the fact that it only checks high-level features can be clearly seen. The exiftool metadata extractor is clearly much more sensitive to the file header, but does not inspect any other parts of the file. The advances made by Jpylyzer over jp2StructCheck are clearly visible. Interestingly, full JHOVE characterisation is sensitive to significantly more of the file than Jpylyzer, but appears to ignore parts of the file that the Jpylyzer covers.


Validation
----------

In this case, we only look at validation tools, and instead of using the whole charactersation output as 'ground truth', we just extract the 'is Valid' result and compare that. Therefore, these maps show which parts of the JP2 appear to be validatable, not just extracted. i.e. if there is a comment in the file, the characterisation process may notice that modifying it changes the text, but cannot know whether it is valid or not.

{% include figure.html src="images/bitwiser/fig-bm-validtools.png" alt="Bitwise map of validation tool sensitivity." %}

Here we can see minor differences between JHOVE versions, indicating how this approach could be used to complement regression testing. More interestingly, it is clear that Jpylyzer is much more descerning that JHOVE in this regard. Many of the JP2 that JHOVE would pass as 'valid' are determined to be invalid by Jpylyzer, indicating that it performs a more rigourous validation process.

Rendering
---------

Judging by the above images, it is clear that none of the tools considered so far can do much to analyse the actual compressed image payload. We have seen the file structure and the metadata, but cannot tell if the image data is usable. For this, there is no alternative but to use an actual JP2 decompresser to convert the image to a different format, and check if that output image is modified when we flip the bits.

{% include figure.html src="images/bitwiser/fig-bm-rendertools.png" alt="Bitwise map of rendering tool sensitivity." %}

This shows that OpenJpeg, ImageMagick (JasPer), and Kakadu are all highly sensitive to the image data, but ignore changes significant fractions of the header data. Kakadu appears to be the most sensitive, although it is a close call, and the maps within the image data are very similar. Note that the small amounts of 'ignored' data in the image payload may well correspond to errors that were noticed but were silently corrected.

Conclusions
-----------

Deeper Understanding - Using it to understand whcih parts are changing.

Regression testing, possible improvement tracking.

Limitation of silent fixing.


[1]: images/bitwiser/16px-photo-png-im.ppm
[2]: images/bitwiser/16px-photo-png-im-ppm-kdu.jp2
[3]: http://wiki.opf-labs.org/display/SPR/SPRUCE+Hackathon+Leeds,+Unified+Characterisation
[4]: http://www.slideshare.net/andrewnjackson/unified-characterisation-please
[5]: http://www.openplanetsfoundation.org/blogs/2013-02-14-exploring-impact-flipped-bits

