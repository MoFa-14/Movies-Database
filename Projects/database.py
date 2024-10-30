# Importing the random module to generate random numbers
import random
# Importing the pandas module and aliasing it as pd for ease of use
import pandas as pd
# Importing the mysql.connector module to connect to the MySQL database
import mysql.connector
# Importing the Error class from mysql.connector module to handle errors
from mysql.connector import Error

# Function to generate a unique mID
def generate_mID(cursor):
    # Infinite loop to generate a unique mID
    while True:
        # Generate a random mID between 10000 and 99999
        mID = random.randint(10000, 99999)
        # Check if the generated mID already exists in the movie_name table
        cursor.execute("SELECT mID FROM movie_name WHERE mID = %s", (mID,))
        # If mID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return mID

# Function to generate a unique cID
def generate_cID(cursor):
    # Infinite loop to generate a unique cID
    while True:
        # Generate a random cID between 10000 and 99999
        cID = random.randint(10000, 99999)
        # Check if the generated cID already exists in the movie_company table
        cursor.execute("SELECT cID FROM movie_company WHERE cID = %s", (cID,))
        # If cID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return cID
        
# Function to generate a unique sID
def generate_sID(cursor):
    # Infinite loop to generate a unique sID
    while True:
        # Generate a random sID between 10000 and 99999
        sID = random.randint(10000, 99999)
        # Check if the generated sID already exists in the movie_star table
        cursor.execute("SELECT sID FROM movie_star WHERE sID = %s", (sID,))
        # If sID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return sID
        
# Function to generate a unique dID
def generate_dID(cursor):
    # Infinite loop to generate a unique dID
    while True:
        # Generate a random dID between 10000 and 99999
        dID = random.randint(10000, 99999)
        # Check if the generated dID already exists in the movie_director table
        cursor.execute("SELECT dID FROM movie_director WHERE dID = %s", (dID,))
        # If dID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return dID
        
# Function to generate a unique wID
def generate_wID(cursor):
    # Infinite loop to generate a unique wID
    while True:
        # Generate a random wID between 10000 and 99999
        wID = random.randint(10000, 99999)
        # Check if the generated wID already exists in the movie_writer table
        cursor.execute("SELECT wID FROM movie_writer WHERE wID = %s", (wID,))
        # If wID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return wID
        
# Function to generate a unique pID
def generate_pID(cursor):
    # Infinite loop to generate a unique pID
    while True:
        # Generate a random pID between 10000 and 99999
        pID = random.randint(10000, 99999)
        # Check if the generated pID already exists in the movie_production table
        cursor.execute("SELECT pID FROM movie_production WHERE pID = %s", (pID,))
        # If pID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return pID
        
# Function to generate a unique gID
def generate_gID(cursor):
    # Infinite loop to generate a unique gID
    while True:
        # Generate a random gID between 10000 and 99999
        gID = random.randint(10000, 99999)
        # Check if the generated gID already exists in the movie_general table
        cursor.execute("SELECT gID FROM movie_general WHERE gID = %s", (gID,))
        # If gID does not exist, it's unique, so return it
        if not cursor.fetchone():
            return gID

# Try block to handle potential errors
try:
    # Establish database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2542",
        database="coursework1"
    )

    # Creating a cursor object to interact with the database
    cursor = connection.cursor()

    # Read movie data from CSV file using pandas
    movieData = pd.read_csv("movies.csv")

    # Iterate over each row in the CSV
    for index, row in movieData.iterrows():
        # Generate unique IDs for each table
        mID = generate_mID(cursor)
        cID = generate_cID(cursor)
        sID = generate_sID(cursor)
        dID = generate_dID(cursor)
        wID = generate_wID(cursor)
        pID = generate_pID(cursor)
        gID = generate_gID(cursor)

        # Replace 'nan' values with None
        row = row.where(pd.notnull(row), None)

        # Insert values into movie_name table
        cursor.execute("INSERT INTO movie_name (mID, name) VALUES (%s, %s)", (mID, row['name']))

        # Insert values into movie_company table
        cursor.execute("INSERT INTO movie_company (cID, company) VALUES (%s, %s)", (cID, row['company']))

        # Insert values into movie_star table
        cursor.execute("INSERT INTO movie_star (sID, star) VALUES (%s, %s)", (sID, row['star']))

        # Insert values into movie_director table
        cursor.execute("INSERT INTO movie_director (dID, director) VALUES (%s, %s)", (dID, row['director']))

        # Insert values into movie_writer table
        cursor.execute("INSERT INTO movie_writer (wID, writer) VALUES (%s, %s)", (wID, row['writer']))

        # Insert values into movie_production table
        cursor.execute("INSERT INTO movie_production (pID, mID, cID, sID, dID, wID) VALUES (%s, %s, %s, %s, %s, %s)",
                       (pID, mID, cID, sID, dID, wID))

        # Insert values into movie_general table
        cursor.execute("INSERT INTO movie_general (gID, pID, votes, score, genre, year, country, released, runtime, rating, budget, gross) \
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (gID, pID, row['votes'], row['score'], row['genre'], row['year'], row['country'],
                         row['released'], row['runtime'], row['rating'], row['budget'], row['gross']))

        # Commit the changes for each row
        connection.commit()

    # Print a success message if no errors occurred
    print("Data inserted successfully.")

# Exception block to handle any errors that occur during execution
except Error as e:
    # Print the error message
    print(f"Error: {e}")

# Finally block to ensure cursor and connection are closed regardless of errors
finally:
    # Check if the connection is still open
    if connection.is_connected():
        # Close the cursor object
        cursor.close()
        # Close the database connection
        connection.close()
        # Print a message indicating that the database connection is closed
        print("Database connection closed.")