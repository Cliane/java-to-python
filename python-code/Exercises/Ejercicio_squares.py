

def print_squares_of_numbers_up_to(times):
    for i in range(0, times):
        print(i*i)
        
        
def print_squares_of_even_numbers_up_to(times):
    for i in range(0, times+1, 2):
        print(i*i)
        
        
def print_numbers_in_reverse(times):
    for i in range(times, -1, -1):
        print(i)

#print_squares_of_numbers_up_to(4)
#print_squares_of_even_numbers_up_to(11)
print_numbers_in_reverse(10)