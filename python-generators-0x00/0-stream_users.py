import csv
import uuid
from itertools import islice

def stream_users():
    with open('user_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = uuid.uuid4()
            yield {
                'user_id': str(user_id),
                'name': row['name'],
                'email': row['email'],
                'age': row['age'],
            }
