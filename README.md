# Netbox-RDP Plugin 🎉

Willkommen zum **Netbox-RDP Plugin**! Dieses Plugin ermöglicht es dir, direkt aus der Geräteübersicht von Netbox eine RDP-Sitzung zu starten. 🚀

## Funktionen ✨

- 🖥️ **Direkte RDP-Verbindung**: Erstelle RDP-Verbindungen direkt aus der Geräteübersicht.
- 🔗 **Einfacher Zugriff**: Klicke einfach auf das RDP-Icon, um die Verbindung zu starten.
- ⚙️ **Einfache Konfiguration**: Leicht zu installieren und zu konfigurieren.

## Installation 📦

1. **Plugin herunterladen**:
   ```bash
   git clone https://github.com/malte325/netbox-rdp.git
   ```

2. **Plugin registrieren**:
   Füge `netbox_rdp` zur `PLUGINS`-Liste in deiner `configuration.py` hinzu:
   ```python
   PLUGINS = [
       'netbox_rdp',
   ]
   ```

3. **Statische Dateien sammeln**:
   ```bash
   python manage.py collectstatic
   ```

4. **Netbox neu starten**:
   ```bash
   sudo systemctl restart netbox
   ```

## Nutzung 📖

Nach der Installation findest du in der Geräteübersicht ein neues RDP-Icon. Klicke darauf, um eine RDP-Verbindung zu dem Gerät herzustellen. 🌐

## Beispiel 📸

![RDP Icon Beispiel](static/netbox_rdp/rdp_icon.png)

## Entwicklung 🛠️

Falls du zur Entwicklung beitragen möchtest, folge diesen Schritten:

1. **Repository klonen**:
   ```bash
   git clone https://github.com/malte325/netbox-rdp.git
   ```

2. **Virtuelle Umgebung erstellen**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Entwicklungsserver starten**:
   ```bash
   python manage.py runserver
   ```

## Lizenz 📄

Dieses Projekt steht unter der [MIT Lizenz](LICENSE).

## Kontakt 📬

Bei Fragen oder Problemen, erstelle bitte ein Issue im [GitHub Repository](https://github.com/malte325/netbox-rdp/issues).

---

Vielen Dank für die Nutzung des Netbox-RDP Plugins! 🎉
