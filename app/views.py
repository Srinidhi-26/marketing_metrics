from flask import Flask, request, jsonify, Blueprint
from datetime import datetime
from datetime import date, timedelta
import random
from .models import db, MarketingMetrics
from .utils import calculate_metrics, fetch_external_data

app = Flask(__name__)

metrics_api = Blueprint("metrics_api", __name__, url_prefix="/metrics")


@metrics_api.route('/', methods=['GET'])
def get_metrics():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Please provide both start_date and end_date"}), 400

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    db_data = MarketingMetrics.query.filter(MarketingMetrics.start_date >= start_date, MarketingMetrics.end_date <= end_date).all()
    db_data = [data.to_dict() for data in db_data]

    api_data1 = fetch_external_data('api1', start_date, end_date)  
    api_data2 = fetch_external_data('api2', start_date, end_date)  


    aggregated_data = calculate_metrics(db_data, api_data1, api_data2)

    return jsonify({
        "database_data": db_data,
        "api_data_1": api_data1,
        "api_data_2": api_data2,
        "aggregated_data": aggregated_data
    })


@metrics_api.route('/insert_data', methods=['POST'])
def insert_random_data():
    for _ in range(30):
        start_date = date.today() - timedelta(days=random.randint(1, 100))
        end_date = start_date + timedelta(days=random.randint(1, 30))
        clicks = random.randint(0, 1000)
        impressions = random.randint(1000, 10000)
        cost = round(random.uniform(50.0, 1000.0), 2)

        new_metric = MarketingMetrics(
            start_date=start_date,
            end_date=end_date,
            clicks=clicks,
            impressions=impressions,
            cost=cost
        )
        db.session.add(new_metric)

    db.session.commit()
    
    return jsonify({'message': 'Inserted random data into marketing_metrics table'}), 201
