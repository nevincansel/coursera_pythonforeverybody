class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

an = PartyAnimal()

an.party()  # PartyAnimal.party(an)
an.party()
an.party()