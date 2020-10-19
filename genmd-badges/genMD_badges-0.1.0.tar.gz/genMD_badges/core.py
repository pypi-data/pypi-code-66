import hashlib
import os
import time

class genMD_badges:
	def __init__(self):
		try:
			with open("Markdown_output.txt", mode="x") as md:
				md.close()
			print("===> File Created...")
			with open("Markdown_output.txt", mode="a+", encoding="UTF8") as md:
				md.write("|–Ú∫≈|√˚≥∆|Hash|\n")
				md.write("|-----|-----|------|\n")
				md.close()
		except:
			print("===> File <Markdown_output.txt> exists...")
			pass
		self.rank = 0

	def insert_str(self, item_without_so, item_with_so, item_sha1, rank):
		alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
		with open("./Markdown_output.txt", "a+") as TextPanel:
			content = "|"+ alphabet[rank] +".	|![](http:" + "//img.shields.io/badge/" + item_with_so + \
			          "-V0.0__Beta-Blue.svg?logo=linux&style=plastic)|![](http:" + "//img.shields.io/badge/Sha1-" + item_sha1 + \
			          "-Red.svg)|"
			TextPanel.write(content)
			TextPanel.write("\n")
			TextPanel.close()
		self.rank += 1


class hashValueCheck:
	def __init__(self, _filepath):
		def calculateSha1(_filepath):
			with open(_filepath, 'rb') as f:
				sha1obj = hashlib.sha1()
				sha1obj.update(f.read())
				hash = sha1obj.hexdigest()
				return hash

		def calculateMD5(_filepath):
			with open(_filepath, 'rb') as f:
				md5obj = hashlib.md5()
				md5obj.update(f.read())
				hash = md5obj.hexdigest()
				return hash

		self.MD5 = calculateMD5(_filepath)
		self.Sha1 = calculateSha1(_filepath)


if __name__ == '__main__':
	file = genMD_badges()

	filePath = input("Input filepath, with default './' : ")
	if not filePath:
		filePath = "./"

	print("===>", filePath)

	fileSuffix = input("Input file suffix, with default '.so' : ")
	if not fileSuffix:
		fileSuffix = ".so"
	print("===>", fileSuffix)

	soFiles = []
	for path, folder, files in os.walk(filePath):
		for item in files:
			if item.find(fileSuffix) != -1:
				soFiles.append(item)
			else:
				continue

	item_without_so = []
	item_with_so = []
	item_sha1 = []

	for item in soFiles:
		item_with_so.append(item)
		item_without_so.append(item.replace(".so", ""))
		item_sha1.append(hashValueCheck(item).Sha1)
	print(item_without_so, item_with_so, item_sha1)

	for _ in range(item_sha1.__len__()):
		print(item_without_so[_])
		file.insert_str(item_without_so=item_without_so[_],
		                item_with_so=item_with_so[_],
		                item_sha1=item_sha1[_],
		                rank=file.rank)

	os.rename("Markdown_output.txt", "Markdown_output.md")

	cmd = "pandoc ./Markdown_output.md --output=./Markdown_output.html"
	os.popen(cmd)

	time.sleep(1)
	os.rename("./Markdown_output.html", "./hash–£—È.html")
	os.remove("Markdown_output.md")
