
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pandas as pd
import json
import random


data = pd.read_csv('./data/preprocessed.csv',
                   encoding='utf-8', on_bad_lines='skip')


def tfidf():

    tf_idf_vectorizor = TfidfVectorizer(max_features=5000)
    tf_idf = tf_idf_vectorizor.fit_transform(data['tweets'][:])
    tf_idf_norm = normalize(tf_idf)

    tf_idf_array = tf_idf_norm.toarray()
    a = pd.DataFrame(
        tf_idf_array, columns=tf_idf_vectorizor.get_feature_names_out())
    return tf_idf_array


def cluster(k):
    tf_idf_array = tfidf()

    sklearn_pca = PCA(n_components=2)
    Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

    model = KMeans(n_clusters=k).fit(Y_sklearn)
    labels = model.labels_

    Y_sklearn = Y_sklearn.tolist()
    labels = labels.tolist()
    cluster = [Y_sklearn, labels]

    return cluster

def transformToDataset(raw):
    cluster = []
    Y_sklearn = raw[0]
    labels = raw[1]

    clusterName = set(labels)
    for i in clusterName:
        hexColor = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
        cluster.append({'label': i, 'data': [],'backgroundColor': hexColor})

    for i in range(0,len(Y_sklearn)):
        data = {
            'x' : Y_sklearn[i][0],
            'y' : Y_sklearn[i][1],
            'r' : 10
        }
        n = labels[i]
        cluster[n]['data'].append(data)
    
    return cluster



if __name__ == "__main__":
    clusters = cluster(3)
    transformedCluster = transformToDataset(clusters)
    c = json.dumps(transformedCluster)
    print(c)
