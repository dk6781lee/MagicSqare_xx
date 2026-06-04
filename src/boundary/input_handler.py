from control.grid_input import validate_grid_input


def handle_grid_input(grid: list[list[int]] | None) -> dict[str, str | None]:
    """격자 입력 처리 — 오류 시 E00x·detail 반환."""
    ok, code, detail = validate_grid_input(grid)
    if ok:
        return {"ok": True, "error_code": None, "detail": None}
    return {"ok": False, "error_code": code, "detail": detail}
