import sys
from pathlib import Path

# Ensure the pages directory is in sys.path for imports
if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from common import initialize_auth_state, render_company_sections, render_sidebar

initialize_auth_state()


st.set_page_config(page_title="About")

st.markdown("# About")
render_sidebar("About")

st.markdown(
    """
    Fake Company LLC Inc. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

# Use absolute path relative to this file
asset_path = Path(__file__).parent.parent / "assets" / "fake_company.png"
st.image(str(asset_path))

render_company_sections()
