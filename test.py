import random
l = []
#print(int(random.random()*100/1))
for x in range(1,100):
	y = int(random.random()*100)
	l.append(y)
print(l)	
print("********************************************************************************************")
# def searchMax(l):
# 	max = l[0]
# 	for x in l:
# 		 if x > max:
# 		 	max = x	 
# 	return max	 		
# print(searchMax(l))
max = l[0]
for x in l:
	if x > max:
		max=x;
print (max)		