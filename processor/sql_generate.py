from typing import Dict

from constant import SQL_SUFFIX, TRANSFER_DICT, NULL_VALUE

func_dict = {
    "business": business_sql_func,
    "user": user_sql_func,
    "tips": tips_sql_func,
    "review": review_sql_func,
    "checkin": checkin_sql_func
}


def generate_sql(v_dict: Dict, entity: str)->Dict:
    """
    """
    return func_dict[entity](v_dict)


def business_sql_func(v_dict: Dict)->Dict:
    """
    @input {"attribute":"value"}
    @return {"sql_file":['sql','sql'],...}
    """
    sql_dict = {}
    sql = 'insert into BUSINESS(businessid,name,stars,isopen) values({0},{1},{2},{3})'.format(
        getVarchar(v_dict['business_id']), getVarchar(v_dict['name']), v_dict['stars'], v_dict['is_open'])

    sql = 'insert into BUSINESSLOCATION(businessid,city,state,postalcode,address,latitude,longitude)\
     values({0},{1},{2},{3},{4},{5},{6})'.format(
        getVarchar(v_dict['business_id']), getVarchar(
            v_dict['city']), getVarchar(v_dict['state']),
        getVarchar(v_dict['postalcode']), getVarchar(v_dict['address']), v_dict['latitude'], v_dict['longitude'])

    sql = 'insert into BUSINESSHOURS(businessid,weekday,opentime,closetime) values({0},{1},{2},{3})'.format(getVarchar(
        v_dict['business_id']), getVarchar(v_dict['business_id']), getVarchar(v_dict['business_id']), getVarchar(v_dict['business_id']))

    sql = 'insert into BUSINESSCATEGORIES(businessid,categories) values({0},{1})'

    sql = 'insert into BUSINESSATTRIBUTES(businessid,takeout,garage,street,validated,lot,valet) values({0},{1},{2},{3},{4},{5},{6})'

    return sql_dict


def user_sql_func(v_dict: Dict)->Dict:
    """
    """
    sql_dict = {}
    sql = 'insert into USER(userid,useful,funny,cool) values({0},{1},{2},{3})'.format(
        getVarchar(v_dict['user_id']), v_dict['useful'], v_dict['funny'], v_dict['cool'])
    sql_dict['user'] = [sql + SQL_SUFFIX]

    sql_dict['user_follow'] = []
    if v_dict['friends'] != NULL_VALUE:
        for user_id in v_dict['friends']:
            sql = 'insert into USERFOLLOW(userid,following) values({0},{1})'.format(
                getVarchar(v_dict['user_id']), getVarchar(user_id))
            sql_dict['user_follow'].append(sql + SQL_SUFFIX)
    return sql_dict


def tips_sql_func(v_dict: Dict)->Dict:
    """
    """
    sql_dict = {}

    sql = 'insert into TIPS(userid,businessid,likes,date,text) \
    values({0},{1},{2},{3},{4})'\
    .format(getVarchar(v_dict['user_id']), getVarchar(v_dict['business_id']), v_dict['likes'],
            getVarchar(v_dict['date']), getVarchar(v_dict['text']))

    sql_dict['tips'] = [sql + SQL_SUFFIX]

    return sql_dict


def review_sql_func(v_dict: Dict)->Dict:
    """
    """
    sql_dict = {}

    sql = 'insert into REVIEW(reviewid,businessid,userid,cool,funny,stars,useful,date,text)\
     values({0},{1},{2},{3},{4},{5},{6},{7},{8})'\
     .format(getVarchar(v_dict['review_id']), getVarchar(v_dict['business_id']), getVarchar(v_dict['user_id']),
             v_dict['cool'], v_dict['funny'], v_dict[
                 'stars'], v_dict['useful'],
             getVarchar(v_dict['date']), getVarchar(v_dict['text']))

    sql_dict['review'] = [sql + SQL_SUFFIX]

    return sql_dict


def checkin_sql_func(v_dict: Dict)->Dict:
    """
    """
    sql_dict = {}
    sql_dict['checkin'] = []

    for time in v_dict['time'].keys():
        dow, clock = time.split('-')
        sql = 'insert into CHECKIN(businessid,weekday,time,count) \
        values({0},{1},{2},{3})'\
        .format(getVarchar(v_dict['business_id']), weekday, time, v_dict['time'][time])
        sql_dict['checkin'].append(sql + SQL_SUFFIX)

    return sql_dict


def transfer_keyword(v: str):
    """
    """
    if v in TRANSFER_DICT.keys():
        return TRANSFER_DICT[v]


def getVarchar(v: str):
    """
    """
    return "'" + v + "'"
