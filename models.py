from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below
class Role (Base):
    __tablename__ = 'roles'
    id=Column(Integer, primary_key=True )
    actors = relationship('Actor', secondary='actor_roles')
    character=Column(Text)

class ActorRole(Base):
    __tablename__='actor_roles'
    id=Column(Integer, primary_key=True )
    actor_id = Column(Integer, ForeignKey('actors.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))

class Actor (Base):
    __tablename__ = 'actors'
    id=Column(Integer, primary_key=True )
    roles = relationship('Role', secondary='actor_roles')
    name = Column(Text)





engine = create_engine('sqlite:///actorroles.db')
Base.metadata.create_all(engine)
