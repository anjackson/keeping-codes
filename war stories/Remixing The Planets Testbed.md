---
title: Remixing the Planets Testbed
layout: default
categories: [war stories]
tags: [stub]
---


Which tests, when, 

Breakdown:

* Designing experiments
** GUI for complex workflows

* Running experiments
** All services hosted centrally

* Analysing results
** Manual and automated analysis
** Aggregation and data mining

* Sharing all of the above

Purpose was to explore available preservation actions and share results that would help evaluate the options. e.g. run-time, robustness, etc.

Overall
* Post hoc rationalisation of the scientific process (Article of experiments).
* Too close to PLATO due to inheritance.
* Designed by the managers instead of the users.

A Service Registry
- Central service provider with instances of all services
- Easy access to services to trial and explore the available options
- Service browser UI
- Service and tool metrics (aggregated, published results)
Corpora and ground truth
- Data browser
Full Test Environment
- Central deployment providing benchmarking environment with isolated processing.
- Also supporting local deployment for testing fairly big dry-runs (and even full local execution of preservation plans, depending who you ask).

The current Testbed software only partially achieves these aims, but suffers because it tries to pack all of these things into a single tightly-coupled package. Unfortunately, this means the software is unsustainable as it is - there are very few people who understand the code well enough to keep it running. I am one of them, and I don't have the time to maintain such a complex system.

So, my propose solution is to break this massive, ambitious system down into a set of smaller, more manageable systems that use more accessible technologies, and to adopt the work of other projects where appropriate.

For example, the SCAPE project is pushing forward the experimental workflow design GUI and execution engine, based on the excellent Taverna. This gives us a mature experiment design system that is already benign very actively used by the bioinformatics community. Critically, Tavera has system to make sharing experiment easy, and various ways to publish information about available services. By joining with this community, we can begin to see how to make an experimental infrastructure sustainable. 

SCAPE is also developing simpler ways to host and access service, by capturing tool information and invocation patterns in simple documents called Tool Specifications. These can then be deployed across different contexts with a greater degree of certainty that the results will be reproducible on different systems. This makes 'wrapping' and hosting tools much simpler, and will hopefully allow the OPF to host more services in the future, and become useful exchangeable data resources in themselves.

To complement the SCAPE work, there are three main areas I believe the OPF should work on to help carry forward the vision of the Planets Testbed.

The OPF Testbed Corpora will be based on the Planets Corpora where appropriate, but also subsume publicly available corpora with appropriate licences.

The OPF community is aware of particular processes that it wishes to perform, and of some of the tools that can be used to execute those processes. These should be developed as 'hard coded' experiments that are run automatically.

The OPF Tested REF (Result Evaluation Framework) provides a way of documenting the results of those experiments and exposing them as linked data. This will also provide a exemplar, demonstrating how preservation test results can be published, aggregated and queries.

The OPF Testbed becomes a gateway to these three distinct systems. Each can function independently and using whatever technologies are appropriate, but they nevertheless work together as web resources.

Together, they provides a rich framework for the functional testing of critical preservation processes. For example, a suite of identification tools could be run against a suitable corpus of material. Aggregate metrics can be derived, such as the fraction of the corpus for which each tool can generate a format identification. Critically, by comparing results of different tools, we can focus in on where tools disagree about the format in order to learn where the tools must be improved. Best of all, this can work from the beginning, before any ground-truth or other annotations have been generated! By pitting the tools against each other, and publishing the results, we provide a strong motive for tools to be improved and a set of concrete metrics for capturing that improvement.

Dave Tarrant has been working on this concept with the OPF, and has been demoing the REF at the Cologne Hackathon.

Service browser bits and dupes
Some parts of (2) in invoke app
Comparison UI (5)
Basic performance graphing (4)
Aggregation and mining results 

OPF Testbed as a gateway to a set of technically independent but interlinked systems:
- Corpora
- REF Results Evaluation Framework
RAT?

Data browser replaced with the web, Drupal for corpora.


Large scale functional testing is best done statically. Identification on GovDocs, parallel testing of jp2 tools.

Large scale data selection in GUI is v clumsy
Simple invocation GUI as exploratory channel when designing large scale experiments - essentially a service browser that can run them too

Corpora

ONB Corpus
BL Corpora
GovDocs1


http://www.3windmills.com/thesis/
http://wiki.opf-labs.org/display/PT/Proposal - Extended MIME Type Identifiers

