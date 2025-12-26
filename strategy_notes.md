# Strategy notes (2025-09-02)

New scoped approach: reviewers must select the entity (franchise restaurant or menu item) before writing a review, and reviews are short. Sentiment is computed at the full-review level (not sentence-level). The system must validate consistency between the selected entity and the review text.

Consistency checks to mitigate mismatch or bias:
- Require the selected entity or known alias to appear in the review text (exact or fuzzy match).
- For dish reviews, require menu item tokens or ingredient keywords.
- For restaurant reviews, require at least one service/location/ambience/staff keyword.
- Use embedding similarity between review text and entity description/aliases; flag low similarity.
- If NER detects a different restaurant/brand than the selected entity, flag the review.
