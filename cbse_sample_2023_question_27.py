"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 27 - CBSE 2023 Computer Science Sample Paper
"""

def COUNTLINES():
    filename = "TESTFILE.TXT"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    count = 0
    vowels = "aeiouAEIOU"
    for line in lines:
        first_char = line[0]
        if( first_char not in vowels ):
            count += 1
    print(f"The number of lines not starting with any vowel - {count}")

def ETCount():
    filename = "TESTFILE.TXT"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    count_E = 0
    count_T = 0
    for line in lines:
        for ch in line:
            if( ch=='e' or ch=='E' ):
                count_E += 1
            if( ch=='t' or ch=='T' ):
                count_T += 1
    print(f"E or e: {count_E}")
    print(f"T or t: {count_T}")

def main():
    # COUNTLINES()
    ETCount()

main()