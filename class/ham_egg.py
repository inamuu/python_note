class HamEgg:
    def __init__(self, ham, egg):
        self.ham = ham
        self.egg = egg

    def sum(self):
        hamegg = self.ham + self.egg
        print(hamegg)

instance = HamEgg(1, 2)
instance.sum()
