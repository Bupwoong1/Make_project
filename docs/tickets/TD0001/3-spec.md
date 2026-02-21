# TD0001: 기술 사양

## 변경 대상

### 1차: 블루프린트 JSON
- **파일**: `ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json`
- **위치**: 8개 이메일 모듈 → `mapper.html` 필드 → `<div class="header">` 섹션

### 2차: 독립 HTML 템플릿
- `ualr_email_automation/templates/Accounting_Email_Logo_Fixed.html`
- `ualr_email_automation/templates/Accounting_Email_With_Logo.html`
- `ualr_email_automation/templates/email_template_ualr.html`
- `ualr_email_automation/templates/UALR_Concise_Email_Template_Example.html`

## 변경 사양

### Header HTML (Before)
```html
<div class="header" style="background: #6e2639; padding: 25px; text-align: center;">
    <div class="logo" style="font-size: 26px; font-weight: 700; color: #ffffff; letter-spacing: 1px;">UA LITTLE ROCK</div>
    <div class="logo-subtitle" style="color: #ffbf00; font-size: 13px; margin-top: 5px; letter-spacing: 1.5px;">SCHOOL OF BUSINESS</div>
</div>
```

### Header HTML (After)
```html
<div class="header" style="background: #6e2639; padding: 25px; text-align: center;">
    <img src="https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png"
         alt="UA Little Rock Logo"
         style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
    <div class="logo-subtitle" style="color: #ffbf00; font-size: 13px; margin-top: 5px; letter-spacing: 1.5px; font-weight: 600;">SCHOOL OF BUSINESS</div>
</div>
```

### JSON 이스케이프 형식 (블루프린트 내부)
```
<img src=\\\"https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png\\\" alt=\\\"UA Little Rock Logo\\\" style=\\\"max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;\\\">
```

## 검증 기준

1. `python -m json.tool < file.json > /dev/null` 성공 (JSON 문법 유효)
2. 8개 모듈 전부 `<img src=` 포함 확인
3. 8개 모듈 전부 `<div class="logo">` 미포함 확인 (텍스트 로고 제거됨)
4. 로고 URL이 https:// 프로토콜 사용
