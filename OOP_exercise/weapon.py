class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets
        self.amount_of_bullets = bullets

    def shoot(self):
        if self.amount_of_bullets > 0:
            self.amount_of_bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.amount_of_bullets}"


weapon = Weapon(5)

print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

