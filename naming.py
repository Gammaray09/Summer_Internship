def formatName(i):
    num = str(i)
    numZeros = 4-len(num)
    if numZeros == 3:
        return f"000{i}"
    elif numZeros == 2:
        return f"00{i}"
    elif numZeros == 1:
        return f"0{i}"
    else:
        return f"{i}"
    

for i in range(355):
    num=formatName(i)
    print(f"snap.{num}.tiff")
    