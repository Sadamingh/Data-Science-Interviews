# Create student table in the current database with sid (int),
# sname (string), gender (character), department (string)
# primary key: sid and sname

query = """
CREATE TABLE IF NOT EXISTS student (
    sid NUMBER(5),
    sname VARCHAR(20),
    gender CHAR,
    department VARCHAR(20),
    PRIMARY KEY (sid, sname)
);
"""

# Do NOT change ------------------------
check = """
SELECT name
FROM sqlite_master;
"""

from utils import *

cur, con = get_school_db()
cur.execute(query)
cur.execute(check)
print(cur.fetchall())
con.close()
