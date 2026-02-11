#!/usr/bin/python3
"""Function that serializes a dictionary to an XML file
 and deserializes an XML file to a dictionary."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Defines a function that serializes a dictionary to an XML file."""
    data = ET.Element('data')
    for key, value in dictionary.items():
        key_element = ET.SubElement(data, key)
        key_element.text = str(value)
    tree = ET.ElementTree(data)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Defines a function that deserializes an XML file to a dictionary."""
    dictionary = {}
    tree = ET.parse(filename)
    data = tree.getroot()
    for item in data:
        key = item.tag
        value = item.text
        dictionary[key] = value
    return dictionary
