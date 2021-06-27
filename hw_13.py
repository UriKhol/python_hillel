import json


def some_func(*args, **kwargs):
    dict = {}
    h = len(args) // len(kwargs)
    for i, key in enumerate(kwargs.values()):
        dict.update({key: list(args[i * h: (i + 1) * h])})
    return dict


def load_dict(some_dict, json_path):
    with open(json_path, 'w') as f:
        json.dump(some_dict, f)
        f.close()


def main():
    some_list = list(range(21))
    dict = some_func(*some_list, rus='rus', eng='eng', spn='spn', usa='usa', ukr='ukr')
    load_dict(dict, "file.json")


if __name__ == '__main__':
    main()