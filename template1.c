// All File IO must be performed using stdio.h
#include <stdio.h>
// #include <stdbool.h>
// template < unsigned SizeOfRec >
#define SizeOfRec 

typedef struct 
{
  int filler; // cant have flexible array in struct alone 
  char m_chdata[];
} Record;

void record_new(Record *rec){ // Record()
  return;
}

void destruct_record(Record *rec){ // ~Record()
  return;
}

void record_new_copy(Record *rec){ // ?idk
  return;
}

long size(Record *rec){}

int operator(Record *r1, Record *r2){
  //  Put your comparison function here.
  return 0;
};

// Total amount of hard drive space used should not exceed twice the
// size of the input file.

// Total amount of memory used should not exceed the amount input by
// the user. An error should occur if you cannot sort in the amount
// of memory the user inputs.


typedef struct 
{
  FILE *m_h_inpfile;   // handle to input file
  FILE *m_h_outfile;   // handle to output file
  long m_lnrecords;    // Number of records in file.
  int  m_i_amt_of_mem; // memory limit 
} FileSorter;

void file_sorter_new(FileSorter *fs) {
  return;
}

void destruct_file_sorter(FileSorter *fs) {
  return;
}

// Status of call: Should return 1 if sorted, -x for an error. You should say what -x is, when you code.
// For instance -1 = No disk space left
//              -2 = File IO error
//              ...

int two_pass_merge_sort_i_j(FileSorter *fs, long i, long j){ // Only sorts records i to j.
  return 1;
}

int two_pass_merge_sort(FileSorter *fs){ // Sorts the whole file.

  passZeroSort(fs->m_h_inpfile); 
  return 1;
}

void perror(FileSorter *fs, int x){ //print a verbose output of what went wrong when sorting was attempted
  return;
}



// split file into 1 page runs for initial sort
void passZeroSort(FILE *input_file){

}

// sort pages via quicksort

void swap(int *i, int *j) {
  int temp = *i;
  *i = *j;
  *j = temp;
}

// function to find the partition position
int partition(int array[], int low, int high) {
  int pivot = array[high];
  int i = (low - 1);

  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
      i++;
      swap(&array[i], &array[j]);
    }
  }
  swap(&array[i + 1], &array[high]);
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {
    int pi = partition(array, low, high);
    quickSort(array, low, pi - 1);
    quickSort(array, pi + 1, high);
  }
}



// Main function: should be short!
int main(int argc, char **argv){

  FileSorter sorter;
  sorter.m_h_inpfile = argv[1]; 
  sorter.m_h_outfile = argv[2]; 
  sorter.m_lnrecords = argv[3]; 
  int key_size = argv[4];
  sorter.m_i_amt_of_mem = argv[5]; 
  
  two_pass_merge_sort(&sorter);

  return 0;
}
