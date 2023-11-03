"""

@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 29 - CBSE 2023 Computer Science Paper
"""

def EOReplace(L):
    for i in range(len(L)):
        integer = L[i]
        if( integer%2!=0 ):
            L[i] -= 1
        else:
            L[i] += 1

    # for integer in L:
    #     if( integer%2!=0 ):
    #         integer -= 1
    #     else:
    #         integer += 1

def main():
    L = [10,20,30,40,35,55]
    EOReplace(L)
    print(L)

    L2 = [1,2,3,4,5,6,7,8]
    EOReplace(L2)
    print(L2)

main()