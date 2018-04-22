import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


query_images = [] # list of images like index images
index_descriptors = {} #dictionary of index images
d = 5 #no of reduced dimensions     
k = 50 #no of clusters   

#index_descriptors = {0:np.array([[1,2,3],[3,2,5],[4,2,5]]),1:np.array([[1,3,5],[2,4,6],[3,3,3]]),2:np.array([[3,4,5],[3,4,7],[7,5,8]])}

index_list = []

count = 0
descrip_vec = None 
for des in index_descriptors.values():
    if descrip_vec is None:
        descrip_vec = des
    else:
        descrip_vec = np.concatenate((descrip_vec, des), axis=0)    
    index_list.append([count,count+len(des)-1])
    count = count + len(des)

pca = PCA(n_components=d)
pca.fit(descrip_vec)
descrip_vec = pca.transform(descrip_vec)

km = None
def cluster():
    global km
    km = KMeans(n_clusters = k).fit(descrip_vec)
cluster()

# bag of words----------------------------------
bag_of_words = np.zeros((len(index_descriptors),k))

for i,indices in enumerate(index_list):
	for j in range(indices[0],indices[1]+1):
		bag_of_words[i][km.labels_[j]] = bag_of_words[i][km.labels_[j]]+1

#nneigbours----------------------------------
nbrs = NearestNeighbors(n_neighbors=1).fit(bag_of_words)

for q in query_images:
	img = cv2.imread(q)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = surf.detectAndCompute(img,None)
    pca.fit(des)
	des = pca.transform(des)
	centers = km.predict(des)
	word = np.zeros((1,k))
	for c in centers:
		word[centers]=word[centers]+1
	dist,indices = nbrs.kneighbors(word)
	print(indices)







