import requests

a = requests.post('http://127.0.0.1:5000/testing2', data={'value1': 10,
                                                          'value2': 20,
                                                          'password': 'lrt1'})

print(a.__dict__)