import multiprocessing

def worker():
    pass

def worker(number):
    print("Worker:",number)
    a=5
    a = a+1
    print(a)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args = (i,))
        # jobs.append(p)
        p.start()

