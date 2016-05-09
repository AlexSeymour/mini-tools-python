import re, random

TEXT = "{Bonjour|Salut|Hello},{Tu vas bien|comment vas-tu ?}"




def content_spinning(text):
	content = re.findall("([^{}]+)", text)
	content = [random.choice(re.split("\|", y)) for y in content]
	content = ' '.join(content)
	return content



def main():
	content = content_spinning(TEXT)
	print(content)

if __name__ == '__main__':
	main()