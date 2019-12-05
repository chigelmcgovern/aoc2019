input = open('day_02_part_1_input.txt', 'r')
intcode = [int(number) for number in input.read().split(',')]

intcode[1] = 12
intcode[2] = 2


class OpcodeTooSpicy(BaseException):
    pass


def process_intcode(intcode):
    for index in range(0, len(intcode), 4):
        operator = intcode[index]
        number1 = intcode[intcode[index + 1]]
        number2 = intcode[intcode[index + 2]]
        if operator == 99:
            return intcode[0]
        elif operator == 1:
            intcode[intcode[index + 3]] = number1 + number2
        elif operator == 2:
            intcode[intcode[index + 3]] = number1 * number2
        else:
            raise OpcodeTooSpicy

    return intcode[0]


print(process_intcode(intcode))
