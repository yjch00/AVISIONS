import numpy as np
from QueryResult import getSearchEngineResult


def readQueryFile(filename):
    query_dict = {}

    with open(filename, 'r', encoding='UTF8') as f:
        text = f.read()
        queries = text.split('   /\n')

        for query in queries:
            br = query.find('\n')
            qID = int(query[:br])
            q = query[br+1:]
            query_dict[qID] = q

    return query_dict


def getGroundtruthRelevance(query_ids):
    relevant_dict = {}

    with open('doc/relevance.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            items = line.split(' ')
            queryID = int(items[0])
            docID = int(items[1])
            if queryID in query_ids:
                # add into relevant_dict
                if queryID in relevant_dict:
                    relevant_dict[queryID].append(docID)
                else:
                    relevant_dict[queryID] = [docID]

    return relevant_dict


def evaluate(query_dict, relevent_dict, results_dict):
    BPREF = []
    dict_job = {1:'네이버 머신러닝', 2:'카카오 디자인/브랜드', 3:'MS 마케팅',
                4:'MS EHS manager', 5:'MS WEB개발자', 6:'MS 마케팅',
                7:'MS 컨설팅', 8:'삼성전자 회로설계', 9:'삼성전자 영업마케팅',
                10:'삼성전자 생산관리', 11:'삼성전자 S/W개발', 12:'하이닉스 Data Science',
                13:'하이닉스 설계', 14:'하이닉스 재무/회계', 15:'하이닉스 IT',
                16: '카카오 안드로이드 개발자', 17: '카카오 브랜드 디자이너', 18: '카카오 연결재무',
                19: '카카오 데이터 분석가'}
    dict_lec = {1:'데이터마이닝', 2:'생산관리', 3:'경제학개론', 4:'선형대수학1',
                5:'통계학', 6:'물리학', 7:'재무관리', 8:'테니스', 9:'기초회로이론 및 실습',
                10 : '기초시각디자인'}
    for queryID in query_dict.keys():
        relevantCount = 0
        nonRelevantCount = 0
        score = 0
        results = results_dict[queryID]
        relevantDocuments = relevent_dict[queryID]
        relDocCount = len(relevantDocuments)

        for document in results:
            if document in relevantDocuments:
                relevantCount += 1
                if nonRelevantCount >= relDocCount:
                    score += 0
                else:
                    score += (1 - nonRelevantCount / relDocCount)
            else:
                nonRelevantCount += 1
            if relevantCount == relDocCount:
                break
        score = score / relDocCount
        BPREF.append(score)

        for i in range(1,20):
            print("{0} 직무와 가장 유사한 강좌는".format(dict_job[i]), end='')
                for j in results_dict[i]:
                    print("[{0}]".format(dict_lec[j]), end='')
            print("순입니다.")




if __name__ == '__main__':
    query_dict = readQueryFile('doc/query.txt')
    relevant_dict = getGroundtruthRelevance(query_dict.keys())
    results_dict = getSearchEngineResult(query_dict)
    evaluate(query_dict, relevant_dict, results_dict)
