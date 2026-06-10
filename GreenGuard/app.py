from flask import Flask, render_template, request, redirect
import json
import heapq
import os

app = Flask(__name__)

FILE_NAME = "plants.json"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def load_plants():
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_plants(plants):
    with open(FILE_NAME, "w") as f:
        json.dump(plants, f, indent=4)


@app.route("/")
def home():
    plants = load_plants()

    total_plants = len(plants)

    reminder_queue = []

    for plant in plants:
        heapq.heappush(reminder_queue,
                       (plant["water_freq"], plant["name"]))

    reminders = []

    while reminder_queue:
        reminders.append(heapq.heappop(reminder_queue)[1])

    return render_template(
        "index.html",
        plants=plants,
        reminders=reminders,
        total_plants=total_plants
    )


@app.route("/add", methods=["POST"])
def add():
    plants = load_plants()

    plant = {
        "id": request.form["id"],
        "name": request.form["name"],
        "type": request.form["type"],
        "water_freq": int(request.form["water_freq"])
    }

    plants.append(plant)

    save_plants(plants)

    return redirect("/")


@app.route("/search", methods=["POST"])
def search():

    search_id = request.form["search_id"]

    plants = load_plants()

    result = None

    for plant in plants:

        if plant["id"] == search_id:
            result = plant
            break

    reminder_queue = []

    for plant in plants:
        heapq.heappush(reminder_queue,
                       (plant["water_freq"], plant["name"]))

    reminders = []

    while reminder_queue:
        reminders.append(heapq.heappop(reminder_queue)[1])

    return render_template(
        "index.html",
        plants=plants,
        reminders=reminders,
        result=result,
        total_plants=len(plants)
    )


@app.route("/doctor", methods=["POST"])
def doctor():

    symptom = request.form["symptom"]

    solutions = {

        "Yellow Leaves":
            ("Overwatering",
             "Reduce watering frequency"),

        "Brown Spots":
            ("Fungal Infection",
             "Use fungicide"),

        "Slow Growth":
            ("Lack of Nutrients",
             "Add fertilizer")
    }

    cause, solution = solutions[symptom]

    plants = load_plants()

    reminder_queue = []

    for plant in plants:
        heapq.heappush(reminder_queue,
                       (plant["water_freq"], plant["name"]))

    reminders = []

    while reminder_queue:
        reminders.append(heapq.heappop(reminder_queue)[1])

    return render_template(
        "index.html",
        plants=plants,
        reminders=reminders,
        cause=cause,
        solution=solution,
        total_plants=len(plants)
    )


if __name__ == "__main__":
    app.run(debug=True)