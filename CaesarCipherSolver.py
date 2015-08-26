class CaesarCipherSolver:

	def __init__(self, key):
		self.key = key

	def encode(self, plainText): #Takes plain text and encodes it using a Caesar Cipher

		cipherText = ""

		for i in range(0, len(plainText)): #Iterate through each character in the plain text string
			currentChar = ord(plainText[i]) + self.key #Convert the current character to its ascii value, and add the user defined key to this value
			if currentChar > 90: #New character has ascii value > 'Z', must be looped
				currentChar = currentChar - 90 + 64
			cipherText = cipherText + chr(currentChar)`

		return cipherText

	def decode(self, cipherText):
		
		plainText = ""

		for i in range(0, len(cipherText)): #Iterate through each character in the cipher text string
			currentChar = ord(cipherText[i]) - self.key #Convert the current character to its ascii value, and subtract the user defined key to this value
			if currentChar < 65: #New character has ascii value < 'A', must be looped  
				currentChar = 90 - (64 - currentChar)
			plainText = plainText + chr(currentChar)

		
		return plainText


solve = CaesarCipherSolver(4)
resultList = solve.decode("MXAEWEHEVOERHWXSVQCRMKLXXLIVEMRJIPPMRXSVVIRXW")
print resultList
resultList = solve.encode("ITWASADARKANDSTORMYNIGHTTHERAINFELLINTORRENTS")
print resultList

