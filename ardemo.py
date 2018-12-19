'''arxiv 美国东部时间的周一至周五的下午2点的提交不会延时。
其他的会延时至美国东部时间的周一发布.
现在美东时间比北京时间晚13个小时。
收到的提交	         将被公布 	  邮寄给订阅者
周一14:00-周二14:00	星期二20:00	周二晚上/周三早上
周二14:00-周三14:00	周三20:00	周三晚上/周四早上
周三14:00-周四14:00	周四20:00	周四晚上/周五早上
周四14:00-周五14:00	周日20:00	周日晚上/周一早上
周五14:00-周一14:00	星期一20:00	周一晚上/周二早上

中国时间
收到的提交	         将被公布 	  邮寄给订阅者
周一1:00-周二1:00	    星期二7:00	周二晚上/周三早上
周二1:00-周三1:00	    周三7:00	    周三晚上/周四早上
周三1:00-周四1:00 	周四7:00	    周四晚上/周五早上
周四1:00-周五1:00	    周日7:00	    周日晚上/周一早上
周五1:00-周一1:00	    星期一7:00	周一晚上/周二早上

update log:
2018-12-14 : 
    1. 代码初步完成
2018-12-16 : 
    1.增加日志记录：每天更新的文章数目
2018-12-18 :
    1.修复\xf6编码错误     
    2.修改命名格式 增加了篇数
    
Attention:
    每周一记得手动添加日期 保证文章的完整性
发布记录:
    
TODO:
    1.增加自动push至github功能
'''
import arxiv
import json


predate = '2018-12-17'
_date = '2018-12-18'
# 14853 2018-12-13
with open('log.json','r') as f:
    data = json.load(f)

_start = data['log'][predate]['start'] + data['log'][predate]['cnt'] 

cnt = 0

paper = arxiv.query(search_query='cat:cs.CV',start=int(_start),max_results=50)
print(type(paper),len(paper),paper)
md = '# Latest CV paper updated in '+ _date


for item in paper:
    if item['updated'][:10] == _date:
        cnt += 1
        downurl = item['id']
        title = item['title_detail']['value'].replace('\n',' ')
        author = ','.join(item['authors'])
        summary = item['summary'].replace('\n',' ')
        
        md +='\n'
        md +='\n'
        md += '#### {_order}. {_title}'.format(_order=cnt,_title=title)
        md +='\n'
        
        md += '##### **Authors**: {_authors}'.format(_authors=author)
        
        md +='\n'
        md += '> **Abstract:** {_summary}'.format(_summary=summary)
        
        
    print('*********',item['id'],item['updated'])
with open(_date+'_'+str(cnt)+'.md','wb') as f:  #w  改为wb
    #print(md)
    f.write(md.encode("UTF-8")) #重新encode
print(_date,'共更新',cnt,'篇paper.')
data['log'][_date]={'start':_start,'cnt':cnt}
with open('log.json','w') as f:
    json.dump(data,f)



