def edit_json(jstr: str)->str:
    '''
    字符串中，双引号在外围，单引号在内嵌，导致转换失败
    '''
    if "BusinessParking" in jstr:
        start_index = jstr.index("BusinessParking")
        part = jstr[start_index:]
        end_index = part.index('}')
        part = part[:end_index + 2]
        #
        part = part.replace('"{', '{').replace('}"', '}').replace('\'', '\"')
        part = part.replace('True', '"True"').replace('False', '"False"')

        jstr[:start_index] + part + jstr[start_index + end_index + 2:]

  