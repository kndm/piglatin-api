import requests 
    
api_endpoint = "http://localhost:80/translate"

user_text = input("Word to translate: ") 
data = {
    "text": user_text
}
  
# sending post request and saving response as response object 
r = requests.post(url = api_endpoint, json = data) 
  
# extracting response text  
request_url = r.text 
print("Succesful request, the json for the translated word is:%s" %request_url) 