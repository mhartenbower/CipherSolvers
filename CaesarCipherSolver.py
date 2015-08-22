class CaesarCipherSolver:

	def __init__(self, cipherText):
		self.cipherText = cipherText

	def decode(self):
		resultStrings = [0] * 26
		for i in range(1,25):
			newString = ""

			for j in range(0, len(self.cipherText)):
				currentChar = ord(self.cipherText[j]) + i
				if currentChar > 90:
					currentChar = currentChar - 90 + 64
				newString = newString + chr(currentChar)

			resultStrings.append(newString)
		return resultStrings

solve = CaesarCipherSolver("NBYWIOLMYCHZILGUNCIHMBIOFXHIQVYUWWYMMCVFYIHVFUWEVIULX")
resultList = solve.decode()
for elem in resultList:
	print elem

