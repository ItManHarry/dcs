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