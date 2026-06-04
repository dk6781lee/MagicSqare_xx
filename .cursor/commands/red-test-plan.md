# RED Test Plan — 설계표만 (코드 생성 없음)

MagicSquare_xxx Dual-Track TDD — **RED 설계·플랜만**. `tests/`·`src/` **파일 생성 금지**.

참고: `.cursorrules`, `docs/PRD.md`, `.cursor/skills/magic-square-tdd/reference.md`.

---

## 필수 선언

응답 **첫 줄**:

```
Phase: red | Layer: <entity|control|boundary> | Track: <Logic|UI> | ID: <D-*|U-*>
```

사용자가 **Track·묶음·ID**를 주면 그에 맞춰 아래 4섹션을 **표로** 작성한다.

---

## 출력 형식 (Logic — Track B)

### 1. C2C 추적 (Rule 1~3 = PRD R1~R3)

- **PRD FR-*** 인용 시도 → `docs/PRD.md`에 없으면 **「미기재」** 명시 후 R1~R3 역매핑
- **To-Do 1개** (판단 포함 — 반환 타입·좌표 index 등)
- **Test ID → Given / When / Then** 표
- G1 등 격자는 **ASCII 블록**으로 명시 (1-index 좌표 주석)

### 2. Track B (D-*) RED 설계표

| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
|---------|-----------|------------|-----------|----------------------|

- 이번 **묶음** ID 강조; 동일 Track B 2·3번 ID는 「다음 파일」로 표시 가능

### 3. 테스트 플랜

| 항목 | 내용 |
|------|------|
| 파일 | `tests/<layer>/test_d_*.py` |
| test 함수명 후보 | 2~3개 |
| conftest 픽스처 | G1 등 — **로직 없음**, `entity.constants` import |
| pytest 명령 | `python -m pytest … -v` |
| RED 묶음 범위 | 이번 1~3 ID |

### 4. ECB · Mock 점검

- Logic Track → Domain Mock **금지**
- entity → E001~E005 **emit 금지**

**마무리 한 줄:** `/red-skeleton`으로 넘길 준비됐습니다.

---

## 출력 형식 (UI — Track A)

Layer만 **boundary**, Track **UI**, 묶음 **U-***.

### Track A 표

| Test ID | Given | Then (기대값) | Expected RED Failure |
|---------|-------|---------------|----------------------|

- E001~E007 boundary 책임 · Mock **허용**
- 테스트 플랜·ECB 요약 (짧게)

---

## 사용자 입력 예시

```
Phase: red | Layer: entity | Track: Logic
이번 RED 묶음: D-LOC-01 (FR-LOC-01)
```

```
Phase: red | Layer: boundary | Track: UI
이번 RED 묶음: U-IN-01, U-IN-02
```

---

## 금지

- `tests/` · `src/` **파일 생성·수정**
- GREEN / REFACTOR 구현
- skip · xfail · assert 완화 제안
- 사용자 미요청 `git commit`

---

## 다음 Command

설계 확정 후 → **`/red-skeleton`** (테스트 스켈레톤만 `tests/`)
