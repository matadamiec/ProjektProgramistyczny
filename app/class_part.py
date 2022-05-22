class Part:
    def __init__(self, p_id: str, name: str, sn: str, producer: str, price: float, availability: int, order_wait_days: int, ordered_qt=None):
        self.p_id = p_id
        self.name = name
        self.sn = sn
        self.producer = producer
        self.price = price
        self.availability = availability
        self.order_wait_days = order_wait_days
        self.ordered_qt = ordered_qt

    def __str__(self):
        return f'#Część#\nNazwa: {self.name}\nNumer seryjny : {self.sn}' \
               f'\nCena: {str(self.price)}\nCzas oczekiwania (dni): {str(self.availability)}'

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def class_info():
        return 'Klasa opisująca część'


class PartSnWithQt:
    def __init__(self, sn: str, qt: str):
        self.sn = sn
        self.qt = qt
