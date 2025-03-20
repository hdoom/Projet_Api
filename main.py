from flask import Flask, jsonify, redirect
from opensky_api import OpenSkyApi
from typing import List, Dict
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_aircraft_data() -> List[Dict]:
    api = OpenSkyApi()
    aircraft_list = []
    
    try:
        states = api.get_states()
        if not states or not states.states:
            logger.warning("No aircraft states received from OpenSky API")
            return []
            
        for state in states.states:
            aircraft_list.append({
                "name_avion": state.callsign.strip() if state.callsign else "Unknown",
                "lat": state.latitude,
                "long": state.longitude
            })
        return aircraft_list
    except Exception as e:
        logger.error(f"Error fetching data from OpenSky API: {e}")
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
    # In production, use Gunicorn instead of the Flask development server
    app.run(host='0.0.0.0', port=5001)
