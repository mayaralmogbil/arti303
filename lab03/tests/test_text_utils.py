"""Tests for text_utils module."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
sys.path.insert(0, os.path.abspath("src"))

import text_utils


def test_clean_name_whitespace():
    assert text_utils.clean_name("   sara   ali  ") == "Sara Ali"
    assert text_utils.clean_name("sara  ali") == "Sara Ali"


def test_clean_name_capitalisation():
    assert text_utils.clean_name("sara ali") == "Sara Ali"
    assert text_utils.clean_name("FAISAL ALHARBI") == "Faisal Alharbi"
