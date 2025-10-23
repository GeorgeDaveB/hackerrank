def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'
    if x1 < x2 and v1 <= v2: # They will never meet, x2 forever in lead
        return 'NO'
    if x2 < x1 and v2 <= v1: # They will never meet, x1 forever in lead
        return 'NO'
    l = [x1,v1,x2,v2]
    lead = max(l[0],l[2])
    trail = min(l[0],l[2])
    lead_v = l[l.index(lead) + 1]
    trail_v = l[l.index(trail) + 1]
    while lead > trail:
        lead += lead_v
        trail += trail_v
        if (lead == trail):
            return 'YES'
    return 'NO'

