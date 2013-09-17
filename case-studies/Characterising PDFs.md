---
title: Characterising PDFs
layout: default
categories: [case-studies]
---

Note Sumatra PDF, no support for Thumbs or Fast View. Other things missing?

11:33

For the ESTAR project, and indeed elsewhere, we want to be able to spot encrypted PDFs so that any access-time problems can be caught as early as possible. Initially, this looked like it would be pretty easy, using JHOVE to pull of the PDF properties and using those to spot the encryption. However, it turns out that PDF encryption and the digital rights management systems are intertwined, and that this complicated matters terribly.

PDF has two types of 'encryption' - it uses an 'user' password to limit the ability to open the document, and a 'creator' password to limit other rights, like printing, copying, etc. The former case, where a password is required to open the file, is the main preservation concern, as our user's won't be able to open a PDF encrypted in this way. However, the latter case causes problems, because the PDF is encrypted here to, but with a special known user password, "" (yes, an empty string, and yes this is not the same as no password!). So, the document is encrypted in both cases, and you can only tell which is which by attempting to decrypt the PDF using the special default password "".

This is important from a characterisation point of view. This is a critical property of the object, but any software that simple enumerates the intrinsic properties of a digital object will not be able to determine it. When JHOVE is run, all it sees are encrypted PDFs, and the same would be true for XCL. This critical property is not a statement about the information content of the object, but a statement about the outcome of a process (algorithm) that must be applied to that document in order to access it - i.e. a statement about the implied performance. This type of 'characteristic' therefore requires that the characterisation tool understand not simply the format of the object, but the interpretation of that data that is required during a performance.
