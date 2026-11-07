def calculate_change(paid,total):
    change = paid - total
    return change

ticket_price = 30

print("---PARKING TICKET PAYMENT HELPER---")
print(f"this parking ticket costs {ticket_price} rupees")
print("coins accepted: 1, 5, 10, 25 \n")

total_inserted = 0
coins_inserted = 0

while True:
    coins = int(input("enter the coin(1,5,10 or 25):"))
    if coins != 1 and coins!= 5 and coins!=10 and coins != 25:
        print("ERROR! invalid coin selected")
        continue
    
    total_money_inserted = total_money_inserted + coins
    coins_inserted = coins_inserted + 1

    if total_inserted >= ticket_price:
        print("enough money inserted \n")
        break
change_due = calculate_change(total_inserted, ticket_price)

if change_due == 0:
    pass
else:
    print(f"the change is {change_due}")

print("\n ---PAYMENT SUMMARY---")
print(f"ticket price: {ticket_price}")
print(f"total money inserted: {total_money_inserted}")
print(f"total coins inserted: {coins_inserted}")
print(f"change amount: {change_due}")
