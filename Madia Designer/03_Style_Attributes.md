# 03_Style_Attributes

## 1. Layout Grid
복잡한 요소를 구조적으로 배치하기 위한 가이드라인 기능.

- **설정 방법**: 우측 패널 `Layout grid` (+) 클릭 -> Grid Settings 설정.
- **주요 속성**:
  - **Columns**: 화면을 나누는 세로 기둥 (웹 표준은 주로 12, 14, 16 사용).
  - **Margin**: 프레임 좌우측의 바깥 여백 (예: 60).
  - **Gutter**: 기둥(Column) 사이의 간격 (예: 32).
  - **Type**: 정렬 방식. 보통 `Stretch`를 사용하여 프레임 크기에 따라 유동적으로 변하게 설정.

### 1-1. 실습: 아이콘 가이드 제작 프로세스
아이콘의 일관된 비율과 시각적 무게감을 통일하기 위한 가이드라인 제작법.

1. **대상 선택**: 아이콘(또는 프레임) 선택 후 `Layout Grid` (+) 클릭.
2. **외곽 가이드 설정 (Safe Area)**:
   - `Rows` 추가: `Count 1` / `Gutter 0` / `Margin` 입력 (외곽에 닿는 정수값).
   - `Columns` 추가: 위와 동일하게 설정하여 전체 틀 생성.
3. **내부 가이드 추가 (Key Shape)**:
   - `Rows` 추가: 다른 색상 선택 및 불투명도 100%. `Margin`을 앞서 설정한 값보다 작게 입력하여 내부 영역 확보.
   - `Columns` 추가: 위와 동일하게 설정.
4. **결과**: 정사각형, 세로형 직사각형, 가로형 직사각형 3가지 형태의 가이드가 중첩됨.
5. **원칙**: 모든 아이콘을 이 가이드의 가로/세로 폭에 맞춰 그려 시각적 통일성 부여.
   
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
  - **Case**: 아무 속성 없음 or 대문자 or 소문자 or 대소문자(Artists' Directory)
  - **List Style**: 구분점.
  - **Vertical Trim**: 폰트 상하단의 불필요한 공백을 제거하여 박스 크기를 폰트 사이즈에 딱 맞게 정렬.
  - **Truncate Text**: 말줄임표(...) 설정. `Max lines`를 통해 노출할 최대 줄 수 정의 가능.
  - **Hanging Punctuation/Lists**: 문장 앞 따옴표(`"`)나 구분점 때문에 정렬이 어긋나 보이지 않도록 텍스트 시작점을 맞춰주는 정렬 기능.

## 3. Fill & Stroke
### Fill (채우기)
- **Solid**: 단색 설정 및 불투명도 조절.
- **Gradient**: 시작과 끝 포인트를 조절하는 그라데이션
  - **Linear**: 선.
  - **Radial**: 원. 중심부 -> 바깥 방향. 가운데를 밝게 하고 싶을 때 많이 쓰임.
  - **Angular**: 원인데 입체적인 효과. 사용하기 까다로운 편.
  - **Diamond**: 안으로 빨려가는 효과.
  - **Rotation Gradiant, Flip Gradiant**: 포인트 위치 뒤집거나 바꾸는 기능.
- **Image**: 
  - `Fill`: 도형에 맞춰 꽉 채움 (기본).
  - `Fit`: 이미지 전체가 보이도록 맞춤.
  - `Crop`: 원하는 영역만 자름.
  - `Blend Mode`: 물방울 아이콘. 이미지와 배경색을 합성.
    - Blending : 색상 혼합
    - 위에 있는 레이어의 색상이 아래에 있는 레이어와 어떻게 섞일지 정하는 규칙
    - Multiply, Pass Through 등 다양한 설정값으로 바꿔보면서 어떻게 뒤에 레이어와 녹아드는지 확인 후 선택
- `Opacity` : 불투명도

### Stroke (테두리)
- **Position**: `Inside` / `Center` / `Outside`. 
  - *Tip: UI 디자인(컴포넌트)에서는 개발자와의 정확한 간격 계산을 위해 주로 `Inside`를 사용함.*
- **Individual Strokes**: 프레임의 상/하/좌/우 중 원하는 면에만 테두리 적용 가능 (예: 하단 라인만 있는 Input Box 제작 시 유용).
  - 프레임 만들기 : `Shift` + `A` or 우클릭 + `Frame Selection` or `Command` + `Option` + `G`.
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
- **Preview**: 내보내기 전 잘리는 부분은 없는지 미리 확인 가능.
