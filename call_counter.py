calls = 0


def count_calls():
    global calls
    calls += 1

def string_info(stroka):
    count_calls()
    lenght = len(stroka)
    verh_register = stroka.upper()
    nizh_register = stroka.lower()
    return (lenght, verh_register, nizh_register)


def is_contains(stroka, spis):
    count_calls()
    new_spis = [i.lower() for i in spis]
    if stroka.lower() in new_spis:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)