# TD0005: Progress & Issues

## Timeline

1. **스티커 시트 추출 시도**
   - `SOB_StickerSheet_0206-A.pdf` 에서 Trojan 캐릭터 크롭
   - PyMuPDF 8x zoom, BFS flood-fill 배경 제거
   - 문제: 첫 크롭에서 plume 잘림 → clip 영역 확장하여 해결
   - 문제: "ACCOUNTING" 텍스트가 책에 있어 전공별 한정적

2. **라운드 스티커로 전환**
   - `SoB_RoundSticker_0205-A.pdf` 발견 (사용자 제공)
   - "BUSINESS" 텍스트 → 8개 전공 공통 사용 가능
   - 4x zoom으로 400x400px 렌더링
   - GitHub push: commit `cafb857`

3. **블루프린트 적용**
   - 8개 라우트 모두 table 레이아웃으로 변환
   - 기존 투명 마스코트 URL → 라운드 스티커 URL로 교체
   - 프리뷰 HTML 8개 파일 재생성

## Issues Resolved

| Issue | Resolution |
|-------|-----------|
| Plume 잘림 | clip Rect 확장 (y: 230→200, height +30px) |
| "ACCOUNTING" 전공 한정 | 라운드 스티커("BUSINESS")로 교체 |
| 이메일 클라이언트 호환성 | div 대신 table 레이아웃 사용 |

## Status: Done (4/4)
