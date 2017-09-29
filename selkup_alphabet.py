class Uni:
    strict = [
        [
            ["ә"],
            "ӭ"
        ],
        [
            ["ә̄"],
            "ӭ̄"
        ],
        [
            ["а́"],
            "ӓ"
        ],
        [
            ["а́̄"],
            "ӓ̄"
        ],
        [
            ["i"],
            "и̇"
        ],
        [
            ["ī"],
            "и̇̄"
        ],
        [
            ["дз"],
            "ҙ"
        ],
        [
            ["қ"],
            "ӄ"
        ],
        [
            ["ң"],
            "ӈ"
        ],
        [
            ["дж"],
            "җ"
        ],
        [
            ["ӌ"],
            "ҷ"
        ],
    ]

    soft = [
        [
            ["ж"],
            "җ"
        ],
        [
            ["х"],
            "ҳ"
        ],
        [
            ["ч"],
            "ҷ"
        ]
    ]

    @staticmethod
    def short(string):
        string = string.replace("̄", "")
        string = string.replace("̈", "")
        return string

    @staticmethod
    def unify(string, strict_only = False):
        strict_result = string
        for group in uni.strict:
            for query in group[0]:
                strict_result = strict_result.replace(query, group[1])
        #
        soft_result = strict_result
        for group in uni.soft:
            for query in group[0]:
                soft_result = soft_result.replace(query, ''.join(["?" for _ in range(len(query))]))
        if strict_only:
            return strict_result
        else:
            return strict_result, soft_result

    @staticmethod
    def soft_compare(string, soft_query):
        if len(string) != len(soft_query):
            return string
        for x in range(len(string)):
            if string[x] == soft_query[x]:
                pass
            elif string[x] != soft_query[x] and soft_query[x] == "?":
                pass
            else:
                return False
        return True


class Compare:
    def __init__(self, first, second=False):
        if second:
            self.first = self.clean(first)
            self.second = self.clean(second)
        else:
            self.first = first

    extension_symbols = [
        [
            ["ё̄", "е̄", "е"],
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
            ["ҳ", "х"],
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

