import requests

def get_token(identifier: str, password: str) -> str:
    auth = requests.post(
		url="http://localhost:1337/auth/local",
		data={
			'identifier': identifier, 
			'password': password,
		}
    )
    auth.raise_for_status()
    token = 'Bearer ' + auth.json()['jwt']
    return token

token = get_token('toto@toto.com', 'mialet30')