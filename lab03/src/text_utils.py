"""Utilities for cleaning and formatting text."""


def clean_name(raw):
    """Clean extra spaces and format name into title case."""
    return " ".join(raw.split()).title()
