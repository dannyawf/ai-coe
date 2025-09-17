#!/bin/bash

# Script to replace Microsoft Teams references with Google Chat
echo "Replacing Microsoft Teams references with Google Chat..."

# Replace Teams channel references with Google Chat
find docs -type f -name "*.md" -exec sed -i '' \
  -e 's/Teams channels/canales de Google Chat/g' \
  -e 's/Teams channel/canal de Google Chat/g' \
  -e 's/canal Teams/canal de Google Chat/g' \
  -e 's/Canal Teams/Canal de Google Chat/g' \
  -e 's/Microsoft Teams/Google Chat/g' \
  -e 's/MS Teams/Google Chat/g' \
  -e 's/Teams corporativo/Google Chat corporativo/g' \
  -e 's/AI Champions Community (Teams)/AI Champions Community (Google Chat)/g' \
  -e 's/Métricas de Teams\/Slack/Métricas de Google Chat\/Slack/g' \
  -e 's/AI Champions Community en Teams/AI Champions Community en Google Chat/g' \
  -e 's/#ai-governance en Teams/#ai-governance en Google Chat/g' \
  -e 's/Canales de Slack\/Teams/Canales de Slack\/Google Chat/g' \
  -e 's/Zoom\/Teams Setup/Zoom\/Google Chat Setup/g' \
  -e 's/Teams:/#Google Chat:/g' \
  -e 's/<h4>Teams<\/h4>/<h4>Google Chat<\/h4>/g' \
  -e 's/Canal CoE-IA/Canal CoE-IA en Google Chat/g' \
  -e 's/Foro de Dudas": Canal Teams dedicado/Foro de Dudas": Canal Google Chat dedicado/g' \
  -e 's/Teams": Canal/Google Chat": Canal/g' \
  -e 's/Teams":/Google Chat":/g' \
  -e 's/hybrid human-AI teams/hybrid human-AI teams/g' \
  {} \;

# Update specific Teams community references
find docs -type f -name "*.md" -exec sed -i '' \
  -e 's/Teams: Nova-Cell Community/Google Chat: Nova-Cell Community/g' \
  -e 's/Teams: #model-risk-management/Google Chat: #model-risk-management/g' \
  -e 's/Teams: Canal #ai-opportunities/Google Chat: Canal #ai-opportunities/g' \
  -e 's/Teams: Canal #roi-iniciativas-ia/Google Chat: Canal #roi-iniciativas-ia/g' \
  -e 's/Teams: Canal #aisia-evaluaciones/Google Chat: Canal #aisia-evaluaciones/g' \
  {} \;

# Update the config variable names to be more clear
sed -i '' \
  -e 's/^  teams:$/  google_chat:/g' \
  -e 's/{{TEAMS_URL}}/{{GCHAT_URL}}/g' \
  -e 's/{{TEAMS_CHANNEL}}/{{GCHAT_CHANNEL}}/g' \
  config/variables.yaml

# Update the replace_variables script
sed -i '' \
  -e "s/'teams' in self.variables\['communication'\]/'google_chat' in self.variables['communication']/g" \
  -e "s/self.variables\['communication'\]\['teams'\]/self.variables['communication']['google_chat']/g" \
  -e "s/{{TEAMS_URL}}/{{GCHAT_URL}}/g" \
  -e "s/{{TEAMS_CHANNEL}}/{{GCHAT_CHANNEL}}/g" \
  scripts/replace_variables.py

# Update the start-here.md Teams link
sed -i '' \
  -e 's|https://teams.microsoft.com/l/channel/coe-ia|https://chat.google.com/room/AAQAugDuKpE?cls=1|g' \
  docs/start-here.md

# Update VARIABLES_USAGE_GUIDE.md
sed -i '' \
  -e 's/Teams: 2 variables/Google Chat: 2 variables/g' \
  docs/VARIABLES_USAGE_GUIDE.md

echo "Replacement completed!"
echo "Files modified:"
grep -l "Google Chat" docs/**/*.md docs/*.md config/variables.yaml scripts/replace_variables.py 2>/dev/null | wc -l
echo "instances replaced."