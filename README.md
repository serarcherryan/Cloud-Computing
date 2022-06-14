# Cloud-Computing

## Introduction
This project contains the source code of the Hadoop assignment. You may not run the code directly until you start Hadoop and HDFS on your own machine. Besides, you should also put the files and directories into the right place.

To run this project, there 2 two options.

## Option1
You should download the [Hadoop-3.3.2](https://dlcdn.apache.org/hadoop/core/hadoop-3.3.2/).

Install and start your Hadoop: [Reference](https://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/)

Then put *run-all.sh* and */scripts* into */hadoop*.

Put your input data([mr.data](http://soudeh.net/teaching/cloud/files/mr.data)) into */tmp/mr.data*.

Finally you can successfully run the *run-all.sh*.

## Option2
For convenience, You can also download the whole project on the shared [Google Drive](https://drive.google.com/file/d/1YJQ1eJgdAhDF_5VfRq3AS6xTM45r0Im6/view?usp=sharing).

In this way, after you initialize the HDFS, you just need to start the hadoop under */hadoop* with the following commands:
```
sudo systemctl start ssh
sbin/start-all.sh
```
