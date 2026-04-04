# Puente del Diablo — Web Edition

A Streamlit-based visual novel adaptation of *Puente del Diablo*, a Philippine horror/fantasy story centered on faith, temptation, and a haunted bridge.

## About

This branch (`web-version`) contains the web-ready story engine built with Streamlit. The game follows a linear progression from:

- Title Screen
- Prologue
- Chapter 1
- Chapter 2
- Village & Church exploration
- Chapter 3
- Chapter 4
- Final battle and Good Ending

## Run locally

1. Install dependencies:

```bash
python3 -m pip install streamlit
```

2. Start the app:

```bash
streamlit run TxtNovelPuente_del_Diablo.py
```

3. Open the local URL shown in the terminal.

## Files

- `TxtNovelPuente_del_Diablo.py` — main Streamlit game script
- `.gitignore` — ignores Python cache files and editor temporary files

## Notes

- The game uses `st.session_state` to keep progression state across scenes.
- The branch is intended for web deployment and interactive testing.

## License

See `LICENSE` for project licensing details.
