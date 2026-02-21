# TD0005: Technical Specification

## 이미지 Asset

| 항목 | 값 |
|------|-----|
| 소스 | `docs/3-reference/SoB_RoundSticker_0205-A.pdf` |
| 출력 | `ualr_email_automation/assets/trojan_round_sticker.png` |
| 크기 | 400x400px |
| 렌더링 | PyMuPDF 4x zoom |
| GitHub URL | `https://raw.githubusercontent.com/Bupwoong1/Make_project/master/ualr_email_automation/assets/trojan_round_sticker.png` |

## HTML 변경 패턴 (8개 모듈 공통)

### Before
```html
<div class="greeting">Welcome, {{1.`1`}}!</div>
<p class="intro-text">Thank you for your interest in the <strong>UA Little Rock School of Business</strong>...</p>
```

### After
```html
<table style="width:100%; border-collapse:collapse; margin-bottom:10px;">
<tr>
<td style="vertical-align:top;">
  <div class="greeting">Welcome, {{1.`1`}}!</div>
  <p class="intro-text">Thank you for your interest in the <strong>UA Little Rock School of Business</strong>...</p>
</td>
<td style="width:120px; vertical-align:top; text-align:right; padding-top:5px;">
  <img src="https://raw.githubusercontent.com/Bupwoong1/Make_project/master/ualr_email_automation/assets/trojan_round_sticker.png" alt="UALR Trojan Mascot" style="width:110px; height:auto;">
</td>
</tr>
</table>
```

## 적용 대상 (8개 라우트)

| Route | 전공 |
|-------|------|
| 0 | Accounting |
| 1 | Business Analytics |
| 2 | Business Information Systems |
| 3 | Economics |
| 4 | Finance |
| 5 | International Business |
| 6 | Management |
| 7 | Marketing |
