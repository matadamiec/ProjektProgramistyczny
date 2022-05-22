from datetime import datetime

from class_part import Part
from class_vehicle import Vehicle


class Order:
    def __init__(self, vehicle: Vehicle, parts: [Part]):
        self.order_id = vehicle.vin_const + str(datetime.timestamp(datetime.now())).replace(".", "")
        self.vehicle_data = vehicle
        self.parts = parts
        self.order_value = 0

        for part in parts:
            if part.ordered_qt is None:
                part.ordered_qt = 1
            self.order_value += float(part.price) * float(part.ordered_qt)

    def __str__(self):
        return f'#Zamówienie#\nNumer zamówienia: {self.order_id}\n{self.vehicle_data.__str__()}\n\'' \
               f'Liczba zamówionych elementów: {str(len(self.parts) + 1)}\nWartość: {str(self.order_value)} '

    def to_dict(self) -> {}:
        parts = [part.to_dict() for part in self.parts]
        order_dict = {
            "id": self.order_id,
            "vehicle_data": self.vehicle_data.to_dict(),
            "parts": parts,
            "order_value": str(self.order_value)

        }
        return order_dict

    @staticmethod
    def class_info():
        return 'Klasa opisująca zamówienie'
