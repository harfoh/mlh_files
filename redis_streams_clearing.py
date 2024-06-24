import redis
r = redis.Redis(host='kudaglobal-prod.redis.cache.windows.net', port=6379, password='EvFB9EF5CvhAAji7lFvgrGqDwJR5ojGeaAzCaAZtaCk=', decode_responses=True)

# Check for pending messages
rkeys = r.keys()
# print (rkeys)
for i in rkeys:
    keyr = (r.keys(i))
    stlen=(r.xlen(i))
    # print (stlen)
    pendingc = r.execute_command("XINFO GROUPS", i)
    # rconsumer = r.xinfo_groups (i)
    #print (pendingc)
    for j in range(len(pendingc)):
        list4 = [d.get('pending') for d in pendingc]
    # print(list4)
    Tpend = sum (list4)
    # print (Tpend)
    cleared = abs(int (stlen - Tpend)) 

    # print (abs(cleared))
    r.xtrim (i, approximate=False, maxlen=str(abs(Tpend)))
    #streamLen = r.xlen(i)
    # if Tpend < stlen:
    #     r.xtrim (i, approximate=False, maxlen=str(abs(Tpend)))
    # else:
    #     r.xtrim (i, approximate=False, maxlen=str(abs(cleared)))

    #print("compare", (keyr, stlen, Tpend, streamLen), (cleared), "was cleared")
    #print (Tpend) #to compare with streamLen