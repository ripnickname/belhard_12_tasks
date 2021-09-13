from db import session_scope, tables

with session_scope() as session:
    person = tables.Person(name="Alex", surname="Jackson", birthdate="02.02.2002")
    session.add(person)
    session.commit()
    session.refresh(person)

    person = session.query(tables.Person).filter(tables.Person.name == "John").first()
    session.delete(person)
    session.commit()

    result = session.query(tables.Person).filter(tables.Person.name == "Alex").first()

    person = session.query(tables.Person).filter(tables.Person.name == "Alex").first()
    person.name = "Bob"
    session.commit()
    session.refresh(person)


