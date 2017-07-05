# tablejs

build work flow:

       build table common proto(use tablejs's buildCommonProto) <-----   extensions
           |
           | (build --> dynamic protos --> table common binary io proto libraries)
           |
           V
	   load tables and parse tables to arrays (use tablejs's parseTables)
	       |
		   |
		   |
		   V
	   _________________________	   
	   for each table (use tablejs's buildTable): 
	             build table proto (use tablejs's buildTableProto) 
    			   |
				   |
				   |
				   V
				 generate table js objects with proto above (use tablejs's createTableObjs)
				   |
				   |
				   |
				   V
				 check table with table js objects (use tablejs's checkTable)
				   |
				   |
				   |
				   V
				 generate table binary file with js objects, js proto and protoc execution (use tablejs's generateTableBin)
	   __________________________
	   
	       |
		   |
		   |
		   V
	   complete work.

