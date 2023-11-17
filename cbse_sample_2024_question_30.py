"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 30 - CBSE 2024 Computer Science Sample Paper
"""

# right end of this list is the stack top
travel = []
def Push_element(NList):
    for record in NList:
        city = record[0]
        country = record[1]
        distance_from_delhi = record[2]
        if( country!="India" and distance_from_delhi<3500 ):
            new_record = [city,country]
            travel.append(new_record)

def Pop_element():
    while( len(travel)!=0 ):
        top_element = travel.pop()
        print(top_element)
    print("Stack Empty")


def main():
     NList=[["New York", "U.S.A.", 11734],
           ["Naypyidaw", "Myanmar", 3219],
           ["Dubai", "UAE", 2194],
           ["London", "England", 6693],
           ["Gangtok", "India", 1580], 
           ["Columbo", "Sri Lanka", 3405]
           ]
     Push_element(NList)
     Pop_element()

main()