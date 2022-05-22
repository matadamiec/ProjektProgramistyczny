import xml.etree.ElementTree as ET
from pathlib import Path

from class_order import Order
from class_part import Part, PartSnWithQt
from class_parts_map import PartMap
from class_vehicle import Vehicle

data_folder = Path("data_source/")
vehcicles_xml = (data_folder / "vehicles.xml")
parts_xml = (data_folder / "parts.xml")
part_car_map_xml = (data_folder / "part_car_map.xml")
orders_folder = Path("orders/")

# Vehicles Functions
def parse_vehicle_file():
    vehicles_tree = ET.parse(vehcicles_xml)
    vehicles_root = vehicles_tree.getroot()
    vehicles_list = []
    for v_item in vehicles_root.findall("vehicle"):
        vehicle = Vehicle(v_item.find("id").text, v_item.find("make").text, v_item.find("model").text, v_item.find("model_code").text,
                          v_item.find("production_years").text, v_item.find("vin_const").text, v_item.find("engine").text,
                          v_item.find("description").text)
        vehicles_list.append(vehicle)

    return vehicles_list


def find_vehicle(vin: str):
    vehicles_list = parse_vehicle_file()
    for vehicle in vehicles_list:
        if vehicle.vin_const == vin:
            print("Vehicle found")
            return vehicle
    return None


def add_new_vehicle(vehicle: Vehicle):
    vehicles_tree = ET.parse(vehcicles_xml)
    vehicles_root = vehicles_tree.getroot()

    new_vehicle = ET.Element("vehicle")
    new_vehicle.append(ET.Element("id"))
    new_vehicle.append(ET.Element("make"))
    new_vehicle.append(ET.Element("model"))
    new_vehicle.append(ET.Element("model_code"))
    new_vehicle.append(ET.Element("production_years"))
    new_vehicle.append(ET.Element("vin_const"))
    new_vehicle.append(ET.Element("engine"))
    new_vehicle.append(ET.Element("description"))
    new_vehicle.find("id").text = str(vehicle.v_id)
    new_vehicle.find("make").text = str(vehicle.make)
    new_vehicle.find("model").text = str(vehicle.model)
    new_vehicle.find("model_code").text = str(vehicle.model_code)
    new_vehicle.find("production_years").text = str(vehicle.production_years)
    new_vehicle.find("vin_const").text = str(vehicle.vin_const)
    new_vehicle.find("engine").text = str(vehicle.engine)
    new_vehicle.find("description").text = str(vehicle.description)
    vehicles_root.append(new_vehicle)
    vehicles_tree.write(vehcicles_xml)
    # print("New vehicle added")
    # return parse_vehicle_file()
    return "New vehicle added"


def remove_vehicle(vin: str):
    vehicles_tree = ET.parse(vehcicles_xml)
    vehicles_root = vehicles_tree.getroot()
    for element in vehicles_root.findall("vehicle"):
        if element.find("vin_const").text == vin:
            vehicles_root.remove(element)
            break
    # print("Skasowano pojazd")
    vehicles_tree.write(vehcicles_xml)
    # return parse_vehicle_file()
    return "Vehicle deleted"


def update_vehicle_parameters(param_name: str, param_value: str, vin: str):
    vehicles_tree = ET.parse(vehcicles_xml)
    vehicles_root = vehicles_tree.getroot()
    if param_name == "vin_const":
        print("Cannot update VIN")
        return False

    for element in vehicles_root.findall("vehicle"):
        if element.find("vin_const").text == vin:
            vehicle_parameter = element.find(param_name)
            vehicle_parameter.text = param_value
            vehicle_parameter.set("updated", "yes")
            vehicles_tree.write(vehcicles_xml)
            print("Vehicle param updated")
            return True
    return False


# Parts functions
def parse_parts_file():
    parts_tree = ET.parse(parts_xml)
    parts_root = parts_tree.getroot()
    parts_list = []
    for p_item in parts_root.findall("part"):
        part = Part(p_item.find("id").text, p_item.find("name").text, p_item.find("sn").text, p_item.find("producer").text,
                    float(p_item.find("price").text), int(p_item.find("availability").text), int(p_item.find("order_wait_days").text))
        parts_list.append(part)

    return parts_list


def find_part(sn: str):
    parts_list = parse_parts_file()
    for part in parts_list:
        if part.sn == sn:
            print("Part found")
            return part
    return None


def add_new_part(part: Part):
    parts_tree = ET.parse(parts_xml)
    parts_root = parts_tree.getroot()

    new_part = ET.Element("part")
    new_part.append(ET.Element("id"))
    new_part.append(ET.Element("name"))
    new_part.append(ET.Element("sn"))
    new_part.append(ET.Element("producer"))
    new_part.append(ET.Element("price"))
    new_part.append(ET.Element("availability"))
    new_part.append(ET.Element("order_wait_days"))
    new_part.find("id").text = str(part.p_id)
    new_part.find("name").text = str(part.name)
    new_part.find("sn").text = str(part.sn)
    new_part.find("producer").text = str(part.producer)
    new_part.find("price").text = str(part.price)
    new_part.find("availability").text = str(part.availability)
    new_part.find("order_wait_days").text = str(part.order_wait_days)
    parts_root.append(new_part)
    parts_tree.write(parts_xml)
    # print("New part added")
    # return parse_parts_file()
    return "New part added"


def remove_part(sn):
    parts_tree = ET.parse(parts_xml)
    parts_root = parts_tree.getroot()
    for part in parts_root.findall("part"):
        if part.find("sn").text == sn:
            parts_root.remove(part)
            break
    # parts_tree.write(parts_xml)
    # return parse_parts_file()
    return "Part deleted"


def update_part_parameters(param_name: str, param_value: str, sn: str):
    parts_tree = ET.parse(parts_xml)
    parts_root = parts_tree.getroot()
    if param_name == "sn":
        print("Cannot update part serial number")
        return False

    for part in parts_root.findall("part"):
        if part.find("sn").text == sn:
            part_parameter = part.find(param_name)
            part_parameter.text = param_value
            part_parameter.set("updated", "yes")
            parts_tree.write(parts_xml)
            print("Part data updated")
            return True
    return False


# Vehicle - part match functions
def parse_parts_mapping_file():
    parts_mapping_tree = ET.parse(part_car_map_xml)
    parts_mapping_root = parts_mapping_tree.getroot()
    parts_mapping_list = []
    for element in parts_mapping_root.findall("part_map"):
        part_map = PartMap(element.find("sn").text, element.find("vin").text)
        parts_mapping_list.append(part_map)

    return parts_mapping_list


def get_parts_for_vin(vin: str):
    parts_map_list = parse_parts_mapping_file()
    filtered_parts_map_list = []
    for item in parts_map_list:
        if item.vin == vin:
            filtered_parts_map_list.append(item)
    parts_list = parse_parts_file()
    matching_parts = []
    for filtered_item in filtered_parts_map_list:
        for part in parts_list:
            if part.sn == filtered_item.sn:
                matching_parts.append(part)
                break

    return matching_parts


# Order functions
def get_parts_full_data(parts_number_with_qt: [PartSnWithQt]):
    ordered_parts = []
    for item in parts_number_with_qt:
        found_part = find_part(item.sn)
        if found_part:
            found_part.ordered_qt = int(item.qt) if item.qt else 1
            ordered_parts.append(found_part)
    return ordered_parts


def create_order(vin: str, parts: []):
    requested_parts = []
    for part in parts:
        requested_parts.append(PartSnWithQt(part["sn"], part["qt"] if part["qt"] else 1))

    ordered_parts = get_parts_full_data(requested_parts)
    if ordered_parts.__len__() > 0:
        vehicle_data = find_vehicle(vin)
        new_order = Order(vehicle_data, ordered_parts)
        if new_order.order_value == 0:
            print("New order cannot have 0 value")
            return None
        order_root = ET.Element("order")

        order_id = ET.Element("order_id")
        order_id.text = new_order.order_id
        order_root.append(order_id)
        vehicle = ET.Element("vehicle")
        vehicle.append(ET.Element("make"))
        vehicle.append(ET.Element("model"))
        vehicle.append(ET.Element("model_code"))
        vehicle.append(ET.Element("vin_const"))
        vehicle.find("make").text = vehicle_data.make
        vehicle.find("model").text = vehicle_data.model
        vehicle.find("model_code").text = vehicle_data.model_code
        vehicle.find("vin_const").text = vehicle_data.vin_const
        order_root.append(vehicle)
        parts = ET.Element("parts")
        for item in new_order.parts:
            part = ET.Element("part")
            part.append(ET.Element("id"))
            part.append(ET.Element("name"))
            part.append(ET.Element("sn"))
            part.append(ET.Element("producer"))
            part.append(ET.Element("price"))
            part.append(ET.Element("qtt"))
            part.find("id").text = item.p_id
            part.find("name").text = item.name
            part.find("sn").text = item.sn
            part.find("producer").text = item.producer
            part.find("price").text = str(item.price)
            part.find("qtt").text = str(item.ordered_qt)
            parts.append(part)

        order_root.append(parts)
        order_tree = ET.ElementTree(order_root)
        order_tree.write((orders_folder / (new_order.order_id + ".xml")))
        print("New order placed")
        return new_order
    else:
        print("New order cannot be placed")
        return None


