import os

from parameterized import parameterized
from dotenv import load_dotenv
import unittest
from yadisk_api import YaDisk

class TestFunctions(unittest.TestCase):

    @parameterized.expand(
        [
            ("folder_1", 201),
            ("folder_2", 201),
            ("folder_3", 201)
        ]
    )
    def test_create_folder(self, folder_mame, result):
        load_dotenv()

        yad_token = os.environ.get('YADISK_TOKEN')
        ya_disk = YaDisk(yad_token)

        # Предварительно удаляем каталог, иначе будет 409 отдавать
        # я бы это вынес в setUp, но не нашел как там параметры текущего теста получить
        ya_disk.delete_folder(folder_mame)

        code = ya_disk.create_folder(folder_mame)
        self.assertEqual(code, result)

    @parameterized.expand(
        [
            ("fol/der_1", 201),
            ("fol/der_2", 201),
            ("fol/der_3", 201)
        ]
    )
    @unittest.expectedFailure
    def test_error_create_folder(self, folder_mame, result):
        load_dotenv()

        yad_token = os.environ.get('YADISK_TOKEN')
        ya_disk = YaDisk(yad_token)

        # Предварительно удаляем каталог, иначе будет 409 отдавать
        # я бы это вынес в setUp, но не нашел как там параметры текущего теста получить
        ya_disk.delete_folder(folder_mame)

        code = ya_disk.create_folder(folder_mame)
        self.assertEqual(code, result)