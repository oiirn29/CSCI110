import sys

def replace (s, old, new):
    first = s.split(old)
    glue = new
    glue = new.join(first)
    return glue



def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():               #defines test suite 

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"           #defines S

    test(replace("Mississippi", "i", "I") == "MIssIssIppI")         #pass tests

    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")           #pass tests

    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite back. pain, spam, yum!")         #fail test

test_suite()