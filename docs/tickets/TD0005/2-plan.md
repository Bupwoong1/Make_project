# TD0005: Implementation Plan

## Phase 1: 이미지 추출 및 준비
1. 스티커 시트 PDF에서 Trojan 마스코트 영역 크롭
2. PyMuPDF로 고해상도 렌더링 (8x zoom)
3. BFS flood-fill로 배경 제거 (투명화)
4. → 결과: 스티커 시트 버전은 "ACCOUNTING" 텍스트가 있어 전공별 한정적

## Phase 2: 라운드 스티커로 전환
1. `SoB_RoundSticker_0205-A.pdf`에서 전체 렌더링 (4x zoom, 400x400px)
2. "BUSINESS" 텍스트 → 8개 전공 공통 사용 가능
3. GitHub에 push하여 raw URL 확보

## Phase 3: 블루프린트 적용
1. 8개 라우트의 greeting 영역을 table 레이아웃으로 변환
2. 좌측: greeting + intro-text, 우측: 마스코트 이미지 (110px)
3. 인라인 스타일 적용 (이메일 클라이언트 호환성)
4. 프리뷰 HTML 재생성 및 렌더링 확인
