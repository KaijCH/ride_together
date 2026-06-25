from base import FailureBase


class FailureCSVMalformation(FailureBase):

    def __init__(self, filepath: str):
        message = f"Malformation in CSV file \"{filepath}\", value exceeds fields count"
        super().__init__(code=1001, message=message)

class FailureFileAccessDenial(FailureBase):

    def __init__(self,  filepath: str):
        message = f"Denial during file access to \"{filepath}\""
        super().__init__(code=1002, message=message)

class FailureValueUnforeseenInField(FailureBase):

    def __init__(self, value: str, fieldname: str, sceanrio: str):
        message = f"Unforeseen value \"{value}\" for field \"{fieldname}\", during {sceanrio} process"
        super().__init__(code=2001, message=message)
