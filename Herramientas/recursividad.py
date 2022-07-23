# primera parte funcion factorial

count = 0

while count <= 5:

    x = int(input("intruducir un numero natural"))

    def factorial(x):

        if x < 2:

            return 1

        else:

            return x*factorial(x-1)

    print("el factorial de", x, "es", factorial(x))

    count += 1

# segunda parte fibbonachi

count2 = 0

while count2 <= 5:

    n = int(input("intruducir un numero natural"))

    def fibonacci(n):

        if n == 0:

            return 0

        elif n == 1:

            return 1

        else:

            return fibonacci(n-1)+fibonacci(n-2)

    print("el termino en la posicion", n, "de Fibonacci es", fibonacci(n))

    count2 += 1
