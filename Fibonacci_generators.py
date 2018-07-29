__about__=""" Fibonacci uising generators. """

def generate_fib(n):
    f0,f1 = 0,1

    while n:
        yield f0
        f0,f1 = f1,f0+f1
        n -=1


for x in generate_fib(5000):
    print(str(x)+" : ")


