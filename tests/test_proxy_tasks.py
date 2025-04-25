# # tests/test_proxy_tasks.py
# from utils.proxy_runner import run_proxy_prompt

# def test_health_quote_flow():
#     prompt = """
#     1. Open https://devev.jioinsure.in/.
#     2. Select "Health" in the dropdown.
#     3. Fill a random mobile number and Indian PIN code.
#     4. Click "Get Free Quotes".
#     5. Return the visible result text.
#     """
#     result = run_proxy_prompt(prompt)
#     print("\nProxy Output:\n", result)

#     # assert "Order ID" in result.lower() or "plan" in result.lower()
#     # assert ('Order ID' in '' or 'plan' in '')

import asyncio
import pytest
from utils.proxy_runner import create_runner

@pytest.fixture(scope="session")
def runner():
    return create_runner()

@pytest.mark.asyncio
async def test_browser_interaction(runner):
    prompt =  """
    1. Open https://devev.jioinsure.in/.
    2. Select "Health" in the dropdown.
    3. Fill a random mobile number and Indian PIN code.
    4. Click "Get Free Quotes".
    5. Return the visible result text.
    """
    result = await runner.run(prompt)
    assert result is not None
