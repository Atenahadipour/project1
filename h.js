class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # عملیات واریز وجه
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"مبلغ {amount} تومان با موفقیت واریز شد.")
        else:
            print("مبلغ واریزی باید بیشتر از صفر باشد.")

    # عملیات برداشت وجه
    def withdraw(self, amount):
        if amount > self.balance:
            print("خطا: موجودی کافی نیست!")
        elif amount <= 0:
            print("مبلغ برداشت باید بیشتر از صفر باشد.")
        else:
            self.balance -= amount
            print(f"مبلغ {amount} تومان از حساب برداشت شد.")

    # نمایش موجودی
    def display_balance(self):
        print(f"موجودی فعلی حساب {self.owner}: {self.balance} تومان")


# --- تست برنامه ---

# ایجاد یک حساب جدید برای علی با موجودی اولیه 1000
account1 = BankAccount("علی", 1000)

account1.display_balance()  # نمایش موجودی
account1.deposit(500)       # واریز 500 تومان
account1.withdraw(200)      # برداشت 200 تومان
account1.withdraw(2000)     # تست برداشت بیش از موجودی (ایجاد خطا)
account1.display_balance()  # نمایش موجودی نهایی
