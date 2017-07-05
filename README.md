# tablejs

build work flow:


       build proto(use tablejs's buildProto) <-----   extensions
           |
           | (build --> dynamic protos --> table binary io proto libraries)
           |
           V
       tables generate table js objects with js proto (use tablejs's parseTables)
           |
           |
           V
       table js objects check (use tablejs's check) <----- extensions
           |
           | (no error)
           |
           |
           V
       table js objects generate table binary files with js proto (use tablejs's generateBin)

