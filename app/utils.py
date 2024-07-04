import requests
import json

API_URLS = {
    'api1': 'https://68dbab736d5a44b6b1c33c4a5c94231e.api.mockbin.io/',
    'api2': 'https://e2e57615968f4859aa105dfe5e4dc6fb.api.mockbin.io/',
}

def fetch_external_data(api_key, start_date, end_date):
    api_url = API_URLS.get(api_key)
    if not api_url:
        return {"error": f"API key '{api_key}' not found."}

    response = requests.get(api_url, params={"start_date": start_date, "end_date": end_date})
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, dict):
            data = [data]
        return data
    else:
        return {"error": f"Failed to fetch data from {api_url}"}
    

def calculate_metrics(db_data, api_data1, api_data2):
    total_clicks = total_impressions = total_cost = 0

    all_data = db_data + api_data1 + api_data2

    for data in all_data:
        total_clicks += data.get('clicks', 0)
        total_impressions += data.get('impressions', 0)
        total_cost += data.get('cost', 0)

    cpc = total_cost / total_clicks if total_clicks else 0
    ctr = total_clicks / total_impressions if total_impressions else 0

    return {
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "total_cost": total_cost,
        "cpc": cpc,
        "ctr": ctr
    }
