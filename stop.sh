#/bin/bash start.sh
echo '🛑 Arrêt du projet et nettoyage des processus...'
pkill -f uvicorn
echo '✅ Serveur arrêté proprement.'
