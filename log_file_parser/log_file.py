""""
Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Найти IP адрес спамера, количество отправленных им запросов. Спамером считать клиента, отправивший больше всех запросов.
Получить файл с информацией вида: <remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
<response_code>, <response_size>
"""
import re
import requests


RE_REMOTE_ADDR = re.compile(r'(?:[\d]{1,3}\.){3}[\d]{1,3} ')
RE_REQUEST_DATETIME = re.compile(r'[\d]{2}\/[a-zA-Z]+\/[\d]{4}(?::[\d]{2}){3}\s\+[\d]{4}')
RE_REQUEST_TYPE = re.compile(r'"(?P<request_type>[A-Z]{2,})')

RE_REQUEST_RESOURCE = re.compile(r' (?P<requested_resource>(?:\/[\w ]*){2,}[\w]) HTTP')
RE_RESPONSE_CODE = re.compile(r' (?P<response_code>[\d]{3}) ')
RE_REQUESTED_SIZE = re.compile(r' (?P<response_size>[\d]{1,10}) "')


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url)
with open('nginx_logs.txt', 'w') as file:
    file.write(r.text)

list_of_addr = list()
final_list = open('customer_requests.txt', 'w', encoding='utf-8')
all_info_list = open('all_info.txt', 'w', encoding='utf-8')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    i = 0
    for line in f:
        if '.' in line[:3]:
            remote_addr = RE_REMOTE_ADDR.search(line).group()
            request_type = RE_REQUEST_TYPE.findall(line)[0]
            requested_resource = RE_REQUEST_RESOURCE.findall(line)[0]
            size_a = RE_REQUESTED_SIZE.findall(line)[0]

            list_of_addr.append(remote_addr)

            final_list.write(f'{remote_addr}, {request_type}, {requested_resource}\n')
            all_info_list.write(f'{remote_addr}, {RE_REQUEST_DATETIME.findall(line)[0]}, {request_type}, '
                                f'{requested_resource}, {RE_RESPONSE_CODE.findall(line)[0]}, '
                                f'{RE_REQUESTED_SIZE.findall(line)[0]}\n')

final_list.close()
all_info_list.close()

dict_of_addr = {}
for el in list_of_addr:
    if el in dict_of_addr:
        dict_of_addr[el] = dict_of_addr[el] + 1
    else:
        dict_of_addr[el] = 1
max_val = 1
ip_of_max_val = ''
for key, val in dict_of_addr.items():
    if val > max_val:
        max_val, ip_of_max_val = val, key
print(f'IP адрес спамера: {ip_of_max_val}\nКоличество отправленных запросов {max_val}')   # 216.46.173.126 2350





