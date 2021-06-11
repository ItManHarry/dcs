from am.extensions import db
'''
    根据产品ID获取产品类别名称
'''
def get_machine_classes(ids):
    sql = '''
        select id,name from cp_machineclass where id <> -1
    '''
    items = [(str(item[0]), item[1]) for item in db.session.execute(sql)]
    class_map = dict(items)
    names = [class_map[id] for id in ids.split(',')]
    return ','.join(names)
'''
    获取代理商信息Map供下拉列表用
    map_type: 
        1 -> 返回ID/名称键值对
        2 -> 返回CODE/名称键值对
        3 -> 返回SAP CODE/名称键值对
    search_type:
        'all'       -> 查询全部
        'active'    -> 查询在用
        'inactive'  -> 查询停用
'''
def get_agent_map(map_type, search_type='all'):
    sql = '''
        select 
            id, 
            code, 
            sapcode, 
            name 
        from cp_branch 
        where id <> -1       
    '''
    if search_type == 'active':
        sql += ' and status in (0, 1) '
    if search_type == 'inactive':
        sql += ' and status = 2 '
    sql += ' order by name '
    if map_type == 1:
        items = [(str(item[0]), item[3]) for item in db.session.execute(sql)]
        return dict(items)
    if map_type == 2:
        items = [(str(item[1]), item[3]) for item in db.session.execute(sql)]
        return dict(items)
    if map_type == 3:
        items = [(str(item[2]), item[3]) for item in db.session.execute(sql)]
        return dict(items)
    return {}