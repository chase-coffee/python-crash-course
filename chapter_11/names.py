from name_function import get_formatted_name

print( "Enter 'q' at any time to quit.")
while True:
    first = input("Please enter your first name: ")
    if first == 'q':
        break
    
    last = input("Please input your last name: ")
    if last == 'q':
        break

    full_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {full_name}.")