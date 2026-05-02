"""Phase-1 placeholder so `pytest -x` exits 0 in CI.

Real protocol-buffer / gRPC contract tests land in Phase 2 — at that
point we'll also add a `[build-system]` table to pyproject.toml so the
package itself can be installed and imported in tests.
"""


def test_placeholder() -> None:
    assert True
