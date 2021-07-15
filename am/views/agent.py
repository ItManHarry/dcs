from flask import Blueprint,render_template,request
from am.extensions import db
from am.dao.public import get_machine_classes, get_agent_map
bp_agent = Blueprint('agent', __name__)
'''
    获取代理商清单
'''
@bp_agent.route('/list')
def list():
    code = request.args.get('code', '')
    name = request.args.get('name', '')
    sql = '''
        select
            a.code,             --DCS代码
            a.sapcode,          --SAP代码
            a.name,             --代理商名称
            a.status,           --系统状态
            a.machineclassid,   --产品类别
            b.name,             --挖掘机大区
            c.name,             --装载机大区
            d.name,             --山猫大区
            curmonth,           --当前结转月份
            nextmonth           --下一结转月份
        from cp_branch a 
        left join cp_branchcommue b
        on a.branchcommueid = b.id
        left join cp_branchcommue c
        on a.branchcommueid_z = c.id
        left join cp_branchcommue d
        on a.branchcommueid_b = d.id
        where 1 = 1
        and curmonth <> '0'
        and nextmonth <> '0'
        and a.id <> -1         
    '''
    if code.strip() != '':
        sql += " and code like '%"+code+"%' "
    if name.strip() != '':
        sql += " and name like '%"+name+"%' "
    sql += ' order by a.name'
    query_result = db.session.execute(sql)
    table_data = []
    for result in query_result:
        data = {}
        data['dcscd'] = result[0]
        data['sapcd'] = result[1]
        data['agent'] = result[2]
        data['status'] = '停用' if result[3] == 2 else '在用'
        data['machine'] = ('' if result[4] == None else get_machine_classes(result[4]))
        data['excavator'] = result[5]
        data['loader'] = result[6]
        data['bobcat'] = result[7]
        data['current'] = result[8]
        data['next'] = result[9]
        table_data.append(data)
    '''
    agent_map = get_agent_map(1, 'all')
    print('Map length is :', len(agent_map))
    for key, value in agent_map.items():
        print('Agent map(ID) key is  %s, value is %s' %(key, value))
    '''
    return render_template('agent/list.html', table_data=table_data)