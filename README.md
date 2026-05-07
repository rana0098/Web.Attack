# Web Brute-Force & CSRF Attack Simulation

## Overview
This project was developed for the **Cyber Security** course at the **UNIME Department of Engineering** under the supervision of **Professor Francesco Longo**[cite: 3, 4, 5]. It demonstrates common web vulnerabilities and implements robust defensive mechanisms using the Flask framework[cite: 1, 14, 17].

## Features & Simulated Concepts
* **Secure Authentication**: Implementation of a login system using **SHA-256 hashed credentials** to protect against database leaks[cite: 12, 33].
* **Brute-Force Simulation**: Automated scripts testing common passwords against the login route to identify valid credentials[cite: 13, 45, 46].
* **CSRF Simulation**: An attacker-controlled environment that auto-submits hidden forms to change a logged-in user's email unknowingly[cite: 16, 153, 154].
* **Bot Detection (CAPTCHA)**: A math-based CAPTCHA system to prevent automated login bots[cite: 15, 90, 92].
* **Rate Limiting**: Integration of `Flask-Limiter` to block repeated login attempts (5 per minute per IP)[cite: 14, 91, 101].
* **CSRF Defenses**: Protection of sensitive state-changing routes using **CSRF tokens** (Flask-WTF) and enforcing **SameSite=Strict** cookie policies[cite: 17, 18, 164, 165].

## Technical Stack
* **Backend**: Python (Flask) [cite: 31]
* **Security Tools**: Flask-Limiter, Flask-WTF (CSRF Protection) [cite: 91, 164]
* **Encryption**: SHA-256 hashing via `hashlib` [cite: 12, 51]
* **Session Management**: Flask Session Handling [cite: 19, 35]

## Results [cite: 179]
* **Before Defense**: Brute-force scripts successfully find weak passwords, and CSRF attacks silently change user data[cite: 46, 184].
* **After Defense**:
    * Incorrect CAPTCHA answers or excessive login attempts result in a **"Too Many Requests"** error[cite: 150, 180].
    * CSRF attempts are rejected with a **CSRF Error** if the token is missing or invalid[cite: 184, 185].

## Contact
**Rana Sanjideh** University of Messina (UniMe) [cite: 6, 190]  
Email: [RanaSanjideh@gmail.com](mailto:RanaSanjideh@gmail.com) [cite: 193]
