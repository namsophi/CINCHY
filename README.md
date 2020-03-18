
# Parallel Processor

This program allows multiple customers to put in a request to process documents while following the SLA (service-level agreement). It simulates the processing time with a delay of 1 second for each estimated minute. The algorithm finds a cost efficient way to process the customers' request. The following are assumptions that the program is built upon:
1) $5/h for each processor
2) it takes 1 minute to process 1 document
3) each processor is auto-charged (once you use one, $5 is charged automatically)

## Getting Started

To run this project, install it locally and run `main.py`. <br />
Type in the series of requests to the python console, following the prompt. <br />
Process report will be written by the program in an external text file `report.txt`.

## Example Case

1) No processors are available for immediate use <br />
```
Would you like to put in a new order? Answer Y/N: Y
Enter the number of documents to process: 1000000
Enter the SLA in minutes: 20
Enter how many minutes to wait until next request: 0
Would you like to put in a new order? Answer Y/N: N
Would you like a report of today's orders? Answer Y/N: Y
```
Customer A wants 1 000 000 documents processed in 20 minutes
* 50 000 processors used in total, costing $250 000

2) A customer's request can be finished without purchase of additional processors<br />

```
Would you like to put in a new order? Answer Y/N: Y
Enter the number of documents to process: 1000000
Enter the SLA in minutes: 10
Enter how many minutes to wait until next request: 5
Would you like to put in a new order? Answer Y/N: Y
Enter the number of documents to process: 1000000
Enter the SLA in minutes: 20
Enter how many minutes to wait until next request: 0
Would you like to put in a new order? Answer Y/N: N
Would you like a report of today's orders? Answer Y/N: Y
```

Customer A wants 1 000 000 documents processed in 10 minutes.<br />
Customer B comes in 5 minutes after A's request is finished, and wants 1 000 000 documents processed in 20 minutes<br />

* We purchase 100 000 processors to finish A's requests in time, so by the time we get to B's request we have 100 000 processors for 45 minutes. Hence we can use these to finish B's request in 10 minutes without purchase of additional processors. 
* 100 000 processors were purchased, costing $500 000
* A's request was processed in 10 minutes, and so was B's request.

3) Same time requests <br />

```
Would you like to put in a new order? Answer Y/N: Y
Enter the number of documents to process: 1000000
Enter the SLA in minutes: 10
Enter how many minutes to wait until next request: 0
Would you like to put in a new order? Answer Y/N: Y
Enter the number of documents to process: 1000000
Enter the SLA in minutes: 10
Enter how many minutes to wait until next request: 0
Would you like to put in a new order? Answer Y/N: N
Would you like a report of today's orders? Answer Y/N: Y

```
Customer A and B put in a request at the same time. <br />
Both of them wants 1 000 000 documents processed in 10 minutes.<br />

* We purchase 100 000 processors to process both of their requests in parallel
* The total process time should be 10 minutes for both A and B, and the total cost would be $500 000

4) A customer's request can be partially completed with previous processors<br />

Customer A wants to process 1 000 000 documents in 30 minutes. <br />
Customer B comes in 10 minutes after A's request is finished, and wants 1 000 000 documents processed in 10 minutes <br />

* we already purchased 33334 processors for A, so by the time we start B's request, we have 33334 processors for 20 minutes
* we then purchase 66666 more processors to finish B's request on time
* we would end up with 33334 processors for 10 more minutes, and 66666 processors for 50 more minutes

## Technology

This project is created with:
 * Python 3.7
