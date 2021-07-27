# Занятие 12. Работа с РСУБД. SQL. SQLAlchemy

## SQL

***

Полученная схема должна выглядеть следующим образом:

![Database schema](schema.png)

## SQLAlchemy

1. Создать пакет ```db```.
2. Создать модуль ```base.by```:

    ```python
    from sqlalchemy.ext.declarative import declarative_base
    
    Base = declarative_base()
    ```

3. Создать модуль ```session.by```:

    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from contextlib import contextmanager
    
    
    engine = create_engine(
        'mysql+pymysql://user:password@localhost:3306/database',
        pool_pre_ping=True,
        pool_recycle=3600,
    )
    Session = sessionmaker(bind=engine)
    
    
    @contextmanager
    def session_scope():
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    ```

4. Создать в пакете ```db``` пакет ```tables```.
5. В пакете ```tables``` описать таблицы из задания по SQL
6. Сделать файл ```__init__.py``` в пакете ```db``` и в пакете ```tables```и описать в нем инструкции импорта пакета.
7. Сделать в корне модуль ```run.py```, в котором произвести следующие операции:

   * Вставка в таблицу
   * Удаление из таблицы
   * Выборка с условием
   * Редактирование элемента
