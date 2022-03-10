import csv

class FileRepository():
    __file_path = ''
    __file_open = None
    
    def __init__(self, file_path):
        self.__file_path = file_path

    def __open_file(self) -> None:
        if(self.__file_open==None):
            self.__file_open = open(self.__file_path)
    
    def __close_file(self) -> None:
        if(self.__file_open):
            self.__file_open.close()

    def read_data(self):
        try:
            data_read = []
            
            self.__open_file()
            csv_reader = csv.reader(self.__file_open)
            
            next(csv_reader)
            for row in csv_reader:
                    data_read.append(row)
                    
            return data_read
        except Exception as exception:
            raise Exception('Error reading data: ' + str(exception))
        finally:
            self.__close_file()