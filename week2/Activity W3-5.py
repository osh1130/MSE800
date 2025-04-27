class Factorial:
    def factorial(self, number: int):
        for i in range(1, number + 1):
            factorial *= i    
        print(f"The factorial of {number} is: {factorial}")

    def prime(self, number: int):
        isprime = True
        for i in range(2,number):
            if number%i==0:
                isprime = False
                print(f"number {number} isnt: prime")
                break
        if isprime:
            print(f"number {number} is: prime")
factorial_instance = Factorial()
#factorial_instance.factorial(5)  
factorial_instance.prime(5)  