# Multi-Factor Authentication (MFA) System

This project is a **Multi-Factor Authentication (MFA) system** implemented in Python.  
It allows users to:

- Register with a username and password  
- Login with username and password  
- Receive a simulated OTP (One-Time Password) for two-factor authentication  

---

## Features

- Secure password hashing using SHA-256  
- OTP generation with 6-digit codes  
- OTP expires after 30 seconds  
- Works in Google Colab (notebook) environment  

---

## How to Run

### In Google Colab
1. copy the code from sc.py file  
2. paste it and run it in google collab
3. Follow the on-screen instructions to register, login, and enter OTP.  

### In Local Python / VS Code
- **Note:** This Colab version **does not run in VS Code** because it uses `ipywidgets` for interactive buttons.  

## Requirements 
- `ipywidgets` (for Google Colab, usually pre-installed)


