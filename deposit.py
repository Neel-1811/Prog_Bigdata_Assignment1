import main


def money_deposit():
    acc_no = main.current_acc
    flag6 = True
    while flag6:
        try:
            print("Current Account : {}".format(main.current_acc))
            print("Available Balance : {}".format(main.amount_list[main.current_acc]))
            deposit_amount = float(input("Enter the deposit Amount:\n"))
            if deposit_amount > 0:
                balance = float(main.amount_list[acc_no]) + deposit_amount
                main.amount_list[acc_no] = balance
                print("Hello {} your have successfully deposited ".format(acc_no), deposit_amount, ".")
                print("Available balance is", main.amount_list[acc_no])
                break
            else:
                print("enter positive amount.")

        except:
            print("Enter integer value.")

    flag7 = True
    while flag7:
        next_step = input('Do you want to Continue "y" for Yes and "n" for No:\n')
        if next_step == "y":
            main.choose_option()
            break
        elif next_step == "n":
            print("Thank You for banking with us!!")
            break
        else:
            print("please choose from 'y' or 'n' ")
