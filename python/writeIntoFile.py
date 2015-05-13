def writeIntoFile(text, fileName):
	with open(fileName, 'w') as f:
		f.write(text)

if __name__ == '__main__':
	writeIntoFile('test file content\nnew line', 'newFile.txt')