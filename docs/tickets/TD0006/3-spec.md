# TD0006: Technical Specification

## CSS Changes

### Before
```css
.major-badge { background: #6e2639; color: #ffffff; padding: 4px 14px; border-radius: 12px; display: inline-block; font-size: 11px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 10px; }
.highlight-section { background: #ffe579; padding: 25px; border-radius: 8px; margin: 20px 0; }
```

### After
```css
.major-banner { background: #6e2639; color: #ffffff; padding: 12px 25px; font-size: 15px; font-weight: 600; letter-spacing: 0.5px; border-radius: 8px 8px 0 0; margin: 20px 0 0 0; border-bottom: 3px solid #245D7A; }
.highlight-section { background: #E4EEF3; padding: 25px; border-radius: 0 0 8px 8px; margin: 0 0 20px 0; }
```

## HTML Structure Change (per module)

### Before
```html
</td></tr></table>
        <div class="highlight-section">
            <div class="major-badge">Finance</div>
            <h3>Why Choose Finance at UALR?</h3>
            ...
```

### After
```html
</td></tr></table>
        <img src="HERO_IMAGE_URL" alt="UALR Finance Students" style="width:100%; height:auto; border-radius:8px; margin:15px 0 0 0;">
        <div class="major-banner">Finance</div>
        <div class="highlight-section">
            <h3>Why Choose Finance at UALR?</h3>
            ...
```

## CTA Link Changes

| Route | Old URL | New URL |
|-------|---------|---------|
| 0 | /business/department/accounting/ | /accounting/bba/ |
| 1 | /bis/business-analytics/ | /bis/business-analytics/ |
| 2 | /business/department/business-information-systems/ | /bis/bba/ |
| 3 | /business/department/economics/ | /economics/ |
| 4 | /business/department/finance/ | /economics/finance/ |
| 5 | /business/department/international-business/ | /internationalbusiness/ |
| 6 | /business/department/management/ | /management/ |
| 7 | /business/department/marketing-and-advertising/ | /marketing/marketing-major/ |

## Color Reference
- UALR Brand Blue: `#245D7A` (rgb 36, 93, 122)
- Light Blue BG: `#E4EEF3` (derived from #245D7A at ~12% on white)
- Maroon: `#6e2639` (unchanged)
