from django.core.exceptions import FieldDoesNotExist
from fabric_solution.models import *


def check_num(number: str) -> bool:
    if number[0] != "7" or len(number) != 11:
        return False

    if number.isdigit():
        return True

    return False


def update_client_data(model_item, data: dict, model_obj) -> bool:
    for key in data:
        try:
            model_obj._meta.get_field(key)
        except FieldDoesNotExist:
            return False

        setattr(model_item, key, data[key])

    model_item.save()
    return True
