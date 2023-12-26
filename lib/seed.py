#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Base
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_engine_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

instance1 = Company(name='MoringaTech', founding_year='2023')
instance2= Dev(name='Justin Sibudi')

session.add(instance1)
session.add(instance2)

session.commit()

session.close()