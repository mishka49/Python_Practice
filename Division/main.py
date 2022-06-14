from division_coins import ATM

while True:
    try:

        amount = input("Enter the desired amount: ")
        print(str(ATM.divides_amount_into_coins(int(amount))))
        break
    except BaseException as ex:
        print(ex)


