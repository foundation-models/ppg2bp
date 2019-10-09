from unittest import TestCase
from focus_group import FocusGroup


class TestFocusGroup(TestCase):

    def test_init(self):
        focus_group = FocusGroup()
        print(focus_group.df.head())
        print(focus_group.diastolic)
