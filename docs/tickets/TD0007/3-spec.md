# TD0007: Technical Specification

## 그래픽 오버레이 기술 사양

### 이미지 합성 (Python PIL)
- **입력**: 8개 학과 히어로 사진 (UALR 웹사이트 원본, ~1200px)
- **출력**: 600px 너비 합성 이미지 (이메일 최적), PNG 또는 JPEG
- **오버레이 요소**: 브랜드 가이드 Transparencies/Wedges 스타일
- **저장 위치**: `ualr_email_automation/assets/hero_*.jpg`

### 오버레이 디자인 옵션

#### Option A: 삼각형 오버레이 (사용자 예시 참조)
- 좌상단에 반투명 삼각형 (민트/틸 또는 브랜드 블루)
- 하단에 얇은 컬러 바 (#245D7A)
- 브랜드 가이드 p.28 "Transparencies" 참조

#### Option B: 대각선 Wedge
- 사진 한쪽에 대각선 마론 오버레이 (반투명)
- 브랜드 가이드 p.29 "Wedges & Angles" 참조

#### Option C: 쉐브론 코너
- 사진 코너에 마론 쉐브론(>>) 그래픽
- 브랜드 가이드 p.28 "Shapes" 참조

## AACSB 로고

### 소스
- URL: `https://ualr.edu/business/wp-content/uploads/sites/163/2025/01/aacsb-logo1-e1737491880842.png`
- 대안: AACSB 공식 로고 에셋

### 배치 옵션
- A: stats 섹션 아래, divider 위
- B: footer 바로 위
- C: stats 섹션 내 AACSB 칸에 로고로 교체

## 히어로 이미지 소스 (8개)

| 전공 | 원본 URL |
|------|---------|
| Accounting | ualr.edu/accounting/.../business-student-portrait-2-2023.jpg |
| Business Analytics | ualr.edu/bis/.../biz-portrait-2022_03.jpg |
| BIS | ualr.edu/bis/.../biz-portrait-2022_03.jpg |
| Economics | ualr.edu/economics/.../ASBTDC-setups-2021_12.jpg |
| Finance | ualr.edu/economics/.../business-team-winners1.jpg |
| International Business | ualr.edu/internationalbusiness/.../business-student-portrait-2-2023.jpg |
| Management | ualr.edu/management/.../business-student-portrait-2023.jpg |
| Marketing | ualr.edu/marketing/.../business-student-portrait-2-2023.jpg |
