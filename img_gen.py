import requests
import time


url_gen = "https://api.prodia.com/v1/sd/generate"
url_img = "https://api.prodia.com/v1/job/"


def generate(prompt):
    headers = {'X-Prodia-Key': 'c177417d-8b42-423a-8dc1-4b02c7a686ae',
               'accept': 'application/json'}
    payload = {'prompt': prompt}
    response = requests.post(url_gen, headers=headers, json=payload)

    return response.json()['job']


def retrieve(job):
    headers = {'X-Prodia-Key': 'c177417d-8b42-423a-8dc1-4b02c7a686ae',
               'accept': 'application/json'}
    response = requests.get(url_img+job, headers=headers).json()
    link = response.get('imageUrl')
    status = response.get('status')

    return link, status


def get_link(prompt):
    a = generate(prompt)
    status = 'generating'
    while status == 'generating':
        link, status = retrieve(a)
        time.sleep(3)

    return link
