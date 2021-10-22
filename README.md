# Anomaly Detection 

## Project Background and Business Goals

Hello,
I have some questions for you that I need to be answered before the board meeting Friday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?

4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

7. Which lessons are least accessed?
Anything else I should be aware of?

## Audience 

The Codeup Data Science management. 

## Data Dictionary

| Feature    | Dataype        | Definition                                                                                                                                           |
|:-----------|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Time       | datetime       | A combination of the calendar date and the twenty-four hour time the site was accessed.                                                              |
| date       | object         | The calendar date the site was accessed.                                                                                                             |
| time       | object         | The time of day the site was accessed.                                                                                                               |
| user_id    | int64          | Number that indicates the user accesssing the site.                                                                                                  |
| cohort_id  | float64        | Number the identifies each cohort.                                                                                                                   |
| ip         | object         | The IP address accessing the site.                                                                                                                   |
| id         | float64        | The ID number identifying each cohort.                                                                                                               |
| name       | object         | The name of each cohort.                                                                                                                             |
| slack      | object         | The Slack channel of the cohort.                                                                                                                     |
| start_date | datetime64[ns] | The date the cohort began classes.                                                                                                                   |
| end_date   | datetime64[ns] | The date the chort ended classes.                                                                                                                    |
| created_at | datetime64[ns] | The date the path accessed was created.                                                                                                              |
| updated_at | datetime64[ns] | The date the path was most recently updated.                                                                                                         |
| program_id | float64        | The ID indicating the program. 1 is PHP Full Stack Development. 2 is Java Full Stack Development. 3 is Data Science. 4 is Front Ned Web Development. |


## Executive Summary 

### Project Goal 

In this project we address Questions 1, 2, 3, 5, 6, and 7. We are looking for anomalies in our data that interesting to the Codeup management.

### Outline 

We will take the following steps:

 - **Acquire** data from the Codeup database. 
     - We use a SQL query from our `acquire.py` file. 
 - **Prepare** the data by:
     - eliminating columns with excessive null values, 
     - imputing null values, 
     - creating a `Time` column that is a combination of the calendar and clock value. Set this column as the index. 
     - convert the remaining time columns to datetime format. 
 - **Explore** the data by creating visualizations for:
        - Visits to each path by program and
        - Visits to each path by ohort.
 - **Answer** questions 1, 2, 3, 5, 6, and 7. 
 
### Key Findings 

#### Question 1

For Program 1, the most frequently accessed page is not a lesson, but rather an index. Therefore, the most frequently accessed lesson is the second value `javascript-i`.

For Program 2, the most frequently accessed page is toc, which is likely Table of Contents. Thus, the most frequently accessed lesson for this program is also `javascript-i`.

For Program 3, the most frequently accessed page is `Classification Overview`, which is in fact a lesson.

#### Question 2
**Program 1**
- Cohort 6 was more likely to visit "javascript-ii/es6" than other cohorts. 

- Cohort 2 was more likely to visit some of the php lessons that the other cohorts. 

**Program 2**
- Cohort 139 is far more likely than the other cohorts in Program 2 to access many of the lessons, specifically Javascript lessons.

**Program 3**
- Students in Cohort 137, the Florence cohort, are more likely to access many of the lessons online than other cohorts in Program 3, including fundamentals, python, classification, etcetera.

- Cohorts 59 and 133, the Darden and Easley cohorts, were more likely to access the online lessons for classification than other cohorts.

#### Question 3
We can indentify 15 students that accessed the curriculum less than 20 times while they were active students. 

#### Questions 5
Students appear to have lost access to the other version of the curriculum in late October to early November 2019. 

#### Question 6
The most popular lessons for students after graduation were:
- javascript-i,
- java-iii,
- java-ii,
- jquery,
- mysql
- java-i,
- javascript-ii

#### Question 7 
There are 407 paths that only received 1 visit.


### Recommendations

It may be useful to elimate some of the paths that students are hardly visitng. Furthermore, more recent paths seem to be more popular, so regularly updating or rewriting the curriculum may increase student engagement. 

## Pipeline Stages Breakdown

### Project Planning 

 - Create a `READ.me` file with an outline for the project. 
 
 - Brainstorm ideas for ways to possibly address the questions at hand. 
 
### Data Acquisition 
#### In the `acquire.py` module 
 
 - Access the SQL database using the credentivals in the `env.py` file. 
 
 - Run a SQL query that returns data for accesses to the Codeup curriculum. 

#### In the Notebook 

 - Run the functions from the `acquire.py` module. 
 
 - Graph the categorical features. 
 
 - Graph the time dependent data. 
 
### Data Preparation 
#### In the `prepare.py` module 

 - Eliminate rows and columns which fail to meet a certain threshold of non-null values. 
 
 - Impute the remaining null values with the most frequent value of that column.
 
 - creating a Time column that is a combination of the calendar and clock value. Set this column as the index.
 
 - convert the remaining time columns to datetime format.

#### In the Notebook 
 
 - import the functions from the `prepare.py` module. 
 
 - eliminate rows from Program 4. 
 
### Explore 

 - Create visualizations for: 
 
     - Visits to each path by program and 
     
     - Visits to each path by cohort. 
     
### Answer the Questions 
We explore the data to address questions 1, 2, 3, 5, 6, and 7. 

## Reproduce my Project 

To reproduct my project, you will need to obtain your own `env.py` file with database credentials, in addition to the actions below:

 - Read this `README.md` file. 
 
 - Download the `acquire.py`, `prepare.py`, and `Main_Notebook.ipynb` files. 
 
 - Add your own `env.py` file to your directionary. You will need to access the SQL database to obtain the Codeup curriculum database. 
 
 - Run the `Main_Notebook.ipynb` files. 
 