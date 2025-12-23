def are_elements_numbers(l: list[str]) -> bool:
    for x in l:
        try:
            float(x)
        except ValueError:
            return False
    return True

def construct_string(l: list[str | list]) -> str:
    return ''.join([construct_string(x) if type(x) is list else x for x in l])