import json


def open_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
        for item in data['questions']:
            item['answer'] = input(item['q'])
        print(data)


    with open(path, 'w') as file:
        json.dump(data, file)


open_file('/Users/Анастасия/.PyCharmCE2019.3/Hillel/questions.json')


