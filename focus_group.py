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


def get_column_names():
    return ColumnNames.DIASTOLIC, ColumnNames.SYSTOLIC, ColumnNames.POSTURE, ColumnNames.STATUS, ColumnNames.PREDICTED


class Posture(IntEnum):
    standing = 0
    sitting = 1


class Status(IntEnum):
    normal = 0
    anxiety = 1


class FocusGroup:

    def __init__(self, poster_filter=None, status_filter=None):
        diastolic, systolic, posture, status, predicted = get_column_names()
        df = pd.read_csv(Constants.SRC_URL, header=0)
        bp = [x.split('/') for x in df[ColumnNames.MEASUREMENT]]
        df[diastolic] = [x[0] for x in bp]
        df[systolic] = [x[1] for x in bp]
        df = df if poster_filter is None else df[df[posture] == poster_filter.name]
        df = df if status_filter is None else df[df[status] == status_filter.name]
        self.df = df


if __name__ == '__main__':
    FocusGroup()
