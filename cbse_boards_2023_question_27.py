"""

@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 27 - CBSE 2023 Computer Science Paper

"""

def LongLines():
    filename = "LINES.TXT"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    for line in lines:
        words = line.split()
        if( len(words)>=10 ):
            print(line,end="")

def count_Dwords():
    filename = "Details.txt"
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    digits = "0123456789"
    num_words_ending_with_digit = 0
    for line in lines:
        words = line.split()
        for word in words:
            last_char = word[len(word)-1]
            if( last_char in digits ):
                num_words_ending_with_digit += 1
    print(f"Number of words ending with a digit are {num_words_ending_with_digit}")

    
def main():
    LongLines()
    print()
    count_Dwords()
    
main()