price_for_work_inp = int(input())
price_for_work = price_for_work_inp * 7.61
discount = price_for_work * 0.18
total_price = price_for_work - discount


print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")