import tempfile
import unittest
from pathlib import Path
from profiles import detect_profile, PROFILE_GUIDES


class ProfileTests(unittest.TestCase):
    def test_flutter_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'pubspec.yaml').write_text('dependencies:\n  flutter:\n    sdk: flutter\n')
            self.assertEqual(detect_profile(root), 'flutter')

    def test_regular_dart_does_not_select_flutter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'pubspec.yaml').write_text('name: dart_server\n')
            self.assertEqual(detect_profile(root), 'fullstack')

    def test_guides_cover_distinct_areas(self):
        self.assertIn('migrations', PROFILE_GUIDES['fullstack'])
        self.assertIn('widget', PROFILE_GUIDES['flutter'])


if __name__ == '__main__':
    unittest.main()
