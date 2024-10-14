import pytest

from e2b_code_interpreter.code_interpreter_async import AsyncSandbox


@pytest.mark.skip_debug()
async def test_execution_count(async_sandbox: AsyncSandbox):
    await async_sandbox.notebook.exec_cell("echo 'E2B is awesome!'")
    result = await async_sandbox.notebook.exec_cell("!pwd")
    assert result.execution_count == 2
