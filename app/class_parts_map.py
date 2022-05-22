class PartMap:
    def __init__(self, sn: str, vin: str):
        self.sn = sn
        self.vin = vin

    def __str__(self):
        return f'#Część#\nSN: {self.sn}\nPasujący vin : {self.vin}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca część'
