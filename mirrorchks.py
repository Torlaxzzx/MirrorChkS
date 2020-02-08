import requests 

req = requests.session()
param={
    "username":"op7torlaxzzx@gmail.com"
    "password":"1456379sl"
    "remember":"true"

}
source = req.post("https://accounts.spotify.com/login",data=param)

if """incorrectos""" in source.text:
	print("LA CUENTA NO ES VALIDA")
else:
	print("LA CUENTA ES VALIDA")