from point2d import Point2D

def main():
    p1 = Point2D(6, 7)
    p2 = Point2D(1, 2)

    print(f'p1 + p2 = {p1 + p2}')
    print(f'p2 + p2 = {p2 + p1}')
    print(f'p1 - p2 = {p1 - p2}')
    print(f'p2 - p2 = {p2 - p1}')
    print(f'p1 * p2 (dot product) = {p1 * p2}')
    print(f'p1 * p2 (dot product) = {p2 * p1}')
    print(f'p1 * 10 (scalar multiplication) = {p1 * 10}')
    print(f'10 * p1 (scalar multiplication) = {10 * p1}')
    
    p1 += p2
    print(f'After p1 += p2, p1 is {p1}')

    print(f'-p1 = {-p1}')

    p3 = Point2D(1, 2)

    print(f'p1 == p2 = {p1 == p2}')
    print(f'p2 == p3 = {p2 == p3}')

    print(f'p1[0] = {p1[0]}')
    print(f'p1[1] = {p1[1]}')

    p1[0] = 42
    print(f'After p[0] = 42, p1 is {p1}')

if __name__ == '__main__':
    main()