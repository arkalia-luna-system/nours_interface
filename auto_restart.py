import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("♻️ Changement détecté, redémarrage du serveur Flask...")
        os.system("pkill -f 'python3 app.py'")  # Tue le processus existant
        subprocess.Popen(["python3", "app.py"])  # Relance Flask

if __name__ == "__main__":
    observer = Observer()
    event_handler = RestartHandler()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print("👀 Surveillance des fichiers activée...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()