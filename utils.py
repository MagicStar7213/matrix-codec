import warnings


def matrix_is_zero(x):
    result = x.is_zero
    if result is None:
        warnings.warn(f"Zero testing of {x} evaluated into None")
    return result

def list_is_ints(lst: list[str]) -> bool:
    for x in lst:
        if not float(x).is_integer():
            return False
    return True