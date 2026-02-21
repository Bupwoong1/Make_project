# TD0005: 이메일 템플릿에 Trojan 마스코트 이미지 추가

## Problem
8개 전공별 이메일 템플릿에 시각적 브랜드 요소가 부족함. UALR School of Business 스티커 시트에 있는 Trojan 마스코트 캐릭터를 이메일에 추가하여 브랜드 아이덴티티를 강화할 필요가 있음.

## Context
- 대상 파일: `ualr_email_automation/blueprints/UALR_Complete_All_8_Majors.blueprint.json` (8개 라우트 전체)
- 소스 이미지: `docs/3-reference/SoB_RoundSticker_0205-A.pdf` (라운드 스티커)
- 배치 위치: 인사말(greeting) 우측, table 레이아웃 사용
- 8개 전공 공통 사용 → "BUSINESS" 텍스트가 있는 라운드 스티커 선택

## Scope
- 라운드 스티커 PDF에서 PNG 추출
- GitHub에 업로드하여 raw URL 확보
- 8개 이메일 모듈에 table 레이아웃으로 마스코트 이미지 삽입
- 프리뷰 HTML 파일 재생성

## Out of Scope
- 이메일 콘텐츠 텍스트 변경 (TD0004에서 완료)
- 로고/헤더 변경 (TD0001/TD0003에서 완료)
