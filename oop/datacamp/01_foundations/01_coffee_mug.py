"""
Challenge 1: The Smart Mug
Build a CoffeeMug class that simulates filling, drinking, and temperature drop.

Attributes:

capacity_ml: Total volume the mug can hold (default: 350).

current_volume_ml: Current liquid level (starts at 0).

temperature_c: Temperature of liquid (starts at 20.0 room temp).

Methods:

fill(amount, temp): Adds liquid up to capacity_ml. If poured over capacity, cap it at capacity_ml. Set temperature_c to temp.

sip(amount): Reduces current_volume_ml by amount. If amount exceeds current volume, empty the mug completely and return what was actually drunk.

cool_down(degrees): Drops temperature_c by degrees, but never lets it go below room temperature (20.0).
"""
class CoffeeMug:
    def __init__(self, capacity_ml =350, current_volume_ml=0, temperature_c=20):
        self.capacity_ml = capacity_ml
        self.current_volume_ml = current_volume_ml
        self.temperature_c = temperature_c

    def fill(self, amount, temp):
        if amount > self.capacity_ml:
            self.current_volume_ml = self.capacity_ml
        else:
            self.current_volume_ml = amount
        self.temperature_c = temp

    def sip(self, amount):
        drank_value = amount
        if amount > self.current_volume_ml:
            drank_value = self.current_volume_ml
            self.current_volume_ml = 0
            return drank_value
        else:
         self.current_volume_ml -= amount
         return amount
    def cool_down(self,degrees):
        if self.temperature_c - degrees < 20:
            self.temperature_c = 20
        else:
            self.temperature_c - degrees

if __name__ == "__main__":
    mug = CoffeeMug()
    mug.fill(amount=400, temp=85.0)  # Should cap at 350ml
    assert mug.current_volume_ml == 350

    drank = mug.sip(100)
    assert drank == 100
    assert mug.current_volume_ml == 250

    mug.cool_down(100)  # Should floor at 20.0°C
    assert mug.temperature_c == 20.0
    print("Challenge 1 Passed!")
    
            
