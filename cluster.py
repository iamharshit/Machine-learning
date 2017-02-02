import numpy as np
import csv
from sklearn.cluster import KMeans

clip1= ['anger','fear','exciting','wonder']
clip2= ['sad','calm','romantic','wonder']
clip3= ['calm','happy','romantic','wonder']
clip4= ['happy','exciting','wonder']
clip5= ['anger','fear','exciting','wonder']
clip10= ['happy','romantic','exciting']

def interval(clipid , emotion_id):
	A = []
	output = []
	with open('c:/users/pratyushsnehi10/desktop/project_ml/dataset1.csv') as g:
		reader_g = csv.reader(g)
		for row in reader_g:
			if int (row[5]) == 1:
				if int (row[2]) == clipid:
					emotion = row[3]
					if emotion.lower() == emotion_id:
						output.append([float(row[4])])
						#output.append([float(row[4]),row[1],clipid,emotion_id])
	for j in range(0,len(output)):
		A.append(output[j])
		A.sort()
	kmeans = KMeans(n_clusters=4,random_state=0).fit(A)
	print kmeans.labels_
	print kmeans.cluster_centers_
	B =[]
	for k in range(0,len(A)):
		B.append([A[k],kmeans.labels_[k],emotion_id])
		
	writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	for row in B:
		writer.writerow(row)
with open('c:/users/pratyushsnehi10/desktop/project_ml/cluster10.csv','a') as f:
	for j in range(0,len(clip10)):
		interval(10,clip10[j])
