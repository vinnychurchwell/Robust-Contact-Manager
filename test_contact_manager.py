"""Unit tests for the Robust Contact Manager."""

import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

import contact_manager


class TestContactManager(unittest.TestCase):
    """Test adding, finding, deleting, and error handling for contacts."""

    def setUp(self):
        """Start each test with a clean contact dictionary."""
        contact_manager.contacts.clear()

    def test_add_new_contact(self):
        """A new contact should be stored in the dictionary."""
        with redirect_stdout(StringIO()):
            contact_manager.add_contact("Alice", "555-1234")
        self.assertEqual(contact_manager.contacts["Alice"], "555-1234")

    def test_find_existing_contact_returns_phone(self):
        """Finding an existing contact should return its phone number."""
        contact_manager.contacts["Alice"] = "555-1234"
        output = StringIO()
        with redirect_stdout(output):
            result = contact_manager.find_contact("Alice")
        self.assertEqual(result, "555-1234")
        self.assertIn("Alice: 555-1234", output.getvalue())

    def test_find_missing_contact_does_not_crash(self):
        """A missing contact should return None and print a friendly message."""
        output = StringIO()
        with redirect_stdout(output):
            result = contact_manager.find_contact("Diana")
        self.assertIsNone(result)
        self.assertIn("Contact not found.", output.getvalue())

    def test_delete_existing_contact(self):
        """Deleting an existing contact should remove it from the dictionary."""
        contact_manager.contacts["Bob"] = "555-5678"
        output = StringIO()
        with redirect_stdout(output):
            result = contact_manager.delete_contact("Bob")
        self.assertTrue(result)
        self.assertNotIn("Bob", contact_manager.contacts)
        self.assertIn("Deleted Bob.", output.getvalue())

    def test_delete_missing_contact_does_not_crash(self):
        """Deleting a missing contact should return False and print a message."""
        output = StringIO()
        with redirect_stdout(output):
            result = contact_manager.delete_contact("Ethan")
        self.assertFalse(result)
        self.assertIn("Contact not found.", output.getvalue())

    def test_add_duplicate_contact_raises_custom_exception(self):
        """Adding an existing name should raise DuplicateContactError."""
        contact_manager.contacts["Alice"] = "555-1234"
        with self.assertRaises(contact_manager.DuplicateContactError):
            contact_manager.add_contact("Alice", "555-9999")

    def test_menu_rejects_non_integer_input(self):
        """A letter at the menu should show an error instead of crashing."""
        inputs = ["hello", "4"]
        output = StringIO()
        with patch("builtins.input", side_effect=inputs):
            with redirect_stdout(output):
                contact_manager.main()
        self.assertIn("Invalid input. Please enter a number from 1 to 4.", output.getvalue())
        self.assertIn("Goodbye!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
