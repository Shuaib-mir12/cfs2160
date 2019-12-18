sweet_1: int = int(input('Enter first sweet price:  '))
sweet_2 = int(input('Enter second sweet price: '))
sweet_3 = int(input('Enter third sweet price:  '))
sweet_4 = int(input('Enter fourth sweet price: '))
sweet_5 = int(input('Enter fifth sweet price:  '))

total_price = sweet_1 + sweet_2 + sweet_3 + sweet_4 + sweet_5

average_price = total_price / 5

lowest_number = min(sweet_1, sweet_2, sweet_3, sweet_4, sweet_5)

highest_number = max(sweet_1, sweet_2, sweet_3, sweet_4, sweet_5)

print('total price is ' + str(total_price))
print('average price is ' + str(average_price))
print('lowest number is ' + str(lowest_number))
print('highest number is ' + str(highest_number))

print
