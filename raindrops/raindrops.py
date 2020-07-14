def convert(number):
    result = ""
    tests = ((3, "Pling"), (5, "Plang"), (7, "Plong"))
    for i in tests:
        if number % i[0] == 0:
            result += i[1]
    if result == "":
        return str(number)
    return result
