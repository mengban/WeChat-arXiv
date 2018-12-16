'''arxiv 美国东部时间的周一至周五的下午2点的提交不会延时。
其他的会延时至美国东部时间的周一发布.
update log:
2018-12-14 : 
    1. 代码初步完成
2018-12-16 : 
    1.增加日志记录：每天更新的文章数目
Attention:
    每周一记得手动添加日期 保证文章的完整性
'''
import arxiv
import json


predate = '2018-12-14'
_date = '2018-12-15'
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
        md += '####{_order}. {_title}'.format(_order=cnt,_title=title)
        md +='\n'
        
        md += '#####**Authors**: {_authors}'.format(_authors=author)
        
        md +='\n'
        md += '> **Abstract:** {_summary}'.format(_summary=summary)
        
        
    print('*********',item['id'],item['updated'])
with open(_date+'.md','w') as f:
        f.write(md)
print(_date,'共更新',cnt,'篇paper.')
data['log'][_date]={'start':_start,'cnt':cnt}
with open('log.json','w') as f:
    json.dump(data,f)



