#!bin/bash
echo "test"
# Pfad zum alternativen Konfigurationsordner
CONFIG_DIR="streamlit/"

# Zielverzeichnis für Streamlit-Konfiguration
STREAMLIT_DIR=".streamlit/"

# Überprüfen, ob der alternative Konfigurationsordner existiert
if [ -d "$CONFIG_DIR" ]; then
    # Erstellen des .streamlit-Verzeichnisses, falls es nicht existiert
    mkdir -p $STREAMLIT_DIR
    
    # Kopieren der Konfigurationsdateien in das .streamlit-Verzeichnis
    cp -r $CONFIG_DIR/* $STREAMLIT_DIR/
fi

# Starten der Streamlit-App
python -m streamlit run bot_page.py --server.port 8000 --server.address 0.0.0.0