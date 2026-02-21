# TD0001: Progress and Issues

## Session 1 — Ticket Created

### 조사 결과
- 블루프린트 8개 이메일 모듈 전부 텍스트 로고(`<div class="logo">UA LITTLE ROCK</div>`) 사용 중
- `<img>` 태그 없음 — 로고 이미지가 전혀 렌더링 안 됨
- 로고 URL (`https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png`) 접근 가능 확인 (PNG 바이너리 반환)
- `LOGO_IMPLEMENTATION_GUIDE.md`에 3가지 구현 방법 이미 문서화됨 (Direct URL, 자체 서버, Base64)
- 독립 템플릿 파일(`Accounting_Email_Logo_Fixed.html`)도 CSS에 `header img` 있지만 HTML body에 `<img>` 없음

### 상태
- 0/4 tests passing
- 티켓 문서 완성: 1-definition, 2-plan, 3-spec, 4-features

### 다음 작업
- 블루프린트 백업 → 8개 모듈 header 교체 → JSON 검증 → 템플릿 동기화
