set(stories.columns) - set(stories.dropna(thresh=10, axis=1).columns)
