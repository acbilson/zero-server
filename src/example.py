from subprocess import run
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import FetchedValue
from sqlalchemy import create_engine, Column, Text, DateTime, Integer

if __name__ == "__main__":

    engine = create_engine('sqlite:///db/temperature.sqlite', echo=True)

    Base = declarative_base()

    class Temperature(Base):
        __tablename__ = "temperature"

        rowid = Column(Integer, primary_key=True)
        celsius = Column(Text)
        timestamp = Column(DateTime, server_default=FetchedValue())

    Session = sessionmaker(bind=engine)
    session = Session()

    result = run(["/opt/vc/bin/vcgencmd", "measure_temp"], capture_output=True, text=True)
    reading = result.stdout.strip().split("=")[1]
    new_record = Temperature(celsius=reading)
    session.add(new_record)
    session.commit()

    initial_result = session.query(Temperature).all()

    for row in initial_result:
        print("rowid: ", row.rowid)
        print("temp: ", row.celsius)
        print("timestamp: ", row.timestamp)

