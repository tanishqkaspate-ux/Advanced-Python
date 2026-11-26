
import multiprocessing

def squares(numbers):
    for n in numbers:
        print("Square of", n, "=", n*n)

def cubes(numbers):
    for n in numbers:
        print("Cube of", n, "=", n*n*n)

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    p1 = multiprocessing.Process(target=squares, args=(numbers,))
    p2 = multiprocessing.Process(target=cubes, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes completed.")
