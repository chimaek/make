import os
import xml.etree.ElementTree as ET
import requests

path = "data/images/train"

list = os.listdir(path)
m_list = [file for file in list if file.endswith(".xml")]
print("file:{}".format(m_list))
for i in m_list:
    tree = ET.parse("C:/Users/pipir/Desktop/object_detection_demo-master/data/images/train/" + i)
    root = tree.getroot()
    for n in root.iter("object"):
        if n[0].text == "Students' Hall":
            n[0].text = str("Students Hall")
            tree.write(i,encoding="utf-8",xml_declaration=True)

    # el = root[0]
    # print(el)
# for i in m_list:
#     resp = requests.get(i)
#     msg = resp.content
#     m = ET.parse(msg)
#     print(msg)
