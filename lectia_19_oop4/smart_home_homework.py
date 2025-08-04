"""
HOMEWORK - Sistem Smart Home
============================

Timp estimat: 30-45 minute
Obiective: Aplicarea tuturor conceptelor OOP învățate

Cerințe:
1. Encapsulare (atribute private/protected/publice)
2. Proprietăți (@property, setter, getter)
3. Compoziție și agregare
4. Moștenire și polimorfism
5. Validarea datelor
6. Operatori magici

Implementați un sistem de gestionare pentru o casă inteligentă cu următoarele componente:
"""

# ===== PARTEA 1: CLASA DE BAZĂ DEVICE =====
class Device:
    """
    Clasa de bază pentru toate dispozitivele inteligente
    
    Implementați:
    - Atribute private pentru: _device_id, _name, _is_online, _power_consumption
    - Atribute protected pentru: _brand, _model
    - Atribute publice pentru: installation_date
    - Proprietăți cu validare pentru name și power_consumption
    - Metode pentru conectarea/deconectarea dispozitivului
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption):
        # TODO: Implementați constructorul
        # - device_id și name să fie private
        # - brand și model să fie protected  
        # - power_consumption să fie private cu validare prin proprietate
        # - is_online să înceapă cu False
        # - installation_date să fie publică (None inițial)
        pass
    
    @property
    def name(self):
        # TODO: Returnați numele dispozitivului
        pass
    
    @name.setter
    def name(self, value):
        # TODO: Validați că numele nu este gol și are minim 3 caractere
        pass
    
    @property
    def power_consumption(self):
        # TODO: Returnați consumul de energie
        pass
    
    @power_consumption.setter
    def power_consumption(self, value):
        # TODO: Validați că consumul este pozitiv
        pass
    
    @property
    def is_online(self):
        # TODO: Returnați starea online (read-only)
        pass
    
    @property
    def status(self):
        # TODO: Proprietate calculată - returnați "Online" sau "Offline"
        pass
    
    def connect(self):
        # TODO: Conectați dispozitivul (setați is_online = True)
        pass
    
    def disconnect(self):
        # TODO: Deconectați dispozitivul (setați is_online = False)
        pass
    
    def get_info(self):
        # TODO: Returnați informații de bază despre dispozitiv
        pass
    
    def __str__(self):
        # TODO: Implementați reprezentarea string
        pass
    
    def __eq__(self, other):
        # TODO: Două dispozitive sunt egale dacă au același device_id
        pass


# ===== PARTEA 2: DISPOZITIVE SPECIFICE (MOȘTENIRE) =====

class SmartLight(Device):
    """
    Lampă inteligentă cu control de luminozitate și culoare
    
    Implementați:
    - Atribute adiționale: brightness (0-100), color, is_on
    - Proprietăți cu validare pentru brightness
    - Metode pentru aprindere/stingere și schimbarea culorii
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, color="white"):
        # TODO: Apelați constructorul părinte și inițializați atributele specifice
        # - brightness să înceapă cu 50
        # - is_on să înceapă cu False
        pass
    
    @property
    def brightness(self):
        # TODO: Returnați luminozitatea
        pass
    
    @brightness.setter
    def brightness(self, value):
        # TODO: Validați că brightness este între 0 și 100
        pass
    
    def turn_on(self):
        # TODO: Aprindeți lumina
        pass
    
    def turn_off(self):
        # TODO: Stingeți lumina
        pass
    
    def change_color(self, color):
        # TODO: Schimbați culoarea (doar dacă lumina e aprinsă)
        pass
    
    def get_info(self):
        # TODO: Suprascrieti metoda pentru informații specifice
        pass


class SmartThermostat(Device):
    """
    Termostat inteligent cu control de temperatură
    
    Implementați:
    - Atribute: current_temp, target_temp, mode (heating/cooling/off)
    - Proprietăți cu validare pentru target_temp (10-35°C)
    - Metode pentru setarea temperaturii și modului
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, current_temp=20):
        # TODO: Implementați constructorul
        # - target_temp să înceapă cu 22
        # - mode să înceapă cu "off"
        pass
    
    @property
    def target_temp(self):
        # TODO: Returnați temperatura țintă
        pass
    
    @target_temp.setter
    def target_temp(self, value):
        # TODO: Validați că temperatura este între 10 și 35
        pass
    
    def set_mode(self, mode):
        # TODO: Setați modul (heating/cooling/off)
        pass
    
    def adjust_temperature(self):
        # TODO: Simulați ajustarea temperaturii actuale către țintă
        pass
    
    def get_info(self):
        # TODO: Suprascrieti pentru informații specifice
        pass


class SecurityCamera(Device):
    """
    Cameră de securitate cu înregistrare
    
    Implementați:
    - Atribute: is_recording, storage_used (GB), max_storage
    - Proprietăți pentru storage_used cu validare
    - Metode pentru începerea/oprirea înregistrării
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, max_storage=64):
        # TODO: Implementați constructorul
        # - is_recording să înceapă cu False
        # - storage_used să înceapă cu 0
        pass
    
    @property
    def storage_used(self):
        # TODO: Returnați storage-ul folosit
        pass
    
    @storage_used.setter
    def storage_used(self, value):
        # TODO: Validați că nu depășește max_storage
        pass
    
    @property
    def storage_available(self):
        # TODO: Proprietate calculată - returnați spațiul disponibil
        pass
    
    def start_recording(self):
        # TODO: Începeți înregistrarea (doar dacă e spațiu disponibil)
        pass
    
    def stop_recording(self):
        # TODO: Opriți înregistrarea
        pass
    
    def clear_storage(self):
        # TODO: Ștergeți înregistrările (storage_used = 0)
        pass
    
    def get_info(self):
        # TODO: Suprascrieti pentru informații specifice
        pass


# ===== PARTEA 3: CAMERĂ (COMPOZIȚIE) =====

class Room:
    """
    Cameră care CREEAZĂ și GESTIONEAZĂ propriile dispozitive
    
    Implementați compoziția - camera creează dispozitivele în constructor
    """
    
    def __init__(self, name, room_type):
        # TODO: Implementați constructorul
        # - name și room_type să fie publice
        # - devices să fie o listă goală (camera va crea dispozitivele)
        pass
    
    def add_device(self, device_type, device_id, name, brand, model, power_consumption, **kwargs):
        """
        Creează și adaugă un dispozitiv în cameră
        
        Args:
            device_type: tipul dispozitivului ("light", "thermostat", "camera")
            **kwargs: parametri specifici pentru fiecare tip
        """
        # TODO: Implementați logica de creare a dispozitivelor
        # - Creați dispozitivul corespunzător în funcție de device_type
        # - Adăugați-l în lista devices
        pass
    
    def get_device_by_id(self, device_id):
        # TODO: Găsiți dispozitivul după ID
        pass
    
    def connect_all_devices(self):
        # TODO: Conectați toate dispozitivele din cameră
        pass
    
    def disconnect_all_devices(self):
        # TODO: Deconectați toate dispozitivele din cameră
        pass
    
    def get_total_power_consumption(self):
        # TODO: Calculați consumul total de energie din cameră
        pass
    
    def get_room_info(self):
        # TODO: Returnați informații despre cameră și dispozitivele ei
        pass
    
    def __str__(self):
        # TODO: Implementați reprezentarea string
        pass


# ===== PARTEA 4: CASĂ INTELIGENTĂ (AGREGARE) =====

class SmartHome:
    """
    Casa inteligentă care GESTIONEAZĂ camere create în exterior
    
    Implementați agregarea - casa primește camere deja create
    """
    
    def __init__(self, address):
        # TODO: Implementați constructorul
        # - address să fie publică
        # - rooms să fie o listă goală
        # - _total_devices să fie privat (contorizează numărul total de dispozitive)
        pass
    
    def add_room(self, room):
        # TODO: Adăugați o cameră existentă în casă
        # - Validați că room este instanță de Room
        # - Actualizați _total_devices
        pass
    
    def remove_room(self, room_name):
        # TODO: Eliminați camera cu numele specificat
        # - Actualizați _total_devices
        pass
    
    def get_room_by_name(self, room_name):
        # TODO: Găsiți camera după nume
        pass
    
    def get_all_devices(self):
        # TODO: Returnați toate dispozitivele din toate camerele
        pass
    
    def get_online_devices(self):
        # TODO: Returnați doar dispozitivele online
        pass
    
    def connect_all_devices(self):
        # TODO: Conectați toate dispozitivele din casă
        pass
    
    def disconnect_all_devices(self):
        # TODO: Deconectați toate dispozitivele din casă
        pass
    
    @property
    def total_devices(self):
        # TODO: Returnați numărul total de dispozitive (read-only)
        pass
    
    @property
    def total_power_consumption(self):
        # TODO: Proprietate calculată - consumul total de energie
        pass
    
    def get_home_status(self):
        # TODO: Returnați statusul general al casei
        pass
    
    def __str__(self):
        # TODO: Implementați reprezentarea string
        pass


# ===== PARTEA 5: TESTARE =====

def test_smart_home_system():
    """Funcția de testare a întregului sistem"""
    
    print("🏠 TESTAREA SISTEMULUI SMART HOME")
    print("=" * 50)
    
    # 1. Creăm casa
    casa = SmartHome("Str. Viitorului 123")
    
    # 2. Creăm camerele (cu dispozitive - compoziție)
    living = Room("Living Room", "living")
    living.add_device("light", "L001", "Living Light", "Philips", "Hue", 10, color="warm_white")
    living.add_device("thermostat", "T001", "Living Thermostat", "Nest", "3rd Gen", 5, current_temp=22)
    
    bedroom = Room("Bedroom", "bedroom")
    bedroom.add_device("light", "L002", "Bedroom Light", "IKEA", "Tradfri", 8, color="blue")
    bedroom.add_device("camera", "C001", "Bedroom Camera", "Ring", "Indoor", 3, max_storage=32)
    
    kitchen = Room("Kitchen", "kitchen")
    kitchen.add_device("light", "L003", "Kitchen Light", "Philips", "Hue", 12, color="white")
    
    # 3. Adăugăm camerele în casă (agregare)
    casa.add_room(living)
    casa.add_room(bedroom)
    casa.add_room(kitchen)
    
    # 4. Testări diverse
    print(f"Casa are {casa.total_devices} dispozitive")
    print(f"Consum total: {casa.total_power_consumption}W")
    
    # 5. Conectăm toate dispozitivele
    casa.connect_all_devices()
    
    # 6. Testăm funcționalități specifice
    living_light = living.get_device_by_id("L001")
    living_light.turn_on()
    living_light.brightness = 80
    living_light.change_color("red")
    
    bedroom_camera = bedroom.get_device_by_id("C001")
    bedroom_camera.start_recording()
    bedroom_camera.storage_used = 10
    
    # 7. Afișăm statusul final
    print("\n" + casa.get_home_status())
    
    print("\n✅ Testarea s-a finalizat cu succes!")


# ===== PARTEA 6: EXERCIȚII BONUS =====

"""
EXERCIȚII BONUS (opționale):

1. Implementați o metodă în SmartHome care găsește dispozitivul cu cel mai mare consum
2. Adăugați o proprietate în Room care returnează True dacă toate dispozitivele sunt online
3. Implementați operatorul __len__ pentru SmartHome să returneze numărul de camere
4. Creați o metodă în SmartHome care generează un raport detaliat cu toate dispozitivele grupate pe camere
5. Implementați validarea ca un dispozitiv să nu poată fi adăugat în mai multe camere simultan

CRITERII DE EVALUARE:
- Encapsulare corectă (private, protected, public) - 20 puncte
- Proprietăți cu validare implementate corect - 20 puncte  
- Compoziție implementată corect în Room - 20 puncte
- Agregare implementată corect în SmartHome - 20 puncte
- Moștenire și polimorfism funcțional - 20 puncte

TOTAL: 100 puncte
Timp recomandat: 30-45 minute
"""

if __name__ == "__main__":
    # Rulați testarea când implementarea este completă
    test_smart_home_system()
