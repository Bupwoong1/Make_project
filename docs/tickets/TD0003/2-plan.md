# TD0003: Plan

## Approach
CSS `filter: brightness(0) invert(1)`을 로고 `<img>` 태그 inline style에 추가하여 RGB 로고를 화이트로 변환

## 기술 근거
- `brightness(0)`: 이미지를 완전 검정으로
- `invert(1)`: 검정을 화이트로 반전
- 결과: 어떤 색상의 로고든 순백색으로 표시됨
- 이미 `Accounting_Email_Logo_Fixed.html` 독립 템플릿에서 검증된 방법

## Before (현재)
```html
<img src="...ua-little-rock-v-rgb.png" alt="UA Little Rock Logo"
     style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;">
```

## After (수정)
```html
<img src="...ua-little-rock-v-rgb.png" alt="UA Little Rock Logo"
     style="max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block; filter: brightness(0) invert(1);">
```

## Steps
1. Python 스크립트로 블루프린트 8개 모듈의 `<img>` inline style에 `filter` 추가
2. JSON 유효성 검증
3. 프리뷰 HTML 재생성 → 브라우저 렌더링 스크린샷 8개 확인
4. 독립 HTML 템플릿 동기화
5. 테스트 결과 업데이트 및 커밋
