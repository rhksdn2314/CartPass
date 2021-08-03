1.Learning to navigate for fine-grained Classification
 - Navigator: 모델의 초점을 가장 유용한 영역에 맞춤. 이미지의 각 영역에 대해 영역이 얼마나 유용한지 예측하고 예측은 가장 유용한 영역 제안
 - Teacher: Navigaotor가 제안한 지역 평가, 피드백 제공 ground-truth class에 속하는 확률 평가, 신뢰도 평가는 손실함수로 더 많은 정보를 제공할 수 있도록 함
 - Scrutinizer: Navigator에서 제안된 영역 면밀히 조사
* 새로운 손실함수 제안
* https://github.com/yangze0930/NTS-Net
