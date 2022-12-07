import typing


def step_2(data_lines):
    sum = 0.0
    for line in data_lines:
        act, op, a, b = line.split()
        sum += basic_calc(op, int(a), int(b))
    return sum


def basic_calc(op: str, a: int, b: int) -> typing.Union[float, int]:
    if op == 'x':
        return a*b
    elif op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '/':
        return a/b
    else:
        raise Exception("invalid operator")


def parse_line(line: str) -> int:
    ''' Returns line number to go to'''
    items = line.split()
    if len(items) == 2:
        return int(items[1])
    else:
        return int(basic_calc(items[2], int(items[3]), int(items[4])))


def step_3(data_lines):
    seen_lines: typing.List[str] = []
    index = 0
    while True:
        if data_lines[index] in seen_lines:
            break
        seen_lines.append(data_lines[index])
        index = parse_line(data_lines[index])

    return (data_lines[index], index+1)


if __name__ == "__main__":
    with open("step_3.txt", 'rt') as f:
        data_lines = [line.strip() for line in f if line.strip() != '']

    # step_2(data_lines)
    print(step_3(data_lines))

