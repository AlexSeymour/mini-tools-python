import argparse, glob, os, imghdr
from PIL import Image
from PIL import ImageOps
parser = argparse.ArgumentParser()

parser.add_argument('--flip', action="store_true", default=False)
parser.add_argument('--mirror', action="store_true", default=False)
parser.add_argument("--grayscale", action="store_true", default=False)
parser.add_argument("--path",  default=os.path.dirname(os.path.realpath(__file__)))

args = parser.parse_args()
args = dict(args._get_kwargs())




def img_edit(key, path):
	for item in path:
			
			if is_image(item):
				image = Image.open(item)
				image = key(image)
				image.save(item)


def get_files(path="*.jpg"):
	return glob.glob(path)


def is_image(path):
	return os.path.isfile(path) and imghdr.what(path)


def main():
	path = []
	if os.path.isdir(args['path']):
		path += get_files(os.path.join(args['path'], "*"))
		

		print("dir")

	elif os.path.isfile(args['path']):
		path += [args['path']]
		

	else:
		raise Exception("erreur")



	


	if args['mirror']:
		img_edit(ImageOps.mirror, path)

	if args['flip']:
		img_edit(ImageOps.flip, path)



	if args['grayscale']:
		img_edit(ImageOps.grayscale, path)








if __name__ == '__main__':
	main()