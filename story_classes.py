class Player:

    def __init__(self, name="Guest"):
        self.name = name
        self._health = 3
        self._moves = 0
        self.has_chest = False
        self.moves = 0

    def view_health(self):
        return self._health

    def view_moves(self):
        return self._moves

    def effect_health(self, amount):
        if amount < 0:
            if self._health - amount > 0:
                self._health += amount
                return self._health
            else:
                self._health = 0
                return self._health
        elif amount > 0:
            self._health += amount
            return self._health

    def effect_moves(self, amount):
        self._moves += amount
        return self._moves

    def obtains_chest(self):
        self.has_chest = True
        return self.has_chest

    def add_move(self):
        self.moves += 1
        return None
