# Long-Tail Music Recommender

Most recommenders keep suggesting the same popular artists, because popular items get more
clicks, which makes them look even more relevant (a popularity feedback loop). This project
measures that bias on Last.fm listening data and tests ways to surface lesser-known artists
that still match a listener's taste.

## Questions
1. How strongly does a standard collaborative-filtering model (ALS) favor popular artists?
2. How much accuracy (NDCG@k, recall@k) do we give up for more novelty and long-tail coverage?
3. Which debiasing method (re-ranking, inverse propensity scoring) gets the best trade-off?

## Data
[Last.fm 360K](http://ocelma.net/MusicRecommendationDataset/lastfm-360K.html): user, artist and
play counts for about 360K users. The data is not included in this repo. Its license allows
non-commercial use only. To download it, run:

```bash
python scripts/download_data.py
```

## Project layout
| Path | What's in it |
|---|---|
| `notebooks/` | Exploration and the analysis story, in order (01_eda, 02_als_baseline, ...) |
| `src/recsys/` | Reusable code: data loading, models, metrics, re-ranking |
| `app/` | Streamlit demo with a "discovery slider" |
| `tests/` | Unit tests for the metrics |
| `reports/figures/` | Charts used in this README |

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Results
_Coming soon: accuracy vs. long-tail coverage trade-off chart._

## License
Code: MIT (see `LICENSE`). Data: see the Last.fm 360K dataset terms.
