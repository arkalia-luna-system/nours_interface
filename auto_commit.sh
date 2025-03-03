#/bin/bash start.sh
echo '📌 Sauvegarde automatique du projet...'
git add .
commit_message="Auto-commit $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_message"
git push origin main
echo "✅ Sauvegarde terminée à $(date '+%H:%M:%S')" | tee -a logs/actions.log
