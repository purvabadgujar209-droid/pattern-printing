for i in range(5,0,-1):
    for j in range(5-i):
        print("-",end=" ")
    for s in range(2*i-1):
        print("*",end=" ")
    print()