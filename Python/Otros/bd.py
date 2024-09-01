import _sqlite3

conn = _sqlite3.connect('Animales.db')
c = conn.cursor()

c.execute("""CREATE TABLE perro(
    nombre text primary key,
    age int,
    live boolean default true
);""")

conn.commit()

conn.close()
