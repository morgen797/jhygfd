class Assistant():
    def __init__(self, name, position):
        self.Name= name
        self.position = position
    def print_info(self):
        print('Name', self.Name)
        print('Position', self.position)
    def water(self, vegetable):
        vegetable.water_sacuration +=1
        print('',vegetable.kind, '\n')
    def fertilize(self, vegetable):
        vegetable.fertilize_sacuration +=1
        print('')
    def turn_ligth(self, vegetable):
        vegetable.turn_ligth_sacuration +=1
        print('', vegetable.kind,'\n')
    def checkresult()
        
    

