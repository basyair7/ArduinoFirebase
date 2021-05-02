from firebase import firebase

url = "https://testing-db1237-default-rtdb.firebaseio.com"

db = firebase.FirebaseApplication(url, None)

data = {
    "Nama": "Fathul Basyair",
    "Nim": "1904105010004",
    "Prodi": "Teknik Elektro",
    "Jurusan": "Teknik Elektro dan Komputer",
    "Fakultas": "Teknik"
}

#result = db.post("/biodata", data)
#db.delete(url, None)
#db.delete(url, "biodata_mahasiswa")

print("Done")
