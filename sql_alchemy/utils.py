from models import People


# entering data
def insert_people():
    people = People(name="Danrlei", age=23)
    print(people)
    people.save()


# query data
def query_db():
    people = People.query.all()

    for i in people:
        print(i.name)

    people = People.query.filter_by(name="Danrlei").first()
    print(people.age)


# change data
def alter_people():
    people = People.query.filter_by(name="Danrlei").first()
    people.age = 24
    people.save()


# delete data
def delete_people():
    people = People.query.filter_by(name="Danrlei").first()
    people.delete()


if __name__ == "__main__":
    insert_people()
    query_db()
    alter_people()
    delete_people()
