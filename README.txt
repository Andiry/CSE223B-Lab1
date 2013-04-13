	CSE223B Lab1
	Jian Xu, A53026658
	jix024@eng.ucsd.edu


********	HOW TO RUN	********

This lab is written in Python, since I don't know how to program in Java. Hope it does not matter.

The lab consists of two files, InvertIndex_map.py, for mapper; and InvertIndex_reduce.py, for reducer.

Before you run the job, change the mode of the two files:
$ chmod 777 InvertedIndex/*

Now you can run the job with following command:
$ $HADOOP_PATH/bin/hadoop jar $HADOOP_PATH/contrib/streaming/hadoop*streaming*jar -input /user/$USER/II_input/* -output /user/$USER/II_output -file InvertedIndex/InvertIndex_map.py -mapper InvertedIndex/InvertIndex_map.py -file InvertedIndex/InvertIndex_reduce.py -reducer InvertedIndex/InvertIndex_reduce.py

Modify the path accordingly. I've also attached the output file II_output in the tar file.


********	EXPLAINATION      ********

InvertIndex_map.py:
This file read from stdin, split the line with space, and for each word, get the filename of current file, and process the word: first low the case, only keep following character valid:
a-z, 0-9, ' -
And remove all the other characters.
Finally, print the output to stdout: key is word, and value is filename.

InvertIndex_reduce.py:
This file read from stdin, get the (key, value), and insert the (key, value) into a dictionary if key is not in it or the (key, value) in the dictionary does not contain the new value.
