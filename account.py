import main


def open_account():

    global acc_no
    flag4 = True
    while flag4:
        try:
            acc_no = abs(int(input("Enter your account number:\n")))
            break
        except:
            print("Enter integer value.")

    if acc_no in main.acc_no_list:
        print("this account number already exists.Please try with other account number.")
        main.start()

    else:
        main.current_acc = acc_no
        main.acc_no_list.append(acc_no)
        main.amount_list[acc_no] = 0
        print("Your account has been created.")
        print("your account number is {} and available balance is {}".format(acc_no, main.amount_list[acc_no]))

    flag5 = True
    while flag5:
        next_step = input('Do you want to Continue "y" for Yes and "n" for No:\n')
        if next_step == "y":
            main.choose_option()
            break
        elif next_step == "n":
            print("Thank You for banking with us!!")
            break
        else:
            print("please choose from 'y' or 'n' ")
