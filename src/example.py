from subprocess import run
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import FetchedValue
from sqlalchemy import create_engine, Column, Text, DateTime, Integer

if __name__ == "__main__":

    engine = create_engine('sqlite:///db/temperature.sqlite', echo=True)

    Base = declarative_base()

    class Pizero(Base):
        __tablename__ = "pizero"

        rowid = Column(Integer, primary_key=True)
        temp = Column(Text)
        timestamp = Column(DateTime, server_default=FetchedValue())

    Session = sessionmaker(bind=engine)
    session = Session()

    initial_result = session.query(Pizero).all()

    for row in initial_result:
        print("rowid: ", row.rowid)
        print("temp: ", row.temp)
        print("timestamp: ", row.timestamp)

    result = run(["/opt/vc/bin/vcgencmd", "measure_temp"], capture_output=True, text=True)
    temp_reading = result.stdout.strip().split("=")[1]
    new_record = Pizero(temp=temp_reading)
    session.add(new_record)
    session.commit()
