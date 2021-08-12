from replit import db
from scratchclient import ScratchSession
import os

Password = os.environ["Password"]
session = ScratchSession("XenoOS", Password)
connection = session.create_cloud_connection(560126438)

db["siteurl"] = connection.get_cloud_variable("Pretend this number is an url")


print(db.keys())
print(db["siteurl"])