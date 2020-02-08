import requests 

req = requests.session()
param={
    "username":"op7torlaxzzx@gmail.com"
    "password":"1456379sl"
    "remember":"true"


}
source = req.post("https://accounts.spotify.com/login",data=param)
print(source.txt