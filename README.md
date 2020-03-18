
# Parallel Processor

This program allows multiple customers to put in a request to process documents while following the SLA (service-level agreement). It simulates the processing time with a delay of 1 second for each estimated minute. The algorithm finds a cost efficient way to process the customers' request in parallel. The following are assumptions that the program is built upon:
1) $5/h for each processor
2) it takes 1 minute to process 1 document
3) each processor is auto-charged (once you use one, $5 is charged automatically)

## Getting Started

To run this project, install it locally and run `main.py`. <br />
Type in input to the python console as prompted. <br />
Process report will be written by the program in an external text file `report.txt`.

## Example Case

1) Customer A wants to process 1 000 000 documents in 20 minutes
* `report.txt` should report once it is done processing the required documents
* there should have been 50 000 processors used total cost should be $250 000


## Technology

This project is created with:
 * Python 3.7
