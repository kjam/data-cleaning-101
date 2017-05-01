set(stories.columns) - set(stories.dropna(thresh=5, axis=1).columns)
