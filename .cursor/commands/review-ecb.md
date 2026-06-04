# Review ECB — 계약·아키텍처 리뷰

MagicSquare_xxx — **코드 수정 금지**. ECB·도메인 계약 위반만 **표로** 리뷰한다.

참고: `.cursorrules`, `docs/PRD.md`, `.cursor/skills/magic-square-tdd/SKILL.md`.

---

## 필수 선언

응답 **첫 줄**:

```
Phase: review | Scope: <경로 또는 diff 범위> | Mode: read-only
```

예: `Phase: review | Scope: src/control, tests/control | Mode: read-only`

---

## 절차

1. **범위 확정** — 사용자가 지정한 파일·디렉터리·최근 diff만 읽는다.
2. **체크 5항** — 아래 기준표대로 파일별 스캔 (import, entity 오류, 출력 계약, 상수, Mock).
3. **위반만 표 작성** — 위반 없으면 「위반 없음」 한 줄 + 체크 통과 표.
4. **수정 제안 금지** — 코드 패치·리팩터·파일 생성 **하지 않음**. 위반 설명만.
5. **한국어**로 요약 (표 + 1~2문장 결론).

---

## 체크 기준

| # | 항목 | 통과 조건 | 위반 예 |
|---|------|-----------|---------|
| 1 | **import 방향** | boundary→control→entity 단방향; entity는 stdlib·typing만 | entity가 control/boundary import; control이 boundary import |
| 2 | **entity E001~E005** | entity에 입력·형식·범위 오류 처리 없음 | entity에서 E001~E005 raise/반환/분기 |
| 3 | **int[6] 1-index** | 정상 출력 `[r1,c1,n1,r2,c2,n2]`, 행·열 **1~4** | 0-index 좌표, 길이≠6, 순서 오류 |
| 4 | **MagicConstant SSOT** | `34`/`16`/`4`/빈칸`2`는 constants SSOT import | src·tests에 `34`/`16` 리터럴 산재 |
| 5 | **Logic Track Domain Mock** | `tests/entity`, `tests/control`에서 Mock·patch·Fake 없음 | `unittest.mock`, boundary I/O Mock on Logic |

---

## 위반 보고 표 (템플릿)

위반이 **있을 때**만 행 추가. 없으면 표 대신 「체크 5항 위반 없음」.

| # | 체크 | 파일:줄 | 위반 내용 | 계약/규칙 |
|---|------|---------|-----------|-----------|
| 1 | import 방향 | `src/entity/foo.py:3` | `from control import ...` | ECB § entity→* 금지 |
| 2 | entity E001~E005 | … | … | `.cursorrules` § 오류 |
| 3 | int[6] 1-index | … | … | 출력 계약 |
| 4 | MagicConstant SSOT | … | … | 리터럴 34/16 |
| 5 | Logic Domain Mock | … | … | Dual-Track Logic |

---

## 체크 통과 요약 표 (위반 없을 때)

| # | 항목 | 결과 |
|---|------|------|
| 1 | import 방향 | ✅ |
| 2 | entity E001~E005 | ✅ |
| 3 | int[6] 1-index | ✅ |
| 4 | MagicConstant SSOT | ✅ |
| 5 | Logic Track Domain Mock | ✅ |

---

## 스캔 힌트 (읽기 전용)

```bash
# import 방향 (수동 확인용 — 실행만, 수정 없음)
rg "^from (entity|control|boundary)" src/ tests/
rg "^import (entity|control|boundary)" src/entity/

# E001~E005 in entity
rg "E00[1-5]" src/entity/

# MagicConstant 리터럴 (SSOT 파일 제외하고 검토)
rg "\b(34|16)\b" src/ tests/

# Logic Track Mock
rg "mock|Mock|patch|MagicMock" tests/entity/ tests/control/
```

코드가 아직 없으면 「범위 내 소스 없음 — Harness만 존재」로 보고.

---

## 금지

- **코드·테스트·설정 수정** (제안 diff 포함)
- pytest 실행으로 Green/Red 유도
- 위반 외 스타일·성능·네이밍 잡담 (본 Command 범위 밖)
- 사용자 미요청 `git commit`

---

## 보고 마무리

| 항목 | 내용 |
|------|------|
| Scope | 검토한 경로 |
| 위반 건수 | N건 (0이면 통과 표) |
| 결론 | 한 문장 (예: 「control 1건 import 위반, 나머지 통과」) |
