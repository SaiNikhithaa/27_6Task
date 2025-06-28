#Create a set with elements from 1 to 5. Add elements 6 and 7 to the set in one line.
s={1,2,3,4,5}
s.update({6,7})
print(s)
#Given two sets:
 #          A = {1, 2, 3, 4, 5}
 #          B = {4, 5, 6, 7, 8}
#Find elements that are present in A or B but not both (symmetric difference).
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.symmetric_difference(b))
#Remove an element from a set, but avoid error if element doesn't exist.
 #Find maximum and minimum element from a set {5, 8, 12, 3, 15, 7}.
a={5,8,12,3,15,7}
print(a.discard(11))
print(max(a))
print(min(a))
#Create a set with the values: 10, 20, 30, 40. Then add the value 50 to the set.
c={10,20,30,40}
c.add(50)
print(c)
#Remove an element 30 from a set {10, 20, 30, 40, 50} using a set method.
d={10,20,30,40,50}
d.remove(30)
print(d)
#Check whether the number 25 exists in the set {15, 20, 25, 30, 35}.
f={15,20,25,30,35}
if 25 in f:
    print("Yes the number is in the set")
else:
    print("No the given number is not htere in the set")
#Find the union of two sets:
 #          A = {1, 2, 3, 4}
#           B = {3, 4, 5, 6}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
#Find the intersection of two sets:
#           A = {10, 20, 30, 40}
#            B = {30, 40, 50, 60}
A={10,20,30,40}
B={30,40,50,60}
print(A.intersection(B))