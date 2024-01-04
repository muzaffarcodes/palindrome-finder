number =  input("Input -> ")
if number == ''.join(reversed(number)):    
    print("Palindrome")
else:
    print('Not palindrome')
