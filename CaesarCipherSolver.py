class CaesarCipherSolver:

	def __init__(self, cipherText, key):
		self.cipherText = cipherText
		self.key = key

	def decode(self):
		
		newString = ""

		for i in range(0, len(self.cipherText)):
			currentChar = ord(self.cipherText[i]) + self.key
			if currentChar > 90:
				currentChar = currentChar - 90 + 64
			newString = newString + chr(currentChar)

		
		return newString


solve = CaesarCipherSolver("ZAPQVQEBMDMYMZMZMXACGQBGQPMETMOQDTAK", 10)
resultList = solve.decode()
print resultList

