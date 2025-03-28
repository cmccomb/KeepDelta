import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestReservedNamesBool(unittest.TestCase):

    def test_change_type_from_conflict_to_normal(self):
        """
        Change a conflicting variable to a normal variable with type change.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = conflict
            new = True
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_normal_to_conflict(self):
        """
        Change a normal variable to a conflicting variable with type change.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = True
            new = conflict
            with self.assertRaises(ValueError):
                kd.create(old, new)


if __name__ == "__main__":
    unittest.main()
