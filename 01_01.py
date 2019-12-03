mass_file = open('day_01_input.txt', 'r')
masses = [float(line.strip('\n')) for line in mass_file.readlines()]


def mass_to_fuel(mass):
    return mass // 3 - 2


total_fuel = sum([mass_to_fuel(mass) for mass in masses])
print(total_fuel)

