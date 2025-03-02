#!/bin/bash

echo "🔧 Nettoyage des ports..."
pkill -9 uvicorn
pkill -9 python
sleep 2

echo "🚀 Vérification des processus encore actifs..."
ps aux | grep uvicorn
ps aux | grep python

echo "🛠 Activation de l'environnement virtuel..."
source venv/bin/activate

echo "🚀 Lancement de FastAPI sur un port dynamique..."
python app.py