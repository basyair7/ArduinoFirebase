# ArduinoFirebase
Project Sederhana menggunakan sensor dht arduino dan database realtime firebase

# Cara install modul Firebase
Spesifikasi : 
       > windows 10
       > python 3.8
        
Important (for windows): 
       > install visual studio, select Visual Studio Community select "Desktop devlopment with C++"
			 > Select MSVC C++ x64/x84 build tools, Windows SDK v10.0.19042, C++ profiling tools, C++ CMake tools for Windows, C++ ATL for latest, C++ AddressSanitizer 
			 > Restart PC

https://visualstudio.microsoft.com/downloads/ (5gb)

======== Install Firebase Database =========
~$ python -m pip install gcloud
~$ python -m pip install sseclient
~$ python -m pip install pycrypto
~$ python -m pip install pycryptodome -> if pycrypto error
~$ python -m pip install firebase-admin
~$ python -m pip install firebase
~$ python -m pip install pyrebase
~$ python -m pip install pyserial
~$ python -m pip install serial
~$ python -m pip install datetime

*for windows : problem Crypto
solved : 1. go c:\Users\"name user"\AppData\Local\Programs\Python\Python38\Lib\site-packages
	 2. rename folder 'crypto' to 'Crypto'
