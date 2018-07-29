__about__="Multiprocessing Example"

import multiprocessing

def calc_squares(n):
    for x in n:
        print("Square of:"+str(x)+":is:",x*x)

def calc_cube(n):
    for y in n:
        print("Cubes of:"+str(y)+":is:",y*y*y)

if __name__=='__main__':
    arr = [1,2,3,4,5,6,7]
    p1 = multiprocessing.Process(target=calc_squares, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()