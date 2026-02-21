# TD0003: Spec

## Blueprint JSON Escaped Format

### Before
```
style=\\"max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block;\\"
```

### After
```
style=\\"max-width: 200px; height: auto; margin: 0 auto 10px auto; display: block; filter: brightness(0) invert(1);\\"
```

## CSS in Blueprint `<style>` Block

### Before
```
.header img { max-width: 200px; height: auto; display: block; margin: 0 auto 10px auto; }
```

### After
```
.header img { max-width: 200px; height: auto; display: block; margin: 0 auto 10px auto; filter: brightness(0) invert(1); }
```

## Rendering Verification Checklist
- [ ] 로고가 화이트로 선명하게 표시되는가
- [ ] "SCHOOL OF BUSINESS" 서브타이틀 가시성
- [ ] CTA "Learn More" 버튼 정상 렌더링
- [ ] Footer 링크 정상 표시
- [ ] 전체 레이아웃 깨짐 없음
