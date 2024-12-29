#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute SELECT query with parameterized query
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """, (sys.argv[4],))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print results as comma-separated string
    print(", ".join([row[0] for row in rows]))

    # Close cursor and database connection
    cursor.close()
    db.close()
