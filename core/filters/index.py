#
#  123 => '123'
#
def convert_int_to_string(value):
    if value and isinstance(value, int):
        return str(value)
    else:
        raise TypeError('value must be integer')

#
#  apple => APPLE
#

def uppercase(value):
    if value and isinstance(value, str):
        return value.upper()
    else: 
        raise TypeError('value must be str')    
#
#  APPLE => apple
#

def lowercase(value):
    if value and isinstance(value, str):
        return value.lower()
    else: 
        raise TypeError('value must be str')

#
#   12345 => 12,345.00
#

def currency(value, currency):
    digitsRE = /(\d{3})(?=\d)/g
    value = float(value)
    if !value and value is not 0:
        return ''
    currency = currency if currency is not None else '$'
    stringfied = round(abs(value), 2)

def comma(value):
    value_str = str(value)
    _int = value[:-3]
    i = _int.length % 3
