from os import path

from pupy import sstr
from pupy.fmt import filesize
from pupy.fmt import nseconds
from pupy.fmt import strip_comments
from pupy.fmt import term_table

TOP_BABY_NAMES = [
    "Aaliyah",
    "Aaron",
    "Abigail",
    "Adam",
    "Addison",
    "Adeline",
    "Adrian",
    "Aiden",
    "Alexa",
    "Alexander",
    "Alice",
    "Allison",
    "Amelia",
    "Andrew",
    "Angel",
    "Anna",
    "Anthony",
    "Aria",
    "Ariana",
    "Arianna",
    "Asher",
    "Aubree",
    "Aubrey",
    "Audrey",
    "Aurora",
    "Austin",
    "Autumn",
    "Ava",
    "Avery",
    "Ayden",
    "Bella",
    "Benjamin",
    "Brayden",
    "Brooklyn",
    "Bryson",
    "Caleb",
    "Cameron",
    "Camila",
    "Caroline",
    "Carson",
    "Carter",
    "Charles",
    "Charlotte",
    "Chase",
    "Chloe",
    "Christian",
    "Christopher",
    "Claire",
    "Clara",
    "Colton",
    "Connor",
    "Cooper",
    "Cora",
    "Daniel",
    "David",
    "Dominic",
    "Dylan",
    "Easton",
    "Eleanor",
    "Elena",
    "Eli",
    "Eliana",
    "Elias",
    "Elijah",
    "Elizabeth",
    "Ella",
    "Ellie",
    "Emilia",
    "Emily",
    "Emma",
    "Ethan",
    "Eva",
    "Evan",
    "Evelyn",
    "Everly",
    "Ezekiel",
    "Ezra",
    "Gabriel",
    "Gabriella",
    "Gavin",
    "Genesis",
    "Gianna",
    "Grace",
    "Grayson",
    "Greyson",
    "Hailey",
    "Hannah",
    "Harper",
    "Hazel",
    "Henry",
    "Hudson",
    "Hunter",
    "Ian",
    "Isaac",
    "Isabella",
    "Isabelle",
    "Isaiah",
    "Jace",
    "Jack",
    "Jackson",
    "Jacob",
    "James",
    "Jameson",
    "Jason",
    "Jaxon",
    "Jaxson",
    "Jayden",
    "Jeremiah",
    "John",
    "Jonathan",
    "Jordan",
    "Jose",
    "Joseph",
    "Joshua",
    "Josiah",
    "Julia",
    "Julian",
    "Kayden",
    "Kaylee",
    "Kennedy",
    "Kinsley",
    "Landon",
    "Layla",
    "Leah",
    "Leo",
    "Leonardo",
    "Levi",
    "Liam",
    "Lillian",
    "Lily",
    "Lincoln",
    "Logan",
    "Lucas",
    "Lucy",
    "Luke",
    "Luna",
    "Lydia",
    "Mackenzie",
    "Madeline",
    "Madelyn",
    "Madison",
    "Mason",
    "Mateo",
    "Matthew",
    "Maverick",
    "Maya",
    "Melanie",
    "Mia",
    "Michael",
    "Mila",
    "Naomi",
    "Natalie",
    "Nathan",
    "Nevaeh",
    "Nicholas",
    "Noah",
    "Nolan",
    "Nora",
    "Nova",
    "Oliver",
    "Olivia",
    "Owen",
    "Paisley",
    "Parker",
    "Penelope",
    "Peyton",
    "Piper",
    "Quinn",
    "Reagan",
    "Riley",
    "Robert",
    "Roman",
    "Ruby",
    "Ryan",
    "Sadie",
    "Samantha",
    "Samuel",
    "Santiago",
    "Sarah",
    "Savannah",
    "Sawyer",
    "Scarlett",
    "Sebastian",
    "Serenity",
    "Skylar",
    "Sofia",
    "Sophia",
    "Stella",
    "Theodore",
    "Thomas",
    "Valentina",
    "Victoria",
    "Violet",
    "Vivian",
    "William",
    "Willow",
    "Wyatt",
    "Xavier",
    "Zoe",
    "Zoey",
]


def test_term_table_col_wise_1():
    expected = [
        "Aaliyah",
        "Carter",
        "Genesis",
        "Kinsley",
        "Olivia",
        "Aaron",
        "Charles",
        "Gianna",
        "Landon",
        "Owen",
        "Abigail",
        "Charlotte",
        "Grace",
        "Layla",
        "Paisley",
        "Adam",
        "Chase",
        "Grayson",
        "Leah",
        "Parker",
        "Addison",
        "Chloe",
        "Greyson",
        "Leo",
        "Penelope",
        "Adeline",
        "Christian",
        "Hailey",
        "Leonardo",
        "Peyton",
        "Adrian",
        "Christopher",
        "Hannah",
        "Levi",
        "Piper",
        "Aiden",
        "Claire",
        "Harper",
        "Liam",
        "Quinn",
        "Alexa",
        "Clara",
        "Hazel",
        "Lillian",
        "Reagan",
        "Alexander",
        "Colton",
        "Henry",
        "Lily",
        "Riley",
        "Alice",
        "Connor",
        "Hudson",
        "Lincoln",
        "Robert",
        "Allison",
        "Cooper",
        "Hunter",
        "Logan",
        "Roman",
        "Amelia",
        "Cora",
        "Ian",
        "Lucas",
        "Ruby",
        "Andrew",
        "Daniel",
        "Isaac",
        "Lucy",
        "Ryan",
        "Angel",
        "David",
        "Isabella",
        "Luke",
        "Sadie",
        "Anna",
        "Dominic",
        "Isabelle",
        "Luna",
        "Samantha",
        "Anthony",
        "Dylan",
        "Isaiah",
        "Lydia",
        "Samuel",
        "Aria",
        "Easton",
        "Jace",
        "Mackenzie",
        "Santiago",
        "Ariana",
        "Eleanor",
        "Jack",
        "Madeline",
        "Sarah",
        "Arianna",
        "Elena",
        "Jackson",
        "Madelyn",
        "Savannah",
        "Asher",
        "Eli",
        "Jacob",
        "Madison",
        "Sawyer",
        "Aubree",
        "Eliana",
        "James",
        "Mason",
        "Scarlett",
        "Aubrey",
        "Elias",
        "Jameson",
        "Mateo",
        "Sebastian",
        "Audrey",
        "Elijah",
        "Jason",
        "Matthew",
        "Serenity",
        "Aurora",
        "Elizabeth",
        "Jaxon",
        "Maverick",
        "Skylar",
        "Austin",
        "Ella",
        "Jaxson",
        "Maya",
        "Sofia",
        "Autumn",
        "Ellie",
        "Jayden",
        "Melanie",
        "Sophia",
        "Ava",
        "Emilia",
        "Jeremiah",
        "Mia",
        "Stella",
        "Avery",
        "Emily",
        "John",
        "Michael",
        "Theodore",
        "Ayden",
        "Emma",
        "Jonathan",
        "Mila",
        "Thomas",
        "Bella",
        "Ethan",
        "Jordan",
        "Naomi",
        "Valentina",
        "Benjamin",
        "Eva",
        "Jose",
        "Natalie",
        "Victoria",
        "Brayden",
        "Evan",
        "Joseph",
        "Nathan",
        "Violet",
        "Brooklyn",
        "Evelyn",
        "Joshua",
        "Nevaeh",
        "Vivian",
        "Bryson",
        "Everly",
        "Josiah",
        "Nicholas",
        "William",
        "Caleb",
        "Ezekiel",
        "Julia",
        "Noah",
        "Willow",
        "Cameron",
        "Ezra",
        "Julian",
        "Nolan",
        "Wyatt",
        "Camila",
        "Gabriel",
        "Kayden",
        "Nora",
        "Xavier",
        "Caroline",
        "Gabriella",
        "Kaylee",
        "Nova",
        "Zoe",
        "Carson",
        "Gavin",
        "Kennedy",
        "Oliver",
        "Zoey",
    ]
    line_vals = []
    for l in term_table(TOP_BABY_NAMES, row_wise=False):
        line_vals.extend(s for s in l.split(" ") if s != "~" and s != "")
    assert expected == line_vals


def test_term_table_row_wise_1():
    expected = [
        "Aaliyah",
        "Aaron",
        "Abigail",
        "Adam",
        "Addison",
        "Adeline",
        "Adrian",
        "Aiden",
        "Alexa",
        "Alexander",
        "Alice",
        "Allison",
        "Amelia",
        "Andrew",
        "Angel",
        "Anna",
        "Anthony",
        "Aria",
        "Ariana",
        "Arianna",
        "Asher",
        "Aubree",
        "Aubrey",
        "Audrey",
        "Aurora",
        "Austin",
        "Autumn",
        "Ava",
        "Avery",
        "Ayden",
        "Bella",
        "Benjamin",
        "Brayden",
        "Brooklyn",
        "Bryson",
        "Caleb",
        "Cameron",
        "Camila",
        "Caroline",
        "Carson",
        "Carter",
        "Charles",
        "Charlotte",
        "Chase",
        "Chloe",
        "Christian",
        "Christopher",
        "Claire",
        "Clara",
        "Colton",
        "Connor",
        "Cooper",
        "Cora",
        "Daniel",
        "David",
        "Dominic",
        "Dylan",
        "Easton",
        "Eleanor",
        "Elena",
        "Eli",
        "Eliana",
        "Elias",
        "Elijah",
        "Elizabeth",
        "Ella",
        "Ellie",
        "Emilia",
        "Emily",
        "Emma",
        "Ethan",
        "Eva",
        "Evan",
        "Evelyn",
        "Everly",
        "Ezekiel",
        "Ezra",
        "Gabriel",
        "Gabriella",
        "Gavin",
        "Genesis",
        "Gianna",
        "Grace",
        "Grayson",
        "Greyson",
        "Hailey",
        "Hannah",
        "Harper",
        "Hazel",
        "Henry",
        "Hudson",
        "Hunter",
        "Ian",
        "Isaac",
        "Isabella",
        "Isabelle",
        "Isaiah",
        "Jace",
        "Jack",
        "Jackson",
        "Jacob",
        "James",
        "Jameson",
        "Jason",
        "Jaxon",
        "Jaxson",
        "Jayden",
        "Jeremiah",
        "John",
        "Jonathan",
        "Jordan",
        "Jose",
        "Joseph",
        "Joshua",
        "Josiah",
        "Julia",
        "Julian",
        "Kayden",
        "Kaylee",
        "Kennedy",
        "Kinsley",
        "Landon",
        "Layla",
        "Leah",
        "Leo",
        "Leonardo",
        "Levi",
        "Liam",
        "Lillian",
        "Lily",
        "Lincoln",
        "Logan",
        "Lucas",
        "Lucy",
        "Luke",
        "Luna",
        "Lydia",
        "Mackenzie",
        "Madeline",
        "Madelyn",
        "Madison",
        "Mason",
        "Mateo",
        "Matthew",
        "Maverick",
        "Maya",
        "Melanie",
        "Mia",
        "Michael",
        "Mila",
        "Naomi",
        "Natalie",
        "Nathan",
        "Nevaeh",
        "Nicholas",
        "Noah",
        "Nolan",
        "Nora",
        "Nova",
        "Oliver",
        "Olivia",
        "Owen",
        "Paisley",
        "Parker",
        "Penelope",
        "Peyton",
        "Piper",
        "Quinn",
        "Reagan",
        "Riley",
        "Robert",
        "Roman",
        "Ruby",
        "Ryan",
        "Sadie",
        "Samantha",
        "Samuel",
        "Santiago",
        "Sarah",
        "Savannah",
        "Sawyer",
        "Scarlett",
        "Sebastian",
        "Serenity",
        "Skylar",
        "Sofia",
        "Sophia",
        "Stella",
        "Theodore",
        "Thomas",
        "Valentina",
        "Victoria",
        "Violet",
        "Vivian",
        "William",
        "Willow",
        "Wyatt",
        "Xavier",
        "Zoe",
        "Zoey",
    ]
    line_vals = []
    for l in term_table(TOP_BABY_NAMES, row_wise=True):
        line_vals.extend(s for s in l.split(" ") if s != "~" and s != "")
    assert line_vals == expected


def test_term_table_row_wise_2():
    expected = [
        "Aaliyah",
        "Aaron",
        "Abigail",
        "Adam",
        "Addison",
        "Adeline",
        "Adrian",
        "Aiden",
        "Alexa",
        "Alexander",
        "Alice",
        "Allison",
        "Amelia",
        "Andrew",
        "Angel",
        "Anna",
        "Anthony",
        "Aria",
        "Ariana",
        "Arianna",
        "Asher",
        "Aubree",
        "Aubrey",
        "Audrey",
        "Aurora",
        "Austin",
        "Autumn",
        "Ava",
        "Avery",
        "Ayden",
        "Bella",
        "Benjamin",
        "Brayden",
        "Brooklyn",
        "Bryson",
        "Caleb",
        "Cameron",
    ]
    line_vals = []
    for l in term_table(TOP_BABY_NAMES[:37], row_wise=True):
        line_vals.extend(s for s in l.split(" ") if s != "~" and s != "")
    assert expected == line_vals


def test_term_table_col_wise_2():
    expected = [
        "Aaliyah",
        "Alexa",
        "Anthony",
        "Aurora",
        "Brayden",
        "Aaron",
        "Alexander",
        "Aria",
        "Austin",
        "Brooklyn",
        "Abigail",
        "Alice",
        "Ariana",
        "Autumn",
        "Bryson",
        "Adam",
        "Allison",
        "Arianna",
        "Ava",
        "Caleb",
        "Addison",
        "Amelia",
        "Asher",
        "Avery",
        "Cameron",
        "Adeline",
        "Andrew",
        "Aubree",
        "Ayden",
        "Adrian",
        "Angel",
        "Aubrey",
        "Bella",
        "Aiden",
        "Anna",
        "Audrey",
        "Benjamin",
    ]
    line_vals = []
    for l in term_table(TOP_BABY_NAMES[:37], row_wise=False):
        line_vals.extend(s for s in l.split(" ") if s != "~" and s != "")
    assert line_vals == expected


def test_ftime_0seconds():
    """

    """
    ti = 5.4321
    tf = 5.4321
    assert nseconds(ti, tf) == "0 sec"


def test_ftime_seconds():
    """

    """
    ti = 1.2345
    tf = 5.4321
    assert nseconds(ti, tf) == "4.198 sec"


def test_ftime_milliseconds():
    """

    """
    ti = 1.2345 * (10 ** (-3))
    tf = 5.4321 * (10 ** (-3))
    assert nseconds(ti, tf) == "4.198 ms"


def test_ftime_microseconds():
    """

    """
    ti = 1.2345 * (10 ** (-6))
    tf = 5.4321 * (10 ** (-6))
    assert nseconds(ti, tf) == "4.198 μs"


def test_ftime_nanoseconds():
    """

    """
    ti = 1.2345 * (10 ** (-9))
    tf = 5.4321 * (10 ** (-9))
    assert nseconds(ti, tf) == "4.198 ns"


def test_filesize(tmpdir):
    """

    """
    filepath = path.join(tmpdir, "somefile.txt")
    sstr(path.join(tmpdir, "somefile.txt"), "12342312312")
    assert filesize(filepath) == "11.0 bytes"


something = """
# this func does a thing
def thisfunc():
    pass # and here we have a comment
# another comment

a = 2.3+4
b = 'pood'

"""
something_no_comments: str = """

def thisfunc():
    pass 


a = 2.3+4
b = 'pood'
"""


def test_strip_comments():
    no_comments = strip_comments(something)
    assert no_comments == something_no_comments
