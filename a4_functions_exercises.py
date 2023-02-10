"""
Python Exercises: functions - see note below
Keith Stateson

Note: this py file is for import use only for the next exercise - imports.
The full exercise is found in the .ipynb jupyter notebook/jupyter lab, as python doesn't import jupyter files
"""

# ------------------------------------------------------------------------------------

# 2.
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(var):
    return bool(len(var) == 1 and var in "AEIOUaeiou")

# ------------------------------------------------------------------------------------

# 5.
# Define a function named calculate_tip. It should accept a tip percentage
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    if tip_percentage == 0:
        return f"$0"
    else:
        return f"${tip_percentage * bill_total:,.2f}"

# ------------------------------------------------------------------------------------

# 8.
# Define a function named get_letter_grade. It should accept a number
# and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'
    else:
        return 'F'
