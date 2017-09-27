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
    def __init__(self, first, second):
        self.first = self.clean(first)
        self.second = self.clean(second)

    def clean(self, query):
        query = query.replace("̄", "")
        query = query.replace("̈", "")
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
                ["ҷ", "ч"]
            ]
        ]
        for group in extension_symbols:
            for subgroup in group:
                for i in range(len(subgroup)):
                    if i == len(subgroup) - 1:
                        break
                    query = query.replace(subgroup[i], subgroup[-1])

        return query
