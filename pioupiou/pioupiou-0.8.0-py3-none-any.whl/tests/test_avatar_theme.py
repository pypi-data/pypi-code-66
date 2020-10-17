from PIL import Image

from pioupiou import AvatarTheme
from pioupiou import BaseLayer


class TestAvatarTheme(object):
    def test_avatar_theme__ok__nominal_case(self):
        layer1 = BaseLayer.create_layer_from_paths(
            level=0, name="star", image_variation_paths=["tests/test_img/black_background.png"]
        )
        layer2 = BaseLayer.create_layer_from_paths(
            level=1, name="star", image_variation_paths=["tests/test_img/white_alpha_star.png"]
        )

        avatar_theme = AvatarTheme(layers=[layer1, layer2])
        image = avatar_theme.generate_avatar("token")
        assert image.mode == "RGBA"

        avatar_theme.save_on_disk(image, "/tmp/test_avatar.png")

        with Image.open("/tmp/test_avatar.png") as avatar:
            assert avatar.height == 20
            assert avatar.width == 20
