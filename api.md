# vs code
: 파이썬 언어를 적을 수 있게 도와주는 도구
- 코드 편집기 (edit area) : 기획의 로직을 파이썬 코드로 구현하는 공간 (~를 불러와)
- 터미널 (terminal) : 컴퓨터에게 명력을 내릴 때(input), 코드의 실행 결과를 확인할 때(output)
- problems : 코드에 오타나 문법 틀렸을 때 경고를 줌.
- Output : 로그 기록
- chat&build with agent : github copilot 같은 ai 기능. 구현하고 싶은 기능 말하면 ai가 코드 제안함.

# API 호출 과정
1. pip3 install requests : 배달 앱 + 설치 + requests라는 부품
2. import requests : 설치한 requests 부품을 불러와라.
3. def : define. 함수를 정의한다.
4. def serch_music(artist_name) : serch music이라는 함수를 정의할 건데, artist name이라는 데이터가 필요해.
5. url = f"..." : 문자열 안에 변수를 집어넣겠다. {변수}.
6. [https://itunes.apple.com/search?term={artist_name}&entity=song&limit=3](https://itunes.apple.com/search?term=%7Bartist_name%7D&entity=song&limit=3)
: 애플이 검색하고 싶으면 /search라고 쓰세요, term= 뒤의 {변수}를 DB에서 검색하세요, {변수}는 아티스트 명을 찾을 거라고 정의한 겁니다, entity=song 정보만 보내주세요(앨범, 뮤비 말고), limit=3 : 3개만 보여줘라.
7. response=requests.get(url) : requests가 url 주소로 신호를 보내서 서버로부터 돌아온 모든 정보를 response에 담아온다. reponse(결과물), requests~(행동)
8. if response.status_code == 200: : 데이터(응답)가 정상적으로 도착했으면
9. data=response.json() : 서버로부터 받은 텍스트 데이터(응답)를 파이썬이 다룰 수 있는 dictionary 구조로 변환해.
10. results = data.get('results', []) : 데이터 뭉치에서 results라는 이름의 리스트만 뽑아내고 없으면 [].
11. print(f"\n[호텔 시스템] 고객님 맞춤의 '{artist_name}' 데이터를 불러왔습니다.") : "[호텔 시스템] 고객님 맞춤의 '{artist_name}' 데이터를 불러왔습니다." 라고 출력해.
12. for song in results: 반복 추출. (limit=3이니까 총 3번) results에 있는 곡을 하나하나 꺼내서 song이라는 변수에 담아.
13. track_name = song.get('trackName') : key값 접근. json은 이름:값의 쌍으로 이루어져있는데, trackName이라는 key가 있음. 이걸로 열고 값을 가져와. 그 값을 track_name이라는 이름으로 저장해. 그리고 print(f"곡명: {track_name}") 이 형식으로 출력해.
14. else: print("API 통신 에러: 데이터를 불러올 수 없습니다.") : 없으면 에러 문구 띄워.
15. search_music("Xdinary Heroes") : Xdinary Heroes라는 데이터로 함수 실행해.
- . : ~의 안에 있는(소유와 위치) or ~해라(기능 실행)
- 파라미터(parameter) : 매개변수. 전달되는 조건값. 파라미터가 바뀌면 결과도 바뀜. '이 조건'을 가지고 해. artist name이라는 조건을 받아서 처리해. 애플 서버(api)에게 term(검색어)와 entity(종류)와 limit(개수)라는 세 조건을 줄테니 맞춰서 데이터 가져와.
- 파싱 : parsing. 받아온 데이터 뭉치를 우리가 원하는 정보(곡명, 이미지)로 쪼개서 정리하는 과정.
