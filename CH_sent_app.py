
import streamlit as st
from textblob import TextBlob
from snownlp import SnowNLP

def main():
    # title
    st.title("Sentiment Analysis App")
    st.subheader("Hello World!")

    st.sidebar.subheader("About the App")
    st.sidebar.info("Use this tool to get the sentiment score!")

    menu = ["English version", "Chinese version"]
    choice = st.sidebar.selectbox("Choose Language", menu)

    # English
    if choice == "English version":
        st.subheader("English version")
        with st.form(key = "nlpForm"):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label = "Analyze")
         
        #layout
        if submit_button:
            st.info("Results")
            result_sent = TextBlob(raw_text).sentiment
            st.write(result_sent)

        #emoji
            if result_sent.polarity > 0:
                st.markdown("Sentiment: Positive :smiley: ")
                st.balloons()
            elif result_sent.polarity < 0:
                st.markdown("Sentiment: Negative :angry: ")
                st.snow()
            else:
                st.markdown("Sentiment: Neutral :neutral_face: ")     

    else:
        # Chinese
        st.subheader("中文版")
        with st.form(key = "nlpForm"):
            raw_text = st.text_area("在這裡打字")
            submit_button = st.form_submit_button(label = "分析")
        
        # layout
        if submit_button:
            st.info("結果")
            result_sent = SnowNLP(raw_text).sentiments
            st.write(result_sent)

        #emoji
            if result_sent > 0.5:
                st.markdown("情感: 正向 :smiley: ")
                st.balloons()
            elif result_sent < 0.5:
                st.markdown("情感: 負向 :angry: ")
                st.snow()
            else:
                st.markdown("情感: 中性 :neutral_face: ")  

if __name__ == '__main__':
    main()