from multiprocessing import Pool
from math import *


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def eval_fun(function, val):
    xs = [x.strip().replace('^', '**') for x in function.split('+')]
    return sum([eval(n.replace('x', str(val))) for n in xs])


def Integrate(funkcja, pocz, kon, skok):
    value = 0
    listed = list(frange(pocz, kon, skok))

    for z in listed:
        value += eval_fun(funkcja, z) * skok

    return value

if __name__ == '__main__':

    foo = str(input("Enter function that will be integrated: "))
    skok = float(input("Enter the step: "))
    a = float(input("Enter the lower integration bound: "))
    b = float(input("Enter the upper integration bound: "))
    ile_przedzialow = int(input("Enter the number of processes used to computation: "))

    pool = Pool()
    results = []

    for z in range(0, ile_przedzialow):
        pocz = a + z * (b - a) / ile_przedzialow
        kon = a + (z + 1) * (b - a) / ile_przedzialow
        results.append(pool.apply_async(Integrate, [foo, pocz, kon, skok]))

    result_value = 0
    for result in results:
        result_value += result.get()

    print(result_value)