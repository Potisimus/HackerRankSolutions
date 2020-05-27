"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi
amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""



from collections import Counter
number_of_shoes = int(input())
shoe_size_list = list(map(int,input().split()))
number_of_customers = int(input())

shoe_size_dict = Counter(shoe_size_list)

total_sales=0

for i in range(number_of_customers):
    shoe_size, shoe_price = map(int,input().split())
    if shoe_size_dict[shoe_size]:
        total_sales += shoe_price
        shoe_size_dict[shoe_size]-=1
print(total_sales)