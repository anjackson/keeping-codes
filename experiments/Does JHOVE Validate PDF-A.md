---
title: Does JHOVE Validate PDF/A Files?
layout: default
categories: [experiments]
tags: [draft]
permalink: "does-jhove-validate-pdfa-files.html"
publish: true
---

Introduction
------------

JHOVE's [PDF-hul page](http://jhove.sourceforge.net/pdf-hul.html#coverage) claims it is capable of validating PDF/A files (*emphasis mine*):

> **The PDF-hul module recognizes and validates the following public profiles:**
>
> - PDF version 1.0-1.6
> - PDF/X-1, PDF/X-1a, PDF/X-2, and PDF/X-3
> - Linearized PDF
> - Tagged PDF
> - **PDF/A (ISO/DIS 19005-1)** 

It is not clear which of the two possible levels of formal compliance this refers to (PDF/A-1a or PDF/A-1b). Later on in that document, the authors enumerate the relatively small number of features that are tested:

> - No encryption dictionary
> - No Encrypt or Info entries in trailer
> - Document catalog dictionary specifies RFC1766 language
> - Document catalog dictionary has no AA or OCProperties
> - Form fields do not have AA actions
> - No Launch, Sound, Movie, ResetForm, ImportData, or JavaScript actions
> - Fonts have recognized encoding
> - Uncalibrated color spaces have OutputIntent specified
> - Page objects do not have Movie, Sound, or FileAttachment
> - Non-text annotations have Contents key
> - Unfiltered metadata stream 

before making a more measured statement of the scope of the validation:

> Note that the PDF module does not parse the contents of streams, so it cannot determine conformance to PDF/A to the degree required by the ISO standard.

This seems like a significant limitation. The [primary author of JHOVE](https://twitter.com/GaryM03062) goes further:

> "The PDF/A profile test is particularly shaky; the requirements are very complicated, and checking them as an afterthought to a module checking PDF conformity doesn't work very well."
> <small>[JHOVE usage notes](http://www.garymcgath.com/jhovenote.html)</small>

Those of us who have spent a significant amount time using or hacking on JHOVE have similar opinions about it's shortcomings ([e.g.](http://fileformats.wordpress.com/2013/02/01/future-jhove/#comment-3292)). However, it's not clear that the wider community understands this, and it still [gets](https://twitter.com/putt1ck/status/494799471604404224) [occasional](http://stackoverflow.com/a/11391783) [recommendations](http://tex.stackexchange.com/q/79947) as a PDF/A validation tool.


### The Value Of Test Suites ###

Ideally, to resolve this issue, we would be able to test how well JHOVE validates PDF/A documents by running it over a suitable test suite. While we do not [yet](http://www.preforma-project.eu/call-description.html) have a compliance-testing corpus that covers the entire PDF/A standard, there is one for *non*-compliance with the PDF/A*-1b* part of the specification: [the Isartor Test Suite](http://www.pdfa.org/2011/08/download-isartor-test-suite/).

The Isartor Test Suite is an excellent resource, and exactly the kind of thing we could use more of in digital preservation. It contains a set of PDF files where each one carefully violates a particular aspect of the PDF/A-1b standard. Each PDF is also self-documenting, in that the text and embedded metadata describe what part of the PDF/A-1b specification is being violated.

Note that [PDF/A-1b](http://www.digitalpreservation.gov/formats/fdd/fdd000252.shtml) is the lowest level of PDF/A compliance, and the test suite only enumerates the individual failure cases. This makes things somewhat easier on the tools, as they only have to avoid *false-positive* validations at the *minimum* level of compliance. However, it is still a very useful baseline test.

So, if JHOVE can validate PDF/A files, it must be able to validate PDF/A-1b files, and therefore every PDF file in the test suite should be found to be invalid.

Method
------

I used JHOVE 1.11[^1], installed on my Mac via Homebrew. I made scripts to [run JHOVE and store the output](./pdfa/run-jhove.sh), and to [do the same for all the files](./pdfa/jhove-all-files.sh). Once I had the JHOVE output, I tabulated and graphed the results.

<!--
     grep --text " Status:" pdfa/isartor-flat-testsuite/*.jhove-1.11.txt | sort > pdfa/results.1-11.txt
-->

Results
-------

Here is a summary of the results[^2], showing how many of the PDF/A-1b test files JHOVE correctly determined to be invalid:

![JHOVE FAILs the Isartor test](pdfa/pie-of-fail.png)

JHOVE only managed to detect one invalid PDF/A-1b file from this set of 204 invalid files. This seemed odd, as even the [presence of encrypted data](./pdfa/isartor-flat-testsuite/isartor-6-1-3-t02-fail-a.pdf.jhove-1.11.txt) was not being picked up. Closer inspection revealed I'd made the classic JHOVE user error of not double-checking what format and profile JHOVE was validating against. I had specified that JHOVE should validate as PDF, but the interface does not allow me to assert that I intend JHOVE to validate against the PDF/A-1b profile[^3]. To understand what was going on, I had to take the `Profile` field into account.

|--------------------------------------+-------------------------------+-------------------------|
| Profile                              | "Well-Formed and valid" count | "Not well-formed" count |
|--------------------------------------+:-----------------------------:+:-----------------------:|
| *none* (i.e. PDF 1.4 only)           | 50                            | 1                       |
| Linearized PDF, ISO PDF/A-1, Level B | 2                             | 0                       |
| ISO PDF/A-1, Level B                 | 151                           | 0                       |
|======================================+===============================+=========================|

For some reason, despite the presence of the PDF/A-1b declaration in the embedded metadata, JHOVE is failing to identify 51 of the test PDFs as being PDF/A-1b and so *only* performs the basic PDF-1.4 validation. The remaining 153 test PDFs were correctly identified as being PDF/A-1b, but were falsely determined to be valid.

![JHOVE Results Broken Down By Profile](pdfa/pie-of-profiles.png)

The full, raw JHOVE results are available [below](#appendix).

Conclusion
----------

Don't use JHOVE to validate PDF/A.

Maybe try [Apache Preflight](https://pdfbox.apache.org/cookbook/pdfavalidation.html) instead.

Appendix
--------

Here, each filename is linked to the JHOVE output, and is shown alongside the overall validation result from JHOVE. If you want to get an idea of what aspect of PDF/A-1b each file is exercising, you can go and look at the text in the JHOVE output, or [examine the original folder structure of the test suite](./pdfa/isartor-flat-testsuite/original-names.txt) as this reflects the structure of the specification.

|----+----|
| Link to full results | JHOVE Status |
|----+----|
| [isartor-6-1-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Not well-formed |
| [isartor-6-1-2-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-2-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-3-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-3-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-3-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-3-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-3-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-3-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-3-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-3-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-4-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-4-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-4-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-4-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-6-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-6-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t04-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t04-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-7-t04-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-7-t04-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t05-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t05-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-8-t06-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-8-t06-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-10-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-10-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-10-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-10-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-10-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-10-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-11-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-11-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-11-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-11-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-12-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-12-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-12-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-12-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-12-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-12-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-12-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-12-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-1-13-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-1-13-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-10-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-10-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-10-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-10-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-10-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-10-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-2-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-2-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-2-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-2-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-2-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-2-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t02-fail-j.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t02-fail-j.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t03-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t03-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t03-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t03-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t03-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t03-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t03-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t03-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t04-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t04-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t04-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t04-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t04-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t04-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t05-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t05-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-3-t05-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-3-t05-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-4-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-4-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-3-4-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-3-4-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-4-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-4-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-4-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-4-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-4-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-4-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-4-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-4-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-5-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-5-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-6-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-6-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-7-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-7-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-7-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-7-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-8-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-8-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-2-9-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-2-9-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-2-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-2-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-2-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-2-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-3-1-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-3-1-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-3-1-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-3-1-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-3-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-3-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-3-3-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-3-3-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-3-3-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-3-3-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-4-t01-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-4-t01-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-5-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-5-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-6-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-6-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-6-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-6-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-6-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-6-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-7-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-7-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-7-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-7-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-3-7-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-3-7-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-4-t05-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-4-t05-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t01-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t01-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-2-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-2-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t02-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t02-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t02-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t02-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t03-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t03-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t03-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t03-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t03-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t03-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t04-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t04-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t04-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t04-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-5-3-t04-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-5-3-t04-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t01-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t01-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t02-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t02-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t03-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t03-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-1-t04-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-1-t04-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-6-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-6-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-2-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-2-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-2-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-2-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-2-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-2-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-2-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-2-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-2-t03-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-2-t03-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-3-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-3-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-3-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-3-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-3-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-3-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-5-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-5-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-5-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-5-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-e.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-e.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-f.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-f.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-g.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-g.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-h.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-h.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-i.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-i.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-j.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-j.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-8-t02-fail-k.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-8-t02-fail-k.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-9-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-9-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-11-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-11-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-11-t01-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-11-t01-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-11-t01-fail-c.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-11-t01-fail-c.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-7-11-t01-fail-d.pdf](./pdfa/isartor-flat-testsuite/isartor-6-7-11-t01-fail-d.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-9-t01-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-9-t01-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-9-t02-fail-a.pdf](./pdfa/isartor-flat-testsuite/isartor-6-9-t02-fail-a.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
| [isartor-6-9-t02-fail-b.pdf](./pdfa/isartor-flat-testsuite/isartor-6-9-t02-fail-b.pdf.jhove-1.11.txt) | Status: Well-Formed and valid |
|----+----|


Footnotes
---------

[^1]: I initially ran the analysis using 1.10, for which the results are the same.
[^2]: I realise this is a rather sarcastic pie chart, but I need a way to drive the magnitude of this discrepancy home to the broader community of users, and to try to ensure they remember it. No offence is intended.
[^3]: Similarly, if you don't specify a format to validate against, and just look at the `Status`, you can miss the fact that the only reason your bitstream appears to be valid is because JHOVE could not identify the format at all, and is just reporting that you have a valid *bytestream*. Always check the `Format` and the `Profile` as well as the `Status`.


