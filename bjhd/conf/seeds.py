url_ = "http://zyk.bjhd.gov.cn/zmhd/lxxd/index_%d.shtml"
urls = ["http://zyk.bjhd.gov.cn/zmhd/lxxd/",]
for i in range(1, 16):
    urls.append(url_ % i)
seeds = [{"parser_name": "list", "url": x} for x in urls]
import json
ret = json.dumps(seeds, indent=2)
print(ret)
