import wikipedia
import math
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


class AcademicSearchEngine:

    def search(self, query):

        query = query.lower()
        query = re.sub(r'[^a-zA-Z ]', '', query)

        stop_words = set(ENGLISH_STOP_WORDS)
        query_words = [w for w in query.split()
                       if w not in stop_words]

        search_results = wikipedia.search(query, results=2)

        documents = []
        urls = []

        for title in search_results:
            try:
                page = wikipedia.page(title,
                                      auto_suggest=False)

                text = re.sub(
                    r'[^a-zA-Z ]',
                    '',
                    page.content.lower()
                )

                documents.append(text)
                urls.append(page.url)
            except:
                continue

        clean_docs = [
            [w for w in doc.split()
             if w not in stop_words]
            for doc in documents
        ]

        vocabulary = list(set(query_words))
        N = len(clean_docs)

        df = [
            sum(1 for doc in clean_docs if t in doc)
            for t in vocabulary
        ]

        idf = [
            math.log((N+1)/(d+1))+1
            for d in df
        ]

        tfidf = []

        for doc in clean_docs:
            doc_len = len(doc)
            row = []

            for i,term in enumerate(vocabulary):
                tf = doc.count(term)/doc_len
                row.append(tf * idf[i])

            tfidf.append(row)

        query_tf = [
            query_words.count(t)/len(query_words)
            for t in vocabulary
        ]

        query_vector = np.array([
            query_tf[i]*idf[i]
            for i in range(len(vocabulary))
        ]).reshape(1,-1)

        doc_matrix = np.array(tfidf)

        similarity = cosine_similarity(
            doc_matrix,
            query_vector
        )

        scores = [s[0] for s in similarity]

        ranked = sorted(
            [(i,score)
             for i,score in enumerate(scores)],
            key=lambda x:x[1],
            reverse=True
        )

        results = []

        for rank,(doc_id,score) in enumerate(ranked,1):

            preview = " ".join(
                documents[doc_id].split()[:80]
            )

            results.append({
                "rank": rank,
                "score": round(score,4),
                "url": urls[doc_id],
                "abstract": preview
            })

        return results