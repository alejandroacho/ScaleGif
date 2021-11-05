import os
import shutil
from PIL import Image

from scale_gif import scale_gif

def test_scale_gif():
    # Copy the test gif
    path = os.path.abspath(os.getcwd())
    shutil.copy(f"{path}/gif.gif",
                f"{path}/copy_test_gif.gif")

    # Test that the original size is 1980x1080
    gif = Image.open(f"{path}/copy_test_gif.gif")
    assert gif.size == (1980, 1080)

    # Test that after the scale the gif size is according the scale
    scale_gif(f"{path}/copy_test_gif.gif", (353, 192))
    gif = Image.open(f"{path}/copy_test_gif.gif")
    assert gif.size == (352, 192)

    # Remove the copy
    os.remove(f"{path}/copy_test_gif.gif")