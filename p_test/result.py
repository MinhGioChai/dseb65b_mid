import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



class Result:
    dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0, 'J/P': 0}
    questions = pd.read_csv("./p_test/qsets.tsv", sep = '\t')
    type_dict = pd.read_csv("./p_test/personality_types.csv", index_col = "type")
    @staticmethod
    def calculate_result():
        for dimension, score in st.session_state['answers'].items():
            Result.dimensions[dimension] += score
        
        mbti_type = (
            ('E' if Result.dimensions['E/I'] >= 0 else 'I') +
            ('S' if Result.dimensions['S/N'] >= 0 else 'N') +
            ('T' if Result.dimensions['T/F'] >= 0 else 'F') +
            ('J' if Result.dimensions['J/P'] >= 0 else 'P')
        )
        
        st.session_state['mbti_type'] = mbti_type
        
        st.session_state.stage = 3
    @staticmethod
    @st.cache_data
    def display_result():
        if 'percentage' not in st.session_state:
            st.session_state['percentage'] = []
        
        Result.calculate_result()
        st.markdown(f"<font size = '4'>**{st.session_state["name"]}'s personality type is**</font>", unsafe_allow_html = True)
        st.markdown(F"[<font size = '8'>**{st.session_state['mbti_type']}: {Result.type_dict.loc[st.session_state['mbti_type'],"title"]}**</font>](https://www.16personalities.com/{st.session_state['mbti_type']}-personality)", unsafe_allow_html = True)
        st.markdown(f"<font size = '5'>{Result.type_dict.loc[st.session_state['mbti_type'],"description"]} </font>", unsafe_allow_html = True)
        st.markdown(f"<font size = '4'>{Result.type_dict.loc[st.session_state['mbti_type'],"percentage"]} of the population</font>", unsafe_allow_html = True)
        
        traits = ["Extraverted", "Observant", "Thinking", "Prospecting"]
        scores = [54, 57, 57, 53]  # Percent scores for each trait
        left_labels = ["Extraverted", "Intuitive", "Thinking", "Judging"]
        right_labels = ["Introverted", "Observant", "Feeling", "Prospecting"]
        colors = ['#5DADE2', '#F4D03F', '#58D68D', '#AF7AC5', '#E74C3C']  # Custom colors