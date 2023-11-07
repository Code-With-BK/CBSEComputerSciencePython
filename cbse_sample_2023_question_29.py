"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 29 - CBSE 2023 Computer Science Sample Paper
"""

def INDEX_LIST(L):
    indexList = []
    for i in range(len(L)):
        if( L[i]!=0 ):
            indexList.append(i)
    return indexList

def main():
    # L = [12,4,0,11,0,56]
    L = [1,2,3,4,5,6,7,8,9,10,0,8,0,6,0,4]
    indexList = INDEX_LIST(L)
    print(indexList)

main()