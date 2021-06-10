from flask import Blueprint, render_template
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
    query_data = db.session.execute(sql, {'showcode': '401107-01048'})
    cnt = 0
    for data in query_data:
        cnt += 1
        print('Index : ', cnt, ', data : ', data)
    return render_template('main/index.html')