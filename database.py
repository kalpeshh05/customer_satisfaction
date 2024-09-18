### database create and table create 



import sqlite3
conn = sqlite3.connect('customerdata.db')

query_to_create_table = """
CREATE TABLE customerdetails(
    age int,
    flight_distance bigint,
    inflight_entertrainment int,
    baggage_hnadling int,
    cleanliness int,
    departure_delay int,
    arrival_delay int,
    gender varchar(10),
    customer_type varchar(20),
    travel_type varchar(20),
    class_type varchar(20),
    prediction varchar(20)
)
"""

cur = conn.cursor()
cur.execute(query_to_create_table)
print("your database and tables is created!!! ")
cur.close()
conn.close()