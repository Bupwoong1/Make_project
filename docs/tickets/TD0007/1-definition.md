# TD0007: 브랜드 그래픽 요소 적용 + AACSB 로고 추가

## Problem
1. 이메일의 학생 사진이 그냥 사각형 이미지로만 존재 - UALR 브랜드 아이덴티티 부재
2. AACSB 인증 로고가 텍스트로만 언급되고 실제 로고 이미지가 없음

## Reference
- **브랜드 가이드 p.28**: Shapes, Transparencies - 반투명 기하학적 오버레이
- **브랜드 가이드 p.29**: Wedges & Angles - 대각선 컬러 바
- **브랜드 가이드 p.30-31**: Graphic Elements in Use - 실제 마케팅 자료 적용 예시
- **사용자 예시 스크린샷**: 사진 좌상단 민트/틸 삼각형 오버레이 + 하단 틸 바

## Scope

### 1. 히어로 사진에 브랜드 그래픽 오버레이
- 브랜드 가이드의 Transparencies/Wedges 스타일 적용
- 사진 위에 기하학적 요소 합성 (삼각형, 대각선 등)
- HTML 이메일 제약 → Python(PIL)으로 이미지에 직접 합성하여 PNG로 생성
- 합성 이미지를 GitHub에 호스팅

### 2. AACSB 로고 이미지 추가
- 현재 stats 섹션에 "AACSB / Top 5% Worldwide" 텍스트만 존재
- 실제 AACSB 인증 로고 이미지 추가
- 소스: `https://ualr.edu/business/wp-content/uploads/sites/163/2025/01/aacsb-logo1-e1737491880842.png`

## Constraints
- HTML 이메일에서 CSS position/clip-path/transform 사용 불가
- 모든 그래픽 요소는 이미지로 사전 합성 필요
- 이미지 파일 크기 최적화 (이메일 로딩 속도)

## Out of Scope
- 이메일 텍스트 콘텐츠 변경
- 레이아웃 구조 변경 (TD0006에서 완료)
