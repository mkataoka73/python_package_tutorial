import re

class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = str(content)

    def processed_content(self):
        """Process content for palindrome testing."""
        return self.letters_and_digits().lower()

    def letters_and_digits(self):
        """Return the letters and digits in the content."""
        return "".join(re.findall(r"[a-zA-Z\d]", self.content))

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self.processed_content() == reverse(self.processed_content())


    def louder(self):
        """Make the phrase LOUDER."""
        processed_content = self.content.upper()
        return processed_content

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self

    def __next__(self):
        return next(self.phrase_iterator)

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))