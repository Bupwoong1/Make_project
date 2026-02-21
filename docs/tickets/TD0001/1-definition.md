# TD0001: UALR 블루프린트 이메일 로고 이미지 적용

## 문제

UALR 이메일 마케팅 Make.com 블루프린트(`UALR_Complete_All_8_Majors.blueprint.json`)의 8개 이메일 모듈에서 UALR 로고가 **텍스트**로만 표시되고, 실제 로고 **이미지**가 나오지 않음.

### 현재 상태 (8개 모듈 전부 동일)

```html
<div class="header">
    <div class="logo">UA LITTLE ROCK</div>
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
```

- `<img>` 태그 없음 — 로고 이미지가 전혀 렌더링되지 않음
- 텍스트 "UA LITTLE ROCK"만 표시됨

### 원하는 상태

```html
<div class="header">
    <img src="[로고 URL]" alt="UA Little Rock Logo"
         style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
    <div class="logo-subtitle">SCHOOL OF BUSINESS</div>
</div>
```

## 영향 범위

- 파일: `ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json`
- 모듈: 8개 이메일 (Accounting, Business Analytics, BIS, Economics, Finance, International Business, Management, Marketing)
- 각 모듈의 `mapper.html` 필드 내 header 섹션

## 참고 문서

- `docs/3-reference/LOGO_IMPLEMENTATION_GUIDE.md` — 3가지 구현 방법 상세 (Direct URL, 자체 서버, Base64)
- 로고 URL: `https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png` (접근 확인됨)

## 제약 조건

- 블루프린트 JSON을 직접 수정해야 함 (Make.com UI 접근 불가 시)
- 모듈 ID 변경 금지
- JSON 문법 검증 필수 (`python -m json.tool`)
- 8개 모듈 모두 동일하게 적용
