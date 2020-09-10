class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars

        cents = self.cents + deposit_cents
        if cents >= 100:
            self.dollars += int(cents / 100)
            self.cents = cents % 100
        else:
            self.cents = cents
#
# piggy_bank = PiggyBank(1, 1)
# piggy_bank.add_money(0, 99)
#
# print(f'{piggy_bank.dollars} {piggy_bank.cents}')
#
# piggy_bank = PiggyBank(1, 1)
# piggy_bank.add_money(0, 88)
#
# print(f'{piggy_bank.dollars} {piggy_bank.cents}')
# piggy_bank = PiggyBank(1, 1)
# piggy_bank.add_money(500, 500)
#
# print(f'{piggy_bank.dollars} {piggy_bank.cents}')
