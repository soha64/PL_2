 
#12/01/2026

#lists

A= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print("Original List:", A) 

print("First element:", A[0]) 

print("Last element:", A[-1]) 

A.append(20)          

A.insert(2, 12)        

print("List after adding elements:", A) 
A.remove(8)           

A.pop()                
print("List after removing elements:", A) 

A.sort() 
print("Sorted List:", A) 

A.reverse() 
print("Reversed List:", A)


#Sets

X = {1, 2, 3, 4, 5} 
Y = {4, 5, 6, 7, 8} 

union_set = X.union(Y) 
print( union_set) 
intersection_set = X.intersection(Y) 
print(intersection_set) 
difference_set = X.difference(Y) 
print(difference_set) 
difference_set2 = Y.difference(X) 
print(difference_set2)