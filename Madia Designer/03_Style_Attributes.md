# 03_Style_Attributes

## 1. Layout Grid
복잡한 요소를 구조적으로 배치하기 위한 가이드라인 기능.

- **설정 방법**: 우측 패널 `Layout grid` (+) 클릭 -> Grid Settings 설정.
- **주요 속성**:
  - **Columns**: 화면을 나누는 세로 기둥 (웹 표준은 주로 12, 14, 16 사용).
  - **Margin**: 프레임 좌우측의 바깥 여백 (예: 60).
  - **Gutter**: 기둥(Column) 사이의 간격 (예: 32).
  - **Type**: 정렬 방식. 보통 `Stretch`를 사용하여 프레임 크기에 따라 유동적으로 변하게 설정.
- **아이콘 가이드**: 아이콘 제작 시 `Rows`와 `Columns`를 교차 추가하여 정사각형/직사각형 가이드를 그려 일관된 비율 유지 가능.

## 2. Typography
- **기본 속성**:
  - **Line height**: 행간 (px 또는 % 단위).
  - **Letter spacing**: 자간.
  - **Paragraph spacing**: 문단 간 간격 (단순 줄바꿈과 다른 개념).
- **텍스트 박스 리사이징**:
  - **Auto Width**: 텍스트 길이에 따라 박스 너비가 자동 조절됨.
  - **Fixed Size**: 박스 크기 고정. 영역을 벗어나는 텍스트는 가려짐 (모바일 하단 가리기 디자인 등에 유용).
  - **Auto Height**: 너비는 고정되되, 텍스트 길이에 따라 높이가 아래로 늘어남.
  - *Tip: 텍스트 박스 우측 경계선을 더블클릭하면 `Fixed`에서 `Auto Width`로 복구됨.*
- **세부 설정 (Type Settings)**:
  - **Vertical Trim**: 폰트 상하단의 불필요한 공백을 제거하여 박스 크기를 폰트 사이즈에 딱 맞게 정렬.
  - **Truncate Text**: 말줄임표(...) 설정. `Max lines`를 통해 노출할 최대 줄 수 정의 가능.
  - **Hanging Punctuation/Lists**: 문장 앞 따옴표(`"`)나 구분점 때문에 정렬이 어긋나 보이지 않도록 텍스트 시작점을 맞춰주는 정렬 기능.

## 3. Fill & Stroke
### Fill (채우기)
- **Solid**: 단색 설정 및 불투명도 조절.
- **Gradient**: 시작과 끝 포인트를 조절하는 그라데이션 (Linear, Radial, Angular, Diamond).
- **Image**: 
  - `Fill`: 도형에 맞춰 꽉 채움 (기본).
  - `Fit`: 이미지 전체가 보이도록 맞춤.
  - `Crop`: 원하는 영역만 자름.
  - `Blend Mode`: 이미지와 배경색을 합성 (Multiply, Pass Through 등).

### Stroke (테두리)
- **Position**: `Inside` / `Center` / `Outside`. 
  - *Tip: UI 디자인(컴포넌트)에서는 개발자와의 정확한 간격 계산을 위해 주로 `Inside`를 사용함.*
- **Individual Strokes**: 프레임의 상/하/좌/우 중 원하는 면에만 테두리 적용 가능 (예: 하단 라인만 있는 Input Box 제작 시 유용).
  - 프레임 만들기 : shift+a or 우클릭+frame selection or cmd+option+g
- **Style**: 실선(Solid) 또는 점선(Dash) 설정 가능.
  - `Dash`: 점의 길이
  - `Dash Cap`: 점선 끝점의 모양
    - 라운드 줬는데 반이 잘려 보이는 이유는 `Inside` 방향으로 되어있기 때문.
    - `Join`: 모서리 모양. 마찬가지로 `Inside`일 때 `Center`일 때 `Outside`일 때 모양 다름. `Center`일 땐 4인 게 `Outside`로 하면 8이기 때문에. 곡선 더 완만해짐. 그리고 단순 `Join`과 도형 자체에 라운드 주는 거랑도 모양 완전히 다름.
  - `Gap`: 점 사이 간격.

## 4. Effect
- **Background Blur**: 객체 뒤쪽 배경을 흐리게 처리. (객체의 투명도를 낮춰야 효과가 보임. 모바일 위젯이나 재생 바 디자인에 다수 활용)
- **Layer Blur**: 객체 자체를 흐리게 처리. (배경에 은은한 색감을 깔 때 유용)
- **Drop Shadow**: 객체 바깥쪽 그림자. 
  - `X, Y`: 그림자 위치 / `Blur`: 번짐 정도 / `Spread`: 그림자 면적 확장. 빈 공간이 더 채워져 보임. 디테일한 그림자 디자인 가능.
- **Inner Shadow**: 객체 안쪽으로 생기는 그림자. 
  - 여러 개의 `Inner Shadow`를 중첩(Stack)하여 입체감 있는 3D 아이콘 등을 제작 가능.
  - `Inner Shadow`로 3d 아이콘 만들기
    1. 라운드 준 사각형
    2. 사각형 `Fill` 대각선으로 그라디언트 입힘.
    3. `Inner Shadow`(4,4,12,컬러값,불투명도100%), `Inner Shadow`(-2,-4,12,컬러값,100%), `Inner Shadow`(2,2,6,white,50%), `Inner Shadow`(-1,-2,6,컬러값,30%) 겹겹이 쌓음.
    4. 사각형 복사 후 shadow 빼고 그라디언트 빼고, 그림자 컬러값 설정, 불투명도 60%, layer blur 200, send to back
    5. 로고 완성

## 5. Export
- **배수 설정**: `1x`, `2x`, `3x` 등 배율 조절 가능. 피그마는 벡터 기반이므로 확대해도 화질 저하가 없음.
- **파일 형식**: PNG, JPG, SVG, PDF 등 선택.
- **Preview**: 내보내기 전 잘리는 부분은 없는지 미리 확인 가능.**# layout grid
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

- preview : 미리보기
- export frame... : frame...을 내보내겠다
