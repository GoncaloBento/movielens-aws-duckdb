## Folder Structure
- This folder is splitted in several preprocessing pipelines depending on the dataset we're working on:
    - Genres dataset: genres_pipeline
    - Movies dataset: movies_pipeline
    - Occupations dataset: occupations_pipeline
    - Ratings dataset: ratins_pipeline

- The ideia of these pipelines is to make the preprocessing stage a bit more automatic and save time when we escalate for other datasets:
    - Example of usage: from src.processing.ratings_pipeline import check_incongruencies --> ratings_df = check_incongruencies(ratings_df)