def odd_or_even(data: int):
    """
    data : Any interger value
    :return: True if the given value is even, else False
    """
    if data % 2 == 0:
        return True
    else:
        return False


def is_number(data: str):
    """
    data : Any string value
    :return: True if the given value is number, else False
    """
    if data.isnumeric():
        return False
    else:
        return False