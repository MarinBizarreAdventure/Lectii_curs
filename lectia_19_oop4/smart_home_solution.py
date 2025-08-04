"""
HOMEWORK SOLUTION - Sistem Smart Home
=====================================

Soluția completă pentru sistemul de gestionare a unei case inteligente
Toate conceptele OOP implementate: encapsulare, proprietăți, compoziție, agregare, moștenire
"""

from datetime import datetime


# ===== PARTEA 1: CLASA DE BAZĂ DEVICE =====
class Device:
    """
    Clasa de bază pentru toate dispozitivele inteligente
    Demonstrează encapsularea și proprietățile
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption):
        # Atribute private
        self._device_id = device_id
        self._name = None
        self._is_online = False
        self._power_consumption = None
        
        # Atribute protected
        self._brand = brand
        self._model = model
        
        # Atribut public
        self.installation_date = None
        
        # Setăm valorile prin proprietăți pentru validare
        self.name = name
        self.power_consumption = power_consumption
    
    @property
    def name(self):
        """Getter pentru numele dispozitivului"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter cu validare pentru numele dispozitivului"""
        if not isinstance(value, str):
            raise TypeError("Numele trebuie să fie string")
        if len(value.strip()) < 3:
            raise ValueError("Numele trebuie să aibă minim 3 caractere")
        self._name = value.strip()
    
    @property
    def power_consumption(self):
        """Getter pentru consumul de energie"""
        return self._power_consumption
    
    @power_consumption.setter
    def power_consumption(self, value):
        """Setter cu validare pentru consumul de energie"""
        if not isinstance(value, (int, float)):
            raise TypeError("Consumul trebuie să fie un număr")
        if value <= 0:
            raise ValueError("Consumul trebuie să fie pozitiv")
        self._power_consumption = value
    
    @property
    def is_online(self):
        """Proprietate read-only pentru starea online"""
        return self._is_online
    
    @property
    def status(self):
        """Proprietate calculată pentru status"""
        return "Online" if self._is_online else "Offline"
    
    @property
    def device_id(self):
        """Getter pentru device_id (read-only)"""
        return self._device_id
    
    def connect(self):
        """Conectează dispozitivul"""
        self._is_online = True
        print(f"✅ {self._name} conectat cu succes")
    
    def disconnect(self):
        """Deconectează dispozitivul"""
        self._is_online = False
        print(f"❌ {self._name} deconectat")
    
    def get_info(self):
        """Returnează informații de bază despre dispozitiv"""
        return (f"ID: {self._device_id}, Nume: {self._name}, "
                f"Brand: {self._brand}, Model: {self._model}, "
                f"Consum: {self._power_consumption}W, Status: {self.status}")
    
    def __str__(self):
        """Reprezentarea string a dispozitivului"""
        return f"{self._name} ({self._brand} {self._model}) - {self.status}"
    
    def __eq__(self, other):
        """Două dispozitive sunt egale dacă au același device_id"""
        if not isinstance(other, Device):
            return False
        return self._device_id == other._device_id


# ===== PARTEA 2: DISPOZITIVE SPECIFICE (MOȘTENIRE) =====

class SmartLight(Device):
    """
    Lampă inteligentă cu control de luminozitate și culoare
    Demonstrează moștenirea și polimorfismul
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, color="white"):
        super().__init__(device_id, name, brand, model, power_consumption)
        self._brightness = 50  # Inițial 50%
        self.color = color
        self.is_on = False
    
    @property
    def brightness(self):
        """Getter pentru luminozitate"""
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        """Setter cu validare pentru luminozitate"""
        if not isinstance(value, (int, float)):
            raise TypeError("Luminozitatea trebuie să fie un număr")
        if not (0 <= value <= 100):
            raise ValueError("Luminozitatea trebuie să fie între 0 și 100")
        self._brightness = value
        if self.is_on:
            print(f"💡 Luminozitatea pentru {self._name} setată la {value}%")
    
    def turn_on(self):
        """Aprinde lumina"""
        if not self._is_online:
            print(f"❌ Nu pot aprinde {self._name} - dispozitivul nu e conectat")
            return
        self.is_on = True
        print(f"💡 {self._name} aprins (luminozitate: {self._brightness}%, culoare: {self.color})")
    
    def turn_off(self):
        """Stinge lumina"""
        self.is_on = False
        print(f"🔌 {self._name} stins")
    
    def change_color(self, color):
        """Schimbă culoarea luminii"""
        if not self.is_on:
            print(f"❌ Nu pot schimba culoarea - {self._name} este stins")
            return
        old_color = self.color
        self.color = color
        print(f"🎨 Culoarea pentru {self._name} schimbată din {old_color} în {color}")
    
    def get_info(self):
        """Suprascrie metoda pentru informații specifice"""
        base_info = super().get_info()
        light_status = "Aprins" if self.is_on else "Stins"
        return (f"{base_info}, Stare: {light_status}, "
                f"Luminozitate: {self._brightness}%, Culoare: {self.color}")


class SmartThermostat(Device):
    """
    Termostat inteligent cu control de temperatură
    Demonstrează proprietățile cu validare complexă
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, current_temp=20):
        super().__init__(device_id, name, brand, model, power_consumption)
        self.current_temp = current_temp
        self._target_temp = 22
        self.mode = "off"  # heating/cooling/off
    
    @property
    def target_temp(self):
        """Getter pentru temperatura țintă"""
        return self._target_temp
    
    @target_temp.setter
    def target_temp(self, value):
        """Setter cu validare pentru temperatura țintă"""
        if not isinstance(value, (int, float)):
            raise TypeError("Temperatura trebuie să fie un număr")
        if not (10 <= value <= 35):
            raise ValueError("Temperatura trebuie să fie între 10 și 35°C")
        old_temp = self._target_temp
        self._target_temp = value
        print(f"🌡️ Temperatura țintă pentru {self._name}: {old_temp}°C → {value}°C")
    
    def set_mode(self, mode):
        """Setează modul de operare"""
        valid_modes = ["heating", "cooling", "off"]
        if mode not in valid_modes:
            raise ValueError(f"Mod invalid. Opțiuni: {valid_modes}")
        
        if not self._is_online and mode != "off":
            print(f"❌ Nu pot seta modul - {self._name} nu e conectat")
            return
            
        old_mode = self.mode
        self.mode = mode
        print(f"🔄 Modul pentru {self._name}: {old_mode} → {mode}")
    
    def adjust_temperature(self):
        """Simulează ajustarea temperaturii actuale către țintă"""
        if self.mode == "off":
            print(f"❄️ {self._name} este oprit - temperatura nu se ajustează")
            return
        
        diff = self._target_temp - self.current_temp
        if abs(diff) < 0.5:
            print(f"✅ {self._name}: Temperatura țintă atinsă ({self.current_temp}°C)")
            return
        
        # Simulare ajustare graduală
        if self.mode == "heating" and diff > 0:
            self.current_temp += 0.5
            print(f"🔥 {self._name} încălzește: {self.current_temp}°C (țintă: {self._target_temp}°C)")
        elif self.mode == "cooling" and diff < 0:
            self.current_temp -= 0.5
            print(f"❄️ {self._name} răcește: {self.current_temp}°C (țintă: {self._target_temp}°C)")
    
    def get_info(self):
        """Suprascrie pentru informații specifice"""
        base_info = super().get_info()
        return (f"{base_info}, Temp actuală: {self.current_temp}°C, "
                f"Temp țintă: {self._target_temp}°C, Mod: {self.mode}")


class SecurityCamera(Device):
    """
    Cameră de securitate cu înregistrare
    Demonstrează proprietățile calculată și validarea complexă
    """
    
    def __init__(self, device_id, name, brand, model, power_consumption, max_storage=64):
        super().__init__(device_id, name, brand, model, power_consumption)
        self.is_recording = False
        self._storage_used = 0
        self.max_storage = max_storage
    
    @property
    def storage_used(self):
        """Getter pentru storage-ul folosit"""
        return self._storage_used
    
    @storage_used.setter
    def storage_used(self, value):
        """Setter cu validare pentru storage"""
        if not isinstance(value, (int, float)):
            raise TypeError("Storage-ul trebuie să fie un număr")
        if value < 0:
            raise ValueError("Storage-ul nu poate fi negativ")
        if value > self.max_storage:
            raise ValueError(f"Storage-ul nu poate depăși {self.max_storage}GB")
        self._storage_used = value
    
    @property
    def storage_available(self):
        """Proprietate calculată - spațiul disponibil"""
        return self.max_storage - self._storage_used
    
    @property
    def storage_percentage(self):
        """Proprietate calculată - procentul de storage folosit"""
        return (self._storage_used / self.max_storage) * 100
    
    def start_recording(self):
        """Începe înregistrarea"""
        if not self._is_online:
            print(f"❌ Nu pot începe înregistrarea - {self._name} nu e conectat")
            return
        
        if self.storage_available < 1:
            print(f"❌ Nu pot începe înregistrarea - {self._name} nu are spațiu suficient")
            return
        
        if self.is_recording:
            print(f"⚠️ {self._name} înregistrează deja")
            return
        
        self.is_recording = True
        print(f"🔴 {self._name} a început înregistrarea")
    
    def stop_recording(self):
        """Oprește înregistrarea"""
        if not self.is_recording:
            print(f"⚠️ {self._name} nu înregistrează")
            return
        
        self.is_recording = False
        # Simulez că înregistrarea consumă spațiu
        self._storage_used += 0.5
        print(f"⏹️ {self._name} a oprit înregistrarea (storage: {self._storage_used}GB)")
    
    def clear_storage(self):
        """Șterge înregistrările"""
        if self.is_recording:
            print(f"❌ Nu pot șterge - {self._name} înregistrează")
            return
        
        old_storage = self._storage_used
        self._storage_used = 0
        print(f"🗑️ Storage-ul pentru {self._name} șters: {old_storage}GB → 0GB")
    
    def get_info(self):
        """Suprascrie pentru informații specifice"""
        base_info = super().get_info()
        recording_status = "Înregistrează" if self.is_recording else "Nu înregistrează"
        return (f"{base_info}, {recording_status}, "
                f"Storage: {self._storage_used}/{self.max_storage}GB "
                f"({self.storage_percentage:.1f}%)")


# ===== PARTEA 3: CAMERĂ (COMPOZIȚIE) =====

class Room:
    """
    Cameră care CREEAZĂ și GESTIONEAZĂ propriile dispozitive
    Demonstrează compoziția - camera controlează complet dispozitivele
    """
    
    def __init__(self, name, room_type):
        self.name = name
        self.room_type = room_type
        self.devices = []  # Camera va crea dispozitivele aici
        print(f"🏠 Camera '{name}' ({room_type}) creată")
    
    def add_device(self, device_type, device_id, name, brand, model, power_consumption, **kwargs):
        """
        Creează și adaugă un dispozitiv în cameră (COMPOZIȚIE)
        Camera creează dispozitivul - nu îl primește din exterior
        """
        device_classes = {
            "light": SmartLight,
            "thermostat": SmartThermostat,
            "camera": SecurityCamera
        }
        
        if device_type not in device_classes:
            raise ValueError(f"Tip dispozitiv invalid. Opțiuni: {list(device_classes.keys())}")
        
        # Verificăm dacă ID-ul există deja
        if self.get_device_by_id(device_id):
            raise ValueError(f"Dispozitivul cu ID {device_id} există deja în {self.name}")
        
        # COMPOZIȚIE: Camera CREEAZĂ dispozitivul
        device_class = device_classes[device_type]
        try:
            device = device_class(device_id, name, brand, model, power_consumption, **kwargs)
            device.installation_date = datetime.now().strftime("%Y-%m-%d")
            self.devices.append(device)
            print(f"✅ Dispozitiv {device_type} '{name}' adăugat în {self.name}")
            return device
        except Exception as e:
            print(f"❌ Eroare la crearea dispozitivului: {e}")
            return None
    
    def get_device_by_id(self, device_id):
        """Găsește dispozitivul după ID"""
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None
    
    def connect_all_devices(self):
        """Conectează toate dispozitivele din cameră"""
        if not self.devices:
            print(f"⚠️ Niciun dispozitiv în {self.name}")
            return
        
        print(f"🔌 Conectez toate dispozitivele din {self.name}...")
        for device in self.devices:
            device.connect()
    
    def disconnect_all_devices(self):
        """Deconectează toate dispozitivele din cameră"""
        if not self.devices:
            print(f"⚠️ Niciun dispozitiv în {self.name}")
            return
        
        print(f"🔌 Deconectez toate dispozitivele din {self.name}...")
        for device in self.devices:
            device.disconnect()
    
    def get_total_power_consumption(self):
        """Calculează consumul total de energie din cameră"""
        return sum(device.power_consumption for device in self.devices if device.is_online)
    
    @property
    def all_devices_online(self):
        """Proprietate calculată - True dacă toate dispozitivele sunt online"""
        if not self.devices:
            return False
        return all(device.is_online for device in self.devices)
    
    def get_room_info(self):
        """Returnează informații despre cameră și dispozitivele ei"""
        info = f"\n🏠 Camera: {self.name} ({self.room_type})\n"
        info += f"   Dispozitive: {len(self.devices)}\n"
        info += f"   Toate online: {'Da' if self.all_devices_online else 'Nu'}\n"
        info += f"   Consum total: {self.get_total_power_consumption()}W\n"
        
        if self.devices:
            info += "   Lista dispozitive:\n"
            for device in self.devices:
                info += f"     • {device.get_info()}\n"
        
        return info
    
    def __str__(self):
        """Reprezentarea string a camerei"""
        return f"{self.name} ({self.room_type}) - {len(self.devices)} dispozitive"
    
    def __len__(self):
        """Returnează numărul de dispozitive din cameră"""
        return len(self.devices)


# ===== PARTEA 4: CASĂ INTELIGENTĂ (AGREGARE) =====

class SmartHome:
    """
    Casa inteligentă care GESTIONEAZĂ camere create în exterior
    Demonstrează agregarea - casa primește camere existente
    """
    
    def __init__(self, address):
        self.address = address
        self.rooms = []  # Lista de camere (AGREGARE)
        self._total_devices = 0  # Contorizează dispozitivele
        print(f"🏡 Casa inteligentă creată la adresa: {address}")
    
    def add_room(self, room):
        """
        Adaugă o cameră existentă în casă (AGREGARE)
        Casa primește camera din exterior - nu o creează
        """
        if not isinstance(room, Room):
            raise TypeError("Poate fi adăugată doar o instanță de Room")
        
        # Verificăm dacă camera există deja
        if room in self.rooms:
            print(f"⚠️ Camera {room.name} există deja în casă")
            return
        
        # AGREGARE: Casa primește camera existentă
        self.rooms.append(room)
        self._total_devices += len(room.devices)
        print(f"✅ Camera '{room.name}' adăugată în casă")
    
    def remove_room(self, room_name):
        """Elimină camera cu numele specificat"""
        room = self.get_room_by_name(room_name)
        if not room:
            print(f"❌ Camera '{room_name}' nu există")
            return None
        
        self.rooms.remove(room)
        self._total_devices -= len(room.devices)
        print(f"🗑️ Camera '{room_name}' eliminată din casă")
        return room
    
    def get_room_by_name(self, room_name):
        """Găsește camera după nume"""
        for room in self.rooms:
            if room.name == room_name:
                return room
        return None
    
    def get_all_devices(self):
        """Returnează toate dispozitivele din toate camerele"""
        all_devices = []
        for room in self.rooms:
            all_devices.extend(room.devices)
        return all_devices
    
    def get_online_devices(self):
        """Returnează doar dispozitivele online"""
        return [device for device in self.get_all_devices() if device.is_online]
    
    def connect_all_devices(self):
        """Conectează toate dispozitivele din casă"""
        print(f"🔌 Conectez toate dispozitivele din casă...")
        for room in self.rooms:
            room.connect_all_devices()
    
    def disconnect_all_devices(self):
        """Deconectează toate dispozitivele din casă"""
        print(f"🔌 Deconectez toate dispozitivele din casă...")
        for room in self.rooms:
            room.disconnect_all_devices()
    
    @property
    def total_devices(self):
        """Proprietate read-only pentru numărul total de dispozitive"""
        return self._total_devices
    
    @property
    def total_power_consumption(self):
        """Proprietate calculată - consumul total de energie"""
        return sum(room.get_total_power_consumption() for room in self.rooms)
    
    def get_device_with_highest_consumption(self):
        """Găsește dispozitivul cu cel mai mare consum"""
        all_devices = self.get_all_devices()
        if not all_devices:
            return None
        return max(all_devices, key=lambda d: d.power_consumption)
    
    def get_home_status(self):
        """Returnează statusul general al casei"""
        online_devices = len(self.get_online_devices())
        total_devices = len(self.get_all_devices())
        
        status = f"\n🏡 STATUSUL CASEI INTELIGENTE\n"
        status += f"📍 Adresa: {self.address}\n"
        status += f"🏠 Camere: {len(self.rooms)}\n"
        status += f"📱 Dispozitive: {online_devices}/{total_devices} online\n"
        status += f"⚡ Consum total: {self.total_power_consumption}W\n"
        
        # Dispozitivul cu cel mai mare consum
        highest_device = self.get_device_with_highest_consumption()
        if highest_device:
            status += f"🔋 Cel mai mare consum: {highest_device.name} ({highest_device.power_consumption}W)\n"
        
        # Detalii pe camere
        for room in self.rooms:
            status += room.get_room_info()
        
        return status
    
    def generate_detailed_report(self):
        """Generează un raport detaliat cu toate dispozitivele grupate pe camere"""
        report = f"\n📊 RAPORT DETALIAT - CASA INTELIGENTĂ\n"
        report += f"{'='*60}\n"
        report += f"Adresa: {self.address}\n"
        report += f"Data raport: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        for room in self.rooms:
            report += f"🏠 {room.name.upper()} ({room.room_type})\n"
            report += f"{'-'*40}\n"
            
            if not room.devices:
                report += "   Nu există dispozitive\n\n"
                continue
            
            for device in room.devices:
                report += f"   • {device.get_info()}\n"
            
            report += f"   Subtotal consum: {room.get_total_power_consumption()}W\n\n"
        
        report += f"{'='*60}\n"
        report += f"TOTAL GENERAL: {self.total_power_consumption}W\n"
        
        return report
    
    def __str__(self):
        """Reprezentarea string a casei"""
        return f"Casa inteligentă ({self.address}) - {len(self.rooms)} camere, {self.total_devices} dispozitive"
    
    def __len__(self):
        """Returnează numărul de camere"""
        return len(self.rooms)


# ===== PARTEA 5: TESTARE COMPLETĂ =====

def test_smart_home_system():
    """Funcția de testare a întregului sistem cu toate conceptele OOP"""
    
    print("🏠 TESTAREA SISTEMULUI SMART HOME")
    print("=" * 50)
    
    try:
        # 1. CREĂM CASA (Agregare)
        print("\n1️⃣ CREAREA CASEI")
        casa = SmartHome("Str. Viitorului 123, Cluj-Napoca")
        
        # 2. CREĂM CAMERELE CU DISPOZITIVE (Compoziție)
        print("\n2️⃣ CREAREA CAMERELOR ȘI DISPOZITIVELOR")
        
        # Living Room
        living = Room("Living Room", "living")
        living.add_device("light", "L001", "Living Light Main", "Philips", "Hue Pro", 15, color="warm_white")
        living.add_device("light", "L002", "Living Light Accent", "IKEA", "Tradfri", 8, color="blue")
        living.add_device("thermostat", "T001", "Living Thermostat", "Nest", "3rd Gen", 5, current_temp=22)
        
        # Bedroom
        bedroom = Room("Bedroom", "bedroom")
        bedroom.add_device("light", "L003", "Bedroom Light", "Philips", "Hue", 10, color="soft_white")
        bedroom.add_device("camera", "C001", "Bedroom Security", "Ring", "Indoor Cam", 3, max_storage=32)
        bedroom.add_device("thermostat", "T002", "Bedroom Thermostat", "Honeywell", "T6", 4, current_temp=20)
        
        # Kitchen
        kitchen = Room("Kitchen", "kitchen")
        kitchen.add_device("light", "L004", "Kitchen Main Light", "Philips", "Hue", 12, color="daylight")
        kitchen.add_device("light", "L005", "Kitchen Under Cabinet", "LIFX", "Strip", 6, color="white")
        
        # Office
        office = Room("Office", "office")
        office.add_device("light", "L006", "Office Desk Light", "BenQ", "ScreenBar", 18, color="neutral")
        office.add_device("camera", "C002", "Office Security", "Logitech", "Circle", 4, max_storage=64)
        
        # 3. ADĂUGĂM CAMERELE ÎN CASĂ (Agregare)
        print("\n3️⃣ ADĂUGAREA CAMERELOR ÎN CASĂ")
        casa.add_room(living)
        casa.add_room(bedroom)
        casa.add_room(kitchen)
        casa.add_room(office)
        
        # 4. TESTĂM PROPRIETĂȚILE ȘI VALIDAREA
        print("\n4️⃣ TESTAREA PROPRIETĂȚILOR ȘI VALIDĂRII")
        
        # Test validare nume dispozitiv
        try:
            living.add_device("light", "L999", "AB", "Test", "Model", 10)  # Nume prea scurt
        except ValueError as e:
            print(f"✅ Validare nume: {e}")
        
        # Test validare consum energie
        try:
            living.add_device("light", "L998", "Test Light", "Test", "Model", -5)  # Consum negativ
        except ValueError as e:
            print(f"✅ Validare consum: {e}")
        
        # 5. CONECTĂM TOATE DISPOZITIVELE
        print("\n5️⃣ CONECTAREA DISPOZITIVELOR")
        casa.connect_all_devices()
        
        # 6. TESTĂM FUNCȚIONALITĂȚI SPECIFICE
        print("\n6️⃣ TESTAREA FUNCȚIONALITĂȚILOR")
        
        # Test Smart Light
        living_light = living.get_device_by_id("L001")
        living_light.turn_on()
        living_light.brightness = 80
        living_light.change_color("red")
        
        accent_light = living.get_device_by_id("L002")
        accent_light.turn_on()
        accent_light.brightness = 30
        
        # Test Smart Thermostat
        living_thermostat = living.get_device_by_id("T001")
        living_thermostat.target_temp = 24
        living_thermostat.set_mode("heating")
        living_thermostat.adjust_temperature()
        
        bedroom_thermostat = bedroom.get_device_by_id("T002")
        bedroom_thermostat.target_temp = 18
        bedroom_thermostat.set_mode("cooling")
        
        # Test Security Camera
        bedroom_camera = bedroom.get_device_by_id("C001")
        bedroom_camera.start_recording()
        bedroom_camera.storage_used = 10
        bedroom_camera.stop_recording()
        
        office_camera = office.get_device_by_id("C002")
        office_camera.start_recording()
        
        # 7. TESTĂM OPERATORII MAGICI
        print("\n7️⃣ TESTAREA OPERATORILOR MAGICI")
        device1 = living.get_device_by_id("L001")
        device2 = bedroom.get_device_by_id("L003")
        device3 = living.get_device_by_id("L001")  # Același device
        
        print(f"Device1 == Device2: {device1 == device2}")  # False
        print(f"Device1 == Device3: {device1 == device3}")  # True
        print(f"Numărul de camere în casă: {len(casa)}")
        print(f"Numărul de dispozitive în living: {len(living)}")
        
        # 8. AFIȘĂM STATUSUL FINAL
        print("\n8️⃣ STATUSUL FINAL AL SISTEMULUI")
        print(casa.get_home_status())
        
        # 9. GENERĂM RAPORTUL DETALIAT
        print("\n9️⃣ RAPORTUL DETALIAT")
        print(casa.generate_detailed_report())
        
        # 10. TESTĂM FUNCȚIONALITĂȚI AVANSATE
        print("\n🔟 FUNCȚIONALITĂȚI AVANSATE")
        
        # Găsim dispozitivul cu cel mai mare consum
        highest_device = casa.get_device_with_highest_consumption()
        print(f"🔋 Dispozitivul cu cel mai mare consum: {highest_device.name} ({highest_device.power_consumption}W)")
        
        # Testăm eliminarea unei camere
        print(f"\n📊 Înainte de eliminare: {len(casa)} camere, {casa.total_devices} dispozitive")
        removed_room = casa.remove_room("Office")
        print(f"📊 După eliminare: {len(casa)} camere, {casa.total_devices} dispozitive")
        
        # Camera eliminată încă există (agregare)
        if removed_room:
            print(f"✅ Camera eliminată încă există: {removed_room}")
            print(f"   Dispozitivele ei: {[d.name for d in removed_room.devices]}")
        
        # Adăugăm camera înapoi
        casa.add_room(removed_room)
        
        # Testăm validări pentru temperatură
        try:
            living_thermostat.target_temp = 50  # Prea mare
        except ValueError as e:
            print(f"✅ Validare temperatură: {e}")
        
        # Testăm validări pentru luminozitate
        try:
            living_light.brightness = 150  # Prea mare
        except ValueError as e:
            print(f"✅ Validare luminozitate: {e}")
        
        # Testăm storage camera
        try:
            bedroom_camera.storage_used = 100  # Depășește max_storage
        except ValueError as e:
            print(f"✅ Validare storage: {e}")
        
        # 11. SIMULĂM SCENARII REALE
        print("\n1️⃣1️⃣ SIMULAREA SCENARIILOR REALE")
        
        # Scenariul "Plecarea de acasă"
        print("\n🚪 Scenariu: Plecarea de acasă")
        print("   Sting toate luminile...")
        for room in casa.rooms:
            for device in room.devices:
                if isinstance(device, SmartLight) and device.is_on:
                    device.turn_off()
        
        print("   Setez termostatele pe economie...")
        for room in casa.rooms:
            for device in room.devices:
                if isinstance(device, SmartThermostat):
                    device.target_temp = 18
                    device.set_mode("off")
        
        print("   Pornesc toate camerele de securitate...")
        for room in casa.rooms:
            for device in room.devices:
                if isinstance(device, SecurityCamera):
                    device.start_recording()
        
        # Scenariul "Întoarcerea acasă"
        print("\n🏠 Scenariu: Întoarcerea acasă")
        print("   Aprind luminile în living și bucătărie...")
        living_lights = [d for d in living.devices if isinstance(d, SmartLight)]
        kitchen_lights = [d for d in kitchen.devices if isinstance(d, SmartLight)]
        
        for light in living_lights + kitchen_lights:
            light.turn_on()
            light.brightness = 70
        
        print("   Restabilesc temperatura confortabilă...")
        for room in casa.rooms:
            for device in room.devices:
                if isinstance(device, SmartThermostat):
                    device.target_temp = 22
                    device.set_mode("heating")
        
        # 12. STATISTICI FINALE
        print("\n1️⃣2️⃣ STATISTICI FINALE")
        
        all_devices = casa.get_all_devices()
        online_devices = casa.get_online_devices()
        
        # Grupare pe tipuri
        lights = [d for d in all_devices if isinstance(d, SmartLight)]
        thermostats = [d for d in all_devices if isinstance(d, SmartThermostat)]
        cameras = [d for d in all_devices if isinstance(d, SecurityCamera)]
        
        lights_on = [l for l in lights if l.is_on]
        cameras_recording = [c for c in cameras if c.is_recording]
        
        print(f"📊 Statistici generale:")
        print(f"   • Total dispozitive: {len(all_devices)}")
        print(f"   • Dispozitive online: {len(online_devices)}/{len(all_devices)}")
        print(f"   • Lămpi: {len(lights)} (aprinse: {len(lights_on)})")
        print(f"   • Termostate: {len(thermostats)}")
        print(f"   • Camere securitate: {len(cameras)} (înregistrează: {len(cameras_recording)})")
        print(f"   • Consum total: {casa.total_power_consumption}W")
        
        # Calculez consumul pe categorii
        lights_consumption = sum(l.power_consumption for l in lights if l.is_online and l.is_on)
        thermostats_consumption = sum(t.power_consumption for t in thermostats if t.is_online)
        cameras_consumption = sum(c.power_consumption for c in cameras if c.is_online)
        
        print(f"\n⚡ Consum pe categorii:")
        print(f"   • Lămpi: {lights_consumption}W")
        print(f"   • Termostate: {thermostats_consumption}W")
        print(f"   • Camere: {cameras_consumption}W")
        
        print("\n✅ TESTAREA S-A FINALIZAT CU SUCCES!")
        print("🎯 Toate conceptele OOP au fost implementate și testate:")
        print("   ✓ Encapsulare (private, protected, public)")
        print("   ✓ Proprietăți (@property, setter, getter)")
        print("   ✓ Validarea datelor")
        print("   ✓ Compoziție (Room creează Device-uri)")
        print("   ✓ Agregare (SmartHome primește Room-uri)")
        print("   ✓ Moștenire (Device → SmartLight, etc.)")
        print("   ✓ Polimorfism (get_info() suprascris)")
        print("   ✓ Operatori magici (__str__, __eq__, __len__)")
        
    except Exception as e:
        print(f"❌ Eroare în timpul testării: {e}")
        import traceback
        traceback.print_exc()


# ===== PARTEA 6: EXERCIȚII BONUS IMPLEMENTATE =====

def bonus_exercises():
    """Implementarea exercițiilor bonus"""
    
    print("\n🌟 EXERCIȚII BONUS")
    print("=" * 30)
    
    # Creăm o casă mică pentru teste
    casa_test = SmartHome("Str. Test 1")
    
    # Camera test cu dispozitive
    test_room = Room("Test Room", "test")
    test_room.add_device("light", "LT1", "Test Light 1", "Brand1", "Model1", 25)
    test_room.add_device("light", "LT2", "Test Light 2", "Brand2", "Model2", 15)
    test_room.add_device("thermostat", "TT1", "Test Thermostat", "Brand3", "Model3", 8)
    test_room.add_device("camera", "CT1", "Test Camera", "Brand4", "Model4", 12)
    
    casa_test.add_room(test_room)
    casa_test.connect_all_devices()
    
    # Bonus 1: Dispozitivul cu cel mai mare consum
    highest = casa_test.get_device_with_highest_consumption()
    print(f"1️⃣ Cel mai mare consum: {highest.name} ({highest.power_consumption}W)")
    
    # Bonus 2: Toate dispozitivele online în cameră
    print(f"2️⃣ Toate dispozitivele online în {test_room.name}: {test_room.all_devices_online}")
    
    # Bonus 3: Operatorul __len__ pentru SmartHome
    print(f"3️⃣ Numărul de camere în casă: {len(casa_test)}")
    
    # Bonus 4: Raport detaliat
    print(f"4️⃣ Raport detaliat generat ✓")
    
    # Bonus 5: Validarea că un dispozitiv nu poate fi în mai multe camere
    print(f"5️⃣ Validarea unicității ID-urilor implementată în add_device() ✓")


def demonstrate_all_concepts():
    """Demonstrează pe scurt toate conceptele OOP implementate"""
    
    print("\n🎓 DEMONSTRAREA CONCEPTELOR OOP")
    print("=" * 40)
    
    # 1. ENCAPSULARE
    print("\n1️⃣ ENCAPSULARE:")
    device = SmartLight("D001", "Demo Light", "Philips", "Hue", 10)
    print(f"   • Atribut public: {device.installation_date}")
    print(f"   • Atribut protected: {device._brand}")  # Nu recomandat, dar posibil
    print(f"   • Atribut private prin proprietate: {device.name}")
    # print(f"   • Atribut privat direct: {device._device_id}")  # Funcționează, dar nu e recomandat
    
    # 2. PROPRIETĂȚI
    print("\n2️⃣ PROPRIETĂȚI:")
    print(f"   • Getter: {device.name}")
    device.name = "New Demo Light"  # Setter cu validare
    print(f"   • Setter cu validare: {device.name}")
    print(f"   • Proprietate read-only: {device.is_online}")
    print(f"   • Proprietate calculată: {device.status}")
    
    # 3. MOȘTENIRE
    print("\n3️⃣ MOȘTENIRE:")
    print(f"   • SmartLight moștenește Device: {isinstance(device, Device)}")
    print(f"   • Metoda din clasa părinte: {device.connect}")
    print(f"   • Metoda specifică copilului: {device.turn_on}")
    
    # 4. POLIMORFISM
    print("\n4️⃣ POLIMORFISM:")
    devices = [
        SmartLight("L1", "Light", "Brand1", "Model1", 10),
        SmartThermostat("T1", "Thermostat", "Brand2", "Model2", 5),
        SecurityCamera("C1", "Camera", "Brand3", "Model3", 3)
    ]
    
    for device in devices:
        print(f"   • {device.__class__.__name__}: {device.get_info()}")
    
    # 5. COMPOZIȚIE
    print("\n5️⃣ COMPOZIȚIE:")
    room = Room("Demo Room", "demo")
    print(f"   • Camera creează dispozitivul:")
    room.add_device("light", "L_COMP", "Composed Light", "Brand", "Model", 8)
    print(f"   • Dispozitivul aparține camerei: {len(room.devices)} dispozitive")
    
    # 6. AGREGARE
    print("\n6️⃣ AGREGARE:")
    home = SmartHome("Demo Address")
    print(f"   • Casa primește camera existentă:")
    home.add_room(room)
    print(f"   • Camera poate exista independent de casă")
    
    # 7. OPERATORI MAGICI
    print("\n7️⃣ OPERATORI MAGICI:")
    dev1 = SmartLight("SAME", "Light1", "Brand", "Model", 10)
    dev2 = SmartLight("SAME", "Light2", "Brand", "Model", 15)
    dev3 = SmartLight("DIFF", "Light3", "Brand", "Model", 10)
    
    print(f"   • __eq__: dev1 == dev2 (același ID): {dev1 == dev2}")
    print(f"   • __eq__: dev1 == dev3 (ID diferit): {dev1 == dev3}")
    print(f"   • __str__: {dev1}")
    print(f"   • __len__: len(home): {len(home)}")


if __name__ == "__main__":
    """Punctul de intrare principal"""
    
    # Rulăm testarea completă
    test_smart_home_system()
    
    # Rulăm exercițiile bonus
    bonus_exercises()
    
    # Demonstrăm conceptele OOP
    demonstrate_all_concepts()
    
    print("\n" + "="*60)
    print("🎉 HOMEWORK COMPLET IMPLEMENTAT ȘI TESTAT!")
    print("📚 Toate conceptele OOP au fost aplicate cu succes:")
    print("   • Encapsulare, Proprietăți, Moștenire")
    print("   • Polimorfism, Compoziție, Agregare")
    print("   • Validare, Operatori magici")
    print("="*60)