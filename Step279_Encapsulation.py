class Protected:
    def __init__(self):
        self._yourMom = 0

mom = Protected()
mom._yourMom = 10
print(mom._yourMom)
