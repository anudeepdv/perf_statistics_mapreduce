import string
import map_reduce
import re
import math
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = int(v1[i]); y = int(v2[i])
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def mapper(input_key,input_value):
  return [(word.strip(),1) for word in 
          remove_punctuation(input_value.lower()).split('\n\n\n')]

def remove_punctuation(s):
  return s.translate(string.maketrans("",""), string.punctuation)

def reducer(intermediate_key,intermediate_value_list):
  return (intermediate_key,sum(intermediate_value_list))

filenames = ["file3.txt"]
i = {}
for filename in filenames:
  f = open(filename)
  i[filename] = f.read()
  f.close()
f = open("output.txt","w")
#print(map_reduce.map_reduce(i,mapper,reducer))
l=map_reduce.map_reduce(i,mapper,reducer)
l3=[];c=[]
for (a,b) in l:
 s=a.split('\n')
 i=0;
 l1=[]
 for a in s:
  l1.append(a.strip())
 l1=l1[2:6]
# print(l1)
 l2=[]
 for a in l1:
  s=list(a.split('      '))
  l2.append(s[0])
 print(l2)
 f.write(str(l2)+'\n')
 if(l3!=[]): 
  cs=cosine_similarity(l2,l3)
  c.append(cs)
  print"cosine similarity:",cs
 l3=l2
f.write(str(c)+'\n')
f.close()
