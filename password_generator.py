import string, random, argparse


parser = argparse.ArgumentParser(description="Création password")
parser.add_argument("--min", help="Longueur minimum du password", type=int, default=6)
parser.add_argument("--max", help="Longueur maximum du password", type=int, default=12)
parser.add_argument("--uppercase", help="Majuscule autorisé", action='store_true', default=None)
parser.add_argument("--lowercase", help="Minuscule autorisé", action='store_true', default=None)
parser.add_argument("--digits", help="Chiffres autorisé", action='store_true', default=None)
parser.add_argument("--punctuation", help="Ponctuaction autorisé", action='store_true', default=None)

args = parser.parse_args()
args = dict(args._get_kwargs())

def generate_password(min_length=8, max_length=20, letters_lowercase=True, letters_uppercase=False, digits=False, punctuation=False):
	"""
	génère un mot de passe entre min_length et max_length. 
	"""
	rd = []
	password = []
	if letters_uppercase:
		rd += string.ascii_uppercase
	if letters_lowercase:
		rd += string.ascii_lowercase
	if digits:
		rd += string.digits
	if punctuation:
		rd += string.punctuation

	
	if not rd:
		rd += string.ascii_lowercase

	rd = list(rd)

	rd=  random.sample(rd, random.randint(min_length, max_length))
	password = rd
	return ''.join(password)

	



def main():



	password = generate_password(args['min'], args['max'], args['lowercase'], args['uppercase'], args['digits'], args['punctuation'])
	print("Votre mot de passe est:", password)




if __name__ == '__main__':
	main()