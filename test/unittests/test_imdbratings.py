# pylint: disable=invalid-name,protected-access,too-many-lines
import os
import unittest
from pathlib import Path

from python.lib.tmdbscraper import imdbratings

TEST_FOLDER = Path(__file__).parent

END_TO_END = os.getenv('TEST_E2E', False)

class TestIMDBRatings(unittest.TestCase):
    def test_parse_imdb_page__goldenpath_2022_04(self):
        self.basetest_loadfilefile_imdb_page_goldenpath("imdb_2022-04.html", (1315176, 8.6, 27))

    def test_parse_imdb_page__goldenpath_2021_06(self):
        self.basetest_loadfilefile_imdb_page_goldenpath("imdb_2021-06.html", (1254540, 8.6, 25))

    def basetest_loadfilefile_imdb_page_goldenpath(self, filename, expected_output):
        with TEST_FOLDER.joinpath(filename).open() as file:
            input_model = file.read()

        actual_output = imdbratings._parse_imdb_result(input_model)
        self.assertEqual(expected_output, actual_output)


    def test_parse_imdb_page__error_return_Nones(self):
        input_model = ''
        expected_output = (None, None, None)

        actual_output = imdbratings._parse_imdb_result(input_model)

        self.assertEqual(expected_output, actual_output)

    def test_parse_imdb_page__changed_page_return_Nones(self):
        # region `input_model` changed IMDB page
        input_model = '''
<!DOCTYPE html>
<html
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///title/tt0076759?src=mdot">

        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>
</head></body>

    </body>
</html>
        '''
        # endregion
        expected_output = (None, None, None)

        actual_output = imdbratings._parse_imdb_result(input_model)

        self.assertEqual(expected_output, actual_output)


    def test_assemble_imdbresult(self):
        input_model = 1, 2, 3
        expected_output = {'info': {'top250': 3}, 'ratings': {'imdb': {'rating': 2, 'votes': 1}}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)


    def test_assemble_imdbresult__no_info_return_empty(self):
        input_model = None, None, None
        expected_output = {}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__no_top250_return_rating(self):
        input_model = 1, 2, None
        expected_output = {'ratings': {'imdb': {'rating': 2, 'votes': 1}}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__votes_no_rating_return_no_rating(self):
        input_model = 1, None, 3
        expected_output = {'info': {'top250': 3}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

    def test_assemble_imdbresult__rating_no_votes_return_no_rating(self):
        input_model = None, 2, 3
        expected_output = {'info': {'top250': 3}}

        actual_output = imdbratings._assemble_imdb_result(*input_model)

        self.assertDictEqual(expected_output, actual_output)

@unittest.skipUnless(END_TO_END, "e2e testing not enabled")
class TestIMDBRatings_E2E(unittest.TestCase):
    def test_e2e__imdb_page_goldenpath_rightnow(self):
        actual_output = imdbratings.get_details({'imdb': 'tt0076759'})

        self.assertIsInstance(actual_output['ratings']['imdb']['rating'], float)
        self.assertIsInstance(actual_output['ratings']['imdb']['votes'], int)
        self.assertIsInstance(actual_output['info']['top250'], int)
