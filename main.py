

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api,reqparse
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pokedex'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

parser1=reqparse.RequestParser()
parser1.add_argument('nombre',help='Por favor indica el nombre , no puede estar en blanco',required=True)
parser1.add_argument('tipo',help='Por favor indica el tipo')
parser1.add_argument('edad',help='Por favor indica la edad, no puede estar en blanco',required=True)
parser1.add_argument('FechaDeNacimiento',help='Por favor indica la Fecha de nacimiento, no puede estar en blanco',required=True)
parser1.add_argument('AtaquePrincipal',help='Por favor indica el Ataque principal, no puede estar en blanco',required=True)
parser1.add_argument('foto',help='Por favor indica la URL de la foto')
parser2=reqparse.RequestParser()
parser2.add_argument('nombre',help='Por favor indica el nombre')
parser2.add_argument('tipo',help='Por favor indica el tipo')
parser2.add_argument('edad',help='Por favor indica la edad')
parser2.add_argument('FechaDeNacimiento',help='Por favor indica la Fecha de nacimiento')
parser2.add_argument('AtaquePrincipal',help='Por favor indica el Ataque principal')
parser2.add_argument('foto',help='Por favor indica la URL de la foto')

class Pokemon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    tipo=db.Column(db.String(60), nullable=True)
    age=db.Column(db.Integer, nullable=False)
    birthdate=db.Column(db.String(15), nullable=False)
    principalattack=db.Column(db.String(50), nullable=False)
    picture=db.Column(db.String(255), nullable=True)
    
    def __repr__(self) :
        return "[Pokemon %s]" % str(self.id)


db.create_all()

class IndexRoute(Resource):
    def get(self):
        return {'response': 'ESTE ES EL INDES ROUTE SIYY'},200

class IndexRoutePokemon(Resource):
    def get(self):

        pokemones= Pokemon.query.all()
        response=[]
        if pokemones:
            for pokemon in pokemones:
                response.append({
                    "id":pokemon.id,
                    "nombre":pokemon.name,
                    "tipo":pokemon.tipo,
                    "edad":pokemon.age,
                    "Fecha de nacimiento": pokemon.birthdate,
                    "Ataque principal": pokemon.principalattack,
                    "foto":pokemon.picture
                })
        return {'response':response},200
    def post(self):
        args1=parser1.parse_args()
        print(args1)
        pokemon_a_crear=request.get_json(args1)
        pokemon=Pokemon(name=args1['nombre'],tipo=args1['tipo'],age=args1['edad'],birthdate=args1['FechaDeNacimiento'],principalattack=args1['AtaquePrincipal'],picture=args1['foto'])
        db.session.add(pokemon)
        db.session.commit()
        return {"response":"Pokemon creado exitosamente siuu!"}, 201

class PokemonbyID(Resource):
    def get(self,id):
        pokemon=Pokemon.query.filter_by(id=id).first()
        if pokemon:
            return{'response':{
                "id":pokemon.id,
                "nombre":pokemon.name,
                "tipo":pokemon.tipo,
                "edad":pokemon.age,
                "Fecha de nacimiento": pokemon.birthdate,
                "Ataque principal": pokemon.principalattack,
                "foto":pokemon.picture
            }},302
        else:
            return{"response":"NOT A VALID ID"},404
    def put(self,id):
        pokemon=Pokemon.query.filter_by(id=id).first()
        if pokemon:
            datos=parser2.parse_args()
            if(datos['nombre']==None and datos['tipo']==None and datos['edad']==None and datos['FechaDeNacimiento']==None and datos['AtaquePrincipal']==None and datos['foto']==None):
                return{"response":"Pokemon no valido"},400
            if datos['nombre']:
                pokemon.name=datos['nombre']
            elif datos['tipo']:
                pokemon.tipo=datos['tipo']
            elif datos['edad']:
                pokemon.age=datos['edad']
            elif datos['FechaDeNacimiento']:
                pokemon.birthdate=datos['FechaDeNacimiento']
            elif datos['AtaquePrincipal']:
                pokemon.principalattack=datos['AtaquePrincipal']
            elif datos['foto']:
                pokemon.picture=datos['foto']
            db.session.commit()
            return{"response":"Pokemon actualizado con exito siuuu!"},202
        else:
            return{"response":"Pokemon no valido"},404
    def delete(self,id):
        pokemon=Pokemon.query.filter_by(id=id).first()
        db.session.delete(pokemon)
        db.session.commit()
        if pokemon:
            return{"response":"Pokemon con id: {pokemon}. deleteado exitosamente siuuu!".format(pokemon=id)},302
        else:
            return{"response":"Pokemon no valido"},




api.add_resource(IndexRoute,'/')
api.add_resource(IndexRoutePokemon,'/pokemon')
api.add_resource(PokemonbyID,'/pokemon/<int:id>')
    

