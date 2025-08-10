
import heapq

def main():
    print("Hello from heapq1!")

    a = [3, 5, 1, 2, 6, 8, 7, 1, 1, 1, 1, 1]
    print(f'a = {a}')
    heapq.heapify(a)
    print(f'a  after heapify = {a}')
    print('')
    while len(a) > 0:
        smallest = heapq.heappop(a)
        print(f'{smallest=}')
        print(f'     {a=}')


if __name__ == "__main__":
    main()
