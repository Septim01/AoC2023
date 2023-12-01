def part_one(line):
    reversed_line = line[::-1]
    sum = 0
    for i in range(len(line)):
        if(line[i].isdigit()):
            sum += int(line[i])*10
            for j in range(len(reversed_line)):
                if(reversed_line[j].isdigit()):
                    sum += int(reversed_line[j])
                    return sum

total_sum = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        total_sum += part_one(line)

print(total_sum)