import logging
import pathlib


class BinaryCreator:
    def __init__(self, output_dir: pathlib.Path):
        self.ouput_dir = output_dir

    def create(self, file_name: str, binary_string: str):
        if len(binary_string) > 0:
            file_path = self.ouput_dir.joinpath(file_name)
            file = open(file_path, "wb")
            file.write(binary_string)
            file.close()
        else:
            logging.info("the target binary string is empty.")
