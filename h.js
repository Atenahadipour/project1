class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Variz Pool (Deposit)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Mablaghe " + str(amount) + " ba movafaghiat variz shod.")
        else:
            print("Mablagh bayad bishtar az 0 bashad.")

    # Bardasht Pool (Withdraw)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Khata: Mojoodi kafi nist!")
        elif amount <= 0:
            print("Mablagh bayad bishtar az 0 bashad.")
        else:
            self.balance -= amount
            print("Mablaghe " + str(amount) + " az hesab bardasht shod.")

    # Namayeshe Mojoodi (Balance)
    def display_balance(self):
        print("Mojoodie hesabe " + self.owner + ": " + str(self.balance) + " Toman")


# --- Test Barname ---

# Sakhte hesab baraye Ali ba 1000 toman mojoodi
hesab1 = BankAccount("Ali", 1000)

hesab1.display_balance()
hesab1.deposit(500)
hesab1.withdraw(200)
hesab1.withdraw(2000) # In yeki khata midahad chon mojoodi kam ast
hesab1.display_balance()
