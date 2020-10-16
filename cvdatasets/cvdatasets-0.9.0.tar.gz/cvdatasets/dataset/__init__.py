from cvdatasets.dataset.mixins.base import BaseMixin
from cvdatasets.dataset.mixins.chainer_mixins import IteratorMixin
from cvdatasets.dataset.mixins.features import PreExtractedFeaturesMixin
from cvdatasets.dataset.mixins.parts import BBCropMixin
from cvdatasets.dataset.mixins.parts import BBoxMixin
from cvdatasets.dataset.mixins.parts import CroppedPartMixin
from cvdatasets.dataset.mixins.parts import MultiBoxMixin
from cvdatasets.dataset.mixins.parts import PartCropMixin
from cvdatasets.dataset.mixins.parts import PartMixin
from cvdatasets.dataset.mixins.parts import PartRevealMixin
from cvdatasets.dataset.mixins.parts import PartsInBBMixin
from cvdatasets.dataset.mixins.parts import RandomBlackOutMixin
from cvdatasets.dataset.mixins.parts import RevealedPartMixin
from cvdatasets.dataset.mixins.parts import UniformPartMixin
from cvdatasets.dataset.mixins.reading import AnnotationsReadMixin
from cvdatasets.dataset.mixins.reading import ImageListReadingMixin
from cvdatasets.dataset.mixins.transform import TransformMixin


class ImageWrapperDataset(PartMixin, PreExtractedFeaturesMixin, AnnotationsReadMixin, IteratorMixin):
	pass

class Dataset(ImageWrapperDataset):

	def get_example(self, i):
		im_obj = super(Dataset, self).get_example(i)
		return im_obj.as_tuple()

__all__ = [
	"Dataset",
	"ImageWrapperDataset",

	### mixins ###
	"BaseMixin",
	# reading
	"AnnotationsReadMixin",
	"ImageListReadingMixin",

	# features
	"PreExtractedFeaturesMixin",

	# parts / bounding boxes
	"BBCropMixin",
	"BBoxMixin",
	"CroppedPartMixin",
	"MultiBoxMixin",
	"PartCropMixin",
	"PartMixin",
	"PartRevealMixin",
	"PartsInBBMixin",
	"RandomBlackOutMixin",
	"RevealedPartMixin",
	"UniformPartMixin",

	# transform mixin
	"TransformMixin",
]
