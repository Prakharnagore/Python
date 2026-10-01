import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1984},
]

data = json.dumps(movies)
# [{"id": 1, "title": "Terminator", "year": 1984}, {"id": 2, "title": "Kindergarten Cop", "year": 1984}]
print(data)

# Write to file
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)  # return an list of dictionaries
print(movies)
