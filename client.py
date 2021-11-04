import requests 
from pprint import pprint



def get():
    response = requests.get('http://127.0.0.1:8000/address/')
    pprint(response.json())

def post():

    data = {'apartamenst': 30,
            'city': 'Рівне',
            'country': 'Україна',
            'house_num': 10,
            'street': 'Київіаав street',
            'zip_code': 33333}    
    response = requests.post('http://127.0.0.1:8000/address/',data=data)
    print(response.json(),response.status_code)

def update():
    data = {'apartamenst': 0,
            'city': 'Рівне',
            'country': 'Україна',
            'house_num': 46,
            'street': 'Київська',
            'zip_code': 33027}
    response = requests.put('http://127.0.0.1:8000/address/1/',
                            data=data)
    print(response.json(), response.status_code)

def delete():
    response = requests.delete('http://127.0.0.1:8000/address/5/')
    print("DELETE:", response.status_code)

if __name__=="__main__":
    # get()
    post()
    # update()
    # delete()
