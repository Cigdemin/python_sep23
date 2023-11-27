num_list = list(range(1,51))
print(num_list)
even_num = []
odd_num = []
for x in num_list:
    if x % 2 == 0 : 
        even_num.append(x)
    else:
        odd_num.append(x)
print(even_num)
print(odd_num)
sum_even_num = 0
for e in even_num:
    sum_even_num += e
print(f"Sum of all even numbers is: {sum_even_num}")
product_of_odd = 1
for o in odd_num:
    product_of_odd *= o
print(f"Product of all odd number is: {product_of_odd}")
largest_num = 0
for n in num_list:
    if n > largest_num :
        largest_num = n
print(f"The largest number in the list is: {largest_num}")
