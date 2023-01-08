from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from calorie_app.calorie import Calorie
from calorie_app.temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieAppPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template("calories_form_page.html", caloriesform=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)

        temperature = Temperature(calorie_form.country.data, calorie_form.city.data).get()

        calorie = Calorie(weight=calorie_form.weight.data, height=calorie_form.height.data, age=calorie_form.age.data,
                           temperature=temperature)

        calories = calorie.calculate()

        return render_template("calories_form_page.html", result=True, caloriesform=calorie_form,
                               calories=calories)


class CalorieForm(Form):
    weight = StringField("Weight: ", default="80")
    height = StringField("Height: ", default="180")
    age = StringField("Age: ", default="25")
    city = StringField("City: ", default="London")
    country = StringField("Country: ", default="Uk")
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form_page', view_func=CalorieAppPage.as_view('calories_form_page'))

app.run(debug=True)
