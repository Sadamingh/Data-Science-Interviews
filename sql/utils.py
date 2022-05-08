import sqlite3

def get_school_db():
    con = sqlite3.connect('/tmp/school.db')
    cur = con.cursor()
    return cur, con

def get_school_db_2():
    con = sqlite3.connect('/tmp/school.db')
    cur = con.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS student (
        sid NUMBER(5),
        sname VARCHAR(20),
        gender CHAR,
        department VARCHAR(20),
        PRIMARY KEY (sid, sname)
    );
    """
    cur.execute(query)

    return cur, con

con = sqlite3.connect('/tmp/school.db')
con.close()

def get_school_db_3():
    con = sqlite3.connect('/tmp/school.db')
    cur = con.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS student (
        sid NUMBER(5),
        sname VARCHAR(20),
        gender CHAR,
        department VARCHAR(20),
        PRIMARY KEY (sid, sname)
    );
    """
    cur.execute(query)
    query = """
    CREATE TABLE IF NOT EXISTS faculty (
        fid NUMBER(5),
        fname VARCHAR(20),
        department VARCHAR(20),
        PRIMARY KEY (fid),
        FOREIGN KEY (department) REFERENCES student (department)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """
    cur.execute(query)

    return cur, con

con = sqlite3.connect('/tmp/school.db')
con.close()
