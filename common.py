import streamlit as st

COPYRIGHT_TEXT = "This site is copyright Fake Company LLC Inc., 2024"
COMPANY_INFO_MD = """
Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
"""
LINKS_MD = """
[Google](https://google.com)

[Gemini](https://gemini.google.com)

[Streamlit Docs](https://docs.streamlit.io/)
"""


def initialize_auth_state() -> None:
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False


def login() -> None:
    st.session_state.logged_in = True


def logout() -> None:
    st.session_state.logged_in = False


def render_sidebar(page_title: str | None = None) -> None:
    if page_title:
        st.sidebar.header(page_title)

    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write(COPYRIGHT_TEXT)


def render_company_sections() -> None:
    with st.expander("Company Info"):
        st.write(COMPANY_INFO_MD)

    with st.expander("Links"):
        st.markdown(LINKS_MD)
import streamlit as st

COPYRIGHT_TEXT = "This site is copyright Fake Company LLC Inc., 2024"
COMPANY_INFO_MD = """
Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
"""
LINKS_MD = """
[Google](https://google.com)

[Gemini](https://gemini.google.com)

[Streamlit Docs](https://docs.streamlit.io/)
"""


def initialize_auth_state() -> None:
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False


def login() -> None:
    st.session_state.logged_in = True


def logout() -> None:
    st.session_state.logged_in = False


def render_sidebar(page_title: str | None = None) -> None:
    if page_title:
        st.sidebar.header(page_title)

    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)

    st.sidebar.write(COPYRIGHT_TEXT)


def render_company_sections() -> None:
    with st.expander("Company Info"):
        st.write(COMPANY_INFO_MD)

    with st.expander("Links"):
        st.markdown(LINKS_MD)