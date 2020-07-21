def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()
    return False if len(set(string)) != len(string) else True
