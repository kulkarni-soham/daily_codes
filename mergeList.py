list1=[1,2,5,5]
list2=[2,7,4,3]
list1.sort()
list2.sort()

list3=[]
i=0
j=0
while i<len(list1) and j<len(list2):
    if list1[i]<=list2[j]:
        list3.append(list1[i])
        i+=1
        
    else:
        list3.append(list2[j])
        j+=1
        
    
if i<len(list1):
    list3.append(list1[i])
    
elif j<len(list2):
    list3.append(list2[j])
        
print(list3)