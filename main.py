__author__ = 'Dilan'

import xml.etree.ElementTree as eT
import hashing
import os
import socket

def hash_and_store(input):
    hash = hashing.hash_kd(input)
    hash_file_name = input[:-3]+"hash"+'.xml'
    if os.path.exists(hash_file_name):
        hash_file = eT.parse(hash_file_name)
        root = hash_file.getroot()
        h = hash_file.find("hash")
        h.text = hash[0]
        s = hash_file.find("salt")
        s.text = hash[1]
        tree = eT.ElementTree(root)
        tree.write(hash_file_name)
    else:
        root = eT.Element("root")
        h = eT.SubElement(root,"hash")
        s = eT.SubElement(root,"salt")
        h.text = hash[0]
        s.text = hash[1]
        tree = eT.ElementTree(root)
        tree.write(hash_file_name)
def check_hash(input):
    xml_file = eT.parse(input[:-3]+'hash.xml')
    hash = xml_file.find("hash").text
    salt = xml_file.find("salt").text
    hashing.test_keyderived_hash(hash,salt,input)

hash_and_store("filename.xml")
check_hash("filename.xml")