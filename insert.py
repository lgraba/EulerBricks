# insert.py
# insert generated Euler Bricks into database

import mysql.connector

cnx = mysql.connector.connect(host='localhost', database='euler', user='root', password='')
cursor = cnx.cursor()

add_brick = ("INSERT INTO bricks "
			"(a, b, c, ab, ac, bc)"
			"VALUES (%s, %s, %s, %s, %s, %s)")

brick_data = (10, 20, 30, 40, 50, 60)

# Insert that Brick, baby!
cursor.execute(add_brick, brick_data)

# Commit data to database
cnx.commit()

cursor.close()
cnx.close()