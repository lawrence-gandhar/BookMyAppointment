import re

#
# REGEX TO CHECK THE STRING CONTAINS ONLY ALPHABETS & SPACES
# @param : string
# return: Boolean
#
def is_text(value=None):
    if value is not None:
        if value.strip()!="":
            return bool(re.match('[a-zA-Z\s]+$', value))
    return False

#
# REGEX TO CHECK THE STRING CONTAINS ONLY ALPHABETS & SPACES
# @param : string
# return: Boolean
#
