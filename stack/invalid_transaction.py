def invalidTransaction(transactions):
    result = []
    records = []

    for transaction in transactions:
        record = transaction.split(",")
        record[1] = int(record[1])
        record[2] = int(record[2])
        records.append(record)
    for rec in records:
        if rec[2] > 1000:
            rec[1] = str(rec[1])
            rec[2] = str(rec[2])
            result.append(",".join(rec))
            continue
        for t in records:
            if rec[0] == t[0] and abs(rec[1] - int(t[1])) <= 60 and rec[3] != t[3]:
                rec[1] = str(rec[1])
                rec[2] = str(rec[2])
                result.append(",".join(rec))
                break
            
    return result
print(invalidTransaction(["alice,20,800,mtv","bob,50,1200,mtv"]))