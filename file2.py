class vegetable():
    def __init__(self, kind, water_saturation, fertilizer_saturation, light_saturation):
        self.water_saturation = water_saturation
        self.fertilizer_saturation = fertilizer_saturation
        self.light_saturation = light_saturation
    def print_info(self):
        print('Sample type:', self.kind)
        print('Water supply:', self.water_saturation)
        print('Nutrient supply:', self.fertilizer_saturation)
        print('Light availability:', self.light_saturation)
    def checkstatus(self, n_water_s, n_fertilizer_s, n_light_s):
        if self.water_saturation >= n_water_s and self.fertilizer_saturation == n_fertilizer_s and self.light_saturation == n_light_s:
            print('Pesult:+')
            return True
        else:
            print('Result:died')
            return False