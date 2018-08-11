

class BankAccount:

    def __init__(self, accountName = "BankAccount", balance = 1500):
        self.__accountname = accountName
        self.__accountbalance = balance


    def deposite(self,value):
        self.__accountbalance = (self.__accountbalance + value)
        print("your new balance :" + str(self.__accountbalance))


    def withdraw(self, value):


        if value > self.__accountbalance:
            print("insufficiant balance")

        else:
            self.__accountbalance = (self.__accountbalance - value)
            print("your new balance:" + str(self.__accountbalance))




class CurrentAccount(BankAccount):

    def __init__(self, accountName = "CurrentAccount", balance = 1500):
        self.__accountname = accountName
        self.__accountbalance = balance
        super().__init__()



    def withdraw(self, value):


        if value > 1000:
            print("Your account balance will be " + str(self.__accountbalance - value))
            print("Contact Bank Manager as Minimum 500 Balance Required")
            print("Transaction Cancelled !")

        else:
            self.__accountbalance = (self.__accountbalance - value)
            print("your new balance:" + str(self.__accountbalance))



class SavingAccount(BankAccount):

    def __init__(self, accountName = "CurrentAccount", balance = 1500):
        self.__accountname = accountName
        self.__accountbalance = balance
        super().__init__()



    def deposite(self,value):
        beforeDeposite = self.__accountbalance
        self.__accountbalance = (self.__accountbalance + (value * 1.03)) # apr added
        print("Your new balance is : " + str(self.__accountbalance))
        interest = self.__accountbalance -  beforeDeposite - value
        print("Interest added to account balance: " + str(round(interest,2)))


# c1 = CurrentAccount()
# c1.withdraw(1003)


s1 =SavingAccount()
s1.deposite(1)
