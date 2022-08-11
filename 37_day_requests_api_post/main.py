from tokenize import Token
import requests

#using pixela api
##need to set up user before you can post

TOKEN = "asdfhjklgqwepoirtuasdf"
USERNAME = "auauauaua"

pixela_endpoint = "https://pixe.la/"

#create a user
pixela_create_user_endpoint = pixela_endpoint + "v1/users"

create_user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

create_user_response = requests.post(pixela_create_user_endpoint, json=create_user_params)
#create_user_response.raise_for_status()
print(create_user_response.content)


# create graph under new user
pixela_create_graph_endpoint = pixela_endpoint + f"v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixela_create_graph_endpoint, json=graph_config, headers=headers)
print(response.content)

# update a point on the graph with put
graph_id = graph_config["id"]
pixela_post_pixel = pixela_endpoint + f"v1/users/{USERNAME}/graphs/{graph_id}"
graph_pixel_post = {
    "date":"20220804",
    "quantity":"3",
}

response = requests.post(url=pixela_post_pixel, json=graph_pixel_post, headers=headers)
print(response.content)



#response = requests.post(url=graph_endpoint, json= graph_config)
#print(response.text)