# -*-coding:utf-8 -*-
from django.http import HttpResponse,JsonResponse
import json
from corenlp_client import CoreNLP # 导入CoreNLP类
annotator = CoreNLP(url="https://corenlp.run", lang="zh") # 创建标注器对象
def echo_index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def entity_extract_index(request):
    json_result = json.loads(request.body)
    content = json_result["content"]
    lsts = annotator.ner(content)
    resp = {
        "PERSON":[],
        "TIME":[],
        "DATE":[],
        "CITY":[],
        "LOCATION":[],
        "FACILITY":[],
    }
    for line in lsts:
        for dic in line:
            for key,value in dic.items():
                if value in resp:
                    resp[value].append(key[0])
    for k in resp.keys():
        resp[k] = list(set(resp[k]))
    return JsonResponse(resp,json_dumps_params={'ensure_ascii': False})