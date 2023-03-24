class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.character = character

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_inventory(self):
        return self.inventory

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("You have been defeated!")
            # Add game over logic here
        else:
            print("You took {} damage! Your health is now {}.".format(damage, self.health))

    def heal(self, amount):
        self.health += amount
        if self.health > self.character.max_health:
            self.health = self.character.max_health
        print("You have been healed for {}. Your health is now {}.".format(amount, self.health))
