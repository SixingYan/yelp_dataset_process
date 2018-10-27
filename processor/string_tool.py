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


def func(jstr):
    # 检查‘attribute’-‘category’之间是否有多余1个的'{'
    sIdx = jstr.index("attributes")
    eIdx = jstr.index("categories")
    acstr = jstr[sIdx:eIdx]
    if acstr.count('{') < 2:
        return
    part = acstr[acstr.index('{') + 1:]
    for i in range(acstr.count('{') - 1):
        s = part.index('{')
        e = part.index('}')
        part = part[:s - 1] + '"True"' + part[e + 2:]
    return jstr[:sIdx] + acstr[:acstr.index('{') + 1] + part + jstr[eIdx:]
