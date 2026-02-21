# TD0001: 구현 계획

## 접근 방식

LOGO_IMPLEMENTATION_GUIDE.md의 **Method 1 (Direct URL)** 적용. UALR 공식 로고 URL이 접근 가능함을 확인했으므로 가장 빠른 방식 사용.

## 구현 단계

### Step 1: 블루프린트 백업
- 원본 블루프린트 복사본 생성

### Step 2: 8개 이메일 모듈의 header HTML 교체
- 블루프린트 JSON에서 각 모듈의 `mapper.html` 필드 검색
- 텍스트 로고를 이미지 로고로 교체:

**찾을 패턴:**
```html
<div class=\"logo\">UA LITTLE ROCK</div>
```

**교체할 내용:**
```html
<img src=\"https://ualr.edu/communications/wp-content/uploads/sites/216/2011/03/ua-little-rock-v-rgb.png\" alt=\"UA Little Rock Logo\" style=\"max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;\">
```

### Step 3: CSS 정리
- `.logo` 클래스 CSS가 있다면 `.header img` CSS로 교체/추가

### Step 4: JSON 문법 검증
```bash
python -m json.tool < UALR_Complete_All_8_Majors.blueprint.json > /dev/null
```

### Step 5: 독립 HTML 템플릿 파일도 동기화
- `ualr_email_automation/templates/` 내 관련 HTML 파일도 동일하게 업데이트

## 위험 요소

| 위험 | 확률 | 대응 |
|------|------|------|
| UALR 서버가 외부 이메일에서 이미지 차단 | 중 | Base64 대안 준비 |
| JSON 이스케이프 문자 오류 | 중 | python -m json.tool로 검증 |
| Gmail이 외부 이미지 차단 | 낮 | https:// 프로토콜 사용 |
