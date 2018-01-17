#!/usr/bin/python3

import selkup_alphabet.Conv


class Compare:
    def __init__(self, first, second=False):
        if second:
            self.first = self.clean(first)
            self.second = self.clean(second)
        else:
            self.first = first

    extension_symbols = [
        [
            ["ё̄", "е̄", "ё", "е"],
            ["ы̄", "ы"],
            ["ӧ", "ӧ̄", "о̄", "о"],
            ["ю̈", "ю̈̄", "ю̄"],
            ["я̄", "я"],
            ["ӭ", "ӭ̄", "э̄", "э"],
            ["ӓ", "ӓ̄", "ā", "а"],
            ["ӱ", "ӱ̄", "ӯ", "у"],
            ["и̇", "и̇̄", "ӣ", "и"],
            ["ӷ", "г"],
            ["ӄ", "к"],
            ["ӈ", "н"],
            ["җ", "ж"],
            ["ӽ", "ҳ", "х"],
            ["ҷ", "ч"],
            ["ҙ", "дз"]
        ]
    ]

    def clean(self, query):
        for pattern in ["̈", "̄", "́"]:
            query = query.replace(pattern, "")
        for group in self.extension_symbols:
            for subgroup in group:
                for i in range(len(subgroup)):
                    if i == len(subgroup) - 1:
                        break
                    query = query.replace(subgroup[i], subgroup[-1])

        return query

    def is_endsym(self, sym):
        for group in self.extension_symbols:
            for subgroup in group:
                if subgroup[-1] == sym:
                    return True

        return False

    def is_extension(self, sym):
        for group in self.extension_symbols:
            for subgroup in group:
                if sym in subgroup[:-1]:
                    return True

        return False

    def get_unaffected_start(self):
        string = ''
        for sym in self.first:
            if not self.is_endsym(sym) and not self.is_extension(sym):
                string += sym
            else:
                return string

        return string

    def first_starts(self):
        return self.first.startswith(self.second)

    def first_ends(self):
        return self.first.endswith(self.second)

    def first_includes(self):
        return self.second in self.first

    def first_ends(self):
        return self.first.endswith(self.second)

    def equal(self):
        return self.first == self.second

    def combine(self, *args):
        for arg in args:
            if self.__getattribute__(arg):
                return self.__getattribute__(arg)
        return False

