def user_enter():
    user_input = float(input("Enter integer\n"))

    start = 0.0

    while 1:
        start += 0.25
        if start == 2:
            break
        elif user_input != 0.25:
            raise ValueError

        return start


print(user_enter())
