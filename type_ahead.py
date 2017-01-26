s2=input("enter your string")
space_idx=[0]
explode=[]
n=len(s2)-1
a=0
for i in range(n):
  if s2.rfind(" ",a,n)>0:
    a=s2.index(" ",a,n)
    space_idx.append(a+1)
  else:
    a=n
  a=a+1
#print(space_idx)
for i in range(len(space_idx)):
    if i<len(space_idx)-1:
      explode.append(s2[space_idx[i]:space_idx[i+1]-1])

    else:
      explode.append(s2[space_idx[len(space_idx)-1]:n+1])

#print(explode)
#ngram=input("number of word in the line")
#word=input("enter the word")
word=input("your word")
start=explode.index(word)
explode2=explode[start:len(explode)]
all_index=[]
all_words=[]
for j in range(len(explode2)):
  matches=[i for i, x in enumerate(explode2) if x==explode2[j]]
  if not explode2[j] in all_words:
    all_words.append(explode2[j])
    all_index.append(matches)
  '''if len(matches)> 0:
    for m in range(0,len(matches)):
      if not matches[m] in all_index:
        all_index.append(matches[m])'''
#print(all_index,all_words)
a=[]
final=[]
count=0
for j in all_index[0]:
  #print(j)  
  if j<len(explode2)-1:
    a.append(explode2[j+1])
#print(a)
b=list(set(a))
counter=[]
for x in b:
  counter.append(a.count(x))
#  final.append([x,a.count(x)])  
#print(b,counter)


total=sum(counter)
prob=[]
for i in range(len(b)):
  cal=round(counter[i]/total,3)
  prob.append([b[i],cal])
prob2=sorted(prob,key=lambda x:x[1],reverse=True)
#prob_final=sorted(prob2, key=lambda x:x[0],reverse=True)
print(prob2)