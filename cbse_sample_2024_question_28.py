"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 28 - CBSE 2024 Computer Science Sample Paper
"""

def function1():
    filename = "Alpha.txt"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    # count = 0
    for line in lines:
        if( len(line)>=3 ):
            if( line[0]=='Y' and line[1]=='o' and line[2]=='u' ):
                print(line, end="")
                # count += 1
    # print(f'Number of lines starting with the word "You" is {count}')

def vowelCount():
    filename = "Poem.txt"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    vowels = "aeiouAEIOU"
    count = 0
    for line in lines:
        for ch in line:
            if( ch in vowels ):
                count += 1
    print(f'Number of vowels in the file "Poem.txt" is {count}')

def main():
    function1()
    vowelCount()

main()
