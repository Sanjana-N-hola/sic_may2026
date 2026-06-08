import pymysql


def connect_db():
    try:
        connection = pymysql.connect(user = 'root', password = 'Papadgang@2008', host = 'localhost' ,port = 3306, database = 'sanjana', charset = 'utf8')
        print('DBconnected')
        return connection
    except:
        print('DB connection failed.')

def disconnect_db(connection):
    try:
        connection.close()
        print('DBdisconnected')
    except:
        print('DB connection failed.')

def create_table():
    query = 'create table IF NOT EXISTS people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, location varchar(32), age int default(0));'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print('Table created.')
        else:
            print('Table connection failed.')
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print('Table creation failed. L bozo')  


def create_person_demo():
    query = 'insert into people(name, gender, age, location) values("felicia", true, 18, "chicago");'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count > 0:
            print('Person created.')
        else:
            print('Insert failed.')
        cursor.close()
        disconnect_db(connection)
    except Exception as b:
        print(b.msg)
        print('Person creation failed. L bozo')

def read_person():
    name = input('Enter person name:')
    gender = input('Enter person gender(m/f):')
    age = int(input('Enter person age:'))
    location = input('Enter person location:')
    if gender.lower() == 'f':
        gender = True   
    else:
        gender = False 
    return(name, gender, age, location)





def create_person():
    query = 'insert into people(name, gender, age, location) values(%s, %s, %s, %s);'
    try:
        person = read_person()
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        if count >= 1:
            print('Person created.')
        else:
            print('Person connection failed.')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as b:
        print(b)
        print('Person creation failed. L bozo')
create_person()



def search_person():
    id = int(input('Enter id of the person to be searched:'))
    query = f'select * from people where id = {id}'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(f'count = {count}')
        if count == 1:
            row = cursor.fetchone()
            print(row)
            print(type(row))
        else:
            print('No person was found.')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as c:
        print(c)
        print('Listing the people failed.')

def update_person():
    id = int(input('Enter id of the person to be updated:'))
    new_location = input('Enter new location of the person:')
    query='update people set location = %s where id = %s'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (new_location, id))
        connection.commit()
        cursor.close()
        disconnect_db(connection)
        print(f'count ={count}')
        if count == 1:
            print(f'Person with id = {id} is updated.')
        else:
            print(f'Person with id = {id} not found.')
       
    except Exception as d:
        print(d)
        print('updating the person failed.')
update_person()

def delete_person():
    id = int(input('Enter id of the person to be deleted:'))
    query=f'delete from people where id = {id}'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        print(count)
        if count == 1:
            print(f'Person with id = {id} is deleted.')
        else:
            print(f'Person with id = {id} not found.')
        cursor.close()
        disconnect_db(connection)
    except Exception as d:
        print(d)
        print('Listing the people failed.')


def list_person():
    query = 'select * from people;'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(count)
        if count >= 1:
            rows = cursor.fetchall()
            print(type(rows))
            for row in rows:
                print(row)
        else:
            print('No person was found.')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as c:
        print(c)
        print('Listing the people failed.')


      

# copy paste and replace connection with yo name

