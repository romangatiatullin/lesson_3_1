calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (s.lower() for s in list_to_search)
print(string_info('Smetana'))
print(string_info('Ketchup'))
print(is_contains('Salat', ['luk', 'SALavat', 'SaLAT']))
print(is_contains('Chesnok', ['chesnochniy', 'Chestniy', 'chistiy']))
print(calls)

