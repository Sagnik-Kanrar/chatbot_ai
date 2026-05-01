import gridfs
from db import db

fs = gridfs.GridFS(db)

# Save file
with open("acne.jpg", "rb") as f:
    file_id = fs.put(f, filename="acne.jpg")

# Get file
file = fs.get(file_id)
with open("downloaded.jpg", "wb") as f:
    f.write(file.read())