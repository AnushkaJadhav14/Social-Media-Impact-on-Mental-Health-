import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('smmh.csv')

#defining function to calculate mental health scores
def calculate_scores(use_of_social_media_without_purpose, social_media_platforms, distraction_level, restlessness, worry_level, comparison, interest_fluctuation, sleep_issues, appetite_issues):
    
    #e.g. logic for mental health scores based on inputs
    adhd_score = use_of_social_media_without_purpose + distraction_level
    self_esteem_score = comparison
    anxiety_score = restlessness + worry_level
    depression_score = interest_fluctuation + worry_level + appetite_issues
        

    if len(social_media_platforms) > 4:  #e.g. if the user uses more than 4 platforms
        adhd_score += 1  #increase ADHD score
        anxiety_score += 1  #increase Anxiety score
        depression_score += 1  #increase Depression score

    if daily_social_media_usage_time in ['4 to 6 hours']:
        anxiety_score += 1  #increase Anxiety score for higher usage time
        depression_score += 1  #increase Depression score for higher usage time

    #total score
    total_score = adhd_score + self_esteem_score + anxiety_score + depression_score

    #return calculated scores
    return adhd_score, self_esteem_score, anxiety_score, depression_score, total_score


#SLit UI
st.markdown("""
    <style>

    /* For Main Title */
    .title {
        text-align: center;
        font-size: 34px;
        color: #ff4081;
        font-weight: bold;
    }
    
    /* Font size for questions asked*/
    .question-label {
        font-size: 22px !important;
        font-weight: bold;
        color: #4B0082;
        margin-bottom: 10px;
    }

    /* Font size for radio button options of questns*/
    .stRadio div {
        padding: 5px;
        font-size: 18px;
    }
    </style>
    <h2 class="title">IMPACT OF SOCIAL MEDIA ON MENTAL HEALTH</h2>
    <br>
    <br>
    <br>
    <br>
    
    <style>
    /* Add custom CSS to adjust the size of the input box*/
    input[type=number] {
        width: 150px;
    }
    

    /* For age column length of textbox
    */
    .custom-header {
        font-size: 22px;
        color: #2E8B57;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    <div class="custom-header">Please Choose An Option<br></div>
    """, unsafe_allow_html=True)

#creating dropdown
option = st.selectbox(
    "",
    ('CHOOSE AN OPTION', 'EXPLORATORY DATA ANALYSIS', 'MENTAL HEALTH PREDICTION'),
    key='main_option',
    help="Select between Exploratory Data Analysis or Mental Health Prediction."
)

#displaying selected option
if option != 'CHOOSE AN OPTION':
    st.success(f"You have selected: {option}")
else:
    st.warning("Please select an option from the dropdown.")


if option == 'MENTAL HEALTH PREDICTION':
    st.write()
    st.markdown("<h5>Please select how you feel:</h5>", unsafe_allow_html=True)
    st.write()
    
    #Text Boxes and MCQ ips for different lvls
    st.write()
    col1, col2 = st.columns(2)
    
    with col1:

        st.markdown('<div class="question-label">AGE:</div>', unsafe_allow_html=True)
        age = st.number_input('Please enter your age (20 to 26 only)', min_value=20, max_value=26, key='age')

        st.markdown('<div class="question-label">GENDER:</div>', unsafe_allow_html=True)
        gender = st.radio('', ['Male', 'Female'], horizontal=True, key='gender')

        st.markdown('<div class="question-label">OCCUPATION STATUS:</div>', unsafe_allow_html=True)
        occupation_status = st.radio('', ['University Student', 'Salaried Worker'], horizontal=True, key='occupation')

        st.markdown('<div class="question-label">SOCIAL MEDIA PLATFORMS YOU USE:</div>', unsafe_allow_html=True)
        social_media_platforms = st.multiselect('', ['Facebook', 'Instagram', 'Twitter', 'YouTube', 'Snapchat', 'Discord', 'Pinterest'], key='social_media_platforms')
        st.write()

        st.markdown('<div class="question-label">DAILY SOCIAL MEDIA USAGE TIME:</div>', unsafe_allow_html=True)
        st.write()
        daily_social_media_usage_time = st.radio('', ['1 to 2 hours', '2 to 4 hours', '4 to 6 hours'], horizontal=True, key="daily_social_media_usage_time")
        
        st.markdown('<div class="question-label">USE OF SOCIAL MEDIA WITHOUT PURPOSE:</div>', unsafe_allow_html=True)
        use_of_social_media_without_purpose = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='use_of_social_media_without_purpose')

    with col2:
        st.markdown('<div class="question-label">DISTRACTION LEVEL:</div>', unsafe_allow_html=True)
        distraction_level = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='distraction_level')
        
        st.markdown('<div class="question-label">RESTLESSNESS WITHOUT SOCIAL MEDIA:</div>', unsafe_allow_html=True)
        restlessness = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='restlessness')
        
        st.markdown('<div class="question-label">WORRY LEVEL:</div>', unsafe_allow_html=True)
        worry_level = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='worry_level')

        st.markdown('<div class="question-label">COMPARISON TO SUCCESSFUL PEOPLE LEVEL:</div>', unsafe_allow_html=True)
        comparison = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='comparison_level')
        
        st.markdown('<div class="question-label">INTEREST FLUCTUATION LEVEL:</div>', unsafe_allow_html=True)
        interest_fluctuation = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='interest_fluctuation')
        
        st.markdown('<div class="question-label">SLEEP ISSUES LEVEL:</div>', unsafe_allow_html=True) 
        sleep_issues = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='sleep_issues')
        
        st.markdown('<div class="question-label">APPETITE ISSUES LEVEL:</div>', unsafe_allow_html=True)
        appetite_issues = st.radio('', [1, 2, 3, 4, 5], horizontal=True, key='appetite_issues')

    #calculate mental health scores 
    adhd_score, self_esteem_score, anxiety_score, depression_score, total_score = calculate_scores(
        use_of_social_media_without_purpose, social_media_platforms, distraction_level, restlessness, worry_level, comparison,
        interest_fluctuation, sleep_issues, appetite_issues
    )


    #display results
    st.markdown("<h2>MENTAL HEALTH SCORES:</h2>", unsafe_allow_html=True)

    #ADHD SCORE
    st.markdown(f"**ADHD SCORE:** {adhd_score} / 11")
    st.progress(int(adhd_score / 11 * 100))

    #explanation for ADHD Score
    if len(social_media_platforms) > 4:
        st.warning("**NOTE:** YOUR ADHD SCORE INCREASED BY 1 DUE TO THE USAGE OF MORE THAN 4 SOCIAL MEDIA PLATFORMS.")

    #ANXIETY SCORE
    st.markdown(f"**ANXIETY SCORE:** {anxiety_score} / 12")
    st.progress(int(anxiety_score / 12 * 100))

    #explanation for Anxiety Score
    if daily_social_media_usage_time in ['4 to 6 hours']:
        st.warning("**NOTE:** YOUR ANXIETY SCORE INCREASED BY 1 DUE TO DAILY SOCIAL MEDIA USAGE TIME OF 4 TO 6 HOURS.")
    if len(social_media_platforms) > 4:
        st.warning("**NOTE:** YOUR ANXIETY SCORE INCREASED BY 1 BECAUSE YOU ARE USING MORE THAN 4 SOCIAL MEDIA PLATFORMS.")

    #SELF-ESTEEM SCORE
    st.markdown(f"**SELF-ESTEEM SCORE:** {self_esteem_score} / 5")
    st.progress(self_esteem_score * 20)

    #DEPRESSION SCORE
    st.markdown(f"**DEPRESSION SCORE:** {depression_score} / 17")
    st.progress(int(depression_score / 17 * 100))
    st.write("")  #extra line gap

    #explanation for Depression Score
    if daily_social_media_usage_time in ['4 to 6 hours']:
        st.warning("**NOTE:** YOUR DEPRESSION SCORE INCREASED BY 1 DUE TO DAILY SOCIAL MEDIA USAGE TIME OF 4 TO 6 HOURS.")
    if len(social_media_platforms) > 4:
        st.warning("**NOTE:** YOUR DEPRESSION SCORE INCREASED BY 1 BECAUSE YOU ARE USING MORE THAN 4 SOCIAL MEDIA PLATFORMS.")
        

    #TOTAL MENTAL HEALTH SCORE
    st.markdown(f"**TOTAL MENTAL HEALTH SCORE:** {total_score} / 45")
    st.progress(int(total_score / 45 * 100))    


    #check for conditions
    if adhd_score > 9:
        st.error('WARNING: THE USER MAY HAVE ADHD.')
    if self_esteem_score > 4:
        st.error('WARNING: THE USER MAY HAVE LOW SELF-ESTEEM.')
    if anxiety_score > 10:
        st.error('WARNING: THE USER MAY HAVE ANXIETY.')
    if depression_score > 15:
        st.error('WARNING: THE USER MAY HAVE DEPRESSION.')
        st.write("") #extra line gap
    
    if total_score > 33:
        st.write("") #extra line gap
        st.write("") 
        st.success('**RECOMMENDATION: THE USER MAY NEED PSYCHOLOGICAL COUNSELLING.**')
        st.write()
    else:
        st.write("") #extra line gap
        st.write("") 
        st.success('**THE USER DOES NOT NEED PSYCHOLOGICAL COUNSELLING.**')
        st.write("")


    #footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: #4B0082;'>Take care of your mental health. Seek help if needed!</h5>", unsafe_allow_html=True)





elif option == 'EXPLORATORY DATA ANALYSIS':

    #sidebar filters
    st.sidebar.header('Filters')

    #filter by age
    age_range = st.sidebar.slider('Select Age Range', int(df['Age'].min()), int(df['Age'].max()), (20, 26))

    #filter by gender
    gender = st.sidebar.multiselect('Select Gender', df['Gender'].unique(), default=df['Gender'].unique())

    #filter by occupation status
    occupation = st.sidebar.multiselect('Select Occupation Status', df['Occupation_Status'].unique(), 
                                        default=df['Occupation_Status'].unique())

    #Daily Social Media Time filter
    time_filter = st.sidebar.multiselect('Daily Social Media Time', df['Daily_Social_Media_Time'].unique(), 
                                         default=df['Daily_Social_Media_Time'].unique())

    #filter dataset based on selected sidebar inputs
    filtered_data = df[
        (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])
    ]
    filtered_data = filtered_data[filtered_data['Gender'].isin(gender)]
    filtered_data = filtered_data[filtered_data['Occupation_Status'].isin(occupation)]
    filtered_data = filtered_data[filtered_data['Daily_Social_Media_Time'].isin(time_filter)]

    #main dashboard
    st.header('Survey Respondents Data Visualization')

    #display filtered data in a dataframe
    st.subheader('Filtered Data')
    st.dataframe(filtered_data)

    #summary statistics
    st.subheader('Summary Statistics')
    st.write(filtered_data.describe())

    #average age
    average_age = df['Age'].mean()
    st.write(f"Average Age of Respondents: {average_age:.2f}")

    #age distribution(Histogram)
    st.subheader("Age Distribution")
    plt.hist(df['Age'], bins=19, color='red')
    plt.xlabel("Age")
    plt.ylabel("Number of Respondents")
    plt.title("Age Distribution")
    st.pyplot(plt)

    #Social Media Platforms Used (Bar Chart)
    st.subheader("Social Media Platforms Used")
    platform_count = df['Social_Media_Platforms'].str.split(';').explode().value_counts()
    st.bar_chart(platform_count)

    #correlation heatmap
    st.subheader('Correlation Heatmap of Mental Health Factors')
    corr_columns = ['adhd_score', 'anxiety_score', 'self_esteem_score', 'depression_score']
    plt.figure(figsize=(10, 6))
    sns.heatmap(filtered_data[corr_columns].corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    st.pyplot(plt)

    #pie chart: Social Media Platforms used by Gender
    st.header('Social Media Platforms used by Gender')

    #exploring the platforms used per gender
    filtered_df = filtered_data.copy()
    filtered_df = filtered_df.assign(Platforms=filtered_df['Social_Media_Platforms'].str.split(';')).explode('Platforms')

    #grouping the data by Gender and Platforms
    gender_platforms = filtered_df.groupby(['Gender', 'Platforms']).size().unstack().fillna(0)

    #plotting pie charts for each gender
    for gender in gender_platforms.index:
        st.subheader(f'Social Media Platform Usage for {gender}')
        platform_count = gender_platforms.loc[gender]
        plt.figure(figsize=(6,6))
        plt.pie(platform_count, labels=platform_count.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
        plt.axis('equal')
        st.pyplot(plt)

    #Histogram: Distribution of ADHD Scores
    st.subheader('Distribution of ADHD Score')
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['adhd_score'], bins=10, kde=True, color="blue")
    st.pyplot(plt)

    #Histogram: Distribution of Anxiety Scores
    st.subheader('Distribution of Anxiety Score')
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['anxiety_score'], bins=10, kde=True, color="red")
    st.pyplot(plt)

    #Histogram: Distribution of Self Esteem Scores
    st.subheader('Distribution of Self Esteem Score')
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['self_esteem_score'], bins=10, kde=True, color="green")
    st.pyplot(plt)

    #Histogram: Distribution of Depression Scores
    st.subheader('Distribution of Depression Score')
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['depression_score'], bins=10, kde=True, color="yellow")
    st.pyplot(plt)

    #Bar Chart: Distribution of Daily Social Media Time
    st.subheader('Distribution of Daily Social Media Usage Times')
    df['Daily_Social_Media_Time'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribution of Daily Social Media Usage Times')
    plt.xlabel('Daily Usage Time')
    plt.ylabel('Number of Respondents')
    plt.xticks(rotation=0)
    st.pyplot(plt)

    #Line Chart: Mental Health Scores by Age Range
    st.subheader('Mental Health Scores by Age Range')
    age_group_scores = df.groupby('Age')[corr_columns].mean().reset_index()
    plt.figure(figsize=(10, 6))
    for score in corr_columns:
        plt.plot(age_group_scores['Age'], age_group_scores[score], label=score)
    plt.title('Mental Health Scores Across Age Groups')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.legend()
    st.pyplot(plt)
