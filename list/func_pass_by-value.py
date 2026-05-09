def func(a: int, b: int):  # pass by value
    # local variable     #immutable
    a = 100
    b = 200
    print(f"id if {id(a)},and id of {id(b)}")


# int,str,float   mutable
a = 1
b = 2
print(f"id of {id(a)}, and id of {id(b)}")
func(a, b)
print(a)
print(b)
