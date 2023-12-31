# How to Install Spark on Linux
This tutorial explains how to install spark on Linux,
if you prefer watching videos, a tutorial is also available [here](https://youtu.be/AnmG5fgfni8).

Notice that this tutorial is one of many video tutorials available
[here](https://www.youtube.com/playlist?list=PLeOoFBQ0kLpPNThRpLDss-StNs7GTNGkY)

## 1) Install Dependecies
Spark has 2 main dependencies:

    1) java -> jdk
    2) python

Before installing them, first step is to make sure your package manager is updated.
You can do it by typing:

    > sudo apt update

if needed then upgrade it:

    > sudo apt upgrade -y

### Java
To check if java is installed:

    > java --version

if not, then this log is displayed:

    Command 'java' not found

To install it:

    > sudo apt-get install openjdk-17-jdk -y

The `-y` option at the end it to answer automatically yes to any prompt
`apt` might ask during the installation.

Once finished, if java has been installed succesfully you should
be able to get this output:

    > which java
    /usr/bin/java

and this one when checking its version:

    > java --version
    openjdk ....
    OpenJDK Runtime Environment (build ...)
    OpenJDK 64-Bit Server VM (...)

Notice that spark should run with java 8/11/17 and here version 17 is used
as the latest, however make always sure to stay up to date by checking
the [official documentation](https://spark.apache.org/docs/latest/)

### Python
To check if python is installed:

    > python3 --version

make sure to use python3 and not python, as python 2 is not under maintenance
anymore since 1st Jan 2020.

To install python:

    > sudo apt-get install python3

if installation is succesfull then you should be able to get this output:

    > which python3
    /usr/bin/python3

and to check it version:

    > python3 --version

## 2) Download and Install Spark
Btw it's easier to check the [video](https://youtu.be/AnmG5fgfni8) for the following steps

Latest spark software can be found [here](https://spark.apache.org/downloads.html)

At this page we can choose the version we prefer, but make sure the one you pick
is compatible with the java and python versions you have just installed

To download it, you can manually click on the spark software name at point 3:

    3.Download Spark: spark-3.5.0-bin-hadoop3.tgz

then you are redirected to a new page with a link to download the software,
if you click it, then spark is downloaded and you will find it in your download folder.

This works fine if you are working on your local machine,
but if you wanna install spark on a remote server then the fastest way
is to copy the download URL and then on your remote machine type:

    > wget <url>

where `<url>` it the URL you have just copied, so for example in my case this would be:

    > wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz

If `wget` is missing, you can install it like `java` and `python` using `apt`.
Now you should have a copy of spark in the folder you are at:

    > ls
    spark-3.5.0-bin-hadoop3.tgz

To extract the file:

    > tar -xzf spark-3.5.0-bin-hadoop3.tgz

these are what the options are for if you don't know them:

    -x -> extract
    -z -> use gzip
    -f -> archive file, ie file to unzip

Again if you are missing `tar` you can install it with `apt`.
Once finished you should see this:

    > ls
    spark-3.5.0-bin-hadoop3
    spark-3.5.0-bin-hadoop3.tgz

so what you have now is a folder called `spark-3.5.0-bin-hadoop3` where
you will find all the spark binaries

## 3) Set up Environmental Variables
Now that we have spark on our machine, we want to be able to use it
anytime we want, but if we try to spin the `python` shell for example, it won't work:

    > pyspark
    spark: command not found

that's bcs the folder where the binaries are found is not added to the `PATH` variable yet.
To do so, let's add the spark folder (usually called `SPARK_HOME`) to your `bash.rc` file.
First let's open the file by:

    > vi ~/.bashrc

then add these new lines at the very end:

    # spark
    export SPARK_HOME=/home/<user>/<folder_name>
    export PATH=$PATH:$SPARK_HOME/bin

notice that `<user>` and `<folder_name>` must be replaced with
your user and the name of the spark folder.
So in my case this would be:

    SPARK_HOME=/home/bwd/spark-3.5.0-bin-hadoop3

To make the changes effective, save and quit the file and then type:

    > source ~/.bashrc

now if you check the `PATH` variable you should see:

    > echo $PATH
    /usr/local/bin:....:/home/bwd/spark-3.5.0-bin-hadoop3/bin

## 4) Play with Spark
Now that you have installed spark, it's finally time to play with.
Spark offers several shells:

        scala   ->   spark-shell
        python  ->   pyspark
        SQL     ->   spark-sql
        R       ->   sparkR

just pick one and start coding, for example the python shell:

    > pyspark
