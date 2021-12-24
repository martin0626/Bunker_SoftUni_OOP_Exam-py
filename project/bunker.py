class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if not result:
            raise IndexError('There are no food supplies left!')
        return result

    @property
    def water(self):
        result = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']
        if not result:
            raise IndexError('There are no water supplies left!')
        return result

    @property
    def painkillers(self):
        result = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if not result:
            raise IndexError('There are no painkillers left!')
        return result

    @property
    def salves(self):
        result = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if not result:
            raise IndexError('There are no salves left!')
        return result

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            self.medicine.remove(medicine)
            medicine.apply(survivor)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            sustain = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
            self.supplies.remove(sustain)
            sustain.apply(survivor)
            return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for s in self.survivors:
            reduce_needs = s.age * 2
            s.needs -= reduce_needs
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')
