"""Module for converting GPA to letter grade."""


def letter_grade(gpa):
    """Convert a numeric GPA on a 5.00 scale to a letter grade."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
