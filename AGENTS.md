# Review Analysis Project Recap

## Purpose
- Open-ended review analysis that discovers evaluable entities and ranks them by aggregated sentiment.
- Source data: `reviews.csv`
- Outputs: `entity_stats.csv`

## Environment setup
- Poetry is used for dependencies and running the notebook.
- `poetry config keyring.enabled false` to avoid DBus keyring errors.
- GitHub CLI installed locally at `/home/lbk/.local/bin/gh` (optional; repo cloned via git).

## Notebook workflow (`entity_sentiment_discovery.ipynb`)
- Entity extraction is open-ended; no fixed categories.
- Uses YAKE + multilingual NER + regex for numeric entities (e.g., `버스 51`).
- Low-confidence NER mentions are kept and tagged `entity_unknown`.
- Sentiment is computed on the sentence containing each entity (entity-level sentiment).
- Entities are clustered by embedding similarity for grouping; ranking is per entity.

## How to run
1) `poetry shell`
2) Open `entity_sentiment_discovery.ipynb` in VS Code.
3) Select the Poetry kernel and run all cells.

## Output columns (`entity_stats.csv`)
- `entity`
- `entity_cluster`
- `entity_tag` (NER tag or `entity_unknown`)
- `n_mentions`
- `n_reviews`
- `mean_sentiment`
- `median_sentiment`

## Tuning knobs
- NER confidence threshold for `entity_unknown` (default 0.70).
- YAKE `top` values to adjust recall vs precision.
- Regex patterns for numeric entities.
