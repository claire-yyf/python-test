from test import fn, num

fn()

print("Hello World", num)


class phoneFactory:
    def __init__(self, num):
        self.nEmployees = num

    def hire(self, nNewEmployees):
        self.nEmployees += nNewEmployees
        self.manager = 'happy'
        return self

    @staticmethod
    def tenEmployees():
        return phoneFactory(10).hire(5)

    def printNumEmployees(self):
        print(self.nEmployees)


phoneFactory1 = phoneFactory(5)
phoneFactory1.printNumEmployees()
phoneFactory1.hire(10).hire(20).printNumEmployees()

phoneFactory2 = phoneFactory(3)
# phoneFactory.tenEmployees().hire(6).printNumEmployees()
