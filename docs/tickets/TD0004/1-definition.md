# TD0004: UALR 이메일 콘텐츠 정확성 검증 및 개선

## 배경
- 대학 설명회에서 미정 전공 신입생들이 QR 코드 → Google Form 작성 후 받는 personalized email
- 관심 전공 선택 시 해당 전공 이메일 자동 발송
- 이메일 내용의 정확성, 언어 적절성, 하이라이트 정보 재검토 필요

## 문제
8개 전공 이메일의 학과 페이지 대조 결과 **다수의 부정확/outdated 정보** 발견:

### 공통 이슈 (8개 전공 전체)
1. **#32 US Ranking** — 2023년 "Best Online Undergraduate Business Programs" 랭킹이지만 전공별 랭킹처럼 표시
2. **$200K+ Scholarships** — School of Business 전체 합산이지 전공별 아님
3. **$3,500 Per Semester** — Bursar 공식 등록금 ~$5,093과 불일치 (4개 전공에서 사용)

### 전공별 Critical 이슈
| 전공 | 이슈 | 심각도 |
|------|------|--------|
| Accounting | "All professors are CPAs" 과장 | Medium |
| Business Analytics | 급여/성장률 outdated, #10 랭킹이 더 강력 | Medium |
| BIS | 377,500 jobs → 317,700으로 감소, 급여 outdated | Medium |
| Economics | "Data Science" → "Data Analytics"가 정확 | Low |
| **Finance** | **100% online 미제공 (critical)**, 전공명 틀림, 경쟁대회명 부정확 | **High** |
| International Business | 필수 해외연수 미언급 (강점) | Low |
| **Management** | **4 specializations → 실제 3개**, "International" 없음 | **High** |
| Marketing | "AI-powered marketing" 근거 약함, "Sales mastery" 미사용 용어 | Medium |

### 누락된 강점 정보
- 50% 등록금 장학금 (Half-Off Scholarship) — 전 신입생 대상
- Trojan Guarantee — Pell 수혜자 등록금 무료
- 87% 학생 재정지원 수혜
- Finance: $510K 학생 운용 투자 포트폴리오
- Business Analytics: STEM 지정, #10 전국 랭킹
- Economics: LSAT 평균 157.4 (인기 전공 중 1위)
- International Business: 필수 해외 field study

## 범위
- 8개 이메일 모듈 콘텐츠 수정 (블루프린트 JSON)
- 언어 톤 조정 (신입생 대상 친근하고 정확한 표현)
- 부정확한 통계/정보 업데이트
- 누락된 강점 정보 추가
