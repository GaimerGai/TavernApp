from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class ServerAdmin(db.Model):
  __tablename__ = 'serverAdmins'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}


  id = db.Column(db.Integer, primary_key=True)
  serverID = db.Column(db.String(255), db.ForeignKey(add_prefix_for_prod('servers.id')), nullable=False)
  userID = db.Column(db.String(255), db.ForeignKey(add_prefix_for_prod('user.id')), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

  server = db.relationship('Server', backref='admins', foreign_keys='ServerAdmin.serverID', lazy=True)
  user = db.relationship('User', backref='admin_servers', foreign_keys='ServerAdmin.userID', lazy=True)

  def to_dict(self):
    return {
        'id': self.id,
        'serverID':self.serverID,
        'userID': self.userID,
        'created_at': self.created_at,
        'updated_at': self.updated_at
    }
