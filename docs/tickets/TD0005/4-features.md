# TD0005: Test Features

## Test 1: 이미지 Asset 존재
- **확인**: `ualr_email_automation/assets/trojan_round_sticker.png` 파일 존재
- **결과**: PASS

## Test 2: GitHub URL 접근 가능
- **확인**: `https://raw.githubusercontent.com/Bupwoong1/Make_project/master/ualr_email_automation/assets/trojan_round_sticker.png` 접근 가능
- **결과**: PASS (commit `cafb857`)

## Test 3: 8개 모듈 모두 적용
- **확인**: 블루프린트 JSON 내 8개 라우트 모두 `trojan_round_sticker.png` URL 포함
- **결과**: PASS (8/8 모듈)

## Test 4: 렌더링 확인
- **확인**: 프리뷰 HTML에서 마스코트가 인사말 우측에 110px로 정상 표시
- **결과**: PASS (Accounting, Finance 스크린샷 확인)
