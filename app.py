"""
app.py - minimal entrypoint for Streamlit app

Keep this file tiny so streamlit can import it without side-effects.
Run the app with:
    streamlit run app.py

This module simply delegates to src.ui.dashboard.main().
"""
from src.ui import dashboard


def main():
    dashboard.main()


if __name__ == "__main__":
    main()