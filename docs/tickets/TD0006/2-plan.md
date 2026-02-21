# TD0006: Implementation Plan

## Phase 1: CSS 변경
1. `.major-badge` → `.major-banner` 클래스로 변경 (8개 모듈)
   - 풀 너비 마론 바, 하단 블루 악센트 (3px #245D7A)
   - `border-radius: 8px 8px 0 0` (상단만 둥글게)
2. `.highlight-section` 배경색 변경
   - `#ffe579` → `#E4EEF3`
   - `border-radius: 0 0 8px 8px` (하단만 둥글게, 배너와 연결)
   - `margin: 0 0 20px 0` (배너와 간격 없이)

## Phase 2: HTML 구조 변경 (8개 모듈)
1. 기존 `<div class="major-badge">` 제거
2. 학과별 히어로 이미지 `<img>` 태그 추가 (greeting table 아래)
3. `<div class="major-banner">` 추가 (이미지 아래)
4. highlight-section은 배너 바로 아래에 연결

## Phase 3: CTA 링크 수정 (8개 모듈)
1. 각 전공별 `href` 값을 실제 BBA 프로그램 페이지 URL로 교체

## Phase 4: 검증
1. 프리뷰 HTML 재생성
2. 브라우저에서 렌더링 확인
3. 히어로 이미지 로드 확인
4. CTA 링크 정상 동작 확인

## 히어로 이미지 소스

| 전공 | 이미지 URL |
|------|-----------|
| Accounting | ualr.edu/accounting/.../business-student-portrait-2-2023.jpg |
| Business Analytics | ualr.edu/bis/.../biz-portrait-2022_03.jpg |
| BIS | ualr.edu/bis/.../biz-portrait-2022_03.jpg |
| Economics | ualr.edu/economics/.../ASBTDC-setups-2021_12.jpg |
| Finance | ualr.edu/economics/.../business-team-winners1.jpg |
| International Business | ualr.edu/internationalbusiness/.../business-student-portrait-2-2023.jpg |
| Management | ualr.edu/management/.../business-student-portrait-2023.jpg |
| Marketing | ualr.edu/marketing/.../business-student-portrait-2-2023.jpg |
