import main


def balance_inquiry():
    acc_no = main.current_acc
    balance = main.amount_list[acc_no]
    print("account no: {} \navailable balance: {}".format(acc_no, balance))

    flag10 = True
    while flag10:
        next_step = input('Do you want to Continue "y" for Yes and "n" for No:\n')
        if next_step == "y":
            main.choose_option()
            break
        elif next_step == "n":
            print("Thank You for banking with us!!")
            break
        else:
            print("please choose from 'y' or 'n' ")
