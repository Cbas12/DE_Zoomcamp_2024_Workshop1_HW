import dlt
from dlt.destinations import postgres

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

# for person in people_1():
#     print(person)
# for person in people_2():
#     print(person)

#credentials and config
user = "admin"
password = "root"
host = "localhost"
port = 5432
db = "people_db"

# define the connection to load to. 
pipeline = dlt.pipeline( destination=postgres(credentials='postgresql://'+str(user)+':'+str(password)+'@'+str(host)+':'+str(port)+'/'+str(db)) )

# run the pipeline with default settings, and capture the outcome
info = pipeline.run(data=people_1(),write_disposition="replace", table_name="people_1")
print(info)

append = pipeline.run(data=people_2(),write_disposition="append", table_name="people_1")
print(append)