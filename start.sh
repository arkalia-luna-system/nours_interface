#!/bin/bash
echo "🚀 Démarrage de l'environnement virtuel..."
source venv/bin/activate

echo "🔄 Arrêt des anciens serveurs Flask..."
pkill -f flask

echo "🔥 Lancement du serveur Flask..."
python3 app.py