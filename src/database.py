import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def checkIfInitialized(self):
        """
        Check if the database has been initialized
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM sqlite_master WHERE type='table'
        ''')
        return self.cursor.fetchone()[0] > 0
    
    def checkIfAnyData(self):
        """
        Check if the database has any data
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM students
        ''')
        return self.cursor.fetchone()[0] > 0
    
    def initializeDB(self):
        """
        Initialize the database with the necessary tables

        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
            sid INTEGER PRIMARY KEY AUTOINCREMENT,
            class TEXT NOT NULL,
            class_number INTEGER NOT NULL,
            std_name TEXT NOT NULL,
            category TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            sid INTEGER NOT NULL,
            eid INTEGER NOT NULL,
            status TEXT DEFAULT '1',
            FOREIGN KEY (sid) REFERENCES students(sid),
            FOREIGN KEY (eid) REFERENCES event(eid)
            )
        ''')
        self.conn.commit()

    def findSid(self, class_name, class_number, std_name):
        """
        Find the student id given their class, class number and std_name
        """
        self.cursor.execute('''
            SELECT sid FROM students WHERE class = ? AND class_number = ? AND std_name = ?
        ''', (class_name, class_number, std_name))
        return self.cursor.fetchone()[0]
    
    def findEid(self, event_name):
        """
        Find the event id given their event_name
        """
        self.cursor.execute('''
            SELECT eid FROM events WHERE event_name = ?
        ''', (event_name,))
        return self.cursor.fetchone()[0]

    def addStudent(self, class_name, class_number, std_name, category):
        """
        Add a student to the database
        """
        self.cursor.execute('''
            INSERT INTO students (class, class_number, std_name, category) VALUES (?, ?, ?, ?)
        ''', (class_name, class_number, std_name, category))
        self.conn.commit()

    def addEvent(self, event_name):
        """
        Add an event to the database
        """
        self.cursor.execute('''
            INSERT INTO events (event_name) VALUES (?)
        ''', (event_name,))
        self.conn.commit()
    
    def addRecord(self, sid, eid, status='1'):
        """
        Add a record to the database
        """
        self.cursor.execute('''
            INSERT INTO records (sid, eid, status) VALUES (?, ?, ?)
        ''', (sid, eid, status))
        self.conn.commit()

    def addEventWithReturn(self, event_name):
        """
        Add an event to the database and return the event id
        """
        self.cursor.execute('''
            INSERT INTO events (event_name) VALUES (?)
        ''', (event_name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def getTotalNumberOfStudents(self):
        """
        Get the total number of students
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM students
        ''')
        return self.cursor.fetchone()[0]
    
    def getTotalNumberOfEvents(self):
        """
        Get the total number of events
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM events
        ''')
        return self.cursor.fetchone()[0]
    
    def getTotalNumberOfRecords(self):
        """
        Get the total number of records
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM records
        ''')
        return self.cursor.fetchone()[0]
    
    def getEvents(self):
        """
        Get the list of events
        """
        self.cursor.execute('''
            SELECT event_name FROM events
        ''')
        return self.cursor.fetchall()
    
    def getNumberOfParticipants(self, eid, category='all'):
        """
        Get the number of participants for an event
        if category is specified, get the number of participants for that category, otherwise get the total number of participants
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT COUNT(*) FROM records WHERE eid = ?
            ''', (eid,))
        else:
            self.cursor.execute('''
                SELECT COUNT(*) FROM records WHERE eid = ? AND sid IN (SELECT sid FROM students WHERE category = ?)
            ''', (eid, category))
        return self.cursor.fetchone()[0]
    
    def getStudentEventCounts(self, sid, category='all'):
        """
        Get the number of events a student has participated in along with their class, class number, and name.
        If category is specified, get the number of events for that category, otherwise get the total number of events.
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT COUNT(*), class, class_number, std_name 
                FROM records 
                JOIN students ON records.sid = students.sid 
                WHERE records.sid = ?
            ''', (sid,))
        else:
            self.cursor.execute('''
                SELECT COUNT(*), class, class_number, std_name 
                FROM records 
                JOIN students ON records.sid = students.sid 
                WHERE records.sid = ? AND eid IN (SELECT eid FROM events WHERE category = ?)
            ''', (sid, category))
        result = self.cursor.fetchone()
        return {
            "event_count": result[0],
            "class": result[1],
            "class_number": result[2],
            "name": result[3]
        }
    
    def getStudentsEventCounts(self, category='all'):
        """
        Get the number of events each student has participated in along with their class, class number, and name.
        If category is specified, get the number of events for that category, otherwise get the total number of events.
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT class, class_number, std_name, COUNT(*)
                FROM records 
                JOIN students ON records.sid = students.sid 
                GROUP BY records.sid
            ''')
        else:
            self.cursor.execute('''
                SELECT class, class_number, std_name, COUNT(*)
                FROM records 
                JOIN students ON records.sid = students.sid 
                WHERE eid IN (SELECT eid FROM events WHERE category = ?)
                GROUP BY records.sid
            ''', (category,))
        return self.cursor.fetchall()
    
    def getStudentsEventsParticipated(self, category='all'):
        """
        Get the list of students and the events they have participated in along with their class, class number, and name.
        If category is specified, get the list of events for that category, otherwise get the total list of events.
        Events for the same student will be grouped together in the event_name column, separated by commas.
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT class, class_number, std_name, GROUP_CONCAT(event_name, ', ') AS events
                FROM records 
                JOIN students ON records.sid = students.sid 
                JOIN events ON records.eid = events.eid
                GROUP BY class, class_number, std_name
            ''')
        else:
            self.cursor.execute('''
                SELECT class, class_number, std_name, GROUP_CONCAT(event_name, ', ') AS events
                FROM records 
                JOIN students ON records.sid = students.sid 
                JOIN events ON records.eid = events.eid 
                WHERE category = ?
                GROUP BY class, class_number, std_name
            ''', (category,))
        return self.cursor.fetchall()
    
    def getStudentEventList(self, sid, category='all'):
        """
        Get the list of events a student has participated in
        if category is specified, get the list of events for that category, otherwise get the total list of events
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT event_name FROM events WHERE eid IN (SELECT eid FROM records WHERE sid = ?)
            ''', (sid,))
        else:
            self.cursor.execute('''
                SELECT event_name FROM events WHERE eid IN (SELECT eid FROM records WHERE sid = ?) AND category = ?
            ''', (sid, category))
        return self.cursor.fetchall()
    
    def getStudentEventTable(self, category='all'):
        """
        Get the list of events and the number of students participated in each event
        if category is specified, get the list of events for that status, otherwise get the total list of events
        """
        if category == 'all':
            self.cursor.execute('''
                SELECT event_name, COUNT(sid) FROM events LEFT JOIN records ON events.eid = records.eid GROUP BY event_name
            ''')
        else:
            self.cursor.execute('''
                SELECT event_name, COUNT(records.sid) FROM events 
                LEFT JOIN records ON events.eid = records.eid 
                LEFT JOIN students ON records.sid = students.sid
                WHERE category = ? 
                GROUP BY event_name
            ''', (category,))
        return self.cursor.fetchall()
    
    def getEventParticipantWithNames(self, category='all'):
        """
        Get the list of events and the number of students participated in each event along with their names
        if category is specified, get the list of events for that category, otherwise get the total list of events
        """
        if category == 'all':
            self.cursor.execute('''
            SELECT event_name, GROUP_CONCAT(std_name, ', ') AS student_names 
            FROM events 
            LEFT JOIN records ON events.eid = records.eid 
            LEFT JOIN students ON records.sid = students.sid 
            GROUP BY event_name
            ''')
        else:
            self.cursor.execute('''
            SELECT event_name, GROUP_CONCAT(std_name, ', ') AS student_names 
            FROM events 
            LEFT JOIN records ON events.eid = records.eid 
            LEFT JOIN students ON records.sid = students.sid
            WHERE category = ? 
            GROUP BY event_name
            ''', (category,))
        return self.cursor.fetchall()
    
    def getStudentsByForm(self, form):
        """
        Get the list of students given their form
        As example, student with class 1A, 1B, 1C, 1D are all in the same form, as their class start with 1, which represent Form 1
        And student with class 2A, 2B, 2C, 2D are all in the same form, e.t.c. 
        """
        self.cursor.execute('''
            SELECT * FROM students WHERE class LIKE ?
        ''', (form + '%',))
        return self.cursor.fetchall()
    
    def isEventExists(self, event_name):
        """
        Check if the event exists in the database
        """
        self.cursor.execute('''
            SELECT COUNT(*) FROM events WHERE event_name = ?
        ''', (event_name,))
        return self.cursor.fetchone()[0] > 0
    
    def getAllStudents(self):
        """
        Get all students in the database
        """
        self.cursor.execute('''
            SELECT class, class_number, std_name, category FROM students
        ''')
        return self.cursor.fetchall()
    
    def getAllEvents(self):
        """
        Get all events in the database
        """
        self.cursor.execute('''
            SELECT event_name FROM events
        ''')
        return self.cursor.fetchall()