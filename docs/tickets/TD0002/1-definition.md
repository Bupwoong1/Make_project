# TD0002: Definition

## Title
UALR 블루프린트 이메일 전공별 CTA 링크 검증 및 수정

## Problem
블루프린트 8개 이메일 모듈의 "Learn More" CTA 버튼이 UALR 웹사이트의 구 URL 패턴(`/academics/`)을 사용하고 있어:
1. **Business Analytics**: 404 에러 (완전히 깨진 링크)
2. **나머지 7개 전공**: `/academics/` → `/department/`로 리다이렉트 발생 (작동하지만 비효율적)
3. **Marketing**: URL 슬러그 자체가 변경됨 (`/marketing/` → `/marketing-and-advertising/`)

## Impact
- Business Analytics 전공 관심 학생이 이메일 CTA 클릭 시 404 페이지 도달
- 나머지 7개 전공은 불필요한 리다이렉트 경유 (UX 지연, 이메일 클릭 추적 정확도 저하)

## Scope
- 블루프린트 8개 이메일 모듈의 CTA href URL 수정
- 독립 HTML 템플릿 파일의 해당 URL도 동기화
