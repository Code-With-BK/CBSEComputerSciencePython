"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 30 - CBSE 2023 Computer Science Sample Paper
"""

# right end of this list is the stack top
status = []

def Push_element(customer):
    name = customer[0]
    phone_num = customer[1]
    city = customer[2]
    if( city=="Goa" ):
        customer_info = [name, phone_num]
        status.append(customer_info)

def Pop_element():
    while( len(status)!=0 ):
        top_element = status.pop()
        print(top_element)
    print("Stack Empty")

# right end of this list is the stack top
item_stack = []
def Push(SItem):
    for item_name in SItem:
        item_price = SItem[item_name]
        if( item_price>75 ):
            item_stack.append(item_name)
    print(f"The count of elements in the stack is {len(item_stack)}")
    # print(item_stack)

def main():
    customer1 = ["Gurdas", "99999999999","Goa"] 
    customer2 = ["Julee", "8888888888","Mumbai"] 
    customer3 = ["Murugan","77777777777","Cochin"] 
    customer4 = ["Ashmit", "1010101010","Goa"]

    # push to the stack
    Push_element(customer1)
    Push_element(customer2)
    Push_element(customer3)
    Push_element(customer4)

    Pop_element()


    Ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}
    Push(Ditem)

main()

    
    

