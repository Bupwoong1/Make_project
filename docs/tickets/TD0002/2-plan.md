# TD0002: Plan

## Approach
모든 CTA 링크를 UALR 웹사이트의 최종 리다이렉트 대상 URL로 직접 교체

## URL Mapping

| # | Major | Current (Old) URL | New (Final) URL | Status |
|---|-------|-------------------|-----------------|--------|
| 1 | Accounting | `ualr.edu/business/academics/accounting/` | `ualr.edu/business/department/accounting/` | Redirect |
| 2 | Business Analytics | `ualr.edu/business/academics/business-analytics/` | `ualr.edu/bis/business-analytics/` | **404 Broken** |
| 3 | Business Info Systems | `ualr.edu/business/academics/business-information-systems/` | `ualr.edu/business/department/business-information-systems/` | Redirect |
| 4 | Economics | `ualr.edu/business/academics/economics/` | `ualr.edu/business/department/economics/` | Redirect |
| 5 | Finance | `ualr.edu/business/academics/finance/` | `ualr.edu/business/department/finance/` | Redirect |
| 6 | International Business | `ualr.edu/business/academics/international-business/` | `ualr.edu/business/department/international-business/` | Redirect |
| 7 | Management | `ualr.edu/business/academics/management/` | `ualr.edu/business/department/management/` | Redirect |
| 8 | Marketing | `ualr.edu/business/academics/marketing/` | `ualr.edu/business/department/marketing-and-advertising/` | Redirect (slug changed) |

## Steps
1. 블루프린트 백업 (TD0001에서 생성한 BACKUP 활용)
2. Python 스크립트로 8개 URL 일괄 교체
3. JSON 유효성 검증
4. HTTP 접근성 재검증 (8개 전부 200, 리다이렉트 없음)
5. 독립 HTML 템플릿 동기화 (해당 URL 포함 시)
6. 테스트 결과 업데이트 및 커밋
