import json


file_name_1 = 'HW.json'
file_name_2 = 'HM_res.json'


def data_load(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    f.close()
    return data


def main(data):
    emp = {}
    for employee in data['employee']:
        name = f"{employee['firstName']} {employee['lastName']}"
        dict = {'int': [], 'string': [], 'float': [], 'none_type': [], 'bool': []}
        for item in employee.items():
            if type(item[1]) == int:
                dict['int'].append(item[0])
            elif type(item[1]) == str:
                dict['string'].append(item[0])
            elif type(item[1]) == float:
                dict['float'].append(item[0])
            elif type(item[1]) == bool:
                dict['bool'].append(item[0])
            elif item[1] is None:
                dict['none_type'].append(item[0])
        emp.update({name: dict})
    return {'employee': emp}


def data_dump(file_name, data):
    f = open(file_name, 'w')
    json.dump(data, f)
    f.close()


data = data_load(file_name_1)
res = main(data)
data_dump(file_name_2, res)

