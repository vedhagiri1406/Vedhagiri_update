from Vedhagiri_update.flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
app.config["SECRET_KEY"] = "supersecretkey123"

db = SQLAlchemy(app)

# ─── Model ─────────────────────────────
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

# ─── Class Based CRUD View ─────────────
class UserAPI(MethodView):
    def get(self):
        user_id = request.args.get("id")
        if user_id:
            user = User.query.get_or_404(user_id)
            return jsonify({"id": user.id, "name": user.name, "age": user.age})
        users = User.query.all()
        return jsonify([{"id": u.id, "name": u.name, "age": u.age} for u in users])

    def post(self):
        data = request.json
        new_user = User(name=data["name"], age=data["age"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created", "id": new_user.id}), 201

    def patch(self):
        data = request.json
        user = User.query.get_or_404(data["id"])
        user.name = data.get("name", user.name)
        user.age = data.get("age", user.age)
        db.session.commit()
        return jsonify({"message": "User updated"})

    def delete(self):
        data = request.json
        user = User.query.get_or_404(data["id"])
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"})

# ─── Register Route ─────────────────────
user_view = UserAPI.as_view("user_api")
app.add_url_rule("/api/user", view_func=user_view, methods=["GET", "POST", "PATCH", "DELETE"])

# ─── Initialize DB on startup ──────────
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
