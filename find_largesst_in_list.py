def find_maximum(number_list):
    
    max_number = number_list[0]
    
    
    for number in number_list:
        if number > max_number:
            max_number = number  
            
    return max_number


my_numbers = [12, 45, 2, 89, 34, 67]


largest = find_maximum(my_numbers)


print("The largest number in the list is:", largest)