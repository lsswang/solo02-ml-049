"""Nearest remembered finger for ordinary monophonic scores."""


def plan(score, request):
    positions=list(request['initial_keys'])
    assignments=[]
    actions=[]
    cost=0
    for event in sorted(score,key=lambda n:(n['start'],n['id'])):
        finger=min(range(10),key=lambda f:(abs(positions[f]-event['pitch']),f))
        cost+=abs(positions[finger]-event['pitch'])
        positions[finger]=event['pitch']
        assignments.append({'id':event['id'],'hand':finger//5,'finger':finger%5})
        common={'id':event['id'],'hand':finger//5,'finger':finger%5,'pitch':event['pitch']}
        actions.append({**common,'op':'press','tick':event['start']})
        actions.append({**common,'op':'release','tick':event['end']})
    actions.sort(key=lambda a:(a['tick'],a['op']=='press',a['id']))
    return {'assignments':assignments,'actions':actions,'cost':cost}
