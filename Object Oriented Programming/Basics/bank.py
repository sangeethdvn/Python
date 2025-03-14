"""

Class Bank

method1 : name, ac_type, balance

method2 : amount_deposite

method3 : amount_withdrawel

method4 : show name and balance

"""

# random pin generator


class Bank:

    def __init__(self,name,ac_type,balance):

        self.name = name

        self.balance = balance

    def amountdeposite(self,amount):

        self.balance = self.balance + amount

        print(f"You have succefully deposited")
        
        print(f"Your available balance is {self.balance}")

    def amount_withdrawel(self,w_amount):

        if w_amount < self.balance:

            self.balance = self.balance - w_amount

            print("Withdrawal Successfull")

            print(f"Your available balance is {self.balance}")

        else:

            print("Withdrawal Failure,insufficient balance")

    def show_balance(self):

        print(self.name)

        print(self.balance)

obj1 = Bank(name="Sangee", ac_type="Savings", balance=5000)

obj1.amountdeposite(2000)

obj1.amount_withdrawel(601)

obj1.show_balance()