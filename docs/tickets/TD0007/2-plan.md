# TD0007: Implementation Plan

## Phase 1: 그래픽 오버레이 디자인 결정
1. 브랜드 가이드 그래픽 요소 분석 (완료)
2. 이메일에 적합한 패턴 선택:
   - Option A: 좌상단 삼각형 오버레이 (사용자 예시 스크린샷 스타일)
   - Option B: 대각선 마론 바 + 틸 악센트 (Wedges & Angles 스타일)
   - Option C: 코너 쉐브론(>>) 장식 (Shapes 스타일)
3. 브랜드 컬러 선택 (마론 #6e2639 반투명, 블루 #245D7A, 민트 등)

## Phase 2: 히어로 이미지 합성
1. 8개 학과별 히어로 사진 다운로드
2. Python PIL로 그래픽 오버레이 합성
   - 일관된 크기로 리사이즈 (600px 너비, 이메일 최적)
   - 선택한 그래픽 요소 오버레이
3. 합성 이미지 `ualr_email_automation/assets/` 에 저장
4. GitHub push → raw URL 확보

## Phase 3: AACSB 로고 추가
1. AACSB 로고 이미지 확보/다운로드
2. 이메일 내 적절한 위치에 배치 (footer 위 또는 stats 섹션 근처)
3. 8개 모듈에 적용

## Phase 4: 블루프린트 업데이트
1. 히어로 이미지 URL을 합성 이미지 URL로 교체
2. AACSB 로고 HTML 추가
3. 프리뷰 재생성 및 렌더링 확인
