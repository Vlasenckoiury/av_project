import psycopg2
from functools import wraps

from av_project.av_backend.av_car.main_bot import *


def db_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        try:
            result = func(cursor, *args, **kwargs)
            conn.commit()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
    return wrapper


@db_connection
def insert_tg(cursor, user_id, username, first_name, last_name):
    # SQL-запрос для вставки данных
    insert_query = """
    INSERT INTO av_car_botuser (telegram_id, username, first_name, last_name) VALUES (%s, %s, %s, %s)
    """
    # Выполнение запроса
    cursor.execute(insert_query, (user_id, username, first_name, last_name))
    print("Данные успешно сохранены в базе данных")


@db_connection
def get_all_links(cursor):
    select_query = f"SELECT name, chat_link FROM av_car_telegramchat"
    cursor.execute(select_query)
    column = cursor.fetchall()
    return column


@db_connection
def get_contact(cursor, message):
    update_query = f"""UPDATE av_car_botuser SET contact = %s WHERE telegram_id = {message.chat.id}"""
    # Выполнение запроса
    cursor.execute(update_query, (message.contact.phone_number, ))
    print(f"Значение в колонке {message.contact.phone_number} пользователя с telegram_id {message.chat.id} успешно обновлено в базе данных")

