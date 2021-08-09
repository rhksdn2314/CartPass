## 딥러닝을 이용한 classification model 만들기를 공부하고 익숙해져보자.
class 수: 10 (임의로 10개 음료 상품 선정)  
Training 데이터셋 크기: 1140 (각 114장)  
Test 데이터셋 크기: 236  
Validation 데이터셋 크기: 150 (각 15장)  
  
Training/Validation 데이터셋은 aihub의 '상품 이미지 데이터' 사용  

---

#### 1. CNN  
  
#### 2. TransferLearning using Resnet34  
### V1 - Resnet34의 fc layer 변경
- Class 수 : 10
- Training Dataset : 1140
- Test Dataset : 154
- Validation Dataset : 150
- Highest Accuracy : 77.92 %
- <img width="294" alt="KakaoTalk_20210805_131915289" src="https://user-images.githubusercontent.com/51364769/128291423-e5472fde-f043-4d98-b959-703a6840819e.png">
- <img width="299" alt="KakaoTalk_20210805_133126278" src="https://user-images.githubusercontent.com/51364769/128291422-45e74a47-ac76-417b-91ab-6999ede01f0d.png">
  
### V2 - V1과 구조 동일
- Class 수 : 30
- Training Dataset : 3420
- Test Dataset : 483
- Validation Dataset : 450
- Highest Accuracy : 52.38 %
- ![dt1](https://user-images.githubusercontent.com/51364769/128653220-0f40d0c6-d5fd-4715-ab36-46e1fc5bd60e.JPG)
- ![dt2](https://user-images.githubusercontent.com/51364769/128653221-dbad29e2-df38-4932-b643-3cf1e059afc8.JPG)

#### 3. NTS-Net
논문(Learning to Navigate for Fine-grained Classification)과 Github을 보고 코드 뜯고 주석 다면서 모델 이해 중 
이것은 중간과정이므로 이후 깔끔한 version으로 업로드 할 예정

논문: https://openaccess.thecvf.com/content_ECCV_2018/papers/Ze_Yang_Learning_to_Navigate_ECCV_2018_paper.pdf 

Github: https://github.com/yangze0930/NTS-Net
