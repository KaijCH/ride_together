from failures.file_read import *
import csv


# extract lines of resp from csv files to sequence
def loading_responses(filepath: str) -> tuple[list, Exception]:
    lines = list()
    try:
        file = open(filepath, mode="r", newline="", encoding="utf-8")
        reader = csv.DictReader(file)
        for _, line in enumerate(reader, start=1):
            # break further reading if empty cols occurs, meaning data malformation and unrecoverable
            if None in line:
                return [], FailureCSVMalformation(filepath=filepath)
            lines.append(line)
        return lines, None
    
    except (FileNotFoundError, PermissionError):
        return [], FailureFileAccessDenial(filepath=filepath)
    
    finally:
        file.close()
