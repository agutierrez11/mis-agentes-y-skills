import json

def process_webhook(lead_data):
    print("Processing incoming lead via n8n webhook...")
    lead = json.loads(lead_data) if isinstance(lead_data, str) else lead_data
    print(f"Lead Name: {lead.get('name')}, Stations: {lead.get('stations')}")
    print("Status: Routed to Sales Rep Call Sheet.")
    return {"status": "success", "routing": "direct_call"}

if __name__ == '__main__':
    process_webhook({'name': 'Grupo Gasolinero Centro', 'stations': 5})
