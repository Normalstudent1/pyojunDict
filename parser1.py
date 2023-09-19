import json

f = open("wordlist.txt", 'w',encoding="UTF-8")

def write(data): # 메모장에 데이터 작성
    wordlist = []
    for i in range(5000):
        if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "동사": #특정 품사의 단어 제거
            if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "형용사":
                if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "구":
                    json_string = data["channel"]["item"][i]["word_info"]["word"]

        if "-" in json_string: # type: ignore ##문자열 내의 특정 문자 제거
            json_string = json_string.replace('-', '') # type: ignore
        if "^" in json_string: # type: ignore
            json_string = json_string.replace('^', '') # type: ignore
        if " " in json_string: # type: ignore
            json_string = json_string.replace(' ', '') # type: ignore

        for k in range(11): # 문자열 안에 숫자가 포함되어있으면 숫자 제거
            if str(k) in json_string: # type: ignore
                json_string = json_string.replace(str(k), '') # type: ignore
            
        if json_string in wordlist: # type: ignore
            pass
        else:
            wordlist.append(json_string) # type: ignore
            f.write(json_string + "\n") # type: ignore
            print(json_string) # type: ignore


with open('C:\\Users\\calvi\\OneDrive\\바탕 화면\\코딩\\Korean_JSON_Parse\\전체 내려받기_표준국어대사전_JSON_20230906\\1200922_5000.json', 'rt', encoding="UTF-8") as json_file:
    json_data = json.load(json_file)


write(json_data)


f.close()
