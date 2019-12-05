input = open('day_02_part_1_input.txt', 'r')
intcode = [int(number) for number in input.read().split(',')]

intcode[1] = 12
intcode[2] = 2


class OpcodeTooSpicy(BaseException):
    pass


def process_intcode(intcode):
    intcode_copy = intcode.copy()
    for index in range(0, len(intcode_copy), 4):
        operator = intcode_copy[index]
        number1 = intcode_copy[intcode_copy[index + 1]]
        number2 = intcode_copy[intcode_copy[index + 2]]
        if operator == 99:
            return intcode_copy[0]
        elif operator == 1:
            intcode_copy[intcode_copy[index + 3]] = number1 + number2
        elif operator == 2:
            intcode_copy[intcode_copy[index + 3]] = number1 * number2
        else:
            raise OpcodeTooSpicy

    return intcode_copy[0]


for noun in range(100):
    for verb in range(100):
        intcode[1] = noun
        intcode[2] = verb

        output = process_intcode(intcode)

        if output == 19690720:
            print(100 * noun + verb)
            break
