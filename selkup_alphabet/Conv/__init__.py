#!/usr/bin/python3

from selkup_alphabet.Conv.srds import *
from selkup_alphabet.Conv.srsi import *


def short(string):
    string = string.replace("̄", "")
    string = string.replace("̈", "")
    return string


def unify(string, strict, soft, strict_only=False):
    strict_result = string
    for group in strict:
        for query in group[0]:
            strict_result = strict_result.replace(query, group[1])
            strict_result = strict_result.replace(query[0].upper() + query[1:], group[0].upper() + group[0][1:])
    #
    soft_result = strict_result
    for group in soft:
        for query in group[0]:
            soft_result = soft_result.replace(query, ''.join(["?" for _ in range(len(query))]))
    if strict_only:
        return strict_result
    else:
        return strict_result, soft_result