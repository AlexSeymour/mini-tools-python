
import sqlite3, re, glob


def write_search_emails(db, files):
	


	for _file in files:
		with open(_file, encoding="utf-8", errors="ignore") as fichier:
			text = fichier.read()
			#text = text.replace("=\n", "")
			#mails = re.findall(r'([\w\.-]+@[outlook|gmail|hotmail]+\.+(com|fr))', text)
			mails = re.findall(r'([\w\.-]{5,20}@(?:outlook|gmail|hotmail|gmx|orange|free|aol|live|yahoo|sfr|laposte){1}\.(?:com|fr|net))', text)
			mails = list(set(mails))


	print(mails)