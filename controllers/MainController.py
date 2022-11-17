from models.PhoneNumber import PhoneNumber


class PhoneController:
    def get(self, phone_name=''):
        phones = []
        with open('phones.txt', 'r', encoding='UTF-8') as file:
            for index, items in enumerate(file):
                items_list = items.split(';')
                if phone_name != '':
                    if items_list[1].lower().find(phone_name.lower()) != -1:
                        phones.append(PhoneNumber(items_list[0], items_list[1], items_list[2], index))
                else:
                    phones.append(PhoneNumber(items_list[0], items_list[1], items_list[2], index))

        return phones

    def create(self, phone_number, phone_name, phone_address):
        phone = PhoneNumber(phone_number, phone_name, phone_address)
        with open('phones.txt', 'a', encoding='UTF-8') as file:
            file.write(phone.__str__())

    def delete(self, id):
        with open('phones.txt', 'r+') as file:
            items = file.readlines()
            file.seek(0)
            file.truncate()
            for index, item in enumerate(items):
                if index != id:
                    file.write(item)

    def exportHTML(self, phones):
        html = '<html> \n <head></head> \n <body> \n <table>'
        html += '<thead>\n<tr>\n<th>ID</th>\n<th>Номер</th>\n<th>Имя</th>\n<th>Адрес</th>\n</tr>\n</thead>\n<tbody>'

        for phone in phones:
            html += f'<tr>\n<th>{phone.id}</th>\n' \
                    f'<th>{phone.number}</th>\n' \
                    f'<th>{phone.name}</th>\n' \
                    f'<th>{phone.address}</th>\n</tr>\n'

        html += '</tbody>\n</table>\n</body>\n</html>'
        with open('phones.html', 'w', encoding='UTF-8') as file:
            file.write(html)

    def exportXML(self, phones):
        xml = '<main>\n'

        for phone in phones:
            xml += f'<id>{phone.id}</id>\n' \
                   f'<number>{phone.number}</number>\n' \
                   f'<name>{phone.name}</name>\n' \
                   f'<address>{phone.address}</address>\n'

        xml += '</main>'

        with open('phones.xml', 'w', encoding='UTF-8') as file:
            file.write(xml)
