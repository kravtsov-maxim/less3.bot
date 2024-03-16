import requests


def fox():
    url = 'https://random.imagecdn.app/v1/image?width=500&height=150'
    respones =requests.get(url)
    if respones.status_code:
        data = respones.json()
        return data.get('image')


if __name__ == '__main__':
    fox()