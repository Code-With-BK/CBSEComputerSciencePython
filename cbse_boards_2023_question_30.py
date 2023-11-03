"""

@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python solution for Question 30 - CBSE 2023 Computer Science Boards Paper

"""

##### a)
# considering the right end of the list as the top of the stack
Hotel = []

def Push_Cust(cust_info):
    room_type = cust_info[1]
    if( room_type == "Delux" ):
        name = cust_info[0]
        Hotel.append(name)

def Pop_Cust():
    while( len(Hotel)!=0 ):
        top_element = Hotel.pop()
        print(top_element)
    print("Underflow")

##### b)
# considering the right end of the list as the top of the stack
vehicles_by_tata = []
def Push(Vehicle):
    for car_name in Vehicle:
        maker = Vehicle[car_name]
        if( maker.upper() == "TATA" ):
            vehicles_by_tata.append(car_name)

def main():
    customer1 = ["Siddarth", "Delux"] 
    customer2 = ["Rahul", "Standard"] 
    customer3 = ["Jerry", "Delux"]
    
    Push_Cust(customer1)
    Push_Cust(customer2)
    Push_Cust(customer3)

    print(Hotel)

    Pop_Cust()

    Vehicle = {"Santro":"ijyundai","Nexon":"TATA","Safari":"Tata"}
    Push(Vehicle)
    print(vehicles_by_tata)

main()
    

