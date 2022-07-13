import menu
import coffee_maker
import money_machine

money = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)