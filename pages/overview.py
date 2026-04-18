import sys
from pathlib import Path

# Ensure the pages directory is in sys.path for imports
if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from common import initialize_auth_state, render_company_sections, render_sidebar

initialize_auth_state()


st.set_page_config(page_title="Overview")

st.markdown("# Overview")
render_sidebar("Overview")

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

render_company_sections()
