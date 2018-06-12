import json
import lz4.block

def dump(file_path, data):
    with open(file_path, "wb+") as file_handle:
        file_handle.write(
            lz4.block.compress(
                bytearray(json.dumps(data), 'UTF-8')))

def load(file_path):
    with open(file_path, "rb") as file_handle:
        return json.loads(
            lz4.block.decompress(
                file_handle.read()))
