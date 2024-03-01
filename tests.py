import src.sampleReddit.sampleReddit as sr

import pytest

class TestCheckLanguage:

    # Returns the comment if it's in English and has more than one word.
    def test_returns_comment_if_english_and_more_than_one_word(self):
        # Arrange
        comment = "This is an English comment"
    
        # Act
        result = sr.check_language(comment)
    
        # Assert
        assert result == comment

    # Returns None if the comment is not in English.
    def test_returns_none_if_comment_not_in_english(self):
        # Arrange
        comment = "Este es un comentario en español"
    
        # Act
        result = sr.check_language(comment)
    
        # Assert
        assert result is None