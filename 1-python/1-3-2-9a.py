import pytest 
# write code
# use these string functions 
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# text = "Hello, World!   "
# text2 = text # save original text for comparison
# for char in ["!", ",", "?", "."]:
#     text2 = text2.replace(char, "")

# text3 = text2.strip()  # remove leading and trailing whitespace
# text4 = text3.lower()  # convert to lowercase

# print(text)
# print(text2)
# print(text3)
# print(text4)

# rewrite as function
def clean_text(text:str) -> str:
    '''
    Function to clean text by removing punctuation: "?!,." 
    stripping whitespace, and converting to lowercase.
    '''
    text2 = text
    for char in ["!", ",", "?", "."]:
        text2 = text2.replace(char, "")
    text3 = text2.strip()
    text4 = text3.lower()
    return text4


# write a pytest function to test the clean_text function
def test_clean_text():
    assert clean_text("Hello, World!   ") == "hello world"
    assert clean_text("   This is a test.   ") == "this is a test"
    assert clean_text("No punctuation here") == "no punctuation here"
    assert clean_text("Multiple!!! Punctuation???") == "multiple punctuation"
    assert clean_text("   Leading and trailing spaces   ") == "leading and trailing spaces"
    assert clean_text("") == ""
    assert clean_text("   ") == ""
    assert clean_text("UPPCASE TO LOWERCASE") == "Uppcase to lowercase"


test_clean_text()