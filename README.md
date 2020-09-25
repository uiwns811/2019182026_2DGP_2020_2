# 2019182026_2DGP_2020_2

2020-2 2DGP 기말 프로젝트 '무한의 계단'
=======================================

1. 게임 소개
	- 제목 : 무한의 계단
	- 기존 모바일 게임 '무한의 계단'을 copy한 모작 게임이다.
	- 계속해서 이어지는 계단을 방향을 바꾸어가며 오르며 떨어지지 않고 버티는 게임이다. 유한하게 정해져 있는 계단을 떨어지지 않고 다 오르는 것을     목표로 한다. 마우스 왼쪽 버튼으로 계단을 올라가며, 스페이스바 입력을 통해 방향을 전환한다. hp는 기본적으로 소모되며, 계단을 오를 때 hp가     상승한다. hp가 다 소모되어도 실패한다.   
  
  <
  <img width = "200" src = "https://user-images.githubusercontent.com/71070963/94255192-d7c34d00-ff62-11ea-990d-2f0e84a8efd5.png">
  <img width = "200" src = "https://user-images.githubusercontent.com/71070963/94255201-d8f47a00-ff62-11ea-8f43-88b41b74b836.jpg">

     
2. Game State의 수 및 각각의 이름
	- 총 Game state의 수는 4개이다.
	- start
	- running
	- gameover
	- ending

    
3. 각 GameState 별 설명
	1) start
	- 본격적인 게임 시작 전 로딩화면으로, 게임을 시작하라는 입력을 받는다.
	- 게임 제목, Game Start, Help
	- 마우스 입력을 받는다. Help를 누르면 간단한 조작법을 출력한다.
	- 마우스 왼쪽 버튼으로 Game Start를 누르면 runnning state로 이동한다.
	    
	2) running
	- 게임이 진행되는 state이다.
	- object, 계단
	- 마우스 왼쪽 버튼 입력으로 계단을 오른다.  스페이스바 입력으로 객체의 방향을 전환한다.
	- 이어지는 계단이 없는데 계단을 오른다면 계단에서 떨어지고, gameover state로 이동한다. 
    또한 hp가 모두 소모되면 gameover state로 이동한   다. 정해진 계단을 모두 올라가면 ending state로 이동한다.
    
	3) gameover
	- 계단에서 떨어졌을 때, hp가 모두 소모되었을 때 실행되는 화면이다.
	- object, score, Retry
	- 마우스 왼쪽 버튼으로 Retry를 클릭하면 게임을 다시 시작한다.
	- Retry를 클릭하면 running state로 이동하여 게임을 다시 시작한다.
    
	4) ending
	- 주어진 계단을 모두 오르면 실행되는 화면이다.
	- object, score, NewGame, Bye
	- 마우스 왼쪽 버튼으로 입력받는다.
	- NewGame을 클릭하면 running state로 이동하여 다시 게임을 시작한다. Bye를 클릭하면 게임을 종료한다.
    

4. 필요한 기술
	- 좌표값 처리, 움직임 철디
	- 사운드 삽입, 화면에 배경이 자연스럽게 움직이도록 구현하는 법
	- 이동하는 객체를 따라 생성되는 그림자(부스터) 구현하는 법
     
