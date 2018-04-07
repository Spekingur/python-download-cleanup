# Download Cleanup

## Grading

Your solutions will be automatically assessed by an online server. The server will score your solutions on a scale from 0 to 100. The score is calculated as a ratio between the correctly categorized shows and the total number of shows, with penalties for moving the wrong files or moving files to the wrong location. After running your script, the server will categorize each file in the target folder into one of these categories.

* **Correct show, correct season:** A show file in a correct show folder and in a correct season folder.
* **Correct show, wrong season:** A show file in a correct show folder but in the wrong season folder
* **Wrong show:** A show file that is not in a correct show folder
* **Incorrect path format:** A file that is not in a [show name]/[season name] folder.
* **Non TV-show:** A file that is not a show
* **New:** A file that was not in the original downloads folder
* **Duplicate:** A file that was moved/copied to more than one place in the target folder

In addition you are given a list of unknown shows, which are show folders that were created but do not match any of the show names in the folder.

The assignment grade will be determined by your score as follows.

Score from server | Points
------------------|-------
0-39 | 0
40-49 | 30
50-59 | 55
60-69	| 65
70-79	| 75
80-84	| 85
85-90	| 90
90-94 | 95
95+	| 100
 
Points can be deducted for

* Overfitting (special cases for certain shows/episodes)
* Code quality and poor setup
* Poor usability
 
Note that the goal is not to get a perfect score from the server. It is impossible to do without overfitting. Keep your solution as general as possible and focus on making your solution well structured and readable.
