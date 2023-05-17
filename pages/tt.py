import streamlit as st
import pandas as pd
import numpy as np
import time
import io
from io import StringIO
import streamlit.components.v1 as components
import sys
from st_aggrid import AgGrid


# To have Wide page
st.set_page_config(page_title="Tranining",
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   page_icon= '✌')

# Hide the Sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# css for page text

css = """
<style>
    .custom-container {
    height: 1%;
    width: 1%;
    border: 1px solid black;
    }
    
    .welcome-font{
        color: red;
        font-size: 50px;
        text-align: center;
    }

    .intro-font{
        font-size: 29px;
        font-family: Rockwell;
    }
    
    .lead-font{
        font-size: 30px;
        color: red;
        font-family: Rockwell;
    }

    .page-font{
        font-family: Comic Sans MS !important;
        font-weight: bold;
        font-size: 19px;
    }

    .color{
        color: red;
    }
    
    .small-font{
    font-family: small-font;
    font-size: 16px;
    font-weight: bold;
    color: red;
    }
    
</style>
"""
# To make css true for st.markdown...
st.markdown(css, unsafe_allow_html=True)

# JavaScript for buttons
def changebtn(label, font_size, marginleft, width):

    btn = f"""
        </style>
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{label}') {{ 
                    elements[i].style.fontSize = '{font_size}';
                    elements[i].style.color = 'white';
                    elements[i].style.textAlign = 'center';
                    elements[i].style.padding = '20px';
                    elements[i].style.marginLeft = '{marginleft}';
                    elements[i].style.backgroundColor = 'rgb(97, 153, 222)';
                    elements[i].style.height = '100%';
                    elements[i].style.width = '{width}';
                    elements[i].style.border = 'solid rgb(89, 94, 101)';
                    elements[i].style.borderRadius = '7px';
                    elements[i].style.transition = 'all 0.6s ease';
                    elements[i].style.cursor = 'pointer';
                    
                    elements[i].onmouseover = function() {{
                        this.style.backgroundColor = 'transparent';
                        this.style.color = 'black';
                        this.style.transform = 'scale(1.1)';
                    }}
                    elements[i].onmouseout = function() {{
                        this.style.backgroundColor = 'rgb(97, 153, 222)';
                        this.style.color = 'white';
                        this.style.transform = 'scale(1)';
                    }}
                }}
            }}
        </script>
        """
    components.html(f"{btn}", height=0)

# Display the balloons
if 'balloons_shown' not in st.session_state:
    st.session_state['balloons_shown'] = False

if not st.session_state['balloons_shown']:
    st.balloons()
    st.balloons()
    st.session_state['balloons_shown'] = True

# Create a markdown string for the welcome message
welcome_message = """
<h1 class='welcome-font'>Welcome to the Training Phase! 🙋‍♂️</h1><br>
"""
# Display the welcome message using markdown
st.markdown(welcome_message, unsafe_allow_html=True)

# Intro
st.markdown("<div class = 'intro-font'><b><span class = 'color'>'The Titanic' 🚢⚓️</span> Dataset is a popular choice for Data Analysts in Training - it's like the Training wheels of Data Analysis!</b></div><br>", unsafe_allow_html=True)

# Get start
st.markdown("<div class = 'lead-font'>I Believe in You, let's Do This! 🌟. Together We Can Achieve Anything! 🤝. <b>Let's Start.</b></div><br><hr>", unsafe_allow_html=True)

# Insert Dataset
st.markdown("<div class = 'page-font' > Press <span class = 'color'>Load Dataset</span> Button, To Add a Dataset for Analysis.</div>", unsafe_allow_html=True)
st.write('')

# Defining columns to use onwards
col1, col2, col3 = st.columns(3)

# button col1
with col1:
    st.write('')
    st.write('')
    dataset_bnt = st.button('# Load Dataset')
    changebtn("Load Dataset", "25px", "0", "96%")
    if dataset_bnt:
        with col2:
            st.file_uploader('Choose a file', type= ['csv', 'xlsx', 'xls', 'txt', 'json', 'html', 'xml'])
        with col3:
            st.write('')
            st.write('')
            st.write('')
            st.markdown("<div class = 'page-font'>Dataset? No problem, we'll just Titanic it and make waves 🌊🚢😉.</div>", unsafe_allow_html= True)
st.write('---')
#time.sleep(3)

# to see head and tail of data set
data = pd.read_csv('titanic.csv')
data.index.name = 'Index'

# if dataset_bnt:
st.markdown("<div class = 'page-font' style = 'text-align: center;'>🎯 Here's where we Begin and End - the <span class = 'color'>Head & Tail</span> of our dataset! 🎲", unsafe_allow_html= True)
st.write('')
st.table(data.head())
st._legacy_table(data.tail())
st.text('See! The Head & Tail. Notice the <NA> ("None" or "null") in Head and nan ("Not a Number") in tail, also true/false in Head and 0/1 in Tail. Both means the same.\nThe purpose to Differencite both is for better understanding with the Data')
st.write('---')


# if 'ready' not in st.session_state:
#     st.session_state.ready = False


# if dataset_bnt:
    # st.session_state.ready = True
    #time.sleep(2)
st.markdown("<div class = 'page-font' style = 'text-align: center;'>Unlock the Secrets of your Data with <span class = 'color'>Statistics</span>, it's like a Treasure Map! 🗺️</div>", unsafe_allow_html=True)
st.markdown("<div class='stat-button'></div>", unsafe_allow_html=True)
go = st.button('# Statistics')
changebtn("Statistics", "30px", "20%", "60%")

    
# if 'stat1' not in st.session_state:
#     st.session_state.stat1 = False

# if st.session_state.stat1:
#     st.session_state.stat1 = True
col1, col2, col3= st.columns((4, 0.0001, 2.1))
with col1:
    st.markdown("<div class = 'small-font'>You can Analyze the Statistics of Data (only Numerical Data). Using dataset.describe()</div>", unsafe_allow_html= True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    formatted_data = data.describe().applymap(lambda x: "{:.1f}".format(x))
    st.table(formatted_data)
    st.text('You can see the Statistics of the Dataset.\nCount is the number of rows. Mean, standard deviation, Minimun and Maximum of each column.\nYou can also Analyse the 4-Quartile. 1st Quartile from 0-25%. 2nd Quartile from 25-50%.\n3rd Quartile from 50-75%. 4th Quartile form 75-100%')

with col3:
    st.markdown("<div class = 'small-font'>All Information of the Dataset. Using dataset.info()</div>", unsafe_allow_html= True)
    st.write('')
    def get_info(df):
        buf = io.StringIO()
        df.info(buf=buf)
        return buf.getvalue()
    st.text(get_info(data))
st.write('---')
st.write('')
st.markdown("<div class = 'page-font' style = 'text-align: center;'>The important part is to see for <span class = 'color'>NULL valuse</span> and <span class = 'color'>Duplicates</span> in the Dataset.</div>", unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns((1,1))
with col1:
    nan_data = pd.DataFrame(data.isna().sum()).reset_index()
    nan_data.columns = ['Column Name', 'Number of NULL values']
    st.markdown("<div class = 'small-font'>You can analyze the NULL values or Empty cells. Using dataset.isna()</div>", unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.table(nan_data)

with col2:
    st.markdown("<div class = 'small-font'>Keep Remember the Data Type of Each column, it will help you further. Using dataset.dtype()</div>", unsafe_allow_html= True)
    data_types = pd.DataFrame(data.dtypes, columns=['Data Type'])
    st.write('')
    st.write('')
    st.table(data_types)


col1, col2, col3 = st.columns((2,0.001,1))
with col1:
    st.markdown("<div class = 'small-font'>Duplicate Values. Using datset.duplicated()</div>", unsafe_allow_html= True)
    st.write('')
    duplicates = data[data.duplicated()]
    st.dataframe(duplicates)



with col3:
    st.markdown("<div class = 'small-font'>Shape of Dataset. Using datset.shape()</div>", unsafe_allow_html= True)
    st.write('')
    initial_shape = data.shape
    shape_after_duplicates_dropped = data.drop_duplicates().shape
    shape_after_nulls_dropped = data.dropna().shape
    num_nulls = data.isna().sum().sum()
    num_duplicates = data.duplicated().sum()
    col1, col2, col3 = st.columns(3)
    # Use the st.metric function to display these values
    with col2:
        st.metric(label="**Initial Dataset Shape**", value=str(initial_shape))
    col1, col2, col3 = st.columns((3,0.001, 3))
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.metric(label="**Number of Null Values**", value=str(num_nulls))
    with col3:
        st.write('')
        st.write('')
        st.write('')
        st.metric(label="**Number of Duplicates**", value=str(num_duplicates))
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.metric(label="**Shape After Dropping Duplicates**", value=str(shape_after_duplicates_dropped), delta=f"-{initial_shape[0] - shape_after_duplicates_dropped[0]} rows")
    with col3:
        st.write('')
        st.write('')
        st.write('')
        st.metric(label="**Shape After Dropping Null Values**", value=str(shape_after_nulls_dropped), delta=f"-{initial_shape[0] - shape_after_nulls_dropped[0]} rows", delta_color= 'inverse')
st.write('---')



# Removing Duplicates
st.markdown("<div class = 'page-font' style = 'text-align: center'>Let's Remove the Duplicates as Duplicates lead to <span class = 'color'>Inaccurate Results</span> and cause of <span class = 'color'>Bias in Machine Learning Models</span>.", unsafe_allow_html= True)
data = data.drop_duplicates()
st.write('')
duplicate = st.button('# Drop Duplicates')
changebtn("Drop Duplicates", "25px", "20%", "60%")
# add section...
st.text('Duplicates removed Successfully')
st.write('---')

# Three columns. Deletion, Imputation, Understanding the Reason
st.markdown("<div class = 'page-font' style = 'text-align: center'>Let's go through the <span class = 'color'>NULL Cells</span>. As <span class = 'color'>NULL Cells</span> lead to <span class = 'color'>Inaccuracy in Results</span>, cause of <span class = 'color'>Incompatibility with Machine Learning Algorithms</span>, and <span class = 'color'>Misrepresentation of Data</span>.", unsafe_allow_html= True)
st.text('There are several ways to handle the NULL Cells.')

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class = 'page-font' style = 'color: red;'>Deletion:</div>", unsafe_allow_html= True)
    st.write('If the proportion of null values is small, you might choose to simply delete the rows or columns that contain them. However, this can lead to loss of information.')
    

with col2:
    st.markdown("<div class = 'page-font' style = 'color: red;'>Imputation:</div>", unsafe_allow_html= True)
    st.write('Imputation means filling in the null values with some value. This could be a central tendency measure like the mean or median, or a prediction from a machine learning model, or simply a constant value like zero.')
    


with col3:
    st.markdown("<div class = 'page-font' style = 'color: red;'>Understanding the Reason:</div>", unsafe_allow_html= True)
    st.write("Try to understand why the data is missing. Is it missing at random, or is there a pattern to the missing data? If it's the latter, the fact that a value is missing might in itself be informative.")


# Three buttons. Drop NuLL, replace with mean, edit your self
col1, col2, col3 = st.columns(3)
with col1:
    drop_null = st.button('# Drop NULL')
    changebtn("Drop NULL", "20px", "5%", "90%")

with col2:
    replace_with_mean = st.button('# Replace with Mean')
    changebtn("Replace with Mean", "20px", "5%", "90%")

with col3:
    edit = st.button('# Edit Yourself')
    changebtn("Edit Yourself", "20px", "5%", "90%")

if drop_null:
    data.dropna(axis=0)
    st.text('NULL Cells droped')


if replace_with_mean:
    numeric_cols = data.select_dtypes(include=[np.number])
    data = numeric_cols.fillna(numeric_cols.mean())
    st.warning('🧨 Only Numberical Data is Replaced.')
    st.text('Successfully replaced with mean')

# Edit buttonnn
if edit:
    # Get a list of the columns with null values
    columns_with_nulls = data.columns[data.isnull().any()].tolist()

    # Create a selectbox for the user to choose which column to edit
    column_to_edit = st.selectbox('Select a column to edit', columns_with_nulls)

    # Ask the user to input a value to fill the nulls
    value_to_fill = st.text_input(f'Enter a value to fill the nulls in {column_to_edit}')

    if st.button('Submit'):
        # Fill the null values in the selected column with the user's input
        data[column_to_edit] = data[column_to_edit].fillna(value_to_fill)




AgGrid(data, editable=True, fit_columns_on_grid_load=True, update_mode="value_changed")
