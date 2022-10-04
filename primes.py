"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    #Case 1 : number of primes = 0
    #Case 2 : number of primes > 0
    print('Working')
    if(number_of_primes>0):
        list.append(2)


        value = 3

        while(len(list) < number_of_primes):
            isPrime = True
            for num in  list :
                if(value % num == 0):
                    isPrime = False
            if(isPrime):
                list.append(value)

            value+=1
    return list


print(primes(20))
