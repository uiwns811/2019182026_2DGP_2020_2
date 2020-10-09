# 2019182026_2DGP_2020_2

2020-2 2DGP 기말 프로젝트 '무한의 계단'
=======================================

1. 게임 소개
	- 제목 : 무한의 계단
	- 기존 모바일 게임 '무한의 계단'을 copy한 모작 게임이다.
	- 계속해서 이어지는 계단을 방향을 바꾸어가며 오르며 떨어지지 않고 버티는 게임이다. 유한하게 정해져 있는 계단을 떨어지지 않고 다 오르는 것을 목표로 한다. 마우스 왼쪽 버튼으로 계단을 올라가며, 스페이스바 입력을 통해 방향을 전환한다. hp는 기본적으로 소모되며, 계단을 오를 때 hp가 상승한다. hp가 다 소모되어도 실패한다.   
  
  <div>
<img width = "200" src = "https://user-images.githubusercontent.com/71070963/94255201-d8f47a00-ff62-11ea-8f43-88b41b74b836.jpg">
 <img width = "200" src = "https://user-images.githubusercontent.com/71070963/94255192-d7c34d00-ff62-11ea-990d-2f0e84a8efd5.png">  
	
	
	
2. Game State의 수 및 각각의 이름
	- 총 Game state의 수는 4개이다.
	- start
	- running
	- gameover
	- ending  
	
	
3. 각 GameState 별 설명
	- start
		* 본격적인 게임 시작 전 로딩화면으로, 게임을 시작하라는 입력을 받는다.
		* 게임 제목, Game Start, Help
		* 마우스 입력을 받는다. Help를 누르면 간단한 조작법을 출력한다.
		* 마우스 왼쪽 버튼으로 Game Start를 누르면 runnning state로 이동한다.     
	
	
	- running
		* 게임이 진행되는 state이다.
		* object, 계단
		* 마우스 왼쪽 버튼 입력으로 계단을 오른다.  스페이스바 입력으로 객체의 방향을 전환한다.
		* 이어지는 계단이 없는데 계단을 오른다면 계단에서 떨어지고, gameover state로 이동한다. 
    또한 hp가 모두 소모되면 gameover state로 이동한다. 정해진 계단을 모두 올라가면 ending state로 이동한다.   
    
    
    
	- gameover
		* 계단에서 떨어졌을 때, hp가 모두 소모되었을 때 실행되는 화면이다.
		* object, score, Retry
		* 마우스 왼쪽 버튼으로 Retry를 클릭하면 게임을 다시 시작한다.
		* Retry를 클릭하면 running state로 이동하여 게임을 다시 시작한다.   
	
	
	
	- ending
		* 주어진 계단을 모두 오르면 실행되는 화면이다.
		* object, score, NewGame, Quit
		* 마우스 왼쪽 버튼으로 입력받는다.
		* NewGame을 클릭하면 running state로 이동하여 다시 게임을 시작한다. Quit를 클릭하면 게임을 종료한다.   
	
# 1차 발표에 대한 내용 추가 (20.10.09)
	
4. 필요한 기술
	- 좌표값 처리, 움직임 철디
	- 사운드 삽입, 화면에 배경이 자연스럽게 움직이도록 구현하는 법
	- 이동하는 객체를 따라 생성되는 그림자(부스터) 구현하는 법
     


5. 게임 컨셉
	- 무한히 이어지는 계단에 맞추어 캐릭터의 진행 방향을 바꾸며 오르는 게임이다.
	- 계단에서 떨어지지 않고 버티는 


6. 예상 게임 실행 흐름
	- 캐릭터의 진행 방향 앞에 계단이 있다면 마우스 입력으로 계단 오르기를 실행한다
	- 캐릭터의 진행 방향 앞에 계단이 없다면 SPACE 입력으로 방향 전환을 한다. 방향 전환에서는 계단을 한 칸 오르는 것이 포함된다.
	- 게임이 진행되며 HP는 계속해서 소모된다.
	- 캐릭터가 계단을 오르면 HP는 소량 증가한다.
	- 캐릭터의 진행 방향 앞에 계단이 없는데 마우스 입력을 했다면 계단에서 추락하고 **GAMEOVER**
	- HP가 모두 소요되면 **GAMEOVER**
	- 캐틱터의 진행 방향 앞에 아이템(코인)이 있는 경우 계단 오르기를 실행하면 자연스럽게 습득하게 되며, 점수를 +5점 획득한다.


7. 개발 범위
	- 캐릭터
		* 최소 범위 : SPACE 입력으로 방향(좌우)전환, 마우스 입력으로 계단 오르기
		* 추가 범위 : 자연스러운 캐릭터의 움직임 구현
	
	- 맵
		* 최소 범위 : 계단 스테이지 1개 구현
		* 추가 범위 : 특정 점수 도달 시 추가 스테이지 구현
	
	- 난이도
		* 최소 범위 : 게임이 진행되며 HP의 소모 속도는 증가한다.
		* 추가 범위 : 게임 시작 화면에서 난이도를 선택할 수 있는 기능을 추가한다 (EASY / HARD)
		
	- 아이템
		* 최소 범위 : 습득시 점수를 획득하는 코인
		* 추가 범위 : 습득시 HP가 증가되는 하트
		
	- 게임 기능
		* 최소 범위 : 시간의 흐름에 따라 HP가 소모되며, 계단을 오르면 HP가 증가한다.
		* 추가 범위 : 게임 종료 시 남은 HP를 점수로 환산, 점수 저장 후 재도전 기능, 간단한 조작법을 설명하는 기능 추가
	
	- 사운드
		* 최소 범위 : 배경음악, 계단 오르기 효과음, 방향 전환 효과음, 게임오버 효과음
		* 추가 범위 : 새로운 스테이지 입장 효과음
		
		
8. 개발 일정
	- 1주차 : 리소스 수집
		* 게임 개발에 필요한 리소스 수집
		* 캔버스에 객체의 좌표 지정
		
	- 2주차 : 캐릭터 기본 오브젝트
		* 캐릭터 기본 애니메이션(방향 전환, 계단 오르기) 구현
		* 맵(계단) 구현
		
	- 3주차 : 아이템 및 HP
		* 아이템 (코인) 구현
		* HP 소모와 GAMEOVER 구현
		
	- 4주차 : 중간 점검
		* 1~4주차를 진행하는 동안 부족한 점 보완
		* 점수 저장 후 재도전하는 기능 추가
		
	- 5주차 : 화면 구현
		* 시작화면, 타이틀화면, 종료화면 구현
		* 게임 시작을 누르면 시작하도록 구현
		* 종료 전 합산 점수 출력
		
	- 6주차 : 충돌 체크
		* 계단 오르기와 추락 점검
		
	- 7주차 : 추가 기능 구현
		* 난이도 선택 기능 구현
		* 특정 점수 도달시 추가 스테이지 구현
		* 튜토리얼 구현
		
	- 8주차 : 밸런스 조절, 최종 점검
		* 밸런스 조절
		* 최종 점검
		* 마무리
