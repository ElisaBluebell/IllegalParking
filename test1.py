import xml.etree.ElementTree as ET
import os


def search_for_vehicle(objects):
    coordinate = []
    for data in objects:
        if data.tag == "name" and "Vehicle" not in data.text:
            break

        else:
            pass

        if data.tag == "bndbox":
            coordinate = parse_coordinate(data)

    if coordinate:
        return coordinate


def parse_coordinate(vehicle):
    xmin, ymin, xmax, ymax = "", "", "", ""
    bndbox = []

    for coordinate in vehicle:
        coortag = coordinate.tag
        coortext = coordinate.text

        if coortag == "xmin":
            xmin = coortext

        elif coortag == "ymin":
            ymin = coortext

        elif coortag == "xmax":
            xmax = coortext

        elif coortag == "ymax":
            ymax = coortext

    bndbox = [xmin, ymin, xmax, ymax]
    return bndbox


full_filename = "e:\\illegalparking\\driving_image\\Training\\bb\\label_downtown\\downtown\\day\\rainy\\30_front\\20200713_155037\\1_annotations_v001_1\\1_20200713_155037_003150_v001_1.xml"


#print(full_filename)
tree = ET.parse(full_filename)

root = tree.getroot()
#print(root[0])
#print(root.attrib)

for child in root:
    if child.tag == "object":
        search_for_vehicle(child)



