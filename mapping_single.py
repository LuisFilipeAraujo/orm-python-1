from sqlalchemy import create_engine, inspect, Column, Integer, String, engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://aluno:aluno123@localhost/orm"

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


def main():
    engine = create_engine(url=URL)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)

    with Session.begin() as session:
        luis = Pessoa(nome="luis filipe araujo")
        session.add(luis)

    with engine.connect() as connection:
        result_set = connection.execute("SHOW DATABASES")
        for row in result_set:
            print(row[0])

    print("\nTable List in world database")
    print("======================================")

    with engine.connect() as connection:
        result_set = connection.execute("SHOW TABLES")
        for row in result_set:
            print(row[0])

    print("\nTable List in world database")
    print("======================================")

'''  
    insp = inspect(engine)
    db_list = insp.get_schema_names()
    print(db_list)
'''

if __name__ == "__main__":
    main()
