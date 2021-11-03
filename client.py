import requests 
from pprint import pprint



def get():
    response = requests.get('http://127.0.0.1:8000/address/')
    pprint(response.json())
def post():
    data={
            'apartamenst': 236,
            'city': 'Рівне',     
            'country': 'Україна',
            'house_num': 25,            
            'street': 'Боровое (Заречненский р-н), Рівненська обл. Пункт приема - выдачи ',           
            'zip_code': 2525252    }
    response = requests.post('http://127.0.0.1:8000/address/',data=data)
    print(response.json(),response.status_codes)

if __name__=="__main__":
    # get()
    post()