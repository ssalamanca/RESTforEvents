import xml.etree.ElementTree as ET
from collections import OrderedDict
import pandas as pd
import xmltodict
from treatingxml.models import Client
from treatingxml.models import AP
from datetime import datetime as dt
import numbers

#Para la parte de limpieza ed datos 
def to_int(item):
    is_number=isinstance(item, numbers.Number)
    if(is_number):
        return item
    elif item == '':
        return None
    elif item == None:
        return None
    else:
        return int(item)
def to_date(item):
    is_date=isinstance(item, dt)
    if(is_date):
        return item
    elif(item == ''):
        return None
    elif(item==None):
        return None
    else:
        return dt.strptime(str(item),'%Y-%m-%d')
def treating_ap():
    ap_id = ap_list_element.attrib["id"]

    is_up_element = ap_detail_element.find("is_up")
    is_up = bool(is_up_element.text) if is_up_element is not None else False

    count_element = ap_list_element.find("client_count")
    client_count = count_element.text if count_element is not None else "-1"

    #TODO
    #Crear y tratar un objeto de tipo Grupo

    mac_address_element = ap_list_element.find("lan_mac")
    mac_address = mac_address_element.text if mac_address_element is not None else ""
    ap = AP(ap_id=ap_id,
            client_count=client_count,
            name=device_name,
            ap_group=ap_group,
            is_up=is_up,
            mac_address=mac_address)
    print(ap.__str__())

def anonizacion_xml():
    return 'hola'
def union_fuentes(fuente1,fuente2,key1,key2):
    tree = ET.parse(fuente1)
    root = tree.getroot()
    for client in root.iter('client'):
        print(client.attrib)
        for ap in client.iter('association'):
            print(ap.attrib)
            bytes_used=str(ap.find('bytes_used').text)
            print('Bytes used ',bytes_used)

    
def parse_XML(xml_file): 
    """Parse the input XML file and store the result in a pandas DataFrame 
    with the given columns. The first element of df_cols is supposed to be 
    the identifier variable, which is an attribute of each node element in 
    the XML data; other features will be parsed from the text content of 
    each sub-element. """
    xtree = ET.parse(xml_file)
    xroot = xtree.getroot()
    df_cols = [elem.tag for elem in xroot.iter()] #Obtengo todos los hijos del xml desde la raiz
    #df_cols = list(OrderedDict.fromkeys(elements)) #Elimino los duplicados y los dejo en orden
    #df_cols.pop(0) #Elimino la raiz
    #print(df_cols)
    out_df = pd.DataFrame(columns = df_cols)
    
    for node in xroot: 
        res = []
        print("------------------------------------------------------------------------------------------------------")
        print(node.attrib.get(df_cols[0]))
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index=True)       
    return out_df
def union_dos_xml(fuente1,fuente2,key1,key2):
    #Armar diccionario siendo la llave cada nombre que se encuentre en la fuente 2 (No importa de cual fuente sea, el resultado seria el mismo)
    #El valor del diccionario va a ser los hijos xml con sus valores 
    dicc= {}
    tree2 = ET.parse(fuente2)
    root2 = tree2.getroot()
    for dish in root2.iter(key2):
        #Revisar que el elemento no este repetido en el diccionario
        name=str(dish.find('dish_name').text)
        print('Nomre dish = ',name)
        dicc[name]=dish

    tree = ET.parse(fuente1)
    root = tree.getroot()
    for food in root.iter(key1):
        name = str(food.find('name').text)
        print("Nombre food = ",name)
        if name in dicc.keys():
            print("Entro")
            food.append(dicc.get(name))
    tree.write('output.xml')
def limpieza():
    print('')

def preparacion():
    print('')