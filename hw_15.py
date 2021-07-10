import json


class MyClass:

    def __init__(self, input_file_name='input.json', output_file_name='output.json'):
        if not input_file_name.endswith('.json'):
            input_file_name += '.json'
        if not output_file_name.endswith('.json'):
            output_file_name += '.json'
        self.in_f_name = input_file_name
        self.out_f_name = output_file_name
        self.in_data = None
        self.out_data = None

    def data_load(self):
        f = open(self.in_f_name, 'r')
        self.in_data = json.load(f)
        f.close()

    def main(self):
        if self.in_data is None:
            return
        emp = {}
        for employee in self.in_data['employee']:
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
        self.out_data = {'employee': emp}

    def get_out_data(self):
        if self.out_data is None:
            if self.in_data is None:
                self.data_load()
            self.main()
        return self.out_data

    def data_dump(self):
        f = open(self.out_f_name, 'w')
        json.dump(self.out_data, f)
        f.close()

    def clear_data(self):
        self.in_data = self.out_data = None

    def set_input_file(self, file_name: str):
        if not file_name.endswith('.json'):
            file_name += '.json'
        self.in_f_name = file_name

    def set_output_file(self, file_name: str):
        if not file_name.endswith('.json'):
            file_name += '.json'
        self.out_f_name = file_name


if __name__ == "__main__":
    handler = MyClass(input_file_name='HW.json')
    handler.data_load()
    handler.main()
    handler.data_dump()

