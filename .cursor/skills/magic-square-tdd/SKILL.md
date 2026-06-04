---
name: magic-square-tdd
description: MagicSquare_xxx Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. MagicSquare_xx에서 entity/control/boundary 구현, test_d_*·test_u_* 작성, RED/GREEN/REFACTOR, ValidateAllLines·CanClaimComplete, E001~E007, MagicConstant SSOT 작업 시 사용.
---

# MagicSquare Dual-Track TDD

프로젝트 규칙 SSOT: `.cursorrules`, `docs/PRD.md`. D-* ID 목록: [reference.md](reference.md).

매 턴 **한국어**로 선언: **Phase** (RED|GREEN|REFACTOR) · **Layer** (entity|control|boundary) · **Track** (Logic|UI).

---

## 언제 이 Skill을 켜는지

| 상황 | Skill 적용 |
|------|------------|
| `src/entity`, `src/control`, `src/boundary` 코드·테스트 작성/수정 | ✅ |
| `test_d_*`, `test_u_*`, `D-*`, `U-*` ID 언급 | ✅ |
| RED/GREEN/REFACTOR, Dual-Track, ECB, MagicConstant | ✅ |
| `ValidateAllLines`, `CanClaimComplete`, 10라인·합 34 | ✅ |
| report/Prompring/README만 편집 | ❌ (Skill 불필요) |
| git commit/push (사용자 미요청) | ❌ |

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| Layer | entity, control | boundary |
| 테스트 ID | `D-*` | `U-*` |
| 파일명 | `test_d_*.py` | `test_u_*.py` |
| 디렉터리 | `tests/entity/`, `tests/control/` | `tests/boundary/` |
| Mock | **Domain Mock 금지** | control/entity·I/O **Mock 허용** |
| 목적 | Rule·Command·도메인 정확성 | E001~E007 매핑·입출력·표시 |
| pytest 범위 | `tests/entity` + `tests/control` | `tests/boundary` |

---

## ECB · Mock · E001~E007

### 의존 방향

```
boundary → control → entity
```

- **entity → \* import 금지** (stdlib·typing만).
- control은 entity만. boundary는 control(·entity 간접)만.

### Mock

| Layer | 허용 | 금지 |
|-------|------|------|
| entity/control 테스트 | 실제 객체·함수 | boundary Mock, Domain Mock, I/O Mock |
| boundary 테스트 | control/entity Mock, stdin/stdout Mock | — |

### 오류 코드 (boundary 전담)

| 코드 | 의미 | entity | control | boundary |
|------|------|--------|---------|----------|
| E001 | 격자 ≠ 4×4 | **처리 금지** | 검증·매핑 | ✅ 반환 |
| E002 | 빈칸(0) ≠ 2 | **처리 금지** | 검증·매핑 | ✅ 반환 |
| E003 | 값 범위 위반 | **처리 금지** | 검증·매핑 | ✅ 반환 |
| E004 | 0 아닌 값 중복 | **처리 금지** | 검증·매핑 | ✅ 반환 |
| E005 | 입·출력 형식 오류 | **처리 금지** | 검증·매핑 | ✅ 반환 |
| E006 | 풀이 불가(모순) | 도메인 결과만 | 오케스트레이션 | ✅ 반환 |
| E007 | 기타 UI/boundary | — | — | ✅ 반환 |

entity는 **순수 도메인**만. E001~E005를 entity에서 raise/반환하지 말 것.

### MagicConstant SSOT

- `34`, `16`, `4`, 빈칸 `2` → constants 모듈 한 곳.
- 테스트·구현에 리터럴 산재 **금지**.

---

## RED (5~7단계)

1. **선언:** Phase=RED, Layer, Track, 대상 `D-*` 또는 `U-*` ID.
2. **시나리오 확인:** PRD §7 또는 [reference.md](reference.md)에서 케이스·기대값 확정.
3. **테스트 1개만** 추가 (`test_d_*.py` / `test_u_*.py`). assert **엄격** (skip·xfail·assert 완화 금지).
4. **MagicConstant** import만 사용; Mock는 UI Track·boundary에서만.
5. **실행:** Logic → `pytest tests/<layer>/test_d_<name>.py -q` / UI → `pytest tests/boundary/test_u_<name>.py -q`
6. **확인:** 해당 테스트 **반드시 실패** (ImportError·AssertionError). 실패 메시지가 의도와 일치하는지 기록.
7. **중단:** 프로덕션 구현 코드 추가 **하지 않음**. RED 완료 보고.

---

## GREEN (5~7단계)

1. **선언:** Phase=GREEN, Layer, Track, RED에서 실패한 테스트 파일명.
2. **최소 구현:** 해당 Layer에만 코드 추가. ECB 위반 import 금지.
3. **entity면** E001~E005 처리 코드 **넣지 않음**. boundary면 E001~E007 매핑만.
4. **범위:** RED 1테스트 Green에 필요한 최소 diff만.
5. **실행:** `pytest tests/<layer>/test_d_<name>.py -q` (또는 `test_u_*`)
6. **확인:** 대상 테스트 **통과** + 기존 Logic/UI 테스트 **깨지지 않음**.
7. **중단:** 리팩터 **하지 않음**. GREEN 완료 보고.

---

## REFACTOR (5~7단계)

1. **선언:** Phase=REFACTOR, Layer, Track.
2. **기준선:** Logic → `pytest tests/entity tests/control -q` / UI → `pytest tests/boundary -q` — 전부 Green 확인.
3. **리팩터:** 동작 불변 — 이름·추출·중복 제거·ECB 정리만.
4. **금지:** assert 완화, skip/xfail, 테스트 삭제로 Green 만들기.
5. **SSOT 점검:** MagicConstant·의존 방향 재확인.
6. **실행:** 변경 Layer 범위 pytest → **Test/Review Loop** (아래) 전체.
7. **중단:** 전체 Green 유지 시 REFACTOR 완료 보고.

---

## Test / Review Loop (pytest 언제 무엇)

| 시점 | 명령 | 통과 조건 |
|------|------|-----------|
| RED 직후 | `pytest tests/<layer>/test_d_xxx.py -q` | **실패** (의도된 RED) |
| GREEN 직후 | 동일 파일 `-q` | **통과** |
| GREEN 안전망 | `pytest tests/entity tests/control -q` (Logic) | 전부 통과 |
| UI GREEN | `pytest tests/boundary/test_u_xxx.py -q` | 통과 |
| REFACTOR 후 | `pytest tests/entity tests/control -q` | Logic 전부 통과 |
| UI REFACTOR 후 | `pytest tests/boundary -q` | UI 전부 통과 |
| **Review Loop** (Phase 종료·PR 전) | `pytest -q` | **전 Track** 통과 |
| Harness만 (코드 없음) | `pytest -q` | `0 items` 허용 |

설치 전제: `pip install -e ".[dev]"` (프로젝트 루트).

---

## 완료 보고 항목

Phase 종료마다 아래를 **한국어**로 보고:

| # | 항목 |
|---|------|
| 1 | Phase / Layer / Track |
| 2 | 테스트 ID (`D-*` / `U-*`) 및 파일 경로 |
| 3 | 실행한 pytest 명령과 결과 (pass/fail/RED 확인) |
| 4 | 변경 파일 목록 (layer별) |
| 5 | ECB·Mock·E001 규칙 준수 여부 |
| 6 | MagicConstant SSOT 위반 여부 (리터럴 34/16 사용 없음) |
| 7 | 다음 Phase 제안 (RED→GREEN→REFACTOR 순) |

---

## 금지 사항 (전 Phase)

- assert 완화 · `@pytest.mark.skip` · `xfail`
- Logic Track에서 Mock
- entity에서 E001~E005 처리
- entity → control/boundary import
- `34`/`16` 리터럴 산재
- 사용자 요청 없는 git commit

---

## 추가 자료

- D-* 테스트 ID: [reference.md](reference.md)
- 도메인·Mom Test P0: `docs/PRD.md` §7, `.cursorrules`
