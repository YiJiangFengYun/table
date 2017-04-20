using System;
using System.Collections.Generic;

namespace table
{
    public static class TableIO
    {
        private static List<Column> m_colAttsHelper = new List<Column>();
        public static Table Read(byte[] byteArray, uint offset, Table resultTable = null)
        {
            uint position = offset;
            int i;
            int j;
            ///1.Parse first table, namely, table attributes.
            //Now there are only one attribute of table (name attribute). so table parsing has one row and one column.
            //3 means three bytes storage row and column count of table.
            position += 3;
            // and 1 means first one byte of cell bytes storage bytes length of cell value.
            byte[] tempBytes = new byte[] { 0, 0, 0, byteArray[position] };
            tranToSystemEndian(tempBytes);
            uint lengthColumnBytes = BitConverter.ToUInt32(tempBytes, 0);  //get length of bytes of column value stored in one byte
            position += 1;

            string tableName = CellIO.Read(CellType.TypeId.CharStr_Value,
                                                 byteArray,
                                                 position,
                                                 lengthColumnBytes) as String;
            position += lengthColumnBytes;


            ///2.Parse second table, namely table column attributes.
            //get table row count;
            tempBytes = new byte[] { 0, 0, byteArray[position], byteArray[position + 1] };
            tranToSystemEndian(tempBytes);
            uint rowCount = BitConverter.ToUInt32(tempBytes, 0);
            position += 2;

            //get table column count;
            tempBytes = new byte[] { 0, 0, 0, byteArray[position] };
            tranToSystemEndian(tempBytes);
            uint columnCount = BitConverter.ToUInt32(tempBytes, 0);
            position += 1;


            var columnAttributes = m_colAttsHelper;
            if (columnAttributes.Capacity < columnCount)
            {
                columnAttributes.Capacity = (int)columnCount;
            }
            for (i = 0; i < rowCount; ++i)
            {
                //first column of this table storage column name of target table. its type is char[].

                //get length of bytes of column value stored in one byte
                tempBytes = new byte[] { 0, 0, 0, byteArray[position] };
                tranToSystemEndian(tempBytes);
                lengthColumnBytes = BitConverter.ToUInt32(tempBytes, 0);
                position += 1;

                //get column name
                string colName = CellIO.Read(CellType.TypeId.CharStr_Value,
                                                   byteArray, position, lengthColumnBytes) as String;
                position += lengthColumnBytes;


                //get column type id
                CellType.TypeId colTypeId = (CellType.TypeId)CellIO.Read(CellType.TypeId.Int_Value, byteArray);
                position += 4;

                //third column of this table storage column description of target table, its type is unicode string.

                //get length of bytes of column value stored in two byte
                tempBytes = new byte[] { 0, 0, byteArray[position], byteArray[position + 1] };
                tranToSystemEndian(tempBytes);
                lengthColumnBytes = BitConverter.ToUInt32(tempBytes, 0);
                position += 2;
                //get column description.
                string colDescription;
                if (lengthColumnBytes != 0)
                {
                    colDescription = CellIO.Read(CellType.TypeId.UnicodeStr_Value,
                                                              byteArray,
                                                              position,
                                                              lengthColumnBytes) as String;
                    position += lengthColumnBytes;
                }
                else
                {
                    colDescription = null;
                }

                Column columnAttribute;
                if (columnAttributes[i] == null)
                {
                    columnAttribute = new Column(colName, colTypeId, colDescription);
                    columnAttributes[i] = columnAttribute;
                }
                else
                {
                    columnAttribute = columnAttributes[i];
                    columnAttribute.Set(colName, colTypeId, colDescription);
                }
            }

            ///3.Parse third table, its is real target table.
            //get table row count;
            tempBytes = new byte[] { 0, 0, byteArray[position], byteArray[position + 1] };
            tranToSystemEndian(tempBytes);
            rowCount = BitConverter.ToUInt32(tempBytes, 0);
            position += 2;

            //get table column count;
            tempBytes = new byte[] { 0, 0, 0, byteArray[position] };
            tranToSystemEndian(tempBytes);
            columnCount = BitConverter.ToUInt32(tempBytes, 0);
            position += 1;

            if (resultTable == null)
            {
                resultTable = new Table(tableName, rowCount, columnCount, columnAttributes); //create table
            }
            else
            {
                resultTable.Set(tableName, rowCount, columnCount, columnAttributes);  //reset table.
            }
            for (i = 0; i < rowCount; ++i)
            {
                for (j = 0; j < columnCount; ++j)
                {
                    Column columnAttribute = columnAttributes[j];
                    Cell cell = resultTable.GetCell((uint)i, (uint)j);
                    if (cell.TypeId == CellType.TypeId.CharStr_Value)
                    {
                        //get length of bytes of column value stored in one byte
                        tempBytes = new byte[] { 0, 0, 0, byteArray[position] };
                        tranToSystemEndian(tempBytes);
                        lengthColumnBytes = BitConverter.ToUInt32(tempBytes, 0);
                        position += 1;

                        cell.WriteWithByteArray(byteArray, position, lengthColumnBytes);
                        position += lengthColumnBytes;
                    }
                    else if (cell.TypeId == CellType.TypeId.UnicodeStr_Value)
                    {
                        //get length of bytes of column value stored in two byte
                        tempBytes = new byte[] { 0, 0, byteArray[position], byteArray[position + 1]};
                        tranToSystemEndian(tempBytes);
                        lengthColumnBytes = BitConverter.ToUInt32(tempBytes, 0);
                        position += 2;

                        cell.WriteWithByteArray(byteArray, position, lengthColumnBytes);
                        position += lengthColumnBytes;
                    }
                    else
                    {
                        if (cell.TypeId != CellType.TypeId.Null_Value)
                        {
                            uint byteCount = (uint)CellType.TypeByteLengths[(int)cell.TypeId];
                            cell.WriteWithByteArray(byteArray,
                                                    position,
                                                    byteCount);
                            position += byteCount;
                        }
                    }
                }
            }

            return resultTable;
        }

        //public static byte[] Write(List<List<object>> tableOfTableAttr, 
        //    List<List<object>> tableOfColumnAttr, List<List<object>> table, 
        //    byte[] result = null, uint offsetOfResult = 0)
        //{
        //    if(result == null)
        //    {
        //        result = new byte[]{ };
        //    }
        //    int position = (int)offsetOfResult;

        //    int rowCount = tableOfTableAttr.Count;
        //    if (rowCount == 0) throw new Exception("Table for target table attribute is empty.");
        //    int colCount = tableOfTableAttr[0].Count;
        //    //row count write to 2 bytes and col count write to 1 byte.
        //    byte[] tempBytes = BitConverter.GetBytes((short)rowCount);
        //    tranToSystemEndian(tempBytes);
        //    tempBytes = BitConverter.GetBytes((byte)colCount);

            
            
        //}

        
        private static void tranToSystemEndian(byte[] bytes)
        {
            if (BitConverter.IsLittleEndian)
                Array.Reverse(bytes);
        }
    }
}
