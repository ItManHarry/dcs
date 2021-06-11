from flask import Blueprint, render_template, redirect, url_for
from am.extensions import db
from sqlalchemy import text
bp_main = Blueprint('main', __name__)
'''
    系统主页
'''
@bp_main.route('/index')
def index():
    sql = text('''
        select 
            name ,
            code ,
            showcode ,
            SAPCode ,
            model ,
            prdha ,
            SgSalePrice ,
            ERPPrice ,
            CostPrice ,
            iszhekou ,
            isjifen 
        from cp_material where showcode = :showcode
    ''')
    '''
    query_data = db.session.execute(sql, {'showcode': '401107-01048'})
    cnt = 0
    for data in query_data:
        cnt += 1
        print('Index : ', cnt, ', data : ', data)    
    from am.dao.public import get_machine_classes
    names = get_machine_classes('10500,10201')
    print('names : ' , names)
    '''
    #return render_template('main/index.html')
    return redirect(url_for('agent.list'))