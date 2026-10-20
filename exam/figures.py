"""
IST356 Exam 1 — Figures (fa26)
Python code to recreate each figure as a pandas DataFrame or Python object.
"""
import numpy as np
import pandas as pd

# df1
df1 = pd.DataFrame({
    "COLA": ["W", "W", "X", "X"],
    "COLB": [4, 9, 5, 3],
    "COLC": [np.nan, 2.0, np.nan, 1.0],
})

# df2
df2 = pd.DataFrame({
    "COLD": [1, 2, 3, 4],
    "COLE": ["Z", "Y", "W", "X"],
})

# df3
df3 = pd.DataFrame({
    "COLD": [3, 4, 4, 5],
    "COLE": ["W", "X", "Y", "Z"],
})

# df4  (DATE and AMT are strings, exactly as shown in the figure)
df4 = pd.DataFrame({
    "NAME": ["Abby Kuss", "Bette Alott", "Chris Peanugget"],
    "DATE": ["2024-01-08", "2024-01-15", "2024-02-22"],
    "AMT": ["$1,000.00", "$25.50", "$300.00"],
})

# df5
df5 = pd.DataFrame({
    "COLD": [1, 2, 3, 4, 4],
    "COLE_x": ["Z", "Y", "W", "X", "X"],
    "COLE_y": [np.nan, np.nan, "W", "X", "Y"],
})

# df6
df6 = pd.DataFrame({
    "COLA": ["W", "X"],
    "COLB": [2.0, 2.0],
    "COLC": [2.0, 1.0],
})

# df7
df7 = pd.DataFrame({
    "COLA": ["A", "B"],
    "COLB": [1.0, 2.0],
    "COLC": [3.0, 4.0],
    "COLD": [5.0, 6.0],
})

# df8
df8 = pd.DataFrame({
    "COLA": ["W", "W", "W", "X", "X", "X"],
    "COLB": ["A", "B", "C", "A", "B", "C"],
    "COLC": [2.0, 1.0, 3.0, 5.0, 4.0, 6.0],
})

# data1 (Python list, already de-serialized from JSON)
data1 = [
    {
        "A": {"B": 1, "C": 2},
        "E": [
            {"F": 10, "G": 11},
            {"F": 12, "G": 13},
        ],
    },
    {
        "A": {"B": 3, "C": 4},
        "E": [
            {"F": 20, "G": 21},
            {"F": 22, "G": 23},
        ],
    },
]

# data2 (Python list, already de-serialized from JSON)
data2 = [
    {
        "OrderId": 501,
        "Customer": {"First": "Abby", "Last": "Kuss"},
        "Items": [
            {"Name": "T-Shirt", "Price": 10.0, "Qty": 3},
            {"Name": "Jacket", "Price": 20.0, "Qty": 1},
        ],
    },
    {
        "OrderId": 502,
        "Customer": {"First": "Bette", "Last": "Alott"},
        "Items": [
            {"Name": "Shoes", "Price": 25.0, "Qty": 1},
        ],
    },
    {
        "OrderId": 503,
        "Customer": {"First": "Chris", "Last": "Peanugget"},
        "Items": [
            {"Name": "T-Shirt", "Price": 10.0, "Qty": 1},
            {"Name": "Hat", "Price": 5.0, "Qty": 2},
            {"Name": "Socks", "Price": 4.0, "Qty": 3},
        ],
    },
]

# data3 (Python dict, already de-serialized from JSON)
data3 = {
    "accounting": [
        {"first": "John", "last": "Doe", "age": 23},
        {"first": "Mary", "last": "Smith", "age": 32},
    ],
    "sales": [
        {"first": "Sally", "last": "Green", "age": 27},
    ],
    "marketing": [
        {"first": "Tom", "last": "Brown", "age": 28},
        {"first": "Ann", "last": "Lee", "age": 35},
    ],
}

# data4 (Python list, already de-serialized from JSON)
data4 = [
    {
        "A": {"B": 1},
        "F": [
            {"W": 10, "X": 11},
            {"W": 12},
        ],
    },
    {
        "A": {"B": 3},
        "F": [
            {"W": 20, "X": 21},
            {"X": 23},
        ],
    },
]


if __name__ == "__main__":
    for name in ["df1", "df2", "df3", "df4", "df5", "df6", "df7", "df8"]:
        print(f"## {name}")
        print(globals()[name], end="\n\n")
    for name in ["data1", "data2", "data3", "data4"]:
        print(f"## {name}")
        print(globals()[name], end="\n\n")