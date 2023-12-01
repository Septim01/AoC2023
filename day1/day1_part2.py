import regex as re

with open('input.txt') as file:
    input_text = file.read().strip()

numbers = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

number_dict = {digit: str(index) for index, digit in enumerate(numbers)}


def part_two():
    n = 2
    total_sum = 0

    for line in input_text.splitlines():
        pattern = r'\d' + ('|' + '|'.join(numbers) if n == 2 else '')
        matches = re.findall(pattern, line, overlapped=True)

        total_sum += int(number_dict.get(matches[0], matches[0]) + number_dict.get(matches[-1], matches[-1]))

    print(total_sum)


part_two()
