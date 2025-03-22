class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  

    def call(self, contact):
        print(f"Calling {contact} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.battery_life = min(100, self.battery_life + amount)  
        print(f"Charging... Battery is now at {self.battery_life}%")

    def battery_status(self):
        print(f"Battery Level: {self.battery_life}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)  
        self.cooling_system = cooling_system 

    def play_game(self, game):
        if self.battery_life > 10:
            self.battery_life -= 10
            print(f"laying {game} on {self.brand} {self.model}. Battery now at {self.battery_life}%")
        else:
            print("Battery too low to play games! Please charge.")


phone1 = Smartphone("Apple", "iPhone 15", 80)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 100, "Advanced Liquid Cooling")

phone1.call("Christine")
phone1.battery_status()
gaming_phone.play_game("PUBG")
gaming_phone.charge(15)
