from flask import Flask, jsonify, render_template
from flask_cors import CORS
from core.memory import get_all_conversations
from tools.system import get_system_info, get_current_time
from config.settings import DASHBOARD_PORT

app = Flask(__name__)
CORS(app)

friday_status = {"online": True, "last_agent": "None", "last_query": "Waiting..."}


def update_status(agent: str, query: str):
    friday_status["last_agent"] = agent
    friday_status["last_query"] = query


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify(friday_status)


@app.route("/api/conversations")
def conversations():
    data = get_all_conversations()
    return jsonify(data)


@app.route("/api/system")
def system():
    info = get_system_info()
    info["time"] = get_current_time()
    return jsonify(info)


def start_dashboard():
    app.run(host="0.0.0.0", port=DASHBOARD_PORT, debug=False, use_reloader=False)
