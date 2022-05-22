class Vehicle:
    def __init__(self, v_id: str, make: str, model: str, model_code: str, production_years: str, vin_const: str, engine: str, description: str):
        self.v_id = v_id
        self.make = make
        self.model = model
        self.model_code = model_code
        self.production_years = production_years
        self.vin_const = vin_const
        self.engine = engine
        self.description = description

    def __str__(self):
        return f'#Pojazd#\nMarka: {self.make}\nModel: {self.model} ({self.model_code})' \
               f'\nLata produkcji: {self.production_years}\nVIN: {self.vin_const}\nSilnik: {self.engine}\nOpis: {self.description}'

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def class_info():
        return 'Klasa opisująca pojazd'
