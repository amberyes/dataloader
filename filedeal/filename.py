import os

def readname():
	filePath = '/Volumes/Amber‘s HP/fivek/fivek/png1/'
	name = os.listdir(filePath)
	return name


if __name__ == "__main__":
	name = readname()
	print(name)
	for i in name:
		if '/Volumes/Amber‘s HP/fivek/fivek/png1/' + i == '/Volumes/Amber‘s HP/fivek/fivek/png1/.DS_Store':
		   continue
		print(i)

