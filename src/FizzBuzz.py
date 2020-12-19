
def fizzbuzz():
    
    #for the numbers between 1 and 100...
    for i in range(1,100):
        #if multiple of 3 and 5...
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        #if only multiple of 3...    
        elif i % 3 == 0:
            print("Fizz")
        #if only multiple of 5...    
        elif i % 5 == 0:
            print("Buzz")
        #otherwise...    
        else:
            print(i)

fizzbuzz()
