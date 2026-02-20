# Make.com 설정 지침서

## 🎯 당신의 시스템 정보

### ✅ 준비 완료:
- **Google Sheets ID**: `1csRNhuvDQqLPoYcmEAAUgoez_vSf3nLGnILTb8af4f8`
- **ML API URL**: `https://ten-bats-glow.loca.lt`
- **Blueprint 파일**: `ML_Customer_Purchase_Prediction_READY.blueprint.json`

---

## 📝 Make.com 설정 단계

### 1단계: Blueprint 가져오기

1. Make.com 로그인: https://www.make.com
2. "시나리오" → "새 시나리오 만들기"
3. 왼쪽 하단 "..." 메뉴 → "Blueprint 가져오기"
4. `ML_Customer_Purchase_Prediction_READY.blueprint.json` 파일 선택

### 2단계: 모듈별 설정

#### 모듈 1: Google Sheets (Watch Rows) - 트리거
- **연결**: Google 계정 연결
- **스프레드시트 ID**: 이미 설정됨 (1csRNhuvDQqLPoYcmEAAUgoez_vSf3nLGnILTb8af4f8)
- **시트 이름**: Sheet1
- **설정 완료**: ✅

#### 모듈 2: HTTP (Send Request) - ML API 호출
- **URL**: 이미 설정됨 (https://ten-bats-glow.loca.lt/predict)
- **메서드**: POST
- **헤더**: Content-Type: application/json
- **본문**: 자동 매핑됨
- **설정 완료**: ✅

#### 모듈 3: JSON Parse
- **JSON 문자열**: {{2.data}}
- **자동 설정됨**
- **설정 완료**: ✅

#### 모듈 4: Router (분기)
- **자동 설정됨**
- 두 개의 경로로 분기:
  - 경로 1: send_now (즉시 발송)
  - 경로 2: send_soon (예약 발송)
- **설정 완료**: ✅

#### 모듈 5: Email (High Priority) - 즉시 발송
- **연결**: 이메일 계정 연결 필요 ⚠️
- **받는 사람**: {{3.customer_email}}
- **제목**: 이미 설정됨
- **본문**: HTML 템플릿 이미 설정됨
- **조건**: email_timing = "send_now"

**이메일 계정 연결 방법:**
1. 모듈 클릭
2. "Connection" 필드 클릭
3. Gmail 또는 SMTP 선택
4. 계정 인증

#### 모듈 6: Google Sheets (Update Row) - 발송 기록
- **연결**: 모듈 1과 동일한 Google 계정
- **스프레드시트 ID**: 이미 설정됨
- **행 번호**: {{1.__ROW_NUMBER__}}
- **업데이트 데이터**: 자동 매핑됨
- **설정 완료**: ✅

#### 모듈 7: Email (Medium Priority) - 예약 발송
- **모듈 5와 동일하게 설정**
- **조건**: email_timing = "send_soon"

#### 모듈 8: Google Sheets (Update Row) - 예약 기록
- **모듈 6과 동일하게 설정**

---

## 🧪 3단계: 테스트 실행

### 시나리오 테스트:

1. **"한 번 실행" 클릭**
2. Google Sheets에서 첫 번째 데이터 행(C001) 확인
3. 실행 흐름 관찰:
   - Google Sheets에서 데이터 읽기 ✅
   - ML API 호출 ✅
   - JSON 파싱 ✅
   - 조건 분기 ✅
   - 이메일 발송 ✅
   - Sheets 업데이트 ✅

### 예상 결과:

1. **이메일 수신**: 자신의 이메일함 확인
2. **Google Sheets 업데이트**: K-N 열에 데이터 표시
   - K열: 이메일 발송 날짜/시간
   - L열: 예측된 다음 구매일
   - M열: "Email Sent" 또는 "Email Scheduled"
   - N열: 신뢰도 점수 (0.0~1.0)

---

## ⚡ 4단계: 시나리오 활성화

테스트가 성공하면:

1. **스케줄 설정**:
   - 시계 아이콘 클릭
   - 실행 주기 선택:
     - 매 15분마다
     - 매 시간마다
     - 하루에 한 번
     - 등등...

2. **시나리오 켜기**:
   - 오른쪽 상단 토글 스위치를 "ON"

3. **모니터링**:
   - "기록" 탭에서 실행 이력 확인
   - 오류 발생 시 로그 확인

---

## 🔧 문제 해결

### 문제 1: Google Sheets 연결 오류
**해결책**:
- Google 계정 재인증
- 스프레드시트 공유 설정 확인
- 시트 이름이 "Sheet1"인지 확인

### 문제 2: HTTP 요청 실패
**해결책**:
- ML API가 실행 중인지 확인: http://127.0.0.1:8080/health
- localtunnel이 활성화되어 있는지 확인
- URL이 올바른지 확인: https://ten-bats-glow.loca.lt

### 문제 3: 이메일 발송 실패
**해결책**:
- 이메일 계정 연결 재인증
- Gmail인 경우 "보안 수준이 낮은 앱 액세스" 허용
- SMTP 설정 확인

### 문제 4: JSON 파싱 오류
**해결책**:
- ML API 응답 형식 확인
- 로그에서 실제 응답 데이터 확인
- ML API 직접 테스트: curl로 호출

---

## 📊 시스템 상태 확인

실행 전 체크리스트:

- [ ] ML API 실행 중 (http://127.0.0.1:8080)
- [ ] localtunnel 활성화 (https://ten-bats-glow.loca.lt)
- [ ] Google Sheets 데이터 입력 완료
- [ ] Make.com Blueprint 가져오기 완료
- [ ] 모든 연결 설정 완료
- [ ] 테스트 실행 성공

---

## 🎉 성공!

모든 설정이 완료되면:
1. 시스템이 자동으로 고객 데이터를 모니터링
2. ML 모델이 구매 시점 예측
3. 자동으로 맞춤형 이메일 발송
4. Google Sheets에 결과 기록

---

## 💡 팁

### 비용 절감:
- 무료 버전은 월 1000회 작업 제한
- 테스트 시에는 수동 실행 ("한 번 실행") 사용
- 스케줄은 필요한 만큼만 설정

### 이메일 템플릿 커스터마이징:
- 모듈 5, 7에서 HTML 수정 가능
- 회사 로고 추가 가능
- 제품 이미지 포함 가능

### 추가 기능:
- Slack 알림 추가
- SMS 발송 추가
- CRM 업데이트 추가
- Google Analytics 이벤트 추적

---

## 📞 지원

문제가 발생하면:
1. SETUP_GUIDE_KR.md 문제 해결 섹션 참조
2. Make.com 로그 확인
3. ML API 로그 확인
4. 각 구성 요소 개별 테스트

---

*생성일: 2025-10-27*
*ML 고객 구매 예측 시스템 v1.0*
