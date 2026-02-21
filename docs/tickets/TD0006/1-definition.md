# TD0006: 이메일 디자인 개선 - 배너/사진/컬러/링크

## Problem
1. **major-badge**: pill 모양이 CTA 버튼과 혼동됨. 클릭 불가능한데 버튼처럼 보임
2. **하이라이트 색상**: 골드(#ffe579)가 아닌 UALR 브랜드 블루(#245D7A) 계열로 변경 필요
3. **학생 사진 없음**: UALR 웹사이트에는 각 학과별 학생 사진이 있으나 이메일에 없음
4. **CTA 링크 오류**: Learn More 버튼이 콘텐츠 없는 스텁 페이지로 연결됨

## Context
- UALR 웹사이트(ualr.edu/bis/bba/ 등)에서 사용하는 디자인 패턴 참조:
  - 마론 배너 (학과명) + 블루 악센트 라인 (#245D7A)
  - 학생 히어로 사진
- 브랜드 블루: `#245D7A` (rgb(36, 93, 122)) - 웹사이트 breadcrumb 바 등에 사용

## Scope

### 1. Badge → 풀 너비 마론 배너
- pill 모양 제거, 전체 너비 마론 바로 변경
- 하단에 블루 악센트 라인 (#245D7A, 3px)
- 하이라이트 섹션과 연결된 형태 (top rounded + bottom rounded)

### 2. 하이라이트 섹션 컬러 변경
- 골드 (#ffe579) → 라이트 블루 (#E4EEF3, #245D7A 기반)

### 3. 학과별 학생 사진 추가
- 각 학과 BBA 페이지에서 히어로 이미지 사용 (외부 URL 직접 참조)
- 인사말 아래, 배너 위에 배치

### 4. CTA 링크 수정
현재 스텁 페이지 → 실제 BBA 프로그램 페이지로 변경:

| 전공 | 현재 (스텁) | 변경 (BBA 프로그램) |
|------|------------|-------------------|
| Accounting | /business/department/accounting/ | /accounting/bba/ |
| Business Analytics | /bis/business-analytics/ | /bis/business-analytics/ (동일) |
| BIS | /business/department/business-information-systems/ | /bis/bba/ |
| Economics | /business/department/economics/ | /economics/ |
| Finance | /business/department/finance/ | /economics/finance/ |
| International Business | /business/department/international-business/ | /internationalbusiness/ |
| Management | /business/department/management/ | /management/ |
| Marketing | /business/department/marketing-and-advertising/ | /marketing/marketing-major/ |

## Out of Scope
- 이메일 콘텐츠 텍스트 변경 (TD0004 완료)
- 로고/헤더 변경 (TD0001/TD0003 완료)
- 마스코트 이미지 변경 (TD0005 완료)
