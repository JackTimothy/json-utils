#!/bin/python3

import os
import json


def sort_json_keys(directory: str):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                except Exception as e:
                    print(f'Could not read file {file_path}: {e}.')
                    continue
                
                try:
                    with open(file_path, 'w', encoding='utf-8') as json_file:
                        json.dump(data, json_file, sort_keys=True, indent=4, ensure_ascii=False)
                except Exception as e:
                    print(f'Could not write file {file_path}: {e}.')
                    

sort_json_keys('./')

