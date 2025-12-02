import numpy as np


def _paperdata(path):
    converters = {
        b'very_high': 4,
        b'high': 3,
        b'normal': 2,
        b'low': 1,
        b'very_low': 0,
        b'yes': 1,
        b'no': 0
    }

    def convert(s):
        return converters[s]

    data = np.genfromtxt(
        open(path, "rb"),
        dtype=int, delimiter=",",
        skip_header=1,
        converters={0: convert, 1: convert, 2: convert, 3: convert, 4: convert}
    )
    return split(data)


def paperdata():
    return (_paperdata('data/_paperdata.csv'), "paperdata")


def paperdata2():
    return (_paperdata('data/_paperdata2.csv'), "paperdata2")


def wisconsin():
    return (split(
        np.genfromtxt(
            open('data/wisconsin683(0:9:0)2.csv', 'rb'),
            dtype=int, delimiter=",",
            skip_header=1,
        )
    ), "wisconsin")


def wdbc():
    converters = {
        b'B': 0.0,
        b'M': 1.0,
    }

    def convert(s):
        return converters[s]

    return (split(
        np.genfromtxt(
            open('data/wdbc569(30:0:0)2.csv', 'rb'),
            dtype=float, delimiter=",",
            skip_header=1,
            converters={30: convert}
        )
    ), 'wdbc')


def monk():
    return (split(
        np.genfromtxt(
            open('data/monk-2432(0:6:0)2.csv', 'rb'),
            dtype=float, delimiter=",",
            skip_header=1,
        )
    ), "monk")


def vehicle():
    import pandas as pd

    # Use pandas to read the CSV - more robust than np.genfromtxt
    df = pd.read_csv('data/pima768(8_0_0)2.csv')

    # Map classes to numeric values
    class_map = {
        'van': 0.0, 'saab': 1.0, 'bus': 2.0, 'opel': 3.0
    }
    df.iloc[:, -1] = df.iloc[:, -1].map(class_map)

    # Convert to numpy array
    data_array = df.to_numpy(dtype=float)

    return (split(data_array), "vehicle")


def split(data):
    return data[:, :-1], data[:, -1]