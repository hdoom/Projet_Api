from flask import Flask, jsonify, redirect
from opensky_api import OpenSkyApi
from typing import List, Dict
import time

app = Flask(__name__)

def get_aircraft_data() -> List[Dict]:
    api = OpenSkyApi()
    aircraft_list = []
    
    try:
        states = api.get_states()
        if states and states.states:
            for state in states.states:
                aircraft_list.append({
                    "name_avion": state.callsign.strip() if state.callsign else "Unknown",
                    "lat": state.latitude,
                    "long": state.longitude
                })
        return aircraft_list
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/avion')
def get_avions():
    # Add CORS headers
    response = jsonify(get_aircraft_data())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def redirect_to_avions():
    return redirect('/avion')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
