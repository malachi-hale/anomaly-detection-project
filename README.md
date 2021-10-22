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