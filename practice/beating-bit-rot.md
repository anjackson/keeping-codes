Beating Bit-Rot
- Bit Bucket Options: Evaluate existing platforms
- Alignment of non arcival and archival content: What stored where? Who accesses it?
- Problems with Petabyte-for-a-century and the half-life model.
- http://lintool.github.io/my-data-is-bigger-than-your-data/
- https://code.facebook.com/posts/229861827208629/scaling-the-facebook-data-warehouse-to-300-pb/
- http://www.openplanetsfoundation.org/blogs/2011-01-12-format-obsolescence-and-sustainable-access
- Pick apart http://queue.acm.org/detail.cfm?id=1866298
"No feasible experiment could validate them. They are projections based on models of how components of the system such as disks and software behave. "
- Pick apart necessity of 'semantic lossy compression', and note increase costs just increases incentive for more clever storage solutions.
-- The 'half life' model as misleading as it's assumption of uncorrelated bits makes everything look weird.
-- Simple model showing how probability of data loss is not necessarily related to volume of data. i.e. same distributed array, but smaller disks. Tunable probability of loss. Uncertainly comes from difficult to model things like disasters, but these have almost no relation to bit-wise errors.
-- 1.33-CKSS: Erasure codes, fountain codes. c.f. OpenStack Swift, Azure, that other company that came in to BL, Ceph.
--- Simple mirrors worse than block codes, can mitigate against the same risks but decouple/reduce correlation between individual bit-streams and their carriers.
-- Smart transparent compression. Hidden FLAC, JP2, etc. but user always sees WAV, TIFF, etc.
- References
-- http://research.microsoft.com/en-us/um/people/chengh/papers/LRC12.pdf
-- http://ceph.com/docs/firefly/dev/erasure-coded-pool/


Use error-correction codes to patch up bit-level errors?
- http://en.wikipedia.org/wiki/Forward_error_correction
Parity Alternatives
-Format+Size+hash+ECC+brute-force is sufficient?
-Shannon Entropy helps?

