import mysql.connector
from mysql.connector import Error

# Establish database connection
connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2542",
        database='coursework1'
    )

cursor = connection.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS coursework1")
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)

# cursor.execute("CREATE TABLE movie_name (\
# mID int NOT NULL,\
# name varchar(255) NOT NULL,\
# primary key (mID)\
# );")

# cursor.execute("create table movie_company (\
# cID int NOT NULL,\
# company varchar(255),\
# primary key (cID)\
# );")

# cursor.execute("create table movie_star (\
# sID int NOT NULL,\
# star varchar(255),\
# primary key (sID)\
# );")

# cursor.execute("create table movie_director (\
# dID int NOT NULL,\
# director varchar(255) NOT NULL,\
# primary key (dID)\
# );")

# cursor.execute("create table movie_writer (\
# wID int NOT NULL,\
# writer varchar(255),\
# primary key (wID)\
# );")

# cursor.execute("create table movie_production (\
# pID int NOT NULL,\
# mID int NOT NULL,\
# cID int NOT NULL,\
# sID int NOT NULL,\
# dID int NOT NULL,\
# wID int NOT NULL,\
# primary key (pID),\
# foreign key (mID) references movie_name (mID),\
# foreign key (cID) references movie_company (cID),\
# foreign key (sID) references movie_star (sID),\
# foreign key (dID) references movie_director (dID),\
# foreign key (wID) references movie_writer (wID)\
# );")

# cursor.execute("create table movie_general (\
# gID int NOT NULL,\
# pID int NOT NULL,\
# votes int,\
# score float,\
# genre varchar(50) NOT NULL,\
# year int NOT NULL,\
# country varchar(100),\
# released varchar(255),\
# runtime int,\
# rating varchar(50),\
# budget int,\
# gross varchar(255),\
# primary key (gID),\
# foreign key (pID) references movie_production (pID)\
# );")

# # 1. SELECT AVG(budget) AS avg_budget, MIN(budget) AS min_budget, MAX(budget) AS max_budget
# #    FROM movie_general
# #    WHERE genre LIKE '%Drama%';
# cursor.execute("""
#     SELECT AVG(budget) AS avg_budget, MIN(budget) AS min_budget, MAX(budget) AS max_budget
#     FROM movie_general
#     WHERE genre LIKE '%Drama%';
# """)
# result = cursor.fetchone()
# print("Average Budget:", result[0])
# print("Minimum Budget:", result[1])
# print("Maximum Budget:", result[2])

# # 2. SELECT genre, MIN(budget) AS min_budget
# #    FROM movie_general
# #    GROUP BY genre;
# cursor.execute("""
#     SELECT genre, MIN(budget) AS min_budget
#     FROM movie_general
#     GROUP BY genre;
# """)
# results = cursor.fetchall()
# for row in results:
#     print("Genre:", row[0], ", Minimum Budget:", row[1])

# # 3. SELECT rating, AVG(score) AS avg_score
# #    FROM movie_general
# #    WHERE rating != 'Not Rated'
# #    GROUP BY rating;
# cursor.execute("""
#     SELECT rating, AVG(score) AS avg_score
#     FROM movie_general
#     WHERE rating != 'Not Rated'
#     GROUP BY rating;
# """)
# results = cursor.fetchall()
# for row in results:
#     print("Rating:", row[0], ", Average Score:", row[1])

# # 4. SELECT AVG(runtime) AS avg_runtime
# #    FROM movie_general
# #    WHERE year BETWEEN 2014 AND 2016;
# cursor.execute("""
#     SELECT AVG(runtime) AS avg_runtime
#     FROM movie_general
#     WHERE year BETWEEN 2014 AND 2016;
# """)
# result = cursor.fetchone()
# print("Average Runtime:", result[0])

# # 5. SELECT COUNT(*) AS num_movies
# #    FROM movie_general
# #    WHERE year < 2000;
# cursor.execute("""
#     SELECT COUNT(*) AS num_movies
#     FROM movie_general
#     WHERE year < 2000;
# """)
# result = cursor.fetchone()
# print("Number of Movies released before 2000:", result[0])

connection.commit()

cursor.close()
connection.close()