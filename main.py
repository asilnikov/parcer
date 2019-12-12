def ParserIP(log):
    access_log = {}
    for line in log:
        ip = line.split(" ")[0]

        if access_log.get(ip) is None:
            access_log[ip] = 1
        else:
            access_log[ip] += 1

    sorted_dict = sorted(access_log, key=access_log.get, reverse=True)
    if len(sorted_dict) > 10:
      for key in sorted_dict[:10]:
        print(key, '-'  ,access_log[key], 'time')
    else:
      for key in sorted_dict:
        print(key)


if __name__ == "__main__":
   with open("access_log.txt", "r") as log:
     ParserIP(log)