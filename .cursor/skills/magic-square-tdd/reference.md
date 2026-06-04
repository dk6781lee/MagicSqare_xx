# D-* Logic Track 테스트 ID

| ID | 우선 | 시나리오 | 기대 |
|----|------|----------|------|
| D-P0-01 | P0 | 슬라이드 예시, 행·열만 34, **D0 또는 D1 실패** | `CanClaimComplete=false`, 실패 라인 ID |
| D-P0-02 | P0 | 10라인 모두 34, 1~16 중복 없음, 빈칸 2 | `CanClaimComplete=true` |
| D-P0-03 | P0 | `ValidateAllLines` — 10라인 개별 통과/실패 | 실패 라인 목록 |
| D-P0-04 | P0 | `ValidateLine(grid, lineId)` 단일 라인 | 해당 라인만 판정 |
| D-P1-01 | P1 | 빈칸(0) 개수 ≠ 2 | `INVALID` (control; boundary E002) |
| D-P1-02 | P1 | 1~16 밖 값 또는 중복 | `INVALID` (control; boundary E003/E004) |
| D-P1-03 | P1 | 격자 크기 ≠ 4×4 | `INVALID` (control; boundary E001) |
| D-P2-01 | P2 | Q2 인지 순간 재현 (TBD) | TBD |

파일명 예: `tests/control/test_d_p0_01_diagonal_fail.py`
