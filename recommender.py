# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# print(df.columns.values)
# cv = CountVectorizer(max_features=5000, stop_words='english')
# vectors = cv.fit_transform(df['tags']).toarray()
# similarity = cosine_similarity(vectors)
# np.save('similarity.npy', similarity)

import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv("Finalized_file.csv"))
similarity = np.load('similarity.npy') # Shape: (4806, 4806)


def recommender_function(movie):
	movie = df[df['title'] == movie.lower()]
	if not movie.empty:
		index = movie.index[0]
		# (index, similarity in scale of 0-1)
		res = [i[0] for i in sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])[1: 6]]
		return [df.loc[i, 'title'] for i in res]

	return "Movie not found"
