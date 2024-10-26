import streamlit as st

# StreamlitのUI部分
st.title("選択されたテキストの位置情報を取得（デモ用）")

# テキストを表示する
text = "Pythonは素晴らしい言語です。Pythonは広く使われています。"
st.write(text)

# 選択テキストを入力するフィールドを用意
selected_text = st.text_input("選択したテキストを入力してください")

# 選択されたテキストの情報を表示
if selected_text:
    occurrences = [i for i in range(len(text)) if text.startswith(selected_text, i)]
    if len(occurrences) > 0:
        if len(occurrences) == 1:
            # 出現箇所が1つだけの場合は直接表示
            start_offset = occurrences[0]
            end_offset = start_offset + len(selected_text)
            st.write(f"選択されたテキスト: {selected_text}")
            st.write(f"開始位置: {start_offset}, 終了位置: {end_offset}")
        else:
            # 各出現箇所をリストで表示して選択させる
            options = [f"{i + 1}番目: 位置 {occurrence}" for i, occurrence in enumerate(occurrences)]
            selected_option = st.selectbox("選択したい出現箇所を選んでください", options)
            selected_index = options.index(selected_option)
            start_offset = occurrences[selected_index]
            end_offset = start_offset + len(selected_text)
            st.write(f"選択されたテキスト: {selected_text}")
            st.write(f"開始位置: {start_offset}, 終了位置: {end_offset}")
    else:
        st.write("入力されたテキストが見つかりませんでした。正しく選択してください。")