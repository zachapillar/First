number=input("enter a number:")
number_list=list(number)
list_length=len(number_list)
middle=list_length//2
first_half_number=number[:middle]
second_half_number=number[middle:]
first_half_number_list=list(first_half_number)
second_half_number_list=list(second_half_number)

if len(second_half_number_list)>len(first_half_number_list):
	del second_half_number_list[0]

second_half_number_list_reverse=second_half_number_list[::-1]

if first_half_number_list==second_half_number_list_reverse:
	print("palindrome!")
else:
	print("not a palindrome ):")