# DataCampus2021_KU_Team3
2021 데이터청년캠퍼스 고려대학교과정 3조입니다.

## 프로젝트 주제
음료수 식별 서비스  

## Related Model List
### 1. Densenet
### 2. NTS-net
### 3. Dynamic Routing Capsnet
### 4. CAP
### \+ Attention, MM, FRL, Humans in the loop
---
### 1. Densenet
- Feature map끼리의 Concatenation을 이용
- 이점
	- Vanishing Gradient 개선
	- Feature Propagation 강화
	- Feature Reuse
	- Parameter 수 절약
- DenseNet-BC : bottleneck layer와 θ<1인 transition layer를 모두 사용하는 모델
  - Accuracy (CIFAR-100 Dataset) : DenseNet-BC(82.82), DenseNet-BC-190, S=4(87.44)
- DenseNet161 + MM + FRL : MinMax, Feature Redundancy Loss 사용
  - Accuracy : 95.2(Stanford Cars Dataset), 94.0(FGVC Aircraft)
  
## 수집할 데이터, Data Feature 과제
![데이터청년캠퍼스_3조_과제](https://user-images.githubusercontent.com/51364769/126651302-d02eb55f-6d7a-4512-95b8-57913b36cbed.png)

## 발표자료


