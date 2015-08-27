# insert.py
# insert generated Euler Bricks into database

import mysql.connector

def addBrick(a, b, c, ab, ac, bc):
	cnx = mysql.connector.connect(host='localhost', database='euler', user='root', password='')
	cursor = cnx.cursor()
	try:
		add_brick = ("INSERT INTO bricks "
					"(a, b, c, ab, ac, bc)"
					"VALUES (%s, %s, %s, %s, %s, %s)")

		brick_data = (a, b, c, ab, ac, bc)

		# Insert that Brick, baby!
		cursor.execute(add_brick, brick_data)

		# Commit data to database
		cnx.commit()
	finally:
		cursor.close()
		cnx.close()

def addPerfect(a, b, c, abc):
	cnx = mysql.connector.connect(host='localhost', database='euler', user='root', password='')
	cursor = cnx.cursor()
	try:
		add_abc = ("UPDATE bricks SET "
				"abc=%s "
				"WHERE a=%s AND b=%s AND c=%s")

		brick_data = (abc, a, b, c)

		# Insert that Brick, baby!
		cursor.execute(add_abc, brick_data)

		# Commit data to database
		cnx.commit()
	finally:
		cursor.close()
		cnx.close()

def addStats(time, maximum):
	cnx = mysql.connector.connect(host='localhost', database='euler', user='root', password='')
	cursor = cnx.cursor()
	try:
		add_stats = ("INSERT INTO bricks_stats "
					"(time_elapsed, maximum_searched)"
					"VALUES (%s, %s)")

		brick_stats = (time, maximum)

		# Insert those stats
		cursor.execute(add_stats, brick_stats)
		cnx.commit()
	finally:
		cursor.close()
		cnx.close()