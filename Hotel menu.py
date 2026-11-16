print(" Welcome to hotel ARYAN")
menu = {
    "vada pav":20,
    "dabeli":25,
    "tea":10,
    "coffee":15,
    "pizza":100,
}
print("========== HOTEL MENU ==========")
for item,price in menu.items():
    print(item,":","Rs.",price)

total = 0
tax = 0
while True:
    order = input("\nEnter your food name (or 'done' to finish): ")

    if order == "done":
        tax = total*0.18
        break

    if order in menu:
        print("Your selected item:", order)
        print("Price: Rs.", menu[order])
        total = total+menu[order]

    else:
        print("Sorry! This item is not available.")


print("\n========== FINAL BILL ==========")
print("Total Amount: Rs. (including 18% gst)", total+tax)
print("Thank you for visiting our hotel!")
print("================================")
