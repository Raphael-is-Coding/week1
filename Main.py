class Plane:
    def __init__(self, id):
        self.id = id
        self.position = (0,0,0)

    def begin_fly(self, position):
        self.position = position

    def end_fly(self, position):
        self.position = position

    def go_forward(self,position):
        self.position = position

    def show(self):
        print("Plane {} , coordinates on {} now".format(self.id, self.position))

ucak =  Plane('utr1')
drone = Plane('utr2')
siha =  Plane('utr3')

class Filo:
    def __init__(self):
        self.planes = []

    def show(self):
        for i in self.planes:
            print('Our filo include {}'.format(i.id))

    def add_filo(self,Plane):
        self.planes.append(Plane)

FirstFilo = Filo()
FirstFilo.add_filo(siha)
FirstFilo.add_filo(drone)
FirstFilo.add_filo(ucak)
FirstFilo.show()






