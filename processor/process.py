import json

import sql_generate as sg
import string_tool as st

from constant import DataSetPath
from WriteTextOptClass import WriteTextOpt

wtp = WriteTextOpt()


def read_json(line: str, func)->Dict:
    """
    transfer JSON format string to Dict format
    """
    v_dict = None
    try:
        jstr = func(line) if func is not None else line
        v_dict = json.loads(jstr)

    except Exception as e:
        continue

    return v_dict


def sql_to_text(sql_dict: Dict):
    """
    """
    for file_name in sql_dict.keys():
        path = SQL_DIR + file_name
        for sql in sql_dict[file_name]:
            wtp.get(sql, path)

    wtp.flush()


def preprocess(fromPath, sql_func, func=None):
    """
    """
    with open(path, 'r') as f:
        for line in f:

            v_dict = read_json(line, func)
            if v_dict is None:
                continue

            sql_dict = sql_func(v_dict)

            sql_to_text(sql_dict)


def main():
    path = DataSetPath.Business.value
    preprocess(path, sg.business_sql, st.edit_json)


if __name__ == '__main__':
    main()
