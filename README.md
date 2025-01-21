# 주식 투자 게임

## 규칙
- 초기 자본금 15,000원, 초기 주식 1주 가격: 3,000원
- 총 5라운드 진행
- 라운드 진행 순서
    - 투자
    - 주가 공개
    - 미니게임
- 첫라운드에는 매수만 가능, 마지막 라운드 종료 시 자동 전량 매도 (미구현)
- 최대 보유 수 10개로 제한하기 (미구현)
- 

## 프로젝트 구조
```
ot-stock-game
├── data
│ ├── round1.txt # 1라운드 매수/매도 정보
│ ├── round2.txt # 2라운드 매수/매도 정보
│ ├── round3.txt # 3라운드 매수/매도 정보
│ ├── round4.txt # 4라운드 매수/매도 정보
│ └── round5.txt # 5라운드 매수/매도 정보
├── results
│ ├── result1.txt # 1라운드 결과
│ ├── result2.txt # 2라운드 결과
│ ├── result3.txt # 3라운드 결과
│ ├── result4.txt # 4라운드 결과
│ └── result5.txt # 5라운드 결과
├── stock
│ ├── stock0.txt # 초기 주식 가격
│ ├── stock1.txt # 1라운드 주식 가격
│ ├── stock2.txt # 2라운드 주식 가격
│ ├── stock3.txt # 3라운드 주식 가격
│ ├── stock4.txt # 4라운드 주식 가격
│ └── stock5.txt # 5라운드 주식 가격
├── src
│ ├── main.py # 앱 진입
│ ├── round_processor.py # 라운드 로직 관리
│ ├── team.py # 팀 정보 정의
│ ├── stock.py # 주식 정보 정의
│ └── file_handler.py # txt 파일 작업
├── ppt
│ ├── ppt1.pptx # 1라운드 결과 PPT
│ ├── ppt2.pptx # 2라운드 결과 PPT
│ ├── ppt3.pptx # 3라운드 결과 PPT
│ ├── ppt4.pptx # 4라운드 결과 PPT
│ └── ppt5.pptx # 5라운드 결과 PPT
└── README.md
```

## 파일 형식
### 입력 파일 
data 폴더 내 각 라운드의 매수/매도 정보 (round.txt)
```
    #팀명, 주식명, 매수/매도, 수량
    1분반, a, buy, 1
    2분반, e, buy, 3
    ...
```
### 출력 파일 
result 폴더 내 각 라운드의 결과 정보 (result.txt)
```
    #팀명, 주식명, 수량, 매입단가, 평가금액, 평가손익, 수익률
    1분반, A, 1, 3000.0, 100, -2900, -96.67%
    2분반, E, 3, 3000.0, 1500, -7500, -83.34%
    ...
```
### 주식 파일
stock 폴더 내 각 라운드의 주식 가격 정보 (stock.txt)
```
    #주식명, 가격
    a, 3000
    b, 3000
    ...
```

## Run
```
cd src
python3 main.py
```

## Requirements
- python-pptx
```
pip install python-pptx
```
