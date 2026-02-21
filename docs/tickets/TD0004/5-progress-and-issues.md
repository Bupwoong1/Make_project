# TD0004: Progress and Issues

## Session 1 — Research & Ticket Created

### 조사 방법
- 8개 전공 이메일 콘텐츠 전체 추출
- 각 학과 페이지 (8개 URL) 방문하여 정보 대조
- BLS, U.S. News, AACSB 등 외부 소스 교차 검증

### 발견 사항 요약

**Critical (즉시 수정)**
1. Finance "100% Online Option" — 현재 온라인 미제공
2. Management "4 Specializations" — 실제 3개 (International 없음)

**Major (정확성 문제)**
3. Accounting "All professors are CPAs" — 개별 검증 불가
4. Business Analytics 급여/성장률 — BLS 데이터 outdated
5. BIS 연간 일자리 수 — 377,500 → 317,700
6. #32 랭킹 — 2023년 온라인 비즈니스 프로그램 랭킹이나 전공별처럼 표시
7. $3,500 등록금 — Bursar 공식 ~$5,093과 불일치

**Enhancement (누락 정보 추가)**
8. Half-Off Scholarship (50% 등록금 할인) 전혀 언급 없음
9. Business Analytics #10 전국 랭킹 미활용
10. Finance $510K 학생 운용 펀드 미언급
11. Economics LSAT 157.4점 데이터 미활용
12. International Business 필수 해외연수 미언급
13. Marketing Center for Professional Selling 미언급

---

## Session 2 — Implementation Complete

### 변경 사항

**공통 (8개 전체)**
- © 2025 → © 2026
- #32 US Ranked → AACSB Top 5% Worldwide (6개) 또는 STEM Designated (BA, BIS)
- $3,500 Per Semester → 50% OFF Freshman Tuition (5개 전공)

**전공별 수정**

| 전공 | 변경 항목 |
|------|----------|
| Accounting | Faculty CPA 표현 완화, CPA exam 문구 수정 |
| Business Analytics | BLS 성장률 33%, 급여 $64K-$194K, #10 랭킹, STEM |
| BIS | 317,700 jobs, $52K-$166K 급여, Capstone 강조, STEM |
| Economics | LSAT 157.4 구체 데이터, Data Science→Data Analytics |
| Finance | emphasis 정확 명칭, 대회 정확 명칭, 100% Online 제거→$510K Fund |
| Intl Business | Study Abroad 필수 해외연수 추가 |
| Management | 3 Emphases (International 제거), 표현 학과 페이지 일치 |
| Marketing | Selling Center 추가, AI-Powered Marketing 유지 |

### 최종 상태
- **4/4 tests passing**
- Test 1: JSON 유효성 ✅
- Test 2: 부정확 정보 제거 ✅ (5개 critical claim 모두 제거)
- Test 3: 업데이트된 통계 ✅ (#10, 317K+, $510K, 3 Emphases, AACSB x6, STEM x2)
- Test 4: 렌더링 ✅ (8개 전체 스크린샷 확인)
