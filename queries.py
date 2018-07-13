from models import *

from sqlalchemy import create_engine

engine = create_engine('sqlite:///actorroles.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_christian_bales_roles(session):

    return session.query(Actor).filter_by(name='Christian Bale').all()[0].roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors(session):
    return session.query(Role).filter_by(character = 'Catwoman').first().actors

    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    batman=session.query(Role).filter_by(character = 'Batman').first().actors
    number_of_batman=len(batman)
    return number_of_batman
    # Return the number of actors that have played Batman
