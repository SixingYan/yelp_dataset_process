func_dict = {
	"business": business_sql_func,
	"user": user_sql_func,
	"tips": tips_sql_func,
	"review": review_sql_func,
	"checkin": checkin_sql_func
	}


def generate_sql(base_path: str, v_dict: Dict, entity: str)->bool:

	if entity == 'business':
		func = business_sql_func


    sql_dict = sql_func(v_dict)

    for file_name in sql_dict.keys():
        path = base_path + file_name
        sql_dict[]


def business_sql_func(v_dict: Dict)->Dict:
    """
    @return {"sql_file":['sql','sql'],...}
    """

def user_sql_func():
	pass


def tips_sql_func():
	pass


def review_sql_func():
	pass

def checkin_sql_func():
	pass
