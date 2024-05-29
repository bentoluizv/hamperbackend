from ..ext.database import db


class User(db.Model):
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(20), nullable=False)
    lastname: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    
    # TODO: Verificar os dados que estão sendo carregados nos testes
    # def __str__(self):
    #     return f'User(id={self.id}, firstname={self.firstname}, email={self.email})'