s=input("Please enter a string: ")

freq={}

for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
lst=[]
k=0
for i in freq:
    k=freq[i]
    lst.append(k)
   
lst.sort()
lst.reverse()

for i in lst:
    for j in freq:
        if(i==freq[j]):
            print(j," = ",i)
            freq[j]=0
