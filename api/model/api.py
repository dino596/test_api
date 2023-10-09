from sqlalchemy import Column, Integer, String
from .. import db

class api(db.Model):
    __tablename__ = "api"
    id = Column(Integer, primary_key=True)
    _class_name = Column(String, nullable=false)
    _heatlh = Column(Integer, nullable=false)
    _attack = Column(Integer, nullable=false)
    _resistance = Column(Integer, nullable=false)
    _power = Column(Integer, nullable=false)

    def __init__(self, class_name, health, attack, resistance, power):
        self._class_name = class_name
        self._heatlh = health
        self._attack = attack
        self._resistance = resistance
        self._power = power
    
    def __repr__(self):
        return "id='%s', class_name='%s', health='%s', attack='%s', resistance='%s', power='%s'" % (self.id, self.class_name, self.attack, self.resistance, self.power)
    
    @property
    def class_name(self):
        return self._class_name
    
    @class_name.setter
    def class_name(self, value):
        self._class_name = value

    @property
    def health(self):
        return self._class_name
    
    @health.setter
    def heatlh(self, value):
        self._class_name = value
    
    @property
    def attack(self):
        return self._class_name
    
    @attack.setter
    def attack(self, value):
        self._class_name = value

    @property
    def resistance(self):
        return self._class_name
    
    @resistance.setter
    def resistance(self, value):
        self._class_name = value

    @property
    def power(self):
        return self._class_name
    
    @power.setter
    def power(self, value):
        self._class_name = value

    def to_dict(self):
        return {"id": self.id, "class_name": self.class_name, "health": self.health, "attack", self.attack, "resistance": self.resistance, "power": self.power}
    
def init_api():
    god = api(class_name="God", health="10000", attack="10000", resistance="10000", power="1")
    warrior = api(class_name="Warrior", health="110", attack="130", resistance="110", power="3")
    knight = api(class_name="Knight", health="140", attack="110", resistance="100", power="3")
    wanderer = api(class_name="Wanderer", health="100", attack="110", resistance="100", power="3")
    bandit = api(class_name="Bandit", health="120", attack="140", resistance="110", power="2")
    hunter = api(class_name="Hunter", health="100", attack="140", resistance="110", power="4")
    cleric = api(class_name="Cleric", health="130", attack="130", resistance="130", power="3")
    depraved = api(class_name="Depraved", health="100", attack="160", resistance="90", power="5")

    db.session.add(god)
    db.session.add(warrior)
    db.session.add(knight)
    db.session.add(wanderer)
    db.session.add(bandit)
    db.session.add(hunter)
    db.session.add(cleric)
    db.session.add(depraved)

    db.session.commit()