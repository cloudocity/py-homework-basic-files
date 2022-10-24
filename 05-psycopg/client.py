import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client.users(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE not null
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client.phone(
        id SERIAL PRIMARY KEY,
        phone VARCHAR(100) UNIQUE NOT NULL,
        user_id int4 NOT NULL REFERENCES client.users(id)
        );
        """)
        conn.commit()

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client.users(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING id;
        """, (first_name, last_name, email))
        id_user = cur.fetchone()[0]
        conn.commit()
        if phones:
            cur.execute("""
            INSERT INTO client.phone(phone, user_id) VALUES(%s, %s);
            """, (phones, id_user))
            conn.commit()
    return id_user

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client.phone(phone, user_id) VALUES(%s, %s);
        """, (phone, client_id))
    conn.commit()
    return print("Телефон успешно добавлен")


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name:
            print("Меняем имя")
            cur.execute("""
            UPDATE client.users set first_name = %s  Where id = %s ;
            """, (first_name, client_id))
        if last_name:
            print("Меняем фамилию")
            cur.execute("""
            UPDATE client.users set last_name = %s  Where id = %s ;
            """, (last_name, client_id))
        if email:
            print("Меняем почту")
            cur.execute("""
            UPDATE client.users set email = %s  Where id = %s ;
            """, (email, client_id))
        conn.commit()
        if phones:
            cur.execute("""
            SELECT id, phone FROM client.phone WHERE user_id=%s;
            """, (client_id,))
            for phone in cur.fetchall():
                print('Телефоны пользователя:', phone)
            id_phone = input('Укажите id номера телефона, который нужно поменять:')
            cur.execute("""
            UPDATE client.phone set phone = %s  Where user_id = %s and id = %s;
            """, (phones, client_id, id_phone))
            conn.commit()
        return print("Данные успешно поменяны")


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client.phone WHERE user_id=%s and phone = %s;
        """, (client_id, phone))
        conn.commit()
        return print("Телефон успешно удален")

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client.phone WHERE user_id=%s;
        """, (client_id,))
        conn.commit()
        cur.execute("""
        DELETE FROM client.users WHERE id=%s;
        """, (client_id,))
        conn.commit()
        return print("Все данные о пользователе успешно удалены")

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute("""
            SELECT * FROM client.users WHERE first_name=%s;
            """, (first_name,))
            for first_name in cur.fetchall():
                print('Найденный пользователь:', first_name)
        if last_name:
            cur.execute("""
            SELECT * FROM client.users WHERE last_name=%s;
            """, (last_name,))
            for last_name in cur.fetchall():
                print('Найденный пользователь:', last_name)
        if email:
            cur.execute("""
            SELECT * FROM client.users WHERE email=%s;
            """, (email,))
            for email in cur.fetchall():
                print('Найденный пользователь:', email)
        if phone:
            cur.execute("""
            SELECT user_id FROM client.phone WHERE phone=%s;
            """, (phone,))
            for phone in cur.fetchall():
                cur.execute("""
                SELECT * FROM client.users WHERE id=%s;
                """, (phone[0],))
                for user_phone in cur.fetchall():
                    print('Найденный, по номеру телефона, пользователь:', user_phone)

with psycopg2.connect(database="postgres", user="postgres", password="2wsx4RFV") as conn:
    #Функция, создающая структуру БД(таблицы)
    create_db(conn)

    #Функция, позволяющая добавить нового клиента
    add_client(conn, 'Vasilyi', 'Petrov', 'vas@yandex.ru', '89998888999')

    #Функция, позволяющая добавить телефон для существующего клиента
    add_phone(conn, 21, '892011125455')

    #Функция, позволяющая изменить данные о клиенте
    change_client(conn, 21 , phones='8777777')

    #Функция, позволяющая удалить телефон для существующего клиента
    delete_phone(conn, 21 , '8777777')

    #Функция, позволяющая удалить существующего клиента
    delete_client(conn, 18)

    # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    find_client(conn, first_name='Vasilyi', last_name='Petrov', email='vas@yandex.ru', phone='89998888999')

conn.close()
