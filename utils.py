def is_empty(string:str) -> bool:
    new_string = str()
    for i in string:
        if i != " ":
            new_string += i
    return new_string == ""