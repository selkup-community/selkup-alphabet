#!/usr/bin/python3
#
# Coding (c) Fyodor Sizov, 2017
# Alphabet specification (c) Grigoriy Korotkih, Fyodor Sizov, 2017
#
# The code is based on the Selkup.Tk alphabet specification and may be updated regularly:
# http://selkup.tk/alphabet-specification
#
#
class uni:
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
			["ю̈"],
			"ӱ"
		],
		[
			["ю̈̄"],
			"ӱ̄"
		],
		[
			["ӯ"],
			"ю̄"
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
	def unify(string):
		strict_result = string
		for group in uni.strict:
			for query in group[0]:
				strict_result = strict_result.replace(query, group[1])
		#
		soft_result = strict_result
		for group in uni.soft:
			for query in group[0]:
				soft_result = soft_result.replace(query, ''.join(["?" for x in range(len(query))]))
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
