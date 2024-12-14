import subprocess
import time
import tkinter as tk
from tkinter import ttk

# Funktion zum Deaktivieren des WLAN-Adapters
def disable_network_adapter():
    adapter_name = "WLAN"  # Hier den richtigen Namen verwenden
    subprocess.run(["netsh", "interface", "set", "interface", adapter_name, "disabled"])
    print(f"{adapter_name} wurde deaktiviert")

# Funktion zum Aktivieren des WLAN-Adapters
def enable_network_adapter():
    adapter_name = "WLAN"  # Hier den richtigen Namen verwenden
    subprocess.run(["netsh", "interface", "set", "interface", adapter_name, "enabled"])
    print(f"{adapter_name} wurde aktiviert")

# Funktion für den Lag-Switch (Deaktivieren und Wiederherstellen der Verbindung)
def lag_switch(duration):
    disable_network_adapter()
    print("Internet deaktiviert.")
    time.sleep(duration)  # Warten für die angegebene Dauer
    enable_network_adapter()
    print("Internet wieder aktiviert.")

# Funktion, um den Lag-Switch mit der vom Benutzer gewählten Dauer zu starten
def on_start_button_click():
    try:
        # Dauer aus der Auswahl des Dropdowns holen
        selected_duration = int(duration_combobox.get())
        lag_switch(selected_duration)
    except ValueError:
        print("Bitte wählen Sie eine gültige Zeitdauer aus.")

# GUI erstellen
def create_gui():
    # Fenster für das GUI
    root = tk.Tk()
    root.title("Lag Switch")

    # Label für die Auswahl der Dauer
    label = tk.Label(root, text="Wählen Sie die Dauer, für die das Internet deaktiviert wird:")
    label.pack(pady=10)

    # Dropdown-Menü (Combobox) mit den Optionen für die Dauer
    durations = ["1", "3", "5", "10", "15", "30"]  # Mögliche Zeitdauern in Sekunden
    global duration_combobox
    duration_combobox = ttk.Combobox(root, values=durations, state="readonly")
    duration_combobox.set("10")  # Standardwert auf 10 Sekunden setzen
    duration_combobox.pack(pady=10)

    # Button, um den Lag-Switch zu starten
    start_button = tk.Button(root, text="Lag Switch starten", command=on_start_button_click)
    start_button.pack(pady=20)

    # Fenster anzeigen
    root.mainloop()

# GUI starten
if __name__ == "__main__":
    create_gui()
