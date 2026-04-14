marks = [54.3, 112.2, 33, 55, 122, 44]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# lists are mutable you can access and change the data 
student = ["asfar", 95.5, 22, "Multan"]
print(student)
student[0] = "ahmad"
print(student)

marks = [55,66,77,5,23,66,98]
print(marks[1:4])
print(marks[-3:-1])

list = ["banana", "litchi", "apple"]
# print(list.append(4)) # mutating the list
list.reverse()
print(list)
list.insert(1, "orange")
print(list)
list.insert(1, 55)
print(list)

list.remove(55) # remove first occurance of element
print(list) 

list.pop(3)
print(list)
