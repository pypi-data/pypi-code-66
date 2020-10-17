import pytest

from pioupiou import BaseLayer
from pioupiou.exceptions import ImageGivenShouldHaveAlphaLayer


class TestLayer(object):
    def test_unit__layer__ok__nominal_case(self):
        layer = BaseLayer.create_layer_from_paths(
            level=0, name="star", image_variation_paths=["tests/test_img/white_alpha_star.png"]
        )
        image = layer.get_random_image(allow_no_alpha_layer=False)
        assert image.format == "PNG"
        assert image.mode == "RGBA"

    def test_unit__layer__err__image_should_have_alpha_layer(self):
        layer = BaseLayer.create_layer_from_paths(
            level=0, name="star", image_variation_paths=["tests/test_img/black_background.png"]
        )
        with pytest.raises(ImageGivenShouldHaveAlphaLayer):
            layer.get_random_image(allow_no_alpha_layer=False)

    def test_unit__layer__err__ok__allow_alpha_laver(self):
        layer = BaseLayer.create_layer_from_paths(
            level=0, name="star", image_variation_paths=["tests/test_img/black_background.png"]
        )
        image = layer.get_random_image(allow_no_alpha_layer=True)
        assert image.mode == "RGBA"
