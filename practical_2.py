#20/01/2026

#tuples

t1 = (10, 20, 30, 40)

print( t1)
print(t1[0])
print(t1[-1])


nested_tuple = (1, 2, (3, 4, 5), 6)
print(nested_tuple)
print(nested_tuple[2][1])

tuple = t1*2
print(tuple)

t2 = (5, 10, 15, 20, 25)
concatinate_tuple = t1 + t2
print("First Tuple:", t1)
print("Second Tuple:", t2)
print("Concatenated Tuple:", concatinate_tuple)


#dictionary

student = {"roll_no":40,"name": "Alcor","marks": 95}

print("Dictionary:", student)
print(student["name"])
print(student.get("marks"))

student["marks"] = 99
student["grade"] = "o"
print(student)

removed_value = student.pop("grade")
print(removed_value)
print(student)

student.popitem()
print(student)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged_dict = d1 | d2
print(d1)
print(d2)
print(merged_dict)