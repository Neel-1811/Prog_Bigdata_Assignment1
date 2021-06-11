import account
import another_account
import balance
import main
import withdrawn
import deposit

acc_no_list = []
amount_list = {}
current_acc = int()


def start():
    print("Do you have an account??")
    x = str(input("Enter 'y' for YES or 'n' for NO:\n"))

    if x == "y":
        verify_acc()

    elif x == "n":
        flag1 = True
        while flag1:
            print("choose from below options ")
            y = input("(1) for create account\n(2) for quit\n ")
            if y == "1":
                account.open_account()
                break
            elif y == "2":
                print("Thank you for banking with us!!")
                break
            else:
                print("choose from (1) or (2)")
    else:
        print("please choose from 'y' or 'n' ")
        start()


def verify_acc():
    flag2 = True
    while flag2:
        try:
            acc_no = abs(int(input("Enter account number:\n")))
            if acc_no in acc_no_list:
                main.current_acc = acc_no
                choose_option()
                break
            else:
                print("There is no account linked with this account number.")
                print("Please enter correct account number Or First create an account.")
                start()
                break
        except:
            print("Enter integer value.")


def choose_option():

    global option_selected
    flag3 = True
    while flag3:
        try:
            print("*********************************")
            print("* Choose your Option to perform *")
            print("*********************************")
            print("Current Account : {}".format(main.current_acc))
            print("Available Balance : {}".format(main.amount_list[main.current_acc]))
            print("(1)Deposit Money  (2)Withdrawn Money (3)Balance inquiry (4)Go to another Account (5) Exit")
            option_selected = int(input("enter the option:\n"))
            break
        except:
            print("Please Choose from (1) (2) (3) (4) (5).")

    if option_selected == 1:
        print("your choice is Deposit Money.")
        deposit.money_deposit()

    elif option_selected == 2:
        print("your choice is Money Withdrawn.")
        withdrawn.money_withdrawn()

    elif option_selected == 3:
        print("your choice is Balance enquiry.")
        balance.balance_inquiry()

    elif option_selected == 4:
        print("your choice is Go to another Account.")
        another_account.other_acc()

    elif option_selected == 5:
        print("Thank you for banking with us!!")

    else:
        print("*********************************")
        print("Please Choose from (1) (2) (3) (4) (5).")
        choose_option()


if __name__ == "__main__":
    print("*********************************")
    print("*   Welcome to Online banking   *")
    print("*********************************")
    start()
