from flask import Flask, render_template, request

app = Flask(__name__)

UNITS = {
    "length": {
        "метры": 1,
        "километры": 1000,
        "сантиметры": 0.01,
        "миллиметры": 0.001,
        "мили": 1609.34
    },

    "mass": {
        "килограммы": 1,
        "граммы": 0.001,
        "фунты": 0.453592,
        "тонны": 1000
    },

    "time": {
        "секунды": 1,
        "минуты": 60,
        "часы": 3600,
        "дни": 86400
    },

    "volume": {
        "литры": 1,
        "миллилитры": 0.001,
        "кубические метры": 1000
    }
}


def convert(category, value, from_unit, to_unit):
    base_value = value * UNITS[category][from_unit]
    result = base_value / UNITS[category][to_unit]
    return round(result, 6)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    category = "length"
    value = ""
    from_unit = ""
    to_unit = ""

    if request.method == "POST":

        category = request.form["category"]
        value = request.form["value"]
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert(
            category,
            float(value),
            from_unit,
            to_unit
        )

    return render_template(
        "index.html",
        units=UNITS,
        result=result,
        selected_category=category,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
