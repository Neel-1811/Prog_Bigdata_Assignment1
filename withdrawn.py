import main


def money_withdrawn():
    acc_no = main.current_acc
    flag8 = True
    while flag8:
        try:
            print("Current Account : {}".format(main.current_acc))
            print("Available Balance : {}".format(main.amount_list[main.current_acc]))
            withdrawn_amount = float(input("Enter the withdrawn Amount:\n"))
            if withdrawn_amount > 0:
                if withdrawn_amount <= main.amount_list[acc_no]:
                    balance = float(main.amount_list[acc_no]) - withdrawn_amount
                    main.amount_list[acc_no] = balance
                    print("Hello {} your have successfully withdrawn ".format(acc_no), withdrawn_amount, ".")
                    print("Available balance is", main.amount_list[acc_no])
                    break
                else:
                    print("you do not have sufficient balance.")
                    print("Available balance: {}".format(main.amount_list[acc_no]))
                    break
            else:
                print("Enter positive amount.")
        except:
            print("Enter integer value.")

    flag9 = True
    while flag9:
        next_step = input('Do you want to Continue "y" for Yes and "n" for No:\n')
        if next_step == "y":
            main.choose_option()
            break
        elif next_step == "n":
            print("Thank You for banking with us!!")
            break
        else:
            print("please choose from 'y' or 'n' ")
