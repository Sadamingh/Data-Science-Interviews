# Create a faculty table in the current database with fid (int),
# fname (string), department (string)
# primary key: fid
# foreign key: department refer to the column in student table

query = """
CREATE TABLE IF NOT EXISTS faculty (
    fid NUMBER(5),
    fname VARCHAR(20),
    department VARCHAR(20),
    PRIMARY KEY (fid),
    FOREIGN KEY (department) REFERENCES student (department)
);
"""

# Do NOT change ------------------------
check = """
SELECT name
FROM sqlite_master;
"""

from utils import *

cur, con = get_school_db_2()
cur.execute(query)
cur.execute(check)
print(cur.fetchall())
con.close()
