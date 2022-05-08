# insert 2 records into the student TABLE
# (1, "Adam", "M", "Math") and (2, "Echo", "F", "Computer")

query = """
INSERT INTO student
VALUES
    (1, "Adam", "M", "Math"),
    (2, "Echo", "F", "Computer")
"""

# Do NOT change ------------------------
check = """
SELECT *
FROM student;
"""

from utils import *

cur, con = get_school_db_2()
cur.execute(query)
cur.execute(check)
print(cur.fetchall())
con.close()
