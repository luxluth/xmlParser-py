"""
XMLPARSER
=========

This module contains the XMLParser class, which is used to parse XML files
and return a list of dictionaries containing the data.

"""

import xml.etree.ElementTree as ET

class XMLParser:
    """
    This class is used to parse XML files and return a list of dictionaries
    containing the data.

    Attributes
    ----------
    xml_file : str
        The path to the XML file to be parsed.
    xml_root : Element
        The root element of the XML file.
    xml_data : list
        A list of dictionaries containing the data from the XML file.

    Methods
    -------
    parse_xml()
        Parses the XML file and returns a list of dictionaries containing the
        data.
    """

    def __init__(self, xml_file):
        """
        Parameters
        ----------
        xml_file : str
            The path to the XML file to be parsed.
        """
        self.xml_file = xml_file
        self.xml_root = ET.parse(self.xml_file).getroot()
        self.xml_data = {}

    def parse_xml(self):
        """
        Parses the XML file and returns a list of dictionaries containing the
        data.

        Returns
        -------
        list
            A list of dictionaries containing the data from the XML file.
        """
        for child in self.xml_root:
            print(child.tag, child.attrib, child.text)
            self.xml_data[child.tag] = child.text
            self.xml_data[f'{child.tag}_attrib'] = child.attrib
            self.xml_data[f'{child.tag}_attrib']['text'] = child.text
        return self.xml_data

if __name__ == "__main__":
    parser = XMLParser("data.xml")
    print(parser.parse_xml())
