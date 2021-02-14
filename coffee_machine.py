class CoffeeMachine:
    total_water = 400
    total_milk = 540
    total_beans = 120
    total_cups = 9
    total_money = 550

    def action_choice(self):
        action = ''
        while action != 'exit':
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "buy":
                self.coffee_choice = input("What do you want to buy? 1 – espresso, 2 – latte, 3 – cappuccino, back - to main menu:")
                if self.coffee_choice == "back":
                    continue
                else:
                    if self.enough(self.coffee_choice) == True:
                        print("I have enough resources, making you a coffee!")
                        if self.coffee_choice == "1":
                            self.total_water -= 250
                            self.total_beans -= 16
                            self.total_money += 4
                            self.total_cups -= 1
                        elif self.coffee_choice == "2":
                            self.total_water -= 350
                            self.total_milk -= 75
                            self.total_beans -= 20
                            self.total_money += 7
                            self.total_cups -= 1
                        elif self.coffee_choice == "3":
                            self.total_water -= 200
                            self.total_milk -= 100
                            self.total_beans -= 12
                            self.total_money += 6
                            self.total_cups -= 1
            elif action == "fill":
                add_water = int(input("Write how many ml of water do you want to add:"))
                self.total_water += add_water
                add_milk = int(input("Write how many ml of milk do you want to add:"))
                self.total_milk += add_milk
                add_beans = int(input("Write how many grams of beans do you want to add:"))
                self.total_beans += add_beans
                add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.total_cups += add_cups
            elif action == "take":
                print(f"I gave you ${self.total_money}")
                self.total_money = 0
            elif action == "remaining":
                print(f"The coffee machine has\n"
                      f"{self.total_water} ml of water\n"
                      f"{self.total_milk} ml of milk\n"
                      f"{self.total_beans} g of coffee beans\n"
                      f"{self.total_cups} of disposable cups\n"
                      f"{self.total_money} of money")

    def enough(self, coffee_choice):
        self.coffee_choice = coffee_choice
        items_needed = set()
        if coffee_choice == "1":
            if self.total_water >= 250:
                items_needed.add("water")
            if self.total_beans >= 16:
                items_needed.add("beans")
            if self.total_cups >= 1:
                items_needed.add("cups")
            expected = {"water", "beans", "cups"}
            lack = ', '.join(expected.difference(items_needed))
            if expected == items_needed:
                return True
            else:
                print(f"Sorry, not enough {lack}!")
        elif coffee_choice == "2":
            if self.total_water >= 350:
                items_needed.add("water")
            if self.total_beans >= 20:
                items_needed.add("beans")
            if self.total_milk >= 75:
                items_needed.add("milk")
            if self.total_cups >= 1:
                items_needed.add("cups")
            expected = {"water", "beans", "cups", "milk"}
            lack = ', '.join(expected.difference(items_needed))
            if expected == items_needed:
                return True
            else:
                print(f"Sorry, not enough {lack}!")
        elif coffee_choice == "3":
            if self.total_water >= 200:
                items_needed.add("water")
            if self.total_beans >= 12:
                items_needed.add("beans")
            if self.total_milk >= 100:
                items_needed.add("milk")
            if self.total_cups >= 1:
                items_needed.add("cups")
            expected = {"water", "beans", "cups", "milk"}
            lack = ', '.join(expected.difference(items_needed))
            if expected == items_needed:
                return True
            else:
                print(f"Sorry, not enough {lack}!")
