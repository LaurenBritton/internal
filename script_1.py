def get_string(n):
    user_input = input(n)
    return user_input


def print_menu(l):
    for x in l:
        print(x)
        output = "{:<10} -- {:<4}".format(x[0], x[1])
        print(output)


def main():
    print("Starting new order")
    print("--------------------------------------------")

    option_list = [
        "P: Print Menu",
        "A: Add/Remove Item From Order",
        "R: Review Current Order",
        "D: Delete Order & Start New Order",
        "E: Edit Order",
        "G: Customer Order Details (Pick-up/Delivery)",
        "C: Confirm Order",
        "Q: Quit",
    ]

    item_list = [
        ["Linguine Gamberi", 23],
        ["Fusilli Petso", 19],
        ["Conchilglie Ala Bolognese", 22],
        ["3: Rigatoni Ala Caponata", 21],
        ["4: Fettuccine Cabonara", 20],
        ["5: Spaghetti Pomodoro", 16],
        ["6: Pappardelle Ricci D'Angello", 26],
        ["7: Raviolo Di Salsiccia", 22],
        ["8: Ravioli Di Ricotta", 20]
    ]

    run_program = True
    while run_program:
        for x in option_list:
            output = "{}".format(x)
            print(output)
        user_choice = get_string("Please select an option: -> ")
        if user_choice == "P":
            print_menu(item_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
        print("Thank you, the program has ended")


main()
