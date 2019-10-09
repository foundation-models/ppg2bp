import pandas as pd
from enum import IntEnum


class Constants:
    SRC_URL = "https://drive.google.com/uc?export=download&id=1c9u2lcHGO0wmyCWZKmPGWzen8B_NNHEi"


class ColumnNames:
    PREDICTED = "predicted"
    MEASUREMENT = "measurement"
    POSTURE = "posture"
    STATUS = "status"
    METADATA = "metadata"
    DIASTOLIC = "diastolic"
    SYSTOLIC = "systolic"


class Posture(IntEnum):
    standing = 0
    sitting = 1


class Status(IntEnum):
    normal = 0
    anxiety = 1


class FocusGroup:
    def __init__(self):
        df = pd.read_csv(Constants.SRC_URL, header=0)
        self.df = df
        self.predicted = df[ColumnNames.PREDICTED]
        bp = [x.split('/') for x in df[ColumnNames.MEASUREMENT]]
        self.diastolic = [x[0] for x in bp]
        self.systolic = [x[1] for x in bp]
        self.posture = [Posture[i] for i in df[ColumnNames.POSTURE]]
        self.status = [Status[i] for i in df[ColumnNames.STATUS]]


if __name__ == '__main__':
    FocusGroup()
