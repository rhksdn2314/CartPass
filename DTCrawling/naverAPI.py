import urllib.request
import json

def main():
    f = open("nameList.txt", "r")
    nameList = f.read().split(',')

    for name in nameList:
        download_image(name)


def download_image(name):
    ## 네이버 api 사용
    client_id = "U6VBsZ6DRyQnuu4bXnPg"
    client_secret = "yQhfsCm0kH"

    # 찾을 상품명 입력
    encText = urllib.parse.quote(name)

    try:
        # 네이버 이미지 검색
        # display 값에 원하는 이미지 개수 입력
        url = "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=20"  # json 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        count = 1;
        if (rescode == 200):
            response_body = response.read()
            py_rt = json.loads(response_body.decode('utf-8'))

            #print(py_rt["items"])
            for _ in py_rt["items"]:
                src = _["link"]
                #print(name + str(count))
                urllib.request.urlretrieve(src, "./download/" + name + "/" + "n_" + str(count) + ".jpg")
                count += 1
        else:
            print("Error Code:" + rescode)
    except:
        print("네이버 이미지 검색 오류 - " + name)


    ###############
    try:
        # 네이버 쇼핑 검색 결과에서 이미지 가져오기
        url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText + "&display=20"  # json 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            py_rt = json.loads(response_body.decode('utf-8'))
            # print(py_rt)
            for _ in py_rt["items"]:
                src = _["image"]
                # print(src)
                urllib.request.urlretrieve(src, "./download/" + name + "/" + "n_" + str(count) + ".jpg")
                count += 1
        else:
            print("Error Code:" + rescode)
    except:
        print("네이버 쇼핑 이미지 검색 오류 - " + name)