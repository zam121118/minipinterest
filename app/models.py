from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)

	def __repr__(self): #tell python how to print the instance of this class used to debug
		return '<User %r>'  %(self.nickname)