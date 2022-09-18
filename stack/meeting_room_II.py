def meetingRoom(intervals):
    start  = sorted([i.start for i in intervals])
    end  = sorted([i.end for i in intervals])
    s,e = 0,0 
    res,count = 0,0

    while e < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res,count)
    return res