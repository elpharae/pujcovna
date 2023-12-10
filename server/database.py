import sqlite3

def create_database(): 
    conn = sqlite3.connect('./server/data.db')
    cursor = conn.cursor()

    cursor.execute('''
    create table if not exists user_roles (
        user_role_id integer primary key autoincrement,
        name text not null,
        privilege integer not null check (privilege >= 0 and privilege <= 3)
    )
    ''')

    cursor.execute('''
    create table if not exists users (
        user_id integer primary key autoincrement,
        email text not null,
        first_name text not null,
        last_name text not null,
        password_hash text not null,
        user_role_id integer not null,
                
        foreign key(user_role_id) references user_roles(user_role_id)
    )
    ''')

    cursor.execute('''
    create table if not exists car_types (
        car_type_id integer primary key autoincrement,
        name text not null
    )
    ''')


    cursor.execute('''
    create table if not exists colors (
        color_id integer primary key autoincrement,
        name text not null
    )
    ''')

    cursor.execute('''
    create table if not exists fuel_types (
        fuel_type_id integer primary key autoincrement,
        name text not null
    )
    ''')

    cursor.execute('''
    create table if not exists cars (
        car_id integer primary key autoincrement,
        brand text not null,
        model text not null,
        image_url text not null,
        car_type_id integer not null,
        fuel_type_id integer not null,
        color_id integer not null,

        foreign key(car_type_id) references car_types(car_type_id), 
        foreign key(fuel_type_id) references fuel_types(fuel_type_id),
        foreign key(color_id) references colors(color_id)
    )
    ''')

    cursor.execute('''
    create table if not exists rentals (
        rental_id integer primary key autoincrement,
        rental_date date not null,
        rented_until date not null,
        user_id integer not null,
        car_id integer not null,

        foreign key(user_id) references users(user_id),
        foreign key(car_id) references cars(car_id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
