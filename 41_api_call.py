import requests

from hashlib import sha256
import datetime

# with open('test_audio.wav', 'rb') as wav:
#     files = {"file": wav}
#     a = requests.post(url="https://cca-recode.herokuapp.com/senti_score",
#                       files=files,
#                       data={'token':
#                                 sha256("recode {0}".format(str(datetime.date.today())).encode('utf-8')).hexdigest(),
#                             'over_all_score': 1,
#                             'count_of_call': 1
#                             })
#     print(a.content)

a = requests.post(url="https://cca-recode.herokuapp.com/store_result",
                  data={
                      'token': sha256("recode {0}".format(str(datetime.date.today())).encode('utf-8')).hexdigest(),
                      "customer_id": 12,
                      "score": 12})
print(a.content)


# a = requests.post(url="https://cca-recode.herokuapp.com/retrieve_result",
#                   data={
#                       'token': sha256("recode {0}".format(str(datetime.date.today())).encode('utf-8')).hexdigest(),
#                       "customer_id": 12})
# print(a.content)
