lst = [1, 2 ,3]
lst2 = lst.copy()

lst2.append(4)

print(id(lst), end='')
print(id(lst2))


print(lst)
