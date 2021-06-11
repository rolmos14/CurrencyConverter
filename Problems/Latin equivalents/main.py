name = input()


def normalize(string):

    replacements = {'é': 'e',
                    'ë': 'e',
                    'á': 'a',
                    'å': 'a',
                    'œ': 'oe',
                    'æ': 'ae'}
    new_name = string
    for diacritic in replacements:
        new_name = new_name.replace(diacritic, replacements[diacritic])

    return new_name


print(normalize(name))
