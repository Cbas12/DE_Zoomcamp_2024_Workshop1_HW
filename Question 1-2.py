#Question 1 & 2

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

limit = int(input("Digit the limit: "))
generator = square_root_generator(limit)

contar = int(1)
suma=0
print("Printing the first " + str(limit) + " values: ")
for sqrt_value in generator:
    print("Square of "+ str(contar) +": "+str(sqrt_value))
    contar += 1
    suma += sqrt_value

print("The sum of the Square Root of the first " + str(limit) + " values is: " + str(suma))