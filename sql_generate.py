from typing import Dict
from constant import BooleanSQL

func_dict = {
    "business": business_sql_func,
    "user": user_sql_func,
    "tips": tips_sql_func,
    "review": review_sql_func,
    "checkin": checkin_sql_func
}


def generate_sql(base_path: str, v_dict: Dict, entity: str)->Dict:

    if entity == 'business':
        func = business_sql_func

    return func(v_dict)


def business_sql_func(v_dict: Dict)->Dict:
    """
    @input {"attribute":"value"}
    @return {"sql_file":['sql','sql'],...}
    """


def user_sql_func(v_dict: Dict)->Dict:
    """
    """
    pass


def tips_sql_func(v_dict: Dict)->Dict:
    pass


def review_sql_func(v_dict: Dict)->Dict:
    pass


def checkin_sql_func(v_dict: Dict)->Dict:
    pass


def transfer_bool(v: str):
    return BooleanSQL.TrueValue.value if v == "True" else BooleanSQL.FalseValue.value
