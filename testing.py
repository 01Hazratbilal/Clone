# import streamlit as st
# import pandas as pd
# import numpy as np
# from scipy import stats
# import time
# import io
# from io import StringIO
# import streamlit.components.v1 as components
# import sys
# from st_aggrid import AgGrid


# data = pd.read_csv('pages/tmdb_5000_credits.csv')
# st.write("Edit the dataset:")
# grid_response = AgGrid(data, editable=True, fit_columns_on_grid_load=True, update_mode="value_changed")



from st_aggrid import AgGrid
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(data, editable=True, fit_columns_on_grid_load=True, update_mode="value_changed")