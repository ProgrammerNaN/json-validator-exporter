from enum import Enum
import jsonpath_ng
import logging

class Restriction(Enum):
    NOT_NULL_RESPONSE = 0
    NOT_NULL = 1

class ValidationStatus(Enum):
    OK = 0
    ERROR = 1

def validate(json, restrictions, root_path):
    result = None
    for restriction in restrictions:
        print("restriction: %s" % restriction)
        if (isinstance(restriction, dict)):
            restriction_name = list(restriction.keys())[0]
            result = validation_type_choose(restriction_name, json, restriction[restriction_name], root_path)
        else:
            result = validation_type_choose(restriction, json, None, None)
    if (result == ValidationStatus.ERROR):
            return ValidationStatus.ERROR
    return ValidationStatus.OK


def not_null_validate(json, path_params, root_path):
    print("not_null_validate")
    for path_param in path_params:
        full_path = root_path + path_param
        matches = jsonpath_ng.parse(full_path).find(json)
        if not matches:
            logging.warn("Не найдено поле %s" % full_path)
            return ValidationStatus.ERROR
        for match in matches:
            if (match.value == None):
                logging.warn("Поле %s = null" % full_path)
                return ValidationStatus.ERROR
    return ValidationStatus.OK


def not_null_response_validate(json):
    print("not_null_response_validate")
    if not json:
        return ValidationStatus.ERROR
    else:
        return ValidationStatus.OK



def validation_type_choose(restriction_type, json, path_params, root_path):
    print(restriction_type.upper())
    if restriction_type.upper() == Restriction.NOT_NULL_RESPONSE.name:
        return not_null_response_validate(json)
    elif restriction_type.upper() == Restriction.NOT_NULL.name:
        return not_null_validate(json, path_params, root_path)
