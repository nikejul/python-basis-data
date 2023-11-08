import psycopg2

connection = psycopg2.connect(
    host= 'localhost',
    user= '5432',
    password= 'nikejul29',
    dbname= 'postgres'
)

cursor = connection.cursor()

#cursor.execute("")

#cursor.execute("select * from mahasiswa")
cursor.execute("insert into mahasiswa (nim, nama, no_hp) values (1234, 'jojon', 124235)")
connection.commit()

#hanya untuk manipulation psy tidak digunakan untuk membuat database

cursor.execute("select nim, nama from mahasiswa")
data = cursor.fetchall()

#print(data)

for row in data:
    print(row)
#isi kode

#jangan lupa menutup koneksi

cursor.close()
connection.close()