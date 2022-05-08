# Create student table in the current database with sid (int),
# sname (string), gender (character), department (string)

query = """
CREATE TABLE IF NOT EXISTS student (
    sid NUMBER(5),
    sname VARCHAR(20),
    gender CHAR,
    department VARCHAR(20)
);
"""

# Do NOT change ------------------------
check = """
SELECT name FROM sqlite_master
WHERE type='table';
"""

from utils import *

cur, con = get_school_db()
cur.execute(query)
cur.execute(check)
print(cur.fetchall())
con.close()
