counter = 0
menu = {"burger":5 , "pizza":7 , "tacos":10 , "fries":3 , "drinks":3 }
order_list =[]
print(menu)
for item , price in menu.items() :
    print(f"{item} - ${price}")
while True :
    order=input(" Welcome here's the menu please order : ")

    if order.lower() in menu   :
        print("good choose you order :", order)
        order_list.append(order)
        counter += 1
        response=input( " do you wanna order more ? (yes/no) or maybe exit ? ")
        total = sum(menu[item] for item in order_list)
        print("Total bill: $", total)
        if response.lower() == "no" :
            print("you have order :" , "\n" , "\n".join(order_list))
            print ("the quantaties is : " , counter)
            print("Total bill: $", total)
            break
        elif response.lower() == "exit" :
            print("you have order :" , "\n" , "\n".join(order_list))
            print ("the quantaties is : " , counter)
            print("Total bill: $", total)
            break
    else:
        print("sorry please enter correct order !")

