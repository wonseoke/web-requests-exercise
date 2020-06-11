print("REQUESTING SOME DATA FROM THE INTERNET...")

import json
import requests
import statistics

""" 
#Part 1
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
print(type(response.text))
print(response.text)

parsed_response = json.loads(response.text)
print(type(parsed_response))

print(parsed_response["name"])


#Part 2
request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url2)
parsed_response2 = json.loads(response2.text)

for x in parsed_response2:
    print(x["id"],x["name"])
 """

#Part 3

gradebook_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json")
gradebook = json.loads(gradebook_response.text)
#print(gradebook)
#breakpoint()
grades = [s["finalGrade"] for s in gradebook["students"]]
print("MIN:", min(grades))
print("MAX:", max(grades))
print("AVG:", statistics.mean(grades))


""" 
request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url3)
response_data3 = json.loads(response3.text)
print(response_data3)

grades = [s["finalGrade"] for s in response_data3["students"]]

print(min(grades))
print(max(grades))

print(statistics.mean(grades))
"""