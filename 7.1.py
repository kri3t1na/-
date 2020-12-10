import xml.etree.ElementTree
import copy


# Создаем класс Prototype
class Prototype:
    # Создаем экземпляр класса
    def __init__(self):
        self._objects = {}

    # Записываем объект
    def write_obj(self, name, obj):
        self._objects[name] = obj

    # Копируем объект
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    xml_d = xml.etree.ElementTree.parse('items.xml')
    # Определяем переменную reference как класс Prototype
    prototype = Prototype()
    # Записываем объект
    prototype.write_obj('items', xml_d)
    # Делаем копию объекта
    dublicate = prototype.clone('items')
    # Выводим оригинал и копию
    print(xml_d)
    print(dublicate)
    # Изменяем скопированный файл
    for elem in dublicate.iter('item'):
        elem.text = 'new text'
        # Изменяем атрибут элемента
    for elem in dublicate.iter('item'):
        elem.set('name', 'new_item')
    # Находим корень xml-файла в оригинале
    root = xml_d.getroot()
    # Находим корень xml-файла в копии
    dub = dublicate.getroot()
    # Выводим содержимое оригинального файла
    print('\nAll item data in xml:')
    for elem in root:
        for sub_elem in elem:
            print(sub_elem.text)
    # Выводим содержимое скопированного файла
    print('\nAll item data in dublicate:')
    for elem in dub:
        for sub_elem in elem:
            print(sub_elem.text)


main()
