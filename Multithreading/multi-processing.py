__about__ = """ Multiprocessing in python."""

# TO DO

from multiprocessing import Process

def worker(name):
    print("Worker :",name)



if __name__ == "__main__":

    p = Process(target= worker, args=("Shreyansh",))
    p.start()
    p.join()




