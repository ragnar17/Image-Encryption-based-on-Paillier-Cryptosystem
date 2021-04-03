import cv2
import paillier
import numpy as np
import ImageOperations as cryp
import floating_point as fp
import copy
path = 'images/a.png'
# path = 'images/acolor.tiff'
# path = 'images/1000px-image.jpg'
img = cv2.imread(path,0)
c = copy.deepcopy(img)

pr,pb = paillier.generateKeypair(30)
print(pb,pr)
bb = []
mod = 256

for i in range(len(c)):
	bb.append([0]*len(c[i]))
	for j in range(len(c[i])):
		E = fp.encryptFP(pb,int(c[i][j]))
		bb[i][j] = E


m = copy.deepcopy(c)

v = 100
xx = cryp.Secure_Image_Adjustment_Brightness_Control(bb,v,pb)
xx = cryp.Secure_Image_Adjustment_Image_negation(bb,v,pb)
xx = cryp.Secure_Noise_Reduction_LPF(bb,2,2,pb)


for i in range(len(c)):
	for j in range(len(c[i])):
		m[i][j] = min(255,int(fp.getValue(pr,pb,xx[i][j])))


cv2.imshow('Naive',m)

cv2.waitKey(0)
cv2.destroyAllWindows()
