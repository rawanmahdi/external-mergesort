import sys
import heapq
import os

class FileSorter:
    def __init__(self, input_file, output_file, record_size, key_size, amt_of_mem):
        self.input_file = input_file
        self.output_file = output_file
        self.record_size = record_size
        self.key_size = key_size
        self.amt_of_mem = amt_of_mem
    
    def two_pass_merge_sort(self):
        # pass 0: seperate file into smaller sorted temporary files
        temp_files = [] # to keep track of the temporary files we generate

        # define the buffer size as 60% of total memory divided by the record size
        buffer_size = max(int(self.amt_of_mem * 0.6) // self.record_size, 4096)

        # read the input file into the buffer in buffer_size chunks
        with open(self.input_file, 'rb') as file:
            while True:
                buffer = file.read(buffer_size)
                if not buffer: # until we get to the end of the file
                    break
                # collect records from the buffer
                buff_records = []
                number_records = len(buffer) // self.record_size
                for i in range(number_records):
                    record = buffer[i*self.record_size: (i+1)*self.record_size]
                    buff_records.append(record)
              
                # sort each buffer using general nlogn sort                
                buff_records.sort( key = lambda r: r[: self.key_size] ) 
                
                # write the sorted buffer to a temporary file under temp folder
                temp_dir = "./temp"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                temp_file = temp_dir+'/'+f"{self.input_file}.temp_{len(temp_files)}"
                
                with open(temp_file, 'wb') as temp:
                    for record in buff_records:
                        temp.write(record) 
                
                temp_files.append(temp_file)

        # destroy input file
        os.remove(self.input_file)

        # pass 1: merge sort the temporary files in 1 pass
        with open(self.output_file, 'wb') as output:

            heap = [] # we use a minheap to keep track of the current minimum record to write to the output
            buffers = [open(temp_file, 'rb') for temp_file in temp_files]

            for buffer in buffers: # for each buffer
                # add firs record, and buffer itself to the heap
                # this value is the minimum record for that buffer
                record = buffer.read(self.record_size)
                heapq.heappush(heap, (record, buffer))

            while heap: # while we still have buffers containing records to write
                
                record, buffer = heapq.heappop(heap) # get the minimum record from the heap
                output.write(record) # write minimum to the output file
                
                next_rec = buffer.read(self.record_size) # add the next record (i.e the next min) for that buffer to the heap
                
                if next_rec:
                    heapq.heappush(heap, (next_rec, buffer))
                else: # indicates that buffer is empty
                    buffer.close()
                    os.remove(buffer.name)  # therefore we can garbage collect the temporary file representing our buffer
   

if __name__ == "__main__":

    # parse args
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    record_size = int(sys.argv[3])
    key_size = int(sys.argv[4])
    amt_of_mem = int(sys.argv[5]) * 1024 * 1024  # Convert MB to bytes
    
    # sort 
    sorter =  FileSorter(input_file, output_file, record_size, key_size, amt_of_mem)
    sorter.two_pass_merge_sort()