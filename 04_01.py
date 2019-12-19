puzzle_input = range(246515, 739105+1)


def adjacent_doubles(password):
    password = str(password)
    for increment in range(0, len(password)-1):
        if password[increment] == password[increment+1]:
            return True
    return False


def never_decrease(password):
    password = str(password)
    for increment in range(0, len(password)-1):
        if password[increment] > password[increment+1]:
            return False
    return True


def possible_password_count(password_range):
    possible_password_counter = 0
    for password in password_range:
        if adjacent_doubles(password) and never_decrease(password):
            possible_password_counter += 1
    print(possible_password_counter)


possible_password_count(puzzle_input)
