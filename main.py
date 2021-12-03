from os import stat, system
import sqlite3

connection= sqlite3.connect('Backup.db')
cursor = connection.cursor()

#create
def create(niz_podataka:list):
    sqlquery = f"""INSERT INTO FamilyTree VALUES(NULL, \"{niz_podataka[1]}\", \"{niz_podataka[2]}\", \"{niz_podataka[3]}\", \"{niz_podataka[4]}\")"""
    connection.execute(sqlquery)
    connection.commit()


def read():
    statement = """SELECT * FROM FamilyTree"""
    cursor.execute(statement)
    resaults = cursor.fetchall()
    print("id || ImeIPrezime || DatumRodjenja || MestoRodjenja || Zanimanje")
    for i in resaults:
        for j in i:
            print(j,end=" || ")
        print()

def update(niz_za_promenu:str, id_za_promenu:int):
    sqlquery=f"""UPDATE FamilyTree set {niz_za_promenu} WHERE id={id_za_promenu}"""
    connection.execute(sqlquery)
    connection.commit()

def delete(id_za_brisanje:int):
    sqlquery = f"""DELETE FROM FamilyTree WHERE id={id_za_brisanje}"""
    connection.execute(sqlquery)
    connection.commit()




def main():
    system('cls')
    while True:
        
        print("""
            WELCOME TO THE FAMILY TREE
1. Create
2. Read
3. Update
4. Delete
        
0. Exit
        """)
        menu = int(input("Unesite opciju iz menija: "))
        if menu == 1:
            system('cls')
            print("Welcome to the Create section!")
            print("The table has this form:")
            print("id || ImeIPrezime || DatumRodjenja || MestoRodjenja || Zanimanje")
            head = ['id','ImeIPrezime','DatumRodjenja','MestoRodjenja','Zanimanje']
            new_array = []
            for i in head:
                new_array.append(input(f"Input {i}: "))
            create(new_array)
        if menu == 2:
            system('cls')
            read()
        if menu == 3:
            system('cls')
            read()
            indeks = int(input("Chose id to edit: "))
            promene= input("Commit changes to wanted columns like this:\nImeIPrezime=\"Mihajlo Veniger\", DatumRodjenja=\"1967-10-24\",etc.\nMake changes: ")
            update(promene,indeks)
        
        if menu == 4:
            system('cls')
            read()
            ind = int(input("Chose an ID to delete from Table: "))
            delete()

        if menu == 0:
            system('cls')
            print("Good bye!")
            exit(1)

if __name__ == "__main__":
    main()




    



