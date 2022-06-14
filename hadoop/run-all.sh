#!/bin/sh

# Before you run this bash file, you should put raw data under the /tmp directory: /tmp/mr.data.
# The source code files are under the /scripts directory.
# To run this bash file, you should have your Hadoop started and HDFS initialized.

# Load your data into HDFS
bin/hadoop dfs -copyFromLocal /tmp/mr.data /input

# Run 5 Map-Reduce scripts, and the results will be stored in /output1-5
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -mapper scripts/mapper-01.py -reducer scripts/reducer-01.py -input /input -output /output1
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -mapper scripts/mapper-02.py -reducer scripts/reducer-02.py -input /input -output /output2
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -mapper scripts/mapper-03.py -reducer scripts/reducer-03.py -input /input -output /output3
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -mapper scripts/mapper-04.py -reducer scripts/reducer-04.py -input /input -output /output4
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar -mapper scripts/mapper-05.py -reducer scripts/reducer-05.py -input /input -output /output5
