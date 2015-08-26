class CaesarCipherSolver:

	def __init__(self, cipherText, key):
		self.cipherText = cipherText
		self.key = key

	def encode(self):
		cipherText = ""

		for i in range(0, len(self.plainText)):
			currentChar = ord(self.plainText[i]) - self.key
			if currentChar > 90:
				currentChar = currentChar - 90 + 64
			cipherText = cipherText + chr(currentChar)

		return cipherText

	def decode(self):
		
		plainText = ""

		for i in range(0, len(self.cipherText)):
			currentChar = ord(self.cipherText[i]) - self.key
			if currentChar < 65:
				currentChar = 90 - (64 - currentChar)
			plainText = plainText + chr(currentChar)

		
		return plainText


solve = CaesarCipherSolver("MXAEWEHEVOERHWXSVQCRMKLXXLIVEMRJIPPMRXSVVIRXW", 4)
resultList = solve.decode()
print resultList

