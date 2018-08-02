__about__ = """ Get process ids. """


from multiprocessing import Process
import os


def generic(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


if __name__ == '__main__':
    generic('main line')
    p = Process(target=generic, args=('bob',))
    p.start()
    p.join()