#!/bin/python3

import os
import json
import sys
import argparse

def get_json_size(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        compact_json = json.dumps(data, separators=(',', ':'))
        return len(compact_json.encode('utf-8'))
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {file_path}")
        return 0
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return 0

def get_total_json_size(directory):
    total_size = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                total_size += get_json_size(file_path)
    return total_size

def format_size(size_bytes):
    kb = size_bytes / 1024
    gb = kb / 1024 / 1024
    return f"{size_bytes:,} bytes | {kb:.2f} kB | {gb:.4f} GB"

def main():
    parser = argparse.ArgumentParser(description="Calculate total size of JSON files in a directory")
    parser.add_argument("directory", help="Path to the directory to search")
    args = parser.parse_args()

    directory_path = args.directory

    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory")
        sys.exit(1)

    total_size = get_total_json_size(directory_path)
    formatted_size = format_size(total_size)
    print(f"Total size of all JSON files in {directory_path}:")
    print(formatted_size)

if __name__ == "__main__":
    main()