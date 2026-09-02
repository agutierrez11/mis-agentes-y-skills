import json
import argparse

def generate_workflow(name, crm, webhook_path):
    workflow_json = {
        "name": f"Universal Sales Pipeline - {name}",
        "nodes": [
            {
                "parameters": {"path": webhook_path, "responseMode": "onReceived"},
                "name": "Webhook Intake",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1
            },
            {
                "parameters": {"crmName": crm, "action": "upsertContact"},
                "name": f"Sync to {crm}",
                "type": "n8n-nodes-base.crm",
                "typeVersion": 1
            }
        ],
        "connections": {}
    }
    print(f"Generated n8n Workflow JSON for '{name}' with CRM '{crm}'.")
    return json.dumps(workflow_json, indent=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="n8n Workflow Generator")
    parser.add_argument("--name", default="B2B Lead Pipeline", help="Workflow name")
    parser.add_argument("--crm", default="HubSpot", help="Target CRM")
    parser.add_argument("--webhook", default="lead-intake", help="Webhook path")
    args = parser.parse_args()
    print(generate_workflow(args.name, args.crm, args.webhook))
