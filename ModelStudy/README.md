## 딥러닝을 이용한 classification model 만들기를 공부하고 익숙해져보자.
class 수: 10 (임의로 10개 음료 상품 선정)  
Training 데이터셋 크기: 1140 (각 114장)  
Test 데이터셋 크기: 236  
Validation 데이터셋 크기: 150 (각 15장)  
  
Training/Validation 데이터셋은 aihub의 '상품 이미지 데이터' 사용  

---

#### 1. CNN  
  
#### 2. transferLearning using Resnet34  
Restnet34 모델의 출력 뉴런 수를 10개로 교체하여 마지막 레이어 다시 학습  
7th epoch - Test Accuracy: 77.92  
validation 과정을 추가함  
  
<img width="522" alt="KakaoTalk_20210805_131219234" src="https://user-images.githubusercontent.com/51364769/128291425-b650a2c9-3c54-41e5-988d-0aed7f23da1a.png">
<img width="524" alt="KakaoTalk_20210805_131159161" src="https://user-images.githubusercontent.com/51364769/128291426-06ba5bc5-1f4e-445d-9259-a14155d74d16.png">
<img width="294" alt="KakaoTalk_20210805_131915289" src="https://user-images.githubusercontent.com/51364769/128291423-e5472fde-f043-4d98-b959-703a6840819e.png">
<img width="299" alt="KakaoTalk_20210805_133126278" src="https://user-images.githubusercontent.com/51364769/128291422-45e74a47-ac76-417b-91ab-6999ede01f0d.png">
  
#### 3. NTS-Net
논문(Learning to Navigate for Fine-grained Classification)과 Github을 보고 코드 뜯고 주석 다면서 모델 이해 중 
이것은 중간과정이므로 이후 깔끔한 version으로 업로드 할 예정

논문: https://openaccess.thecvf.com/content_ECCV_2018/papers/Ze_Yang_Learning_to_Navigate_ECCV_2018_paper.pdf 

Github: https://github.com/yangze0930/NTS-Net
