from database.CRUD import CRUDInterface
from database.models import db, Client

def initialize_database():
    """Инициализация базы данных и создание таблиц."""
    try:
        db.connect()
        db.create_tables([Client], safe=True)
        crud = CRUDInterface
        print(f"База данных успешно инициализирована{crud}.")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")
    finally:
        db.close()