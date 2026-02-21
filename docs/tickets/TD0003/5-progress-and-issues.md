# TD0003: Progress and Issues

## Session 1 — Ticket Created

### 조사 결과
- 블루프린트에서 8개 이메일 HTML 추출 → `_preview/` 폴더에 렌더링 가능 파일 생성
- 브라우저 스크린샷 촬영 — 로고 RGB 컬러가 마룬 배경에서 거의 안 보임
- UALR 공식 화이트 로고 PNG 미존재 확인
- 해결책으로 CSS `filter: brightness(0) invert(1)` 계획

---

## Session 2 — Implementation Complete

### 변경 사항 (최초 계획 대비 확장)

사용자 피드백으로 **3가지 주요 변경** 수행:

1. **Unit Mark 적용** (계획 변경)
   - 일반 로고 + CSS filter 대신, 공식 School of Business Unit Mark 사용
   - PDF(`SOB_StickerSheet_0206-A.pdf`)에서 PyMuPDF로 벡터 렌더링 → PNG 추출
   - `ualr_email_automation/assets/sob_unit_mark.png` (738x390px)
   - GitHub public repo에 push → raw URL로 이메일에서 접근 가능
   - URL: `https://raw.githubusercontent.com/Bupwoong1/Make_project/master/ualr_email_automation/assets/sob_unit_mark.png`

2. **배경색 통일** (사용자 피드백)
   - 기존 `#6e2639` → Unit Mark 배경색 `#6b0733`으로 통일
   - 이미지와 헤더 배경 이음새 없이 일체감 표현
   - 8개 모듈 전체 accent color도 동시 교체 (96건)

3. **텍스트 서브타이틀 제거**
   - `<div class="logo-subtitle">SCHOOL OF BUSINESS</div>` 삭제 (Unit Mark에 포함)

### GitHub 레포
- `Bupwoong1/Make_project` → public으로 변경 (이미지 URL 접근용)

### 최종 상태
- **4/4 tests passing**
- Test 1: JSON 유효성 ✅
- Test 2: Unit Mark 8/8 ✅
- Test 3: 로고 선명 + 배경 일치 ✅ (8개 스크린샷 확인)
- Test 4: 레이아웃 정상 ✅
