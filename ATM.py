class atm(object):
    def __init__(self,atm_card_num, pin_num,balance):
        self.atm_card_num = atm_card_num
        self.pin_num = pin_num
        self.balance = int(balance)
    def checkBalance(self):
        console.log(self.balance)
    def cashWithdrawal(self, amount):
        self.balance = self.balance - amount
        print("Your remaining balance is $" + str(self.balance))

cardNumber = input("Insert your card number: ")
pinNumber = input("Insert your pin number: ")
user = atm(cardNumber, pinNumber, 50000)
print("Choose your activity")
print("1. Balance Enquiry  2. Withdrawal")
activity = int(input("Enter your activity number: "))
if(activity == 1):
    user.checkBalance()
elif(activity == 2):
    amount = int(input("Enter the amount to be withdrawn: "))
    user.cashWithdrawal(amount)
else:
    print("Enter a valid number: ")