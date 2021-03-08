from typing import List


def main(image: List[int], debug: bool):

	equ = []

	image.insert(0, [0 for i in range(len(image[0]))])
	for row in range(0, len(image)):
		image[row].insert(0, 0)
	max_equ = 1
	for row in range(1, len(image)):
		for col in range(1, len(image[0])):
			if image[row][col] != 0:
				if 0 == image[row][col - 1] and 0 == image[row - 1][col]:
					max_equ = max_equ + 1
					equ.append([max_equ, max_equ])
					image[row][col] = max_equ
				elif 0 != image[row][col - 1] and 0 == image[row - 1][col]:
					image[row][col] = image[row][col - 1]
				elif 0 == image[row][col - 1] and 0 != image[row - 1][col]:
					image[row][col] = image[row - 1][col]
				elif 0 != image[row][col - 1] and 0 != image[row - 1][col]:
					small = min(image[row][col - 1], image[row - 1][col])
					big = max(image[row][col - 1], image[row - 1][col])

					image[row][col] = small
					for i in range(len(equ)):
						if big == equ[i][0]:
							equ.append((big, small))
							break
						else:
							continue
	if debug:
		for e in equ:
			print(f'{e[0]} -> {e[1]}')

	for row in range(0, len(image)):
		for col in range(0, len(image[0])):
			for e in reversed(equ): # prevent 26 -> 15 and 15-> 14, but actually equ is a ordered list
				if image[row][col] == e[0] and e[0] > e[1]: image[row][col] = e[1]


def read_image(image_file: str, debug: bool):
	image = []
	with open(image_file, 'r') as f:
		for l in f.readlines():
			l = l.strip()
			l = l.split('\t')
			image.append([int(i) for i in l])
	if debug: print(f'{image}')
	return image


def save_image(image_file: str, image):
	image.pop(0)
	for row in range(0, len(image)):
		image[row].pop(0)

	with open(image_file, 'w') as f:

		for row in range(0, len(image)):
			for col in range(0, len(image[0]) - 1):
				f.write(f'{image[row][col]}\t')
			f.write(f'{image[row][len(image[0]) - 1]}\n')


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='right sum operation')

	parser.add_argument('--image', type=str, required=True)
	parser.add_argument('--output', type=str, required=True)

	parser.add_argument('-D', '--debug', action='store_true', help='show more debug info')

	args = parser.parse_args()
	image = read_image(args.image, args.debug)
	main(image=image, debug=args.debug)
	save_image(image_file=args.output, image=image)
