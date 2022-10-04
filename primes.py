"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    
    #Case 1 : number of primes = 0
    #Case 2 : number of primes > 0

    if(number_of_primes>0):
        list.append(2)

        value = 3
        while(len(list) < number_of_primes):
            for num in  list :
                if(value % num == 0):
                    break
                list.append(value)
            value += 1
    return list
