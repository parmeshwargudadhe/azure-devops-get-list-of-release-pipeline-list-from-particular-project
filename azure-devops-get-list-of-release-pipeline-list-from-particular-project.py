from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import requests
import pprint

# Replace with your actual Azure DevOps organization URL and PAT
organization_url = "https://vsrm.dev.azure.com/dostorg"
personal_access_token = ""

# Project names list
project_names = [
    "Project One",
    "My Project Two",
    # ... (add others as needed)
]

# Auth for requests
auth = ('' , personal_access_token)

# Loop over all projects
for project in project_names:
    # Release pipeline REST API endpoint (vsrm for releases)
    url = f"{organization_url}/{project}/_apis/release/definitions?api-version=7.0"

    response = requests.get(url, auth=auth)

    print(f"\n🔹 Project: {project}")

    if response.status_code == 200:
        data = response.json()
        definitions = data.get('value', [])
        if definitions:
            for d in definitions:
                print(f"  - {d['name']}")
        else:
            print("  No release pipelines found.")
    else:
        print(f"  ⚠️ Failed to fetch release pipelines (HTTP {response.status_code})")
