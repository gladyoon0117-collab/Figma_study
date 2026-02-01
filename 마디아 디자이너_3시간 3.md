# layout grid
- 웹 디자인할 때 복잡한 요소를 잘 정리되어 보이게끔 레이아웃 구성하는 기능
- 우측 패널 -> layout guide 추가(+) -> layout guide settings에서 속성 선택 (colums(화면을 몇 개로 나누어서 볼 건지=12, 대부분 colums=12,14,16으로 설정), color=default(red), margin(좌우측 여백=60), gutter(박스 사이의 여백=32), type(정렬 축=보통은 stretch 설정)
- 웹 디자인뿐 아니라 아이콘 가이드 그릴 때도 사용 가능

# 01.31 (2h 43m)
# 아이콘 가이드 그리기
- rows : 상단/하단
- columns : 좌측/우측
1. 아이콘 select -> 우측 패널 layout grid 추가(+) -> layout guide settings에서 rows -> count 1 -> gutter 0 -> margin (아이콘 외곽 닿는 만큼/정수로만 설정 가능)
2. columns 동일하게 추가
3. rows 추가 -> 다른 색 설정 및 100% -> count 1, gutter 0 -> 1,2 margin보다 작은 값
4. columns 동일하게 추가
5. 정사각형, 세로가 긴 직사각형, 가로가 긴 직사각형 3개 만들어짐.
6. 아이콘은 가로/세로 가이드에 맞춰 그려짐.

# 블렌딩 모드 설정값
- blending : 색상 혼합
- 위에 있는 레이어의 색상이 아래에 있는 레이어와 어떻게 섞일지 정하는 규칙
- 우측 패널 appearance -> 물방울 아이콘 -> pass through, multiply 등 다양한 설정값으로 바꿔보면서 어떻게 뒤에 레이어와 녹아드는지 확인 후 선택
- opacity : 불투명도

# typography
- line height : 행간. 픽셀 또는 퍼센티지로 정의 가능. 폰트 사이즈에 알맞는 행간 사이즈 대부분 있음.
- letter spacing : 자간. 픽셀 또는 퍼센티지로 정의 가능.
- paragraph spacing : 문단별 간격. 줄간격과 다른 개념.
- 텍스트 박스
  - auto width : 텍스트의 길이에 따라 박스 너비가 자동으로 늘어나거나 줄어드는 기능.
  - fixed size : 내가 정해놓은 텍스트 박스 사이즈가 고정됨. 길어지면 줄바꿈 되는 셈. 그리고 고정한 크기보다 더더 길어지면 박스 영역 밖의 텍스트는 가려짐. 모바일 디자인에서 bottom에 가려지는 디자인 필요할 때 유용.
  - auto height : fixed size와 유사하지만 길어져도 박스 영역 밖의 텍스트가 넘쳐서라도 보임.
  - 보통 텍스트를 처음 쓰면 기본적으로 auto width 상태이지만, 마우스로 텍스트 박스 크기를 한 번이라도 건드리면 fixed size로 고정되어 버림. 이 상태에서 텍스트 박스 우측 세로변을 더블클릭하면 auto width로 다시 바꿀 수 있음.
- alignment : 정렬값. 좌/우/중앙 and 상/중/하. default는 좌측+상단 고정. 텍스트가 추가되면 좌측과 상단은 고정되고 아래로 추가됨. e.g. 좌측+중앙 select 되어있으면 텍스트가 위와 아래로 추가되면서 박스 넓어짐.
- type settings : 텍스트 설정값 더 세부적으로 조정할 수 있음.
  - basics
    - case : 아무 속성 없음 or 대문자 or 소문자 or 대소문자(Artists' Directory)
    - vertical trim : 박스 높이. 보통 대소문자와 y같이 튀어나오는 부분 때문에 guide가 2개 제공되는데 standard 일반적으로 씀. 폰트의 프레임 영역 박스가 같이 잡힘(standard) or 폰트 사이즈에 딱맞게 박스 크기가 잡힘.
    - list style : 구분점
    - truncate text : 말줄임
    - max lines : 최대 몇 줄까지 보여줄 것인지 정의
  - details
    - hanging punctuation : "" 들어가면 정렬 안 맞아보이는 경우 많은데, "의 뒤 텍스트로 정렬 맞춰줌.
    - hanging lists : 한 줄에면 구분점 빠져서 정렬 뭉개질 때 텍스트 기준으로 정렬 맞춰줌.

# fill
- fill : 모든 컬러값 설정
- + : 색 추가하면서 조합해서 사용할 수 있음. 원래는 투명 이미지인데 약간 그레이 톤 깔린 것처럼 가고 싶을 때. 잔잔한 그라데이션 배경 넣을 수도.
- custom
  - solid : 색 설정과 불투명도 조절. hex(컬러값을 수치화한 것)
  - gradient : 그라데이션. start point와 end point 움직여 컬러 위치 설정 가능. bar에서 중간 지점 클릭하면 중간에도 색 추가 point 생성할 수 있음.
    - 형태
      - linear : 선
      - radial : 원. 중심부 -> 바깥 방향. 가운데를 밝게 하고 싶을 때 많이 쓰임.
      - angular : 원인데 입체적인 효과. 사용하기 까다로운 편.
      - diamond : 안으로 빨려가는 효과.
      - rotation gradiant, flip gradiant : point 위치 뒤집거나 바꾸는 기능.
  - image : 이미지 삽입.
    - fill : default. 도형에 맞게 꽉 채움.
    - fit : 원본 사이즈 이미지 보여줌.
    - crop : 원하는 대로 사이즈 조정하면서 자름. 
    - exposure, contrast... : 사진 보정
  - 물방울 아이콘 : blend mode
    
# stroke
- stroke : 외곽선
- inside/center/outside : 박스에서 안쪽/가운데 기점/바깥쪽 어디에 넣을지. 보통 UI 디자인의 컴포넌트에서는 inside만 활용함. 개발자가 정확한 간격 재기 위해.
- individual strokes : 프레임의 위쪽만/아래쪽만/... 테두리를 주고 싶을 때. 그냥 텍스트일 때는 설정 불가, 프레임으로 만들어야 설정 가능. (shift+a or 우클릭+frame selection or cmd+option+g)
  - 프레임 : 글자를 담는 투명한 상자. 자기만의 w,h와 배경색, 테두리를 가질 수 있음.
- stroke settings
  - style : 실선/점선
  - dash : 점선일 때 점의 길이
  - gap : 점 사이의 여백 길이
  - dash cap : 점선 끝점의 모양
    - round 시켰는데 반이 잘려 보이는 이유는 inside 방향으로 되어있기 때문.
    - join : 모서리 모양. 마찬가지로 inside일 때 center일 때 outside일 때 모양 다름. center일 땐 4인 게 outside로 하면 8이기 때문에. 곡선 더 완만해짐. 그리고 단순 stroke join과 도형 자체에 round 주는 거랑도 모양 완전히 다름.
  - e.g. 검색 input box 만들 때 전체 테두리 말고 밑에만 주고 싶을 때 그리지 않고 stroke 하단만 주는 방식으로 디자인할 수 있음.

# effect
- background blur : 뒤에 blur 효과. blur 값 조정도 가능. 뒤에 효과를 주는 것이므로 투명도와 함께 써야 의미가 있음. 에어드롭 레이어 같은. 모바일에 위젯이나 재생중인 음악 레이어 등에서 많이 쓰이네.
- layer blur : 오브젝트 자체에 blur 효과. blur 값 1000 정도로 주고 배경에 양쪽 깔아서 은은한 그라디언트 배경 만들 수도!
- drop shadow : x축(+100 우측/-100 좌측), y측(+100 상단/-100 하단), blur(그림자에 blur), spread(디테일한 그림자 만들 수 있음. 그림자 공간이 수치만큼 확장됨. 빈공간이 더 채워져 보임)
- inner shadow : 안쪽으로 그림자. 상단+좌측 상태에서 우측+하단도 강하게 inner shadow 주고 싶으면 +추가해서 2개 inner shadow 가져가면 됨.
  - inner shadow로 3d 아이콘 만들기
    1. 라운드 준 사각형
    2. 사각형 fill 대각선으로 그라디언트 입힘.
    3. inner shadow(4,4,12,컬러값,불투명도100%), inner shadow(-2,-4,12,컬러값,100%), inner shadow(2,2,6,white,50%), inner shadow(-1,-2,6,컬러값,30%) 겹겹이 쌓음.
    4. 사각형 복사 후 shadow 빼고 그라디언트 빼고, 그림자 컬러값 설정, 불투명도60%, layer blur 200, send to back
    5. 로고

# export
- 몇 배수로 키워서/축소해서 내보낼지 사이즈 조절해서 내보낼 수 있음.
  - x1 : 디자인한 그 사이즈 그대로
  - x3 : 3배 사이즈
  - 확대해서 커져도 화질의 차이는 같음. 피그마는 벡터 기반이기 때문.
- 원하는 파일의 속성으로(png, jpg...)
- preview : 미리보기
- export frame... : frame...을 내보내겠다
