class CoffeeMachine:
    def __init__(self, amount_of_water = 400, amount_of_beans = 120, amount_of_milk = 540, amount_of_cups = 9, money = 550):
        self.money = money
        self.amount_of_water = amount_of_water
        self.amount_of_cups = amount_of_cups
        self.amount_of_beans = amount_of_beans
        self.amount_of_milk = amount_of_milk
        self.state = 'choosing an action'

    def fill_action(self, new_water, new_milk, new_beans, new_cups):
        self.amount_of_water += int(new_water)
        self.amount_of_milk += int(new_milk)
        self.amount_of_beans += int(new_beans)
        self.amount_of_cups += int(new_cups)

    def print_machine_state(self):
        print("The coffee machine has:")
        print(f"{self.amount_of_water} of water")
        print(f"{self.amount_of_milk} of milk")
        print(f"{self.amount_of_beans} of coffee beans")
        print(f"{self.amount_of_cups} of disposable cups")
        print(f"${self.money} of money")

    def can_buy(self, user_choice):
        water_per_cup = 0
        milk_per_cup = 0
        beans_per_cup = 0
        user_can_buy = True
        if user_choice == '1':
            water_per_cup = 250
            beans_per_cup = 16
        elif user_choice == '2':
            water_per_cup = 350
            beans_per_cup = 20
            milk_per_cup = 75
        elif user_choice == '3':
            water_per_cup = 200
            milk_per_cup = 100
            beans_per_cup = 12

        if self.amount_of_water < water_per_cup:
            user_can_buy = False
            print('Sorry, not enough water!')
        if self.amount_of_milk < milk_per_cup and user_choice is not '2':
            user_can_buy = False
            print('Sorry, not enough milk!')
        if self.amount_of_beans < beans_per_cup:
            user_can_buy = False
            print('Sorry, not enough coffee beans!')
        if self.amount_of_cups < 1:
            user_can_buy = False
            print('Sorry, not enough disposable cups!')

        if user_can_buy:
            print('I have enough resources, making you a coffee!')
        return user_can_buy

    def buy_action(self, choice):
        user_choice = choice

        if user_choice == '1' and self.can_buy(user_choice):
            self.amount_of_water -= 250
            self.amount_of_beans -= 16
            self.amount_of_cups -= 1
            self.money += 4
        elif user_choice == '2' and self.can_buy(user_choice):
            self.amount_of_water -= 350
            self.amount_of_beans -= 20
            self.amount_of_cups -= 1
            self.amount_of_milk -= 75
            self.money += 7
        elif user_choice == '3' and self.can_buy(user_choice):
            self.amount_of_water -= 200
            self.amount_of_beans -= 12
            self.amount_of_milk -= 100
            self.amount_of_cups -= 1
            self.money += 6

    def take_action(self):
        print(f'I give you ${self.money}')
        self.money = 0

    def run(self, user_input):
        ret_strs = []
        if user_input[0] == 'choosing an action':
            ret_strs.append('Write action (buy, fill, take, remaining, exit):')
            return ret_strs
        elif user_input[0] == 'remaining':
            self.print_machine_state()
            return ret_strs
        elif user_input[0] == 'take':
            self.take_action()
            return ret_strs
        elif user_input[0] == 'fill':
            ret_strs.append('Write how many ml of water do you want to add:')
            ret_strs.append('Write how many ml of milk do you want to add:')
            ret_strs.append('Write how many grams of coffee beans do you want to add:')
            ret_strs.append('Write how many disposable cups of coffee do you want to add:')
            self.state = 'filling the machine'
            return ret_strs
        elif user_input[0] == 'buy':
            ret_strs.append('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            self.state = "choosing a type of coffee"
            return ret_strs
        elif user_input[0] == 'exit':
            ret_strs.append('exit')
            return ret_strs
        elif self.state == "choosing a type of coffee":
            user_choice = user_input[0]
            self.buy_action(user_choice)
            self.state = 'choosing an action'
            return []
        elif self.state == 'filling the machine':
            new_water = user_input[0]
            new_milk = user_input[1]

            new_beans = user_input[2]
            new_cups = user_input[3]
            self.fill_action(new_water, new_milk, new_beans, new_cups)
            self.state = 'choosing an action'
            return []


isExit = False
isStarted = False
coffee_machine = CoffeeMachine()
ret_strs = []

while not isExit:
    actions = []
    if not isStarted or len(ret_strs) == 0:
        ret_strs = coffee_machine.run(['choosing an action'])
        isStarted = True
    elif ret_strs[0] =='exit':
        isExit = True
    else:
        for retstr in ret_strs:
            action = input(retstr)
            actions.append(action)
        ret_strs = coffee_machine.run(actions)
        actions = []
