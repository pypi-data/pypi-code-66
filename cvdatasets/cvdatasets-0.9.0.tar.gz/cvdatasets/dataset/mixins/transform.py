import abc
import chainer

from cvdatasets.dataset.image.size import Size
from cvdatasets.dataset.mixins.base import BaseMixin

class TransformMixin(BaseMixin):

	def __init__(self, size, *args, **kwargs):
		super(TransformMixin, self).__init__(*args, **kwargs)

		self.size = size

	@abc.abstractmethod
	def transform(self, im_obj):
		pass

	def get_example(self, i):
		im_obj = super(TransformMixin, self).get_example(i)
		return self.transform(im_obj)

	@property
	def size(self):
		if chainer.config.train:
			return self._size // 0.875
		else:
			return self._size

	@size.setter
	def size(self, value):
		self._size = Size(value)
