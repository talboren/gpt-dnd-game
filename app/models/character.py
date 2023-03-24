class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.health = 100
        self.inventory = []

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

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
            print("{} has been defeated!".format(self.name))
        else:
            print("{} took {} damage! Their health is now {}.".format(self.name, damage, self.health))
