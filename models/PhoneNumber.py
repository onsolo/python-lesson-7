class PhoneNumber:

    def __init__(self, number, name, address, id=None):
        self.id = id
        self.number = number
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.number};{self.name};{self.address}\n'

    def getAttributes(self):
        return [self.id, self.number, self.name, self.address]


