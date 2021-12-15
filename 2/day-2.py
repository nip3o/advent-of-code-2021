import click

def part_one(input):
    horizontal = 0
    depth = 0

    for line in input.readlines():
        match line.split():
            case ["up", i]:
                depth -= int(i)

            case ["down", i]:
                depth += int(i)

            case ["forward", i]:
                horizontal += int(i)

            case _:
                raise AssertionError()

    print(f"{horizontal=} {depth=} => result = {horizontal * depth}")

def part_two(input):
    aim = 0
    horizontal = 0
    depth = 0

    for line in input.readlines():
        match line.split():
            case ["up", i]:
                aim -= int(i)

            case ["down", i]:
                aim += int(i)

            case ["forward", i]:
                horizontal += int(i)
                depth += aim * int(i)

            case _:
                raise AssertionError()

    print(f"{horizontal=} {depth=} => result = {horizontal * depth}")


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
