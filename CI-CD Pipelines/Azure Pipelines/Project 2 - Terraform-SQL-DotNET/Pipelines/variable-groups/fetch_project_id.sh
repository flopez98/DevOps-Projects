#!/bin/bash

# Variables
ORG_URL="$1"
ORG_NAME=$(echo $ORG_URL | awk -F'/' '{print $4}') # Fetch organization name from the URL
PAT="$2"
PROJECT_NAME="$3"

# Make the API call to fetch project details
PROJECTS_JSON=$(curl -s -u ":$PAT" "https://dev.azure.com/$ORG_NAME/_apis/projects?api-version=7.0-preview.1")

# Parse JSON to get Project ID for the given project name
PROJECT_ID=$(echo "$PROJECTS_JSON" | jq -r --arg PROJECT_NAME "$PROJECT_NAME" '.value[] | select(.name==$PROJECT_NAME) | .id')

if [ -z "$PROJECT_ID" ]; then
  echo "Project with name $PROJECT_NAME not found."
  exit 1
fi

# Output the Project ID
echo "Project ID for $PROJECT_NAME is $PROJECT_ID"

# Set the Project ID Var
echo "##vso[task.setvariable variable=Project_ID;]$PROJECT_ID"

# Optional: Write Project ID to a file
#echo "$PROJECT_ID" > project_id.txt