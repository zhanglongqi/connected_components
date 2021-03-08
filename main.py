from typing import List


def main(image: List[int]):

	equ = [[1,1]]

	image.insert(0, image[0])
	for row in range(0, len(image)):
		image[row].insert(0, 0)

	for row in range(1, len(image)):
		for col in range(1, len(image[0])):
			if image[row][col] != 0:
				if 0== image[row][col-1] and 0== image[row-1][col]:
					new_val = equ[len(equ)-1][0]


def read_image(image_file: str, debug: bool):
	image = []
	with open(image_file, 'r') as f:
		for l in f.readlines():
			l = l.strip()
			l = l.split('\t')
			image.append([int(i) for i in l])
	if debug: print(f'{image}')
	return image


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='right sum operation')

	parser.add_argument('--image', type=str, required=True)

	parser.add_argument('-D', '--debug', action='store_true', help='show more debug info')

	args = parser.parse_args()
	image = read_image(args.image, args.debug)
	main(image=image)
