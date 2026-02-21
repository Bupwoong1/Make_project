# Claude Code Agent Teams 시스템 가이드

> 출처: Claude Opus 4.6 Agent Teams 영상 분석 및 공식 가이드 종합

---

## 1. 개요

Agent Teams는 Claude Code에서 여러 AI 에이전트가 **독립 인스턴스**로 동시 실행되며, 공유 Task 시스템을 통해 소통하고 협업하는 기능이다.

### 핵심 차이: Sub-agent vs Agent Team

| 항목 | Sub-agent (심부름꾼) | Agent Team (동료) |
|------|---------------------|-------------------|
| 인스턴스 | 호출자 컨텍스트 안에서 실행 | 각자 **독립 Claude 인스턴스** |
| 컨텍스트 윈도우 | 호출자와 공유 | 각자 **독립 컨텍스트 윈도우** |
| 소통 방식 | 결과만 반환 (단방향) | **직접 메시지** 교환 (양방향) |
| 작업 방식 | 단일 작업 → 보고 → 종료 | 공유 Task 리스트에서 자율적으로 작업 |
| 협업 | 불가 | 토론, 반박, 상호 검증 가능 |
| 비용 | 저렴 | 약 **7배** (일 $6 → $40~50) |
| 적합한 상황 | 단순 작업, 단일 파일, 버그 수정 | 복잡한 병렬 개발, 다단계 워크플로 |

### 비유

```mermaid
graph LR
    subgraph "❌ Sub-agent = 프리랜서 3명"
        direction TB
        User1["사용자"] --> F1["프리랜서 A"]
        User1 --> F2["프리랜서 B"]
        User1 --> F3["프리랜서 C"]
        F1 -.-> R1(("결과 A"))
        F2 -.-> R2(("결과 B"))
        F3 -.-> R3(("결과 C"))
    end

    subgraph "✅ Agent Team = 팀 협업"
        direction TB
        Lead2["Team Lead"] --> T1["팀원 A"]
        Lead2 --> T2["팀원 B"]
        Lead2 --> T3["팀원 C"]
        T1 <-. "소통" .-> T2
        T2 <-. "소통" .-> T3
        T3 -.-> Result(("통합 결과물"))
    end
```

---

## 2. 아키텍처

### 2.1 팀 구성

```mermaid
graph TD
    Lead["🎯 Team Lead<br/>(Opus)<br/>━━━━━━━━━━━━<br/>프로젝트 초기화<br/>Task 생성 및 배분<br/>워크플로 모니터링<br/>위험 작업 승인<br/>최종 완료 확인"]

    Lead --> M1["👤 Member 1<br/>(Sonnet)<br/>독립 인스턴스"]
    Lead --> M2["👤 Member 2<br/>(Sonnet)<br/>독립 인스턴스"]
    Lead --> M3["👤 Member 3<br/>(Sonnet)<br/>독립 인스턴스"]

    M1 -. "직접 메시지" .-> M2
    M2 -. "직접 메시지" .-> M3
    M1 -. "직접 메시지" .-> M3

    style Lead fill:#4f46e5,stroke:#312e81,color:#fff
    style M1 fill:#0891b2,stroke:#155e75,color:#fff
    style M2 fill:#0891b2,stroke:#155e75,color:#fff
    style M3 fill:#0891b2,stroke:#155e75,color:#fff
```

### 2.2 핵심 메커니즘

**1) 공유 Task 리스트**
- Team Lead가 `TaskCreate`로 각 멤버의 작업을 생성
- 멤버가 자율적으로 Task를 확인하고 수행
- `blockedBy` 의존성으로 실행 순서 제어

**2) 직접 메시지 (Peer Messaging)**
- 멤버끼리 직접 메시지를 보내 소통
- 토론, 반박, 상호 오류 수정 가능
- 예: QA 에이전트가 백엔드 에이전트에게 "이 테스트 실패함, 수정 필요" 전달

**3) 릴레이 실행 (Relay/Sequential)**
- `blockedBy`로 순서 강제
- 앞 작업이 완료되어야 다음 작업 시작
- 예: 분석가 완료 → 기획자 시작 → 소통 시작

**4) 병렬 실행 (Parallel)**
- 겹치지 않는 작업은 동시 실행
- 예: 프론트엔드와 백엔드 동시 개발

**5) 승인 게이트 (Approval Gates)**
- 위험/고영향 작업은 Team Lead 승인 필요
- Plan Mode Required 설정으로 강제
- 예: 인증 모듈 수정, 대규모 리팩터링

---

## 3. agent.md 파일 작성법

`agent.md`는 팀 전체를 정의하는 **단일 설계 문서**. "채용공고를 쓴다"고 생각하면 됨.

### 3.1 구조

```markdown
# 에이전트 1: [이름]

## 역할
- [구체적 업무 설명]

## 도구
- [사용할 라이브러리/기술]
- [파일 읽기/쓰기 권한]

## 규칙
- [출력 형식 규칙]
- [디자인 규칙 (상세)]
- **끝나면 다음 사람([에이전트 2 이름])한테 결과를 넘겨라** ← 필수!

---

# 에이전트 2: [이름]
...

# 에이전트 3: [이름]
...
```

### 3.2 필수 포함 요소

| 요소 | 설명 | 누락 시 결과 |
|------|------|-------------|
| 역할 정의 | 이 에이전트가 무엇을 하는지 | 작업 범위 불명확 |
| 도구/기술 명시 | 어떤 라이브러리/프레임워크 사용 | 기본 도구만 사용 |
| 디자인 규칙 | 출력물의 스타일/형식 상세 | 기본 테마, 낮은 퀄리티 |
| **핸드오프 규칙** | "끝나면 다음에게 넘겨라" | **프리랜서 모드** (각자 따로) |
| 파일 소유권 | 수정 가능 파일 범위 | 파일 충돌/덮어쓰기 |

### 3.3 예시: 데이터 분석 팀

```markdown
# 분석가 (Analyst)

## 역할
- CSV와 엑셀 데이터를 읽고 통계 분석을 돌린다
- 트렌드와 이상치, 핵심 지표를 잡아낸다

## 도구
- Python: pandas, matplotlib, seaborn, numpy
- 파일 읽기/쓰기 허용

## 차트 스타일 규칙
- 한글 폰트: 맑은 고딕 (Malgun Gothic)
- 배경: 다크 (#1a1a2e)
- 글씨: 화이트
- 메인 컬러: #0ea5e9, #22d3ee, #f59e0b
- 차트 종류: 선, 도넛, 막대
- 스파인(테두리): 전부 제거
- 막대: 둥근 모서리
- 글로우 효과 적용

## 일반 규칙
- 분석 완료 후 결과를 JSON으로 저장
- **끝나면 기획자(Strategist)에게 결과를 넘겨라**

---

# 기획자 (Strategist)

## 역할
- 분석가의 결과를 받아서 핵심 인사이트 3개를 정리한다

## 출력 형식 규칙
- 인사이트당 제목 + 설명 + 수치 근거
- insights.json으로 저장

## 일반 규칙
- **끝나면 소통 담당(Communicator)에게 결과를 넘겨라**

---

# 소통 담당 (Communicator)

## 역할
- python-pptx로 PPT 슬라이드 5장을 만든다
- 보고서 이메일 초안을 작성한다

## PPT 디자인 규칙
- 카드 UI 레이아웃
- 강조 라인 (accent line)
- 원형 배지 (circular badge)
- 배경: 다크 (#1a1a2e)
- 폰트: 맑은 고딕
- 차트 이미지: 분석가가 생성한 파일 사용

## 이메일 규칙
- 제목: "[기간] [주제] 보고"
- 본문: 핵심 수치 3개 + 인사이트 요약
```

---

## 4. 핵심 규칙 6개

### 규칙 1: 1 에이전트 = 1 역할 (One Agent, One Role)

**가장 중요한 규칙.** 하나의 에이전트에 여러 역할을 주면 결과물이 엉망이 된다.

```mermaid
graph TD
    subgraph "❌ 나쁜 예: 1 에이전트 = 2 역할"
        BAD["분석가"]
        BAD -->|"CSV 분석"| R1["📊 분석 결과"]
        BAD -->|"PPT 생성"| R2["📄 PPT"]
        R1 -.-> MESS["💥 결과 엉망"]
        R2 -.-> MESS
    end

    subgraph "✅ 좋은 예: 1 에이전트 = 1 역할"
        AN2["📊 분석가<br/>CSV 분석만"] -->|핸드오프| CM2["📨 소통 담당<br/>PPT만"]
        AN2 --> GOOD1["고품질 분석"]
        CM2 --> GOOD2["고품질 PPT"]
    end

    style MESS fill:#dc2626,stroke:#991b1b,color:#fff
    style GOOD1 fill:#059669,stroke:#065f46,color:#fff
    style GOOD2 fill:#059669,stroke:#065f46,color:#fff
```

### 규칙 2: 명시적 핸드오프 (Explicit Handoff)

각 에이전트에게 "끝나면 다음 사람한테 넘겨라"를 반드시 명시해야 한다. 이게 없으면 프리랜서 3명이 따로 일하는 것과 같다.

```mermaid
graph LR
    AN["📊 분석가"] -->|"끝나면 넘겨라"| ST["💡 기획자"]
    ST -->|"끝나면 넘겨라"| CM["📨 소통 담당"]
    CM -->|"끝나면 보고하라"| TL["🎯 Team Lead"]

    style AN fill:#0891b2,stroke:#155e75,color:#fff
    style ST fill:#0891b2,stroke:#155e75,color:#fff
    style CM fill:#0891b2,stroke:#155e75,color:#fff
    style TL fill:#4f46e5,stroke:#312e81,color:#fff
```

### 규칙 3: 파일 소유권 경계 (File Ownership)

두 에이전트가 같은 파일을 동시에 수정하면 충돌이 발생한다. 각 에이전트의 파일 영역을 명확히 구분해야 한다.

```mermaid
graph TD
    subgraph "🖥️ 프론트엔드 에이전트 영역"
        F1["src/components/"]
        F2["src/pages/"]
    end

    subgraph "⚙️ 백엔드 에이전트 영역"
        B1["src/api/"]
        B2["src/db/"]
    end

    subgraph "🧪 QA 에이전트 영역"
        Q1["tests/"]
    end

    F1 ~~~ B1
    B1 ~~~ Q1

    style F1 fill:#0891b2,stroke:#155e75,color:#fff
    style F2 fill:#0891b2,stroke:#155e75,color:#fff
    style B1 fill:#7c3aed,stroke:#4c1d95,color:#fff
    style B2 fill:#7c3aed,stroke:#4c1d95,color:#fff
    style Q1 fill:#d97706,stroke:#92400e,color:#fff
```

### 규칙 4: 상세한 디자인 규칙 (Design Rules)

에이전트에게 출력물의 시각적 규칙을 상세하게 정의해야 한다. 정의하지 않으면 기본 테마로 나오며 퀄리티가 크게 떨어진다.

정의해야 할 항목:
- 폰트 (한글 깨짐 방지)
- 배경색/글씨색/메인 컬러
- 차트 종류 (선, 도넛, 막대)
- UI 요소 (카드 UI, 강조 라인, 원형 배지)
- 제거할 요소 (스파인, 기본 테두리)
- 추가 효과 (글로우, 둥근 막대)

### 규칙 5: Team Lead는 실행하지 않는다 (Delegation Mode)

Team Lead가 직접 코드를 쓰거나 작업을 실행하면 병목이 생긨다. `Shift+Tab`으로 위임 모드를 활성화하여 Lead가 조정(coordination)만 하도록 강제한다.

```mermaid
graph TD
    TL["🎯 Team Lead<br/>(Shift+Tab 위임 모드)"]

    subgraph "✅ 해야 할 것"
        DO1["📖 설계 문서 읽기"]
        DO2["📋 Task 생성 및 배분"]
        DO3["👁️ 진행 상황 모니터링"]
        DO4["🔒 위험 작업 승인/거부"]
        DO5["🏁 최종 완료 확인"]
    end

    subgraph "❌ 하면 안 되는 것"
        NO1["💻 직접 코드 작성"]
        NO2["📝 직접 파일 수정"]
        NO3["📊 직접 분석 수행"]
    end

    TL --> DO1
    TL --> DO2
    TL --> DO3
    TL --> DO4
    TL --> DO5

    TL -.-x NO1
    TL -.-x NO2
    TL -.-x NO3

    style TL fill:#4f46e5,stroke:#312e81,color:#fff
    style NO1 fill:#dc2626,stroke:#991b1b,color:#fff
    style NO2 fill:#dc2626,stroke:#991b1b,color:#fff
    style NO3 fill:#dc2626,stroke:#991b1b,color:#fff
    style DO1 fill:#059669,stroke:#065f46,color:#fff
    style DO2 fill:#059669,stroke:#065f46,color:#fff
    style DO3 fill:#059669,stroke:#065f46,color:#fff
    style DO4 fill:#059669,stroke:#065f46,color:#fff
    style DO5 fill:#059669,stroke:#065f46,color:#fff
```

### 규칙 6: 모델 혼합으로 비용 절감 (Model Mixing)

| 역할 | 모델 | 이유 |
|------|------|------|
| Team Lead | **Opus** | 복잡한 조정, 계획, 승인 판단 필요 |
| Team Members | **Sonnet** | 실행 작업, input 토큰 비용 절감 |

일일 비용 비교:
- 전원 Opus: ~$40~50/일
- Lead=Opus + 멤버=Sonnet: 비용 대폭 절감
- 단일 AI: ~$6/일

---

## 5. 워크플로 패턴

### 5.1 릴레이 (Sequential) — 데이터 분석/보고

```mermaid
sequenceDiagram
    participant TL as 🎯 Team Lead (Opus)
    participant AN as 📊 분석가 (Sonnet)
    participant ST as 💡 기획자 (Sonnet)
    participant CM as 📨 소통 담당 (Sonnet)

    TL->>AN: TaskCreate: CSV 분석 + 차트 생성
    activate AN
    Note right of AN: CSV 읽기<br/>통계 분석<br/>차트 생성<br/>analysis.json 저장
    AN-->>TL: Task 완료 보고
    deactivate AN

    TL->>ST: blockedBy 해제 → 인사이트 추출
    activate ST
    Note right of ST: analysis.json 읽기<br/>인사이트 3개 추출<br/>insights.json 저장
    ST-->>TL: Task 완료 보고
    deactivate ST

    TL->>CM: blockedBy 해제 → PPT + 이메일
    activate CM
    Note right of CM: insights.json + 차트<br/>PPT 5장 생성<br/>이메일 초안 작성
    CM-->>TL: Task 완료 보고
    deactivate CM

    Note over TL: 전체 파이프라인 완료 → 셧다운
```

소요 시간: **약 5분** (사람이 하면 1시간+)

### 5.2 병렬 (Parallel) — 풀스택 개발

```mermaid
graph TD
    TL["🎯 Team Lead<br/>(Opus)"] -->|TaskCreate| FE["🖥️ 프론트엔드<br/>React + Tailwind"]
    TL -->|TaskCreate| BE["⚙️ 백엔드<br/>Express + SQLite"]
    TL -->|TaskCreate<br/>blockedBy: FE, BE| QA["🧪 QA<br/>Jest + Playwright"]

    FE -->|"UI 완성"| DONE_FE["✅ 프론트엔드 완료"]
    BE -->|"API 완성"| DONE_BE["✅ 백엔드 완료"]

    DONE_FE -->|blockedBy 해제| QA
    DONE_BE -->|blockedBy 해제| QA

    QA -->|"테스트 실패"| FIX["🔄 개발자에게<br/>직접 메시지"]
    QA -->|"전체 통과"| FINAL["✅ Task 완료 보고"]
    FIX -.->|수정 후 재실행| QA
    FINAL --> TL_DONE["🎯 Team Lead<br/>전체 완료 → 셧다운"]

    style TL fill:#4f46e5,stroke:#312e81,color:#fff
    style FE fill:#0891b2,stroke:#155e75,color:#fff
    style BE fill:#0891b2,stroke:#155e75,color:#fff
    style QA fill:#d97706,stroke:#92400e,color:#fff
    style TL_DONE fill:#059669,stroke:#065f46,color:#fff
```

소요 시간: **수 분** (사람 팀이면 반나절)

---

## 6. 실전 적용 시나리오

### 6.1 데이터 분석 + PPT + 이메일 (릴레이)

| 단계 | 에이전트 | 입력 | 출력 |
|------|----------|------|------|
| 1 | 분석가 | sales.csv | 차트 이미지들, analysis.json |
| 2 | 기획자 | analysis.json | insights.json (인사이트 3개) |
| 3 | 소통 | insights.json + 차트 | PPT 5장 (.pptx), 이메일 초안 (.md) |

### 6.2 풀스택 앱 개발 (병렬)

| 에이전트 | 기술 스택 | 담당 파일 |
|----------|----------|----------|
| 프론트엔드 | React, Tailwind | src/components/, src/pages/ |
| 백엔드 | Express, SQLite | src/api/, src/db/ |
| QA | Jest, Playwright | tests/ |

### 6.3 적합/부적합 판단

| 적합한 경우 | 부적합한 경우 |
|------------|-------------|
| 병렬 개발 가능한 풀스택 앱 | 단일 파일 수정 |
| 반복 리포트 자동화 (주간/월간) | 단순 버그 수정 |
| 복잡한 디버깅 (다중 가설 검증) | 순차적 단순 작업 |
| 대규모 코드 리뷰/리팩터링 | 간단한 코드 리뷰 |
| 동시 리서치 (여러 주제) | 단일 질문 답변 |

---

## 7. 품질 관리 (Quality Control)

### 7.1 자동화 훅 (Quality Gates)

이벤트 트리거로 자동 테스트를 실행한다:

```mermaid
graph LR
    DEV["🖥️ 코딩 에이전트<br/>작업 완료"] -->|"teammate_idle<br/>이벤트 발생"| HOOK["⚡ Hook 트리거"]
    HOOK -->|자동 실행| QA["🧪 QA 테스트<br/>Jest / Playwright"]
    QA -->|"test_complete"| REPORT["📋 결과 보고"]
    REPORT -->|전체 통과| PASS["✅ 다음 단계"]
    REPORT -->|실패 발견| FIX["🔄 개발자에게<br/>수정 요청"]

    style HOOK fill:#f59e0b,stroke:#92400e,color:#000
```

코딩 에이전트가 작업을 마치면 수동 개입 없이 즉시 테스트가 돌아간다.

### 7.2 Plan Approval (계획 승인)

위험한 작업 전 계획서를 제출하고 승인을 받아야 한다:

```mermaid
graph TD
    DETECT["🚨 멤버가 위험 작업 감지<br/>(리팩터링, 인증 수정 등)"]
    DETECT --> PLAN["📝 계획서(Plan) 작성"]
    PLAN --> SUBMIT["📤 Team Lead에게 제출"]
    SUBMIT --> REVIEW{"🎯 Team Lead 검토"}
    REVIEW -->|"승인 ✅"| EXEC["▶️ 작업 실행"]
    REVIEW -->|"거부 ❌"| REVISE["🔄 계획 수정 후 재제출"]
    REVISE --> SUBMIT

    style REVIEW fill:#4f46e5,stroke:#312e81,color:#fff
    style EXEC fill:#059669,stroke:#065f46,color:#fff
    style DETECT fill:#dc2626,stroke:#991b1b,color:#fff
```

### 7.3 80/20 규칙

```mermaid
pie title 작업 분배
    "AI 자동화 (80%)" : 80
    "사람 검토 (20%)" : 20
```

| AI가 처리 (80%) | 사람이 처리 (20%) |
|-----------------|------------------|
| 데이터 분석 | 폰트 미세 조정 |
| 차트 생성 | 레이아웃 미세 수정 |
| PPT 코딩 | 최종 검토 |
| 이메일 초안 | 발송 |

---

## 8. 비용 관리

### 일일 비용 비교

| 구성 | 예상 비용 |
|------|----------|
| 단일 Claude 사용 | ~$6/일 |
| Agent Team (전원 Opus) | ~$40~50/일 |
| Agent Team (Lead=Opus, 멤버=Sonnet) | 대폭 절감 |

### 비용 절감 전략

1. **모델 혼합**: Lead만 Opus, 나머지 Sonnet
2. **팀 사용 판단**: 단순 작업에는 단일 AI 사용
3. **스킬/플러그인**: 반복 패턴을 커스터마이징하여 토큰 절약

---

## 9. Gartner 전망

- 멀티 에이전트 시스템 관련 문의: 전년 대비 **1,445% 증가**
- 2026년 말까지 전체 엔터프라이즈 앱의 **40%**가 AI 에이전트를 포함할 것으로 예측

### AI 에이전트 진화 타임라인

```mermaid
timeline
    title AI 에이전트 진화
    2024 : AI가 코드를 제안
         : 사람이 검토/수정
    2025 : AI가 파일을 생성/실행
         : 단독 작업
    2026 : AI가 팀을 구성
         : 독립적으로 협업
         : Gartner - 40% 앱에 AI 에이전트 포함
```

### 인간의 역할 변화

```mermaid
graph LR
    subgraph "2024: Coder"
        C1["👨‍💻 사람이 직접 코딩"]
        C2["📝 사람이 직접 보고서 작성"]
        C3["🔧 사람이 직접 실행"]
    end

    subgraph "2026: Tech Lead"
        T1["🏗️ AI 팀 구조 설계"]
        T2["❓ 올바른 질문과 규칙 설정"]
        T3["✅ 결과 검증 + 20% 다듬기"]
    end

    C1 -->|"역할 전환"| T1
    C2 -->|"역할 전환"| T2
    C3 -->|"역할 전환"| T3

    style C1 fill:#dc2626,stroke:#991b1b,color:#fff
    style C2 fill:#dc2626,stroke:#991b1b,color:#fff
    style C3 fill:#dc2626,stroke:#991b1b,color:#fff
    style T1 fill:#059669,stroke:#065f46,color:#fff
    style T2 fill:#059669,stroke:#065f46,color:#fff
    style T3 fill:#059669,stroke:#065f46,color:#fff
```
