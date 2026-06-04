# TDD RED — 실패 테스트 먼저

MagicSquare_xxx Dual-Track TDD — **RED 단계만**. 프로덕션 구현·리팩터 금지.

참고: `.cursorrules`, `.cursor/skills/magic-square-tdd/reference.md` (D-* ID), `docs/PRD.md` §7.

---

## 필수 선언

응답 **첫 줄** (한국어 본문 전에):

```
Phase: red | Layer: <entity|control|boundary> | Track: <Logic|UI> | ID: <D-*|U-*>
```

예: `Phase: red | Layer: control | Track: Logic | ID: D-P0-01`

---

## 절차

1. **ID 확인** — `reference.md` 또는 사용자 지정 `D-*` / `U-*`에서 시나리오·기대값 확정.
2. **파일 위치**
   - Logic → `tests/entity/test_d_*.py` 또는 `tests/control/test_d_*.py`
   - UI → `tests/boundary/test_u_*.py`
3. **AAA 테스트 1개만** 작성
   - **Arrange:** 격자·입력 (4×4, 빈칸 0×2, 1~16 규칙 준수)
   - **Act:** 검증 대상 호출 (아직 없으면 import 대상 명시)
   - **Assert:** PRD/`reference.md` 기대값 **엄격** 비교
4. **MagicConstant** — `34`/`16` 리터럴 금지; constants SSOT import만 (모듈 없으면 테스트 상수 헬퍼에 TODO 주석 + RED 유지).
5. **pytest 실행** — 아래 예시. **FAIL 확인** (AssertionError / ImportError / ModuleNotFoundError).
6. **중단** — `src/` 미수정. FAIL이 의도와 맞으면 RED 완료 → **보고** 섹션 작성.

---

## pytest 예시 (bash)

프로젝트 루트에서 (`pip install -e ".[dev]"` 후):

```bash
# Logic — control 예시
pytest tests/control/test_d_p0_01_diagonal_fail.py -q

# Logic — entity 예시
pytest tests/entity/test_d_p0_02_complete.py -q

# UI — boundary 예시
pytest tests/boundary/test_u_e001_invalid_size.py -q
```

**RED 성공 조건:** 위 대상 테스트가 **실패**한다 (`1 failed` 또는 import 실패). `passed`면 assert가 약하거나 이미 구현됨 → 테스트 수정(완화 금지) 또는 ID 재확인.

---

## 보고

RED 종료 시 **한국어**로:

| 항목 | 내용 |
|------|------|
| 테스트 ID | `D-*` / `U-*` |
| FAIL 요약 | pytest 마지막 3~5줄 (실패 유형·assert 메시지) |
| 변경 파일 | **`tests/` 아래만** (경로 목록) |
| 다음 | GREEN 시 Layer·파일 힌트 (구현은 하지 않음) |

---

## 금지

- `src/` **수정·생성** (entity / control / boundary)
- Logic Track에서 **Domain Mock** (boundary·I/O Mock 포함)
- UI Track에서도 **도메인 로직을 Mock으로 대체**해 assert 통과시키기
- assert 완화 · `@pytest.mark.skip` · `xfail`
- RED 중 GREEN/REFACTOR 코드·리팩터
- 사용자 미요청 `git commit`
