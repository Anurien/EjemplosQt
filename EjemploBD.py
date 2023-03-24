import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)

try:
    bbdd = dbapi.connect('bbdd.dat')

except (dbapi.DataBaseError):
    print("Erro na BD")
else:
    print("Conectado a BD")
    # print(bbdd)

try:
    c = bbdd.cursor()

    '''c.execute (""" create table usuarios (dni text,
                                          nome text,
                                          direccion text)""")
    c.execute ("""insert into usuarios
                     values ('3333-A', 'Maria', 'Canceleiro')""")
    c.execute ("""insert into usuarios
                      values ('4444-B', 'Manuel', 'Rosalia')""")
    c.execute ("""insert into usuarios
                      values ('5555-C', 'Ana', 'Areal')""")
    '''

    bbdd.commit()


except dbapi.OperationalError as e:
    print("Erro na base de datos: " + str(e))

try:
    c.execute('''select dni, nome, direccion from usuarios''')

    print(type(c.fetchall()))
    for rexistro in c.fetchall():
        print("Nome: " + rexistro[1])

except dbapi.OperationalError as e:
    print("Erro na base de datos, facendo a consulta: " + str(e))

try:
    """Non facer asi!!!!!
    """
    dni = input("Introduce o dni ")
    """
    c.execute ('''select dni, nome, direccion from usuarios where dni="'''+ dni + '"' )
    """

    c.execute('''select dni, nome, direccion from usuarios where dni=?''', (dni,))

    for rexistro in c.fetchall():
        print("Dni: " + rexistro[0])
        print("Nome: " + rexistro[1])
        print("Dirección: " + rexistro[2])

except dbapi.OperationalError as e:
    print("Erro na base de datos, facendo a consulta: " + str(e))
