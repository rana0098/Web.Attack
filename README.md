# Web Brute-Force & CSRF Attack Simulation

## Overview
This project was developed for the **Cyber Security** course at the **UNIME Department of Engineering** under the supervision of **Professor Francesco Longo**. It demonstrates common web vulnerabilities and implements robust defensive mechanisms using the Flask framework.

## Features & Simulated Concepts
* **Secure Authentication**: Implementation of a login system using **SHA-256 hashed credentials** to protect against database leaks.
* **Brute-Force Simulation**: Automated scripts testing common passwords against the login route to identify valid credentials.
* **CSRF Simulation**: An attacker-controlled environment that auto-submits hidden forms to change a logged-in user's email unknowingly.
* **Bot Detection (CAPTCHA)**: A math-based CAPTCHA system to prevent automated login bots.
* **Rate Limiting**: Integration of `Flask-Limiter` to block repeated login attempts (5 per minute per IP).
* **CSRF Defenses**: Protection of sensitive state-changing routes using **CSRF tokens** (Flask-WTF) and enforcing **SameSite=Strict** cookie policies.

## Technical Stack
* **Backend**: Python (Flask)
* **Security Tools**: Flask-Limiter, Flask-WTF (CSRF Protection) 
* **Encryption**: SHA-256 hashing via `hashlib` 
* **Session Management**: Flask Session Handling 

## Results 
* **Before Defense**: Brute-force scripts successfully find weak passwords, and CSRF attacks silently change user data.
* **After Defense**:
    * Incorrect CAPTCHA answers or excessive login attempts result in a **"Too Many Requests"** error.
    * CSRF attempts are rejected with a **CSRF Error** if the token is missing or invalid.

## Contact
**Rana Sanjideh** University of Messina (UniMe) 
Email: [RanaSanjideh@gmail.com](mailto:RanaSanjideh@gmail.com)
