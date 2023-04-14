import pandas as pd
import matplotlib.pyplot as plt


def createPieChart(labels, sizes, name): #создание круговой диаграммы
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.5f%%')
    plt.legend(loc='best')

    image_format = 'svg'
    image_name = name + '.svg'
    plt.savefig(image_name, format=image_format, dpi=1200, bbox_inches="tight")  # save the figure to file
    plt.close(fig)

def createBarChart(ds, name): #создание гистограммы
    fig, ax = plt.subplots()
    plt.legend(loc='best')

    ds.plot.bar(rot=0)

    image_format = 'svg'
    image_name = name + '.svg'
    plt.savefig(image_name, format=image_format, dpi=1200, bbox_inches="tight")  # save the figure to file
    plt.close(fig)


df = pd.read_csv('group.csv') #чтение датасета из файла

#создание круговой диаграммы по полу
labels = ['Муж', 'Жен', 'Не указан']
sizes = [df[df['sex'] == 2]['id'].count(), df[df['sex'] == 1]['id'].count(), df[df['sex'] == 0]['id'].count()]

createPieChart(labels, sizes, 'sex')

#создание круговой диаграммы по закрытый/открытый аккаунт
labels = ['Закрытый', 'Открытый']
sizes = [df[df['is_closed'] == True]['id'].count(), df[df['is_closed'] == False]['id'].count()]

createPieChart(labels, sizes, 'Closed_accounts')
#создание гистограммы "Топ-5 имен"
ds = df.groupby('first_name')['id'].count().sort_values(ascending=False).head(5)
createBarChart(ds,'first_name')
#создание гистограммы "Топ-5 фамилий"
ds = df.groupby('last_name')['id'].count().sort_values(ascending=False).head(5)
createBarChart(ds,'last_name')
#создание гистограммы "Топ-5 стран"
ds = df.groupby('country')['id'].count().sort_values(ascending=False).head(5)
createBarChart(ds,'country')
#создание гистограммы "Топ-5 городов"
ds = df.groupby('city')['id'].count().sort_values(ascending=False).head(5)
createBarChart(ds,'city')


