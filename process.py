# deal with each


jstr = '{"business_id":"Apn5Q_b6Nz61Tq4XzPdf9A","name":"Minhas Micro Brewery","neighborhood":"","address":"1314 44 Avenue NE","city":"Calgary","state":"AB","postal_code":"T2E 6L6","latitude":51.0918130155,"longitude":-114.031674872,"stars":4.0,"review_count":24,"is_open":1,"attributes":{"BikeParking":"False","BusinessAcceptsCreditCards":"True","BusinessParking":{"garage": "False", "street": "True", "validated": "False", "lot": "False", "valet": "False"},"GoodForKids":"True","HasTV":"True","NoiseLevel":"average","OutdoorSeating":"False","RestaurantsAttire":"casual","RestaurantsDelivery":"False","RestaurantsGoodForGroups":"True","RestaurantsPriceRange2":"2","RestaurantsReservations":"True","RestaurantsTakeOut":"True"},"categories":"Tours, Breweries, Pizza, Restaurants, Food, Hotels & Travel","hours":{"Monday":"8:30-17:0","Tuesday":"11:0-21:0","Wednesday":"11:0-21:0","Thursday":"11:0-21:0","Friday":"11:0-21:0","Saturday":"11:0-21:0"}}'


"BusinessParking":
    "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}",

import json
import sql_generate as sg
import string_tool as st


def preprocess(path, sql_func, func=None):
    with open(path, 'r') as f:
        for line in f:
            try:
                jstr = line[:]
                if func is not None:
                    jstr = func(jstr)
                v_dict = json.loads(jstr)
            except Exception as e:
                continue

            sql_func(v_dict)


def main():
    path = '/Users/alfonso/Downloads/yelp_dataset/yelp_academic_dataset_review.json'

    preprocess(path, sg.business_sql, st.edit_json)


if __name__ == '__main__':
    main()


def write_txt_mgr(path: str, ):
    """
    """
    global txt_buffer

    if txt_buffer.path == path:

    else:
        write_txt_


def write_txt(path: str, line: str):
    """
    """
    with open(path, 'a') as f:
        f.write()


def write_txt_batch(path: str, line_list: List):
    """
    """
    with open() as f:


def generate_sql(base_path: str, v_dict: Dict, sql_func)->bool:

    sql_dict = sql_func(v_dict)

    for file_name in sql_dict.keys():
        path = base_path + file_name
        sql_dict[]


def business_sql_func(v_dict: Dict)->Dict:
    """
    @return {"sql_file":['sql','sql'],...}
    """
