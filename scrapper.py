import requests
import time
import pandas as pd


DELAY_REQUEST = 0.05
GROUP_NAME = 'bsuir_official'

#получение списка пользователей группы
def getVKMembers(group_id, count=1000, offset=0):
    # http://vk.com/dev/groups.getMembers
    host = 'http://api.vk.com/method'

    if count > 1000:
        raise Exception('Bad params: max of count = 1000')
    #http get запрос к VK API
    response = requests.get(
        '{host}/groups.getMembers?group_id={group_id}&count={count}&offset={offset}&fields=sex,bdate,city,country&access_token=80503f3580503f3580503f353e80389fae8805080503f35dc31a0a665bd74832c777ca4&v=5.131.'
        .format(host=host, group_id=group_id, count=count, offset=offset))

    if not response.ok:
        raise ConnectionError('Bad response code')

    return response.json()

#получение всех пользователей группы с учетом пагинации ответов (макс. 1000 пользователей за один запрос)
def allCountOffset(func, func_id):
    set_members_id = []
    count_members = -1
    offset = 0
    while count_members != len(set_members_id): 
        response = func(func_id, offset=offset)['response']
        time.sleep(DELAY_REQUEST)
        if count_members != response['count']:
            count_members = response['count']
        new_members_id = response['items']
        offset += len(new_members_id)

        set_members_id.extend(new_members_id)
        if len(new_members_id) == 0:
            break

    return set_members_id

def getTitle(name):
    if not pd.isna(name):
        return name['title']
    else:
        return name


#массив из списка ссылок на анализируемые группы

groups = [
          'http://vk.com/bsuir_official'
          ]

#формирование словаря пользователей группы
members = {}
for g in groups:
    name = g.split('http://vk.com/')[1]
    members[name] = allCountOffset(getVKMembers, name)

#создание dataframe из словаря
df = pd.DataFrame.from_records(members[GROUP_NAME])

#фильтрация датасета
df['city']=df['city'].apply(getTitle)
df['country']=df['country'].apply(getTitle)
#сохранение датасета в .csv
df.to_csv('group.csv')






