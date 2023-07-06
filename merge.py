import os
import json

def merge_files(page):
    data = []
    print(f'Merging {page} objects')
    # for i in range(1, page+1):
    #     entries = []
    #     file_name = f'output/output{i}.json'
    #     with open(file_name, encoding='utf-8') as fl:
    #         entries = json.load(fl)
    #     data.append(entries)

    entries = []
    file_name = f'output/output{page}.json'
    with open(file_name, encoding='utf-8') as fl:
        entries = json.load(fl)
        data.append(entries)

    modified = []
    counter = 0
    for entry in data:
        for obj in entry:
            modified.append(obj)
            counter += 1

    json_object = {
        "size": str(counter),
        "data": modified
    }

    # file_name = 'testoutput.json'
    # with open(file_name, 'w', encoding='utf-8') as fl:
    #     json.dump(json_object, fl, indent=2)

    return json_object

def clean(page):
    # try:
    #     for i in range(1, page+1):
    #         print(f'Removing files:- output/output{i}.json')
    #         os.remove(f'output/output{i}.json')
    #     os.rmdir('output')
    # except OSError as e:
    #     print("Path not recognised or directory is not empty")
    try:
        print(f'Removing files:- output/output{page}.json')
        os.remove(f'output/output{page}.json')
        os.rmdir('output')
    except OSError as e:
        print('Path not recognised')
