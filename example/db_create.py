import pyrebase
import collections

firebaseConfig = {
    "apiKey": "AIzaSyDb7uvq_45rQPS7Je7amnGhMXevdZgz4Nk",
    "authDomain": "testing-db1237.firebaseapp.com",
    "databaseURL": "https://testing-db1237-default-rtdb.firebaseio.com",
    "projectId": "testing-db1237",
    "storageBucket": "testing-db1237.appspot.com",
    "messagingSenderId": "332796751686",
    "appId": "1:332796751686:web:538a66c90c010ce7a6bf47",
    "measurementId": "G-S7KPWECYDN"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Push data
data = {
    "Nama": "Fathul Basyair", 
    "Nim": "1904105010004",
    "Fakultas": "Teknik",
    "Jurusan": "Teknik Elektro dan Komputer",
    "Prodi": "Teknik Elektro",
    "Bidang": "Energi Listrik Terbarukan"
    }

#db.push(data)
#db.set(data)
#db.update(data)
#db.child('biodata_mahasiswa').push(data)
#db.child('biodata_mahasiswa').set(data)
#db.remove() #remove all
#db.child('biodata_mahasiswa').remove()
#print("Done")

"""
print_db = collections.OrderedDict()
print_db = db.child('biodata_mahasiswa').child("Bidang").get().val()
print()

for get_data in print_db.items():
    print(f"{get_data[0]} : {get_data[1]}")
"""
"""
nama = db.child('biodata_mahasiswa').child('Nama').get().val()
nim = db.child('biodata_mahasiswa').child('Nim').get().val()
prodi = db.child('biodata_mahasiswa').child('Prodi').get().val()
jurusan = db.child('biodata_mahasiswa').child('Jurusan').get().val()
fakultas = db.child('biodata_mahasiswa').child('Fakultas').get().val()
bidang = db.child('biodata_mahasiswa').child('Bidang').get().val()
print(f"Nama\t : {nama}\nNim\t : {nim}\nProdi\t : {prodi}\nJurusan\t : {jurusan}\nFakultas : {fakultas}\nBidang\t : {bidang}")
"""