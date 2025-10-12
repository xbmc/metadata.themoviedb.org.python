import unittest
from python.lib.tmdbscraper.tmdb import _build_fanart_list, _build_image_list

class TestBuildImageList(unittest.TestCase):
    def setUp(self):
        self.urlbases = {
            'original': 'o',
            'preview': 'p'
        }

    def test_build_image_list_no_language_filter(self):
        imagelist = [
            {'file_path': '/img1.jpg', 'iso_639_1': 'en'},
            {'file_path': '/img2.jpg', 'iso_639_1': 'fr'}
        ]
        result = _build_image_list(imagelist, self.urlbases)

        self.assertEqual(len(result), 2)

    def test_build_image_list_with_language_filter(self):
        imagelist = [
            {'file_path': '/img1.jpg', 'iso_639_1': 'en'},
            {'file_path': '/img2.jpg', 'iso_639_1': 'fr'}
        ]
        result = _build_image_list(imagelist, self.urlbases, ['fr'])

        self.assertEqual(len(result), 1)

    def test_build_fanart_list_from_language_none(self):
        imagelist = [
            {'file_path': '/img1.jpg', 'iso_639_1': None},
            {'file_path': '/img3.jpg', 'iso_639_1': 'en'}
        ]
        result = _build_fanart_list(imagelist, self.urlbases)

        self.assertEqual(len(result), 1)

    def test_build_fanart_list_from_language_xx(self):
        imagelist = [
            {'file_path': '/img1.jpg', 'iso_639_1': 'xx'},
            {'file_path': '/img3.jpg', 'iso_639_1': 'en'}
        ]
        result = _build_fanart_list(imagelist, self.urlbases)

        self.assertEqual(len(result), 1)
