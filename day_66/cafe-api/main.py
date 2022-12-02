import random

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

#name of the app
cafe_app = Flask(__name__)


##Db connection
cafe_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
cafe_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(cafe_app)


#DB table
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    #return name of the cafe or restaurant. We need this when we querying DB.
    def __repr__(self):
        return self.name

    #Here we go through our database tables and get all table names, returned in new dict
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@cafe_app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@cafe_app.route("/random", methods=["GET"])
def random_cafe():
    get_cafes = Cafe.query.all()
    random_cafe = random.choice(get_cafes)
    print(type(random_cafe))
    return jsonify(cafe=random_cafe.to_dict())


@cafe_app.route("/all", methods=["GET"])
def all_cafes():
    all_cafes = Cafe.query.all()
    cafes = []
    for cafe in all_cafes:
        cafes.append(cafe.to_dict())
    return jsonify(coffees=cafes)

@cafe_app.route("/search", methods=["GET"])
def search():
    search_param = request.args["loc"]
    searched_cafe = db.session.query(Cafe).filter_by(location=search_param).first()
    if searched_cafe:
        return jsonify(searched_cafe.to_dict())
    else:
        return jsonify(error={"NOT FOUND": "Sorry, did not find anything here."})    
## HTTP POST - Create Record

@cafe_app.route("/add", methods=["POST", "GET"])
def add():
    add_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        has_sockets = bool(int(request.form.get("sockets"))),
        has_toilet = bool(int(request.form.get("toilet"))),
        has_wifi = bool(int(request.form.get("wifi"))),
        can_take_calls = bool(int(request.form.get("calls"))),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price")
        )
    db.session.add(add_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@cafe_app.route("/update-price/<int:cafe_id>", methods=["PATCH", "GET"])
def update_cafe_price(cafe_id):
    cofe_to_update = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cofe_to_update:
        new_coffee_price = request.args.get('coffee_price')
        cofe_to_update.coffee_price = new_coffee_price
        db.session.commit()
        return jsonify(response={"success": "Successuflly updated!"})
    else:
        return jsonify(error={"Sorry": "can't find any cafe...!"})

## HTTP DELETE - Delete Record

@cafe_app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    secret_key = request.args.get("api-key")
    cafe_to_delete = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe_to_delete:
        if secret_key == "TopSecretAPIKey":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successuflly deleted cafe!"})
        else: 
            return jsonify(error={"Forbiden": "You don't have privileges to delete the record!"})
    else:
        return jsonify(error={"Not ofund": "Cafe with that id doesn't exist."})
    

if __name__ == "__main__":
    cafe_app.run(debug=True)