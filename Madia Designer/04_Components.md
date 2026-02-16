# 어제 실습 A/S... + Component (2월 8일 46분...)
- component 걸면 자동으로 assets에 추가됨.
- create component : 전체를 통으로 component 거는 기능
  - e.g. 프로젝트에서 쓰는 버튼 종류가 9개일 때 : 전체 drag + 우측 패널에서 create component(통으로 component 거는 기능) + 좌측 패널 assets에서 통째로 걸린 frame 찾을 수 있음.
- create multiple components
  - 최소 2개 이상의 레이어나 프레임을 한꺼번에 잡아야 메뉴가 활성화됨.
  - 전체 drag했어도 전부 개별적으로 걸림 -> assets에서 확인 가능

# 2월 10일 1h 32m
- create component set : 모양은 비슷하지만 상태나 설정값이 다른 여러 개의 컴포넌트를 하나의 그룹으로 묶는 기능
  -component가 통째로 걸리기는 하지만 set로 걸림.
  - 아이콘 색상을 일일이 바꿀 필요 없이 우측 패널에서 Property만 변경하면 즉시 바뀜.
  - 속성 거는 법 : component set 선택 -> 우측 패널 property 1 같은 input field에 속성 title(e.g. 사이즈) 입력 -> e.g.사이즈별로 전부 선택(큰 애들/중간 애들/작은 애들) -> 각각의 property name에 입력(e.g. 크게=사이즈 56) -> 반복 -> 그럼 사이즈 등록됨 -> assets에서 버튼 불러와서 property에서 건 속성 중 하나 select 해주면 그 속성이 적용됨. -> property에 [+]->variant 통해 속성 추가(e.g.스타일) -> 반복 -> assets에서 보이는 대표 인스턴스 불러와서 샘플처럼 적용 가능 (속성 바꿔가며)
  - 그룹핑 기준에 따라 속성이 생성되고 그룹핑할 수 있는 기준은 다양해서, 같은 component라도 사용자에 따라 다른 속성이 걸릴 듯. e.g. 기본/비활성화/로딩
  - toggle switch
    - property 추가해서 boolean 선택 -> name 작성 e.g. 왼쪽 아이콘 -> 왼쪽 아이콘들 클릭한 뒤 appearance의 apply variable/property 클릭 -> 왼쪽 아이콘 컴포넌트에 추가 -> on/off 토글 완성 -> assets에서 컴포넌트 하나 불러와서 on/off 하면 반응형으로 만들었기 때문에 on/off에 따라 상자 크기도 저절로 따라감
  - create instance swap property
    - 요소 교체하고 싶을 때 select box를 통해 쉽게 바꾸기 위한 기능
    - property 추가해서 instance swap -> name 작성 e.g. 아이콘 종류 -> value(기본 아이콘, 변경 가능) 설정 -> 미리 교체하고 싶은 to-be 요소 component set로 assets에 등록 -> assets에 구분 쉽게 frame 명을 통해 이름 변경 -> 바꿀 아이콘들 컴포넌트에 추가 -> assets에서 컴포넌트 하나 불러와서 select box를 통해 교체 가능
    - 아이콘을 한번에 다 교체해줘야할 때도 있으므로 아이콘 미리 다 만들고 -> 버튼 만드는 거 추천
      - 아이콘 종류 별(마이페이지 아이콘)로 component set -> property 추가해서 등록 e.g. size 12,14,... -> property 추가 가능 e.g. style 선, 면...
      - property 정렬 바꾸고 싶으면(23,15,17 중 23을 가장 아래에 두고 싶을 때) -> properties에서 hover -> 필터 아이콘 -> 클릭 후 드래그해서 옵션 순서 변경
      - 무조건 아이콘 먼저 만들기 : 버튼 위에 먼저 아이콘 만들고 그걸 기반으로 아이콘 컴포넌트 만들면, 나중에 버튼에 있는 아이콘들은 assets이 안 걸려있는 거라 교체 대상이 안됨 -> assets에 컴포넌트화한 아이콘들로 다시 다 교체해준 뒤 다시 instance swap property... 여기부터 시작해야함.
        - 어휴,,, 아이콘 컴포넌트 목록에서 복사해서 버튼으로 끌어올 땐 일반 복붙이면 안됨(메인 컴포넌트=꽉 찬 다이아몬드로 불러와져서 얘는 버튼이라는 또 다른 메인 컴포넌트 안에 못 들어감) -> option 눌러서 복사본 만들면 인스턴스?(빈 다이아몬드)가 되어서 그제야 버튼에 들어올 수 있게 됨.
    - 우측 요소 drag해서 올리면 왼쪽아이콘 toggle 위에 선택지 추가됨.
    - expose properties item : 아이콘 사이즈와 스타일이 무엇인지까지 궁금하면 걸어주는 기능
    - 무수히 많은 버튼이 하나의 컴포넌트 세트로 묶여있음.

  2월 14일 (1h 54m)

2월 15일 (2h 1m) <남은 파트 : 2시간 45분~53분, 2시간 18분~2시간 33분>
<img width="1020" height="694" alt="스크린샷 2026-02-15 오후 10 02 43" src="https://github.com/user-attachments/assets/9a1b52ab-33b1-4a11-9598-b592eeb8ede6" />

<img width="617" height="291" alt="스크린샷 2026-02-15 오후 10 04 59" src="https://github.com/user-attachments/assets/6d089054-5c11-4f34-93fb-0eccf2985aa9" />


