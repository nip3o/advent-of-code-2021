import click

from collections import defaultdict, Counter

def part_one(input):
    γ = ''
    ε = ''
    bits = defaultdict(list)

    for line in input.readlines():
        for (position, digit) in enumerate(line.strip()):
            bits[position].append(digit)

    for position in sorted(bits.keys()):
        zeroes = sum(x == '0' for x in bits[position])
        ones = sum(x == '1' for x in bits[position])

        if zeroes > ones:
            γ += '0'
            ε += '1'
        else:
            γ += '1'
            ε += '0'

    print(f"γ ={int(γ, 2)}, ε ={int(ε, 2)} => {int(γ, 2) * int(ε, 2)}")

def part_two(input):
    γ = ''
    ε = ''
    amounts = defaultdict(list)

    for line in input.readlines():
        for (position, digit) in enumerate(line.strip()):
            amounts[position].append(digit)

    first_bits = amounts[0]
    print(f"γ ={int(γ, 2)}, ε ={int(ε, 2)} => {int(γ, 2) * int(ε, 2)}")



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
