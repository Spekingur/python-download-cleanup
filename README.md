# Download Cleanup

Internet Pirates, i.e. the people that download movies and shows, often have a folder on their computer that temporarily stores the files that they are currently downloading. This temporary storage can become a little bit more permanent than intended at first, and they end up with a huge directory that no sane man would ever want to go through and categorize.

Your task is to write a Python script that goes through a download folder and categorizes it (or sorts it out), by moving the files in the download folder to their appropriate directory.

Suppose your script is called clean.py (you can choose the name, of course). In this assignment you are required to implement a script that can be called as follows.

    python3 clean.py /path/to/download/folder /path/to/structured/folder

This call should find as many episodes in the download folder as possible and move them to a new "structured" folder. Suppose the structured folder is called target. In that case, an episode of a given show should be moved to a subfolder of target whose name is the title of the show. If that folder does not exist, it is created. If it is possible to determine which season the episode belongs to, it should be moved to a subfolder of the show's folder, dedicated to episodes of that season. If that folder does not exist, it is created.

Suppose the script comes across the file the.big.bang.theory.s05e05.hdtv.xvid-fqm.avi inside the download folder. We can determine from the name of the episode, that it is episode 5 from season 5 of The Big Bang Theory. The file should therefore be moved to:

    target/The Big Bang Theory/Season 05/the.big.bang.theory.s05e05.hdtv.xvid-fqm.avi

When moving files to the target folder, these naming rules should be followed:

* The name of the show folder (in this case The Big Bang Theory) should contain no punctuations (no periods, apostrophes, etc.) and its words should be separated by a single space.
* The name of the season folder should be Season [number] where [number] is the season number, zero padded to two places. Therefore an episode in season 4 should be in the folder Season 04 and an episode in season 12 in the folder Season 12.
* The name of the file can be kept as it or you can rename the files to anything you like.

The download folder used to test your solutions on the server can be found here.

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
