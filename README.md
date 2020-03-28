# bus-schedule
Индексируемое расписание автобусов.

http://asu.cravtr.ru:5000/bush-api/schedule.html?point=16
http://asu.cravtr.ru:5000/bush-api/ns/trips/16/all?showAll=true
    
new_a = []
for item in a:
    item_new = item.copy()
    u = parse.urlparse(item['link'])
    point = parse.parse_qs(u.query)['point'][0]
    u = u._replace(
        path=f'/bush-api/ns/trips/{point}/all',
        query='showAll=true'
    )
    item_new['link'] = u.geturl()
    item_new['point'] = point
    new_a.append(item_new)