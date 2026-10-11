# Robust Contact Manager

## Purpose
This project is a command-line contact manager that can add, find, and delete contacts while handling common errors gracefully.

## Files
- `buggy_contacts.py`: the original starter code supplied for the assignment.
- `contact_manager.py`: the corrected application.
- `test_contact_manager.py`: automated unit tests using Python's `unittest` framework.

## Bugs and improvements
- Menu input is converted to an integer inside a `try/except ValueError` block, so letters and other non-integer input do not crash the program.
- `find_contact()` catches `KeyError` and prints `Contact not found.` when a contact does not exist.
- `delete_contact()` catches `KeyError` and prints `Contact not found.` when a contact does not exist.
- `DuplicateContactError` is a custom exception raised when a duplicate contact name is added. The menu catches it and displays an error message.
- Unit tests cover adding, finding, deleting, missing contacts, duplicate contacts, and invalid menu input.

## Requirements
Python 3.8 or newer.

## Run the program
Open a terminal in this folder and run:

```bash
python3 contact_manager.py
```

## Run the tests
From this folder, run:

```bash
python3 -m unittest test_contact_manager.py
```

All tests should pass. The test suite uses a clean contact dictionary before each test.

## GitHub repository
Create a public repository on GitHub and upload these three files: `buggy_contacts.py`, `contact_manager.py`, and `test_contact_manager.py`, plus this `README.md`.

## Screencast
Record a 3–5 minute video showing:
1. Adding a contact.
2. Finding an existing contact.
3. Searching for a missing contact.
4. Entering letters at the menu.
5. Trying to add a duplicate contact.
6. Deleting an existing contact and a missing contact.
7. Running `python3 -m unittest test_contact_manager.py` and showing the tests pass.
8. Briefly explaining `try/except`, `DuplicateContactError`, and `raise`.

Add your screencast link here after recording:

`Screencast link: [paste your video link here]`
