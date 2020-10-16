import numpy as np

from os.path import isfile
from PIL import Image

def read_image(im_path, n_retries=5):
	_read = lambda: Image.open(im_path, mode="r")
	if n_retries <= 0:
		assert isfile(im_path), "Image \"{}\" does not exist!".format(im_path)
		return _read()

	else:
		error = None
		for i in range(n_retries):
			try:
				return _read()
			except Exception as e:
				error = e

		raise RuntimeError("Reading image \"{}\" failed after {} n_retries! ({})".format(im_path, n_retries, error))


def asarray(im, dtype=np.uint8):
	if isinstance(im, np.ndarray):
		return im.astype(dtype)

	elif isinstance(im, Image.Image):
		return np.asarray(im, dtype=dtype)

	else:
		raise ValueError("Unknown image instance ({})!".format(type(im)))
