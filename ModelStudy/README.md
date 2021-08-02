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
Test Accuracy: 52.96  
위 Test Accuracy는 20 epoch을 돌린 후 나온 accuracy로, validation 과정을 거치지 않아 비교를 하지 못하였음.  
validation 과정을 추가하고 learning curve를 보고 수정할 예정  
  
Training Accuracy는 다음과 같음.  
![input](https://user-images.githubusercontent.com/51364769/127870250-ba2bbab0-4f94-4566-a5ff-9a50b930d7f5.JPG)  
주요 참고 사이트: https://youtu.be/Lu93Ah2h9XA  
