# TD0003: Definition

## Title
UALR 이메일 렌더링 검증 및 로고 가시성 수정

## Problem
8개 이메일 모듈을 브라우저에서 실제 렌더링한 결과, 다음 이슈 발견:

1. **로고 가시성 심각**: RGB 컬러 로고(어두운 색)가 마룬(#6e2639) 배경 위에 렌더링되어 거의 보이지 않음
   - UALR 공식 화이트 로고 PNG 없음 (ualr.edu/communications 확인 완료)
   - 기존 독립 템플릿(`Accounting_Email_Logo_Fixed.html`)에는 `filter: brightness(0) invert(1)` CSS가 있었으나, 블루프린트에는 미적용
2. **레이아웃/콘텐츠**: 전체적인 구조는 정상 (greeting, features, stats, CTA, footer)
3. **CTA 링크**: TD0002에서 수정 완료, "Learn More" 버튼 정상 작동

## Impact
- 이메일 수신자가 UALR 로고를 인식할 수 없음 — 브랜드 신뢰도 저하
- 헤더 영역이 빈 공간처럼 보여 비전문적 인상

## Scope
- 블루프린트 8개 모듈의 로고 `<img>` 태그에 CSS filter 추가
- 독립 HTML 템플릿 동기화
- 8개 모듈 전체 렌더링 스크린샷 검증
