
import hashlib
import random
import time
from IPython.display import display, clear_output
import ipywidgets as widgets
# DATABASE (SIMULATED)
users_db = {}
otp_db = {}
OTP_VALIDITY = 30  # seconds
# SECURITY FUNCTIONS
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def generate_otp(username):
    otp = random.randint(100000, 999999)
    expiry = time.time() + OTP_VALIDITY
    otp_db[username] = (otp, expiry)
    return otp
# MFA Application Logic
class MFAColabApp:
    def __init__(self):
        self.username = None
        self.main_menu()
    # MAIN MENU
    def main_menu(self):
        clear_output()
        print("=== Multi-Factor Authentication ===")
        register_btn = widgets.Button(description="Register")
        login_btn = widgets.Button(description="Login")      
        register_btn.on_click(lambda x: self.register_ui())
        login_btn.on_click(lambda x: self.login_ui()) 
        display(widgets.VBox([register_btn, login_btn]))
    # REGISTER UI
    def register_ui(self):
        clear_output()
        print("=== User Registration ===")   
        username_input = widgets.Text(description="Username:")
        password_input = widgets.Password(description="Password:")
        register_btn = widgets.Button(description="Register")
        back_btn = widgets.Button(description="Back")      
        def register_clicked(b):
            username = username_input.value.strip()
            password = password_input.value.strip()            
            if not username or not password:
                print(" All fields required!")
                return           
            if username in users_db:
                print(" User already exists!")
                return  
            users_db[username] = hash_password(password)
            print(" Registration successful!")
            time.sleep(1)
            self.main_menu()       
        register_btn.on_click(register_clicked)
        back_btn.on_click(lambda x: self.main_menu())      
        display(widgets.VBox([username_input, password_input, register_btn, back_btn]))
    # LOGIN UI
    def login_ui(self):
        clear_output()
        print("=== Login ===")
        username_input = widgets.Text(description="Username:")
        password_input = widgets.Password(description="Password:")
        login_btn = widgets.Button(description="Login")
        back_btn = widgets.Button(description="Back")
        def login_clicked(b):
            username = username_input.value.strip()
            password = password_input.value.strip()
            if username not in users_db:
                print(" User not found!")
                return
            if users_db[username] != hash_password(password):
                print("Incorrect password!")
                return          
            self.username = username
            otp = generate_otp(username)
            print(f" OTP Sent (Simulated): {otp}")
            self.otp_ui()      
        login_btn.on_click(login_clicked)
        back_btn.on_click(lambda x: self.main_menu())  
        display(widgets.VBox([username_input, password_input, login_btn, back_btn]))
    # OTP UI
    def otp_ui(self):
        clear_output()
        print("=== OTP Verification ===")
        otp_input = widgets.Text(description="Enter OTP:")
        verify_btn = widgets.Button(description="Verify OTP")
        def verify_clicked(b):
            entered_otp = otp_input.value.strip()
            if not entered_otp.isdigit():
                print(" Invalid OTP format!")
                return
            otp, expiry = otp_db.get(self.username, (None, None))
            if time.time() > expiry:
                print(" OTP expired!")
                time.sleep(1)
                self.main_menu()
                return
            if int(entered_otp) == otp:
                print("Authentication successful! Access Granted.")
                time.sleep(1)
                self.main_menu()
            else:
                print(" Incorrect OTP!")
        verify_btn.on_click(verify_clicked)
        display(widgets.VBox([otp_input, verify_btn]))
# RUN THE APP
app = MFAColabApp()
