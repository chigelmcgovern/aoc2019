mass_file = open('day_01_input.txt', 'r')
masses = [float(line.strip('\n')) for line in mass_file.readlines()]


def mass_to_fuel(mass):
    marginal_fuel = mass // 3 - 2
    total_fuel = [marginal_fuel]
    while marginal_fuel > 0:
        marginal_fuel = marginal_fuel // 3 - 2
        if marginal_fuel > 0:
            total_fuel.append(marginal_fuel)
    return sum(total_fuel)


total_fuel = sum([mass_to_fuel(mass) for mass in masses])
print(total_fuel)

