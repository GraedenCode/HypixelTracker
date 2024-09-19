import streamlit as st

st.set_page_config(layout='wide')

st.title('Daily Tasks')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    farming_expander = st.expander('Farming')
    with farming_expander:
        st.checkbox('Visitors')

with col2:
    mining_expander = st.expander('Mining')
    with mining_expander:
        st.checkbox('Commissions')
        st.checkbox('Fetchur')
        st.checkbox('Puzzler')

with col3:
    crimson_island_expander = st.expander('Crimson island')
    with crimson_island_expander:
        st.checkbox('Heavy Pearls')
        st.checkbox('Quests')
        st.checkbox('Kuudra Runs')
        st.checkbox('Bosses')

with col4:
    dungeon_expander = st.expander('Dungeons')
    with dungeon_expander:
        st.checkbox('Four Runs')

with col5:
    enchanting_expander = st.expander('Enchanting')
    with enchanting_expander:
        st.checkbox('Experiment Table')