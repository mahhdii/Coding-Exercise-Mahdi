JUNIOR DATA ENGINEER POSITION

# Map-Reduce Word Count Exercise

This project is implemented in Python using gRPC. The input files are given in .txt format and the word count operation is performed. 

## **Description**

MapReduce is a programming model and an associated implementation for processing and generating large data sets. 


# Installation and Usage

## Setup

## Dependencies


```bash
$ python -V
    Python 3.8.5
$ python -m pip install grpcio
$ python -m pip install grpcio tools
```

## Code Structure

There are three main files called the client, worker and driver. The client gives the input files and the number of output files and the worker ports (e.g. 127.0.0.1:4001). The worker nodes are launched with their ports and are responsible for the map and reduce operations. The driver takes the input from the client and distributes the work among all the worker nodes. 

### Proto Files

The code implenation begins with writing the proto files for the driver and worker.

#### **driver.proto**

Driver file launches the data processing operation, which is carried out when `rpc launchDriver (launchData) returns (status);` is executed in the code. 

Once the proto file is written, the following command is executed in the terminal.

```python
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. driver.proto
```
This generates two files in the directory named, driver_pb2_grpc.py and driver_pb2.py.

#### **worker.proto**

The worker file sets the driver port, carries out the map and reduce operations. An additional method, die, is provided to terminate the process. The worker methods are as follows:
```
rpc setDriverPort(driverPort) returns (status);
rpc map(mapInput) returns (status);
rpc reduce (rid) returns (status);
rpc die (empty) returns (status);
```
Similar to driver, the following command is executed in the terminal.

```python
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. worker.proto
```
This generates two files in the directory named, worker_pb2_grpc.py and worker_pb2.py.

### Python Files

Once the proto files are ready, python files for client, driver and worker are written.

#### **worker.py**

The files worker_pb2_grpc.py and worker_pb2.py are imported along with the python libraries. The code for map and reduce are defined in the worker class along with connecting to the driver port.

**MAP** 

Mapper function maps input key/value pairs to a set of intermediate key/value pairs. Maps are the individual tasks that transform input records into intermediate records. The transformed intermediate records do not need to be of the same type as the input records. A given input pair may map to zero or many output pairs. The number of maps is usually driven by the total size of the inputs, that is, the total number of blocks of the input files.

The input text files are opened in read mode. The operations performed on a given input file  are converting it to lower case, removing special charectors (other than words) and tranform the document into words. Then each word is sent to a bucket and these are stored in files.

**REDUCE**

Reducer reduces a set of intermediate values which share a key to a smaller set of values. The numver of reduce operations are drfined in client.py.
In reduce function, glob library is used to extract all files based on a similar id. Then we use the counter function (imported from library collections) to generate a dictionary with the frequency of words.


#### **driver.py**

The worker.py file, all the files generated from proto files and python libraries are imported. The Driver class has several functions. The files are loaded and the worker ports are saved in launchDriver and then connections are established with all the workers. 


#### **client.py**

The in-built python libraries are imported along with the files generated from the proto file. A connection channel is established with the driver. Inputs and number of reduce operations and worker ports are initialized when the client is launched. Once the word count operation is performed, it exits with a message.




## Running the Code

You can run the code with any number of workers and output files. Here, I am running for 3 workers and 6 output files.
1. Launch 3 workers by running the following command in the terminal.Provide the port number along with the command.
```python
$ python worker.py 4001
```
Open another terminal and run the following command:
```python
$ python worker.py 4002
```
Each worker needs to be declared in a seperate terminal. Open a new terminal and run the following command:
```python
$ python worker.py 4003
```
2. Launch the driver in a new terminal using the following command:

```python
$ python driver.py 4000
```
3. Finally launch the client in a new terminal using the following command:
   
```python
$ python client.py ./inputs 6 4001 4002 4003
```

# References 
[GRPC Tutorial](https://grpc.io/docs/languages/python/basics/)

[Map Reduce](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

[Map Reduce Tutorial using Python](https://riptutorial.com/hadoop/example/13413/word-count-program-in-java---python-)

[Bloom RPC](https://github.com/bloomrpc/bloomrpc/releases)

https://programmer.ink/think/wordcount-of-mapreduce-implemented-by-python.html


