from multiprocessing import Process,Pool

def f(x):
    return x*x

if __name__ == "__main__":
    try:
        p = Pool(5)
        result = p.map(f,[1,2,3,4,5])
        print(result)
    except Exception as e:
        print("The Actual Error is:",e)