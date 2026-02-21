# TD0006: Test Features

## Test 1: CSS 클래스 변경
- **확인**: 8개 모듈에서 `.major-badge` 제거, `.major-banner` 적용
- **확인**: `.highlight-section` 배경색 `#E4EEF3` (라이트 블루)
- **결과**: PASS

## Test 2: 히어로 이미지 로드
- **확인**: 8개 모듈의 학과별 이미지가 브라우저에서 정상 표시
- **결과**: PASS (Accounting, BIS, Finance 스크린샷 확인)

## Test 3: CTA 링크 정상 동작
- **확인**: 8개 모듈의 Learn More 버튼이 실제 BBA 프로그램 페이지로 연결
- Accounting → /accounting/bba/
- Business Analytics → /bis/business-analytics/
- BIS → /bis/bba/
- Economics → /economics/
- Finance → /economics/finance/
- International Business → /internationalbusiness/
- Management → /management/
- Marketing → /marketing/marketing-major/
- **결과**: PASS (8/8)

## Test 4: 렌더링 확인
- **확인**: 마론 배너 + 블루 악센트 라인(#245D7A) + 라이트 블루 하이라이트가 연결된 형태로 표시
- **확인**: 배너(rounded top) + 하이라이트(rounded bottom) 연결 블록
- **결과**: PASS
