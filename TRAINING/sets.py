#create a set
myset={1,4,"harsha","sriraj",4.2,3,"nandu"}
print(myset)

#acccessing elements
#print(myset[1])

#remove
myset.remove(4)
print(myset)

#pop
myset.pop()
print(myset)

#frozenset
fs=frozenset(myset)
print(type(fs))
print(fs)