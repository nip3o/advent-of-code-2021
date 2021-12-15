from collections import deque

import click

def part_one(input):
    last = None
    increase_count = 0

    for line in input.readlines():
        number = int(line)

        print(number, end=" ")
        if number is None or last is None:
            print('(N/A - no previous measurement)')
        elif number == last:
            print('(no change)')
        elif number < last:
            print('(decreased)')
        elif number > last:
            print('(increased)')
            increase_count += 1
        else:
            raise AssertionError()

        last = number

    print(f'{increase_count=}')

def part_two(input):
    last = None
    increase_count = 0
    window = deque()

    for line in input.readlines():
        number = int(line)

        window.append(number)
        if len(window) > 3:
            window.popleft()

        window_sum = sum(window) if len(window) == 3 else None

        print(window_sum, end=" ")
        if window_sum is None or last is None:
            print('(N/A - no previous measurement)')
        elif window_sum == last:
            print('(no change)')
        elif window_sum < last:
            print('(decreased)')
        elif window_sum > last:
            print('(increased)')
            increase_count += 1
        else:
            raise AssertionError()

        last = window_sum

    print(f'{increase_count=}')



@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('part', type=click.INT)
def main(input, part):
    if part == 1:
        return part_one(input)

    if part == 2:
        return part_two(input)

    raise AssertionError('Invalid part')


if __name__ == '__main__':
    main()
