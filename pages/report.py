import sys
from pathlib import Path

# Ensure the pages directory is in sys.path for imports
if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from common import initialize_auth_state, render_company_sections, render_sidebar

initialize_auth_state()


st.set_page_config(page_title="Report")

st.markdown("# Report")
render_sidebar("Report")

st.write(
    """
        Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
"""
)

render_company_sections()
