from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine= create_engine('sqlite:///freebies.db')

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')
    devs= relationship('Dev')

    def give_freebie(self, dev, name, session):
        freebie = Freebie(name=name, dev=dev, company=self)
        session.add(freebie)
        session.commit()

    def __repr__(self):
        return f'<Company {self.name}>' \
            + f"{self.founding_year}"
        

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', backref='dev')
    companies = relationship('Company')

    def give_away(self, dev, freebie , session):
        if freebie.dev ==self:
            freebie.dev ==dev
            session.commit()

    def __repr__(self):
        return f'<Dev {self.name}>'
class Freebie(Base):
    __tablename__='freebies'

    id= Column(Integer(), primary_key=True)
    name= Column(String())

    Dev_id= Column(Integer(), ForeignKey('devs.id'))
    Company_id= Column(Integer, ForeignKey('companies.id'))

    dev = relationship('Dev', backref='freebies')
    company = relationship('Company', backref='freebies')
    
    print_details=print(f'{dev.name}' "owns a" f'{name}' "from"f'{company.name}' )

    

Freebie.print_details()
 