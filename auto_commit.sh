#/bin/bash start.sh
echo '📌 Sauvegarde automatique du projet...'
git add .
git commit -m "Auto-commit $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo '✅ Sauvegarde terminée !'
