"""
for i in range(1,11):
    if i != 1:
        print(end="\n")
    for j in range(1,11):
        if i*j < 10:
            print(i*j,end="   ")
        else:
            print(i * j, end="  ")
"""
for i in range(1,11):
    if i != 1:
        print("*********************")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
