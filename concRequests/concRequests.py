import concurrent.futures
import requests
import random
import string

url = 'http://localhost:3000'

def random_name():
  # Generate a random string of 6 characters
  return ''.join(random.choices(string.ascii_letters, k=6))

# Set the maximum number of requests to send concurrently
max_concurrent = 50

# Generate a list of 10000 random names
names = [random_name() for _ in range(10000)]
bodies = [{'name': name} for name in names]

# Use a ThreadPoolExecutor to send the requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_concurrent) as executor:
  # Submit a task to send each request
  futures = [executor.submit(requests.post, url, json=body) for body in bodies]
  
  # Iterate through the completed tasks
  for i, future in enumerate(concurrent.futures.as_completed(futures)):
    response = future.result()
    if response.status_code == 200:
      print(f'Successfully sent request {i} with name {names[i]}')
    else:
      print(f'Error sending request {i}: {response.status_code}')
