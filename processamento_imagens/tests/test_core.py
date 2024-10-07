# test_core.py
import unittest
from image_processor.core import load_image, resize_image

class TestImageProcessor(unittest.TestCase):
    
    def test_load_image(self):
        image = load_image("test_image.jpg")
        self.assertIsNotNone(image)

    def test_resize_image(self):
        image = load_image("test_image.jpg")
        resized_image = resize_image(image, (100, 100))
        self.assertEqual(resized_image.size, (100, 100))

if __name__ == '__main__':
    unittest.main()
