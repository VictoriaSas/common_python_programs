"""
Функция currency_rates(), принимает в качестве аргумента код валюты(USD, EUR, GBP, ...) и возвращающую курс этой валюты
по отношению к рублю числовым типом и дату объектом date.
Если в качестве аргумента передали код валюты, которого нет в ответе, возвращает None.
Вызов из консоли.
"""

import requests
from decimal import Decimal
import datetime
import re

RE_DATE = re.compile(r'[A-Za-z]+, (?P<day>\d{2}) (?P<month>[A-Za-z]+) (?P<year>\d{4}) .*')


def currency_rates(val):
    response_currency_website = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
             'Nov': 11, 'Dec': 12}
    if response_currency_website.status_code == 200:

        # Date
        date_cw_re = re.match(RE_DATE, response_currency_website.headers['Date'])
        day_cw, year_cw = int(date_cw_re.group('day')), int(date_cw_re.group('year'))
        month_cw = month[date_cw_re.group('month')]
        date_cw = datetime.date(year_cw, month_cw, day_cw)

        # Val
        currency_website = response_currency_website.text
        if val in currency_website:
            first_match_index = currency_website.find(val)
            new_str = currency_website[first_match_index:]
            start_str = new_str.find('<Value>') + 7
            end_str = new_str.find('</Value>')
            currency = Decimal(new_str[start_str:end_str].replace(',', '.'))
            return currency, date_cw
        else:
            return None, None
    else:
        print('An error has occurred.')
        return None, None


if __name__ == '__main__':
    print('Список валют:\n'
        "{:46s}".format('AUD - Австралийский доллар'), "{:46s}".format('AZN - Азербайджанский манат'),
        "{:46s}".format('GBP - Фунт стерлингов Соединенного королевства'), '\n'
        "{:46s}".format('AMD - Армянских драмов'), "{:46s}".format('BYN - Белорусский рубль'), "{:46s}".format('BGN - '
        'Болгарский лев'), '\n'
        "{:46s}".format('BRL - Бразильский реал'), "{:46s}".format('HKD - Гонконгских долларов'),
        "{:46s}".format('DKK - Датская крона'), '\n'
        "{:46s}".format('USD - Доллар США'), "{:46s}".format('EUR - Евро'), "{:46s}".format('INR - Индийских рупий'),
        '\n'
        "{:46s}".format('KZT - Казахстанских тенге'), "{:46s}".format('CAD - Канадский доллар'),
        "{:46s}".format('KGS - Киргизских сомов'), '\n'
        "{:46s}".format('CNY - Китайский юань'), "{:46s}".format('MDL - Молдавских леев'), "{:46s}".format('NOK - '
        'Норвежских крон'), '\n'
        "{:46s}".format('PLN - Польский злотый'), "{:46s}".format('RON - Румынский лей'), "{:46s}".format('XDR - СДР '
        '(специальные права заимствования)'), '\n'
        "{:46s}".format('SGD - Сингапурский доллар'), "{:46s}".format('TJS - Таджикских сомони'), "{:46s}".format('TRY '
        '- Турецких лир'), '\n'
        "{:46s}".format('TMT - Новый туркменский манат'), "{:46s}".format('UZS - Узбекских сумов'),
        "{:46s}".format('UAH - Украинских гривен'), '\n'
        "{:46s}".format('CZK - Чешских крон'), "{:46s}".format('SEK - Шведских крон'), "{:46s}".format('CHF - '
        'Швейцарский франк'), '\n'
        "{:46s}".format('ZAR - Южноафриканских рэндов'), "{:46s}".format('KRW - Вон Республики Корея'),
        "{:46s}".format('JPY - Японских иен'), '\n')

    desired_currency = input('Введите валюту, курс которой хотите узнать: ').upper()
    final_currency, today_date = currency_rates(desired_currency)
    if final_currency is None:
        print('Такой валюты нет в списке, попробуйте еще раз.')
    else:
        print(f'1 RUB = {final_currency} {desired_currency}\nДата курса: {today_date}')
