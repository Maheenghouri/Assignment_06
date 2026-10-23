from abc import ABC, abstractmethod

 
rates = {
     
    'margherita': 5.0,
    'bbq_chicken': 7.5,
    'veggie_supreme': 6.0,
    'garlic_mayo_paneer': 6.8,
    'four_cheese': 7.2,
   
    'cheese': 1.0,
    'olives': 0.75,
    'mushrooms': 0.85,
    'pepperoni': 1.5,
    
    'jalapenos': 0.90,
    'chili_flakes': 0.60,
    'spicy_chicken': 1.80
}

 
coupons = {
    'SAVE10': 10,
    'PIZZA20': 20,
    'HOT30': 30
}

 
class Pizza(ABC):
    @abstractmethod
    def description(self) -> str: pass
    @abstractmethod
    def cost(self) -> float: pass


class Margherita(Pizza):
    def description(self): return "Margherita Pizza"
    def cost(self): return rates['margherita']

class BBQChicken(Pizza):
    def description(self): return "BBQ Chicken Pizza"
    def cost(self): return rates['bbq_chicken']

class VeggieSupreme(Pizza):
    def description(self): return "Veggie Supreme Pizza"
    def cost(self): return rates['veggie_supreme']

class GarlicMayoPaneer(Pizza):
    def description(self): return "Garlic Mayo Paneer Pizza"
    def cost(self): return rates['garlic_mayo_paneer']

class FourCheese(Pizza):
    def description(self): return "Four Cheese Pizza"
    def cost(self): return rates['four_cheese']


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

 
class Cheese(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Cheese"
    def cost(self): return self.pizza.cost() + rates['cheese']

class Olives(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Olives"
    def cost(self): return self.pizza.cost() + rates['olives']

class Mushrooms(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Mushrooms"
    def cost(self): return self.pizza.cost() + rates['mushrooms']

class Pepperoni(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Pepperoni"
    def cost(self): return self.pizza.cost() + rates['pepperoni']

 
class Jalapenos(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Jalapeños"
    def cost(self): return self.pizza.cost() + rates['jalapenos']

class ChiliFlakes(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Chili Flakes"
    def cost(self): return self.pizza.cost() + rates['chili_flakes']

class SpicyChicken(ToppingDecorator):
    def description(self): return self.pizza.description() + " + Spicy Chicken"
    def cost(self): return self.pizza.cost() + rates['spicy_chicken']

 
def menu():
    print("\n🍕 Welcome to Pizza Builder!")
    print("Choose your base pizza:")
    print("1. Margherita (${})".format(rates['margherita']))
    print("2. BBQ Chicken (${})".format(rates['bbq_chicken']))
    print("3. Veggie Supreme (${})".format(rates['veggie_supreme']))
    print("4. Garlic Mayo Paneer (${})".format(rates['garlic_mayo_paneer']))
    print("5. Four Cheese (${})".format(rates['four_cheese']))

    base_choice = input("Enter your choice (1–5): ")

    if base_choice == "1":
        pizza = Margherita()
    elif base_choice == "2":
        pizza = BBQChicken()
    elif base_choice == "3":
        pizza = VeggieSupreme()
    elif base_choice == "4":
        pizza = GarlicMayoPaneer()
    elif base_choice == "5":
        pizza = FourCheese()
    else:
        print("❌ Invalid choice. Exiting.")
        return
 
    print("\n🧀 Regular Toppings:")
    print("1. Cheese (${:.2f})".format(rates['cheese']))
    print("2. Olives (${:.2f})".format(rates['olives']))
    print("3. Mushrooms (${:.2f})".format(rates['mushrooms']))
    print("4. Pepperoni (${:.2f})".format(rates['pepperoni']))

    print("\n🌶️ Spicy Toppings:")
    print("5. Jalapeños (${:.2f})".format(rates['jalapenos']))
    print("6. Chili Flakes (${:.2f})".format(rates['chili_flakes']))
    print("7. Spicy Chicken (${:.2f})".format(rates['spicy_chicken']))

    topping_map = {
        '1': Cheese,
        '2': Olives,
        '3': Mushrooms,
        '4': Pepperoni,
        '5': Jalapenos,
        '6': ChiliFlakes,
        '7': SpicyChicken
    }

    while True:
        topping_input = input("Add topping number (or 'done'): ")
        if topping_input.lower() == 'done':
            break
        elif topping_input in topping_map:
            pizza = topping_map[topping_input](pizza)
        else:
            print("⚠️ Invalid topping option.")

    
    try:
        quantity = int(input("How many pizzas would you like to order? "))
    except:
        quantity = 1

    coupon_code = input("Enter coupon code (or press Enter to skip): ").strip().upper()
    discount = coupons.get(coupon_code, 10)

    if discount:
        print(f"🎉 Coupon applied: {discount}% off!")
    elif coupon_code:
        print("❌ Invalid coupon. No discount applied.")

    
    sub_total = pizza.cost() * quantity
    discount_amount = (discount / 100) * sub_total
    final_total = sub_total - discount_amount

    print("\n✅ Your Pizza:", pizza.description())
    print("💵 Price per Pizza: ${:.2f}".format(pizza.cost()))
    print("🧾 Quantity: {}".format(quantity))
    print("🏷️ Subtotal: ${:.2f}".format(sub_total))
    if discount > 0:
        print("💸 Discount: -${:.2f} ({}%)".format(discount_amount, discount))
    print("💰 Final Total: ${:.2f}".format(final_total))

 
if __name__ == "__main__":
    menu()
