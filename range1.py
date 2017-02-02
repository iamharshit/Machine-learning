import numpy as np
import csv

clip1= ['anger','fear','exciting','wonder']
clip2= ['sad','calm','romantic','wonder']
clip3= ['calm','happy','romantic','wonder']
clip4= ['happy','exciting','wonder']
clip5= ['anger','fear','exciting','wonder']
clip10= ['happy','romantic','exciting']
output = []

r1 = [0.35,0.17,0.11,0.1]
r2 = [0.2,0.11,0.1,0.1]
r3 = [0.2,0.16,0.14,0.13]
r4 = [0.3,0.11,0.1]
r5 = [0.46,0.1,0.12,0.08]
r10 = [0.15,0.1,0.1]

def interval(clipid , emotion_id):
	with open('c:/users/pratyushsnehi10/desktop/project_ml/cont_music_data.csv') as g:
		reader_g = csv.reader(g)
		for row in reader_g:
			if int (row[5]) == 1:
				if int (row[2]) == clipid:
					emotion = row[3]
					if emotion.lower() == emotion_id:
						output.append(float(row[4]))
	output.sort(reverse = 1)
	B=[]
	A = []
	count =0
	count1=0
	count2=0
	count3=0
	i =0
	for i in range(0,len(output)-1):
		a= output[i] - output[i+1]
		A.append(a)
	A.sort()
	d=int(0.75*len(A))
	# print d
	print A[d]
	# writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	# for row in A:
	# 	writer.writerow(row)
# i=0   
# with open('c:/users/pratyushsnehi10/desktop/project_ml/clip2.csv','a') as f:
for j in range(0,len(clip10)):
	interval(10,clip10[j])
# j=0