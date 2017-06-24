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
                CellType.TypeId colTypeId = (CellType.TypeId)CellIO.Read(CellType.TypeId.Int_Value, byteArray, position);
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
                if (columnAttributes.Count <= i)
                {
                    columnAttribute = new Column(colName, colTypeId, colDescription);
                    columnAttributes.Add(columnAttribute);

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
                        tempBytes = new byte[] { 0, 0, byteArray[position], byteArray[position + 1] };
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

        public static byte[] Write(object[,] tableOfTableAttr,
            object[,] tableOfColumnAttr, object[,] table)
        {
            List<byte> resultList = new List<byte>();

            ///Write first table.
            int rowCount = tableOfTableAttr.GetLength(0);
            if (rowCount == 0) throw new ArgumentException("Table for target table attribute is empty.");
            int colCount = tableOfTableAttr.GetLength(1);
            if (colCount == 0) throw new ArgumentException("Table for target table attribute is empty.");
            //row count write to 2 bytes and col count write to 1 byte.
            byte[] tempBytes = BitConverter.GetBytes((short)rowCount);
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);
            tempBytes = new byte[] { (byte)colCount };
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);

            //write table name.
            if (tableOfTableAttr[0, 0] == null) throw new ArgumentException("Table name don't exist.");
            string tableName = tableOfTableAttr[0, 0].ToString();
            byte[] stringTempBytes = System.Text.Encoding.ASCII.GetBytes(tableName);
            if (stringTempBytes.Length > byte.MaxValue) throw new ArgumentException("Table name length exceed limit " + byte.MaxValue + ".");
            //write length of bytes of tableName
            tempBytes = new byte[] { (byte)stringTempBytes.Length };
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);
            //continue write table name.
            resultList.AddRange(stringTempBytes);
            ///End write first table.

            ///Write second table.
            rowCount = tableOfColumnAttr.GetLength(0);
            if (rowCount == 0) throw new ArgumentException("Table for target table columns attributes is empty.");
            colCount = tableOfColumnAttr.GetLength(1);
            if (colCount == 0) throw new ArgumentException("Table for target table columns attributes is empty.");
            //row count write to 2 bytes and col count write to 1 byte.
            tempBytes = BitConverter.GetBytes((short)rowCount);
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);
            tempBytes = new byte[] { (byte)colCount };
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);

            int[] typeIds = new int[rowCount];
            for (int i = 0; i < rowCount; ++i)
            {
                //first column of this table storage column name of target table. its type is char[].
                if (tableOfColumnAttr[i, 0] == null) throw new ArgumentException("Column name don't exist.");
                tableName = tableOfColumnAttr[i, 0].ToString();
                stringTempBytes = System.Text.Encoding.ASCII.GetBytes(tableName);
                if (stringTempBytes.Length > byte.MaxValue) throw new ArgumentException("Column name length exceed limit " + byte.MaxValue + ".");
                //write length of bytes of column name, it is stored in one byte.
                tempBytes = new byte[] { (byte)stringTempBytes.Length };
                tranToBigEndian(tempBytes);
                resultList.AddRange(tempBytes);
                //continue write column name.
                resultList.AddRange(stringTempBytes);

                //second column of this table store column type name of target table.
                if (tableOfColumnAttr[i, 1] == null) throw new ArgumentException("Column type don't exist.");
                string colTypeName = tableOfColumnAttr[i, 1].ToString();
                int typeId = Array.FindIndex(CellType.TypeNames, s => s.Equals(colTypeName));
                if (typeId < 0) throw new ArgumentException("Column type name (" + colTypeName + ") specified don't exist.");
                typeIds[i] = typeId;
                //write type id.
                resultList.AddRange(CellIO.Write(CellType.TypeId.Int_Value, typeId));

                //thrid column of this table store column description of target table. its type is unicode string.
                string columnDes;
                if (tableOfColumnAttr[i, 2] != null)
                {
                    columnDes = tableOfColumnAttr[i, 2].ToString();
                }
                else
                {
                    columnDes = "";
                }
                stringTempBytes = System.Text.Encoding.UTF8.GetBytes(columnDes);
                int maxLength = 2 * byte.MaxValue;
                if (stringTempBytes.Length > maxLength) throw new ArgumentException("Column description length exceed limit " + maxLength + ".");
                //write length of bytes of description, it is stored in two bytes.
                tempBytes = BitConverter.GetBytes((short)stringTempBytes.Length);
                tranToBigEndian(tempBytes);
                resultList.AddRange(tempBytes);
                //continue write description to bytes
                resultList.AddRange(stringTempBytes);
            }
            ///End write second table.

            ///Write third table. it is real target table.
            rowCount = table.GetLength(0);
            if (rowCount == 0) throw new ArgumentException("Target table is empty.");
            colCount = table.GetLength(1);
            if (colCount == 0) throw new ArgumentException("Target table is empty.");
            //The valid columns of target table should match the rows of second table.
            if (colCount > typeIds.Length) colCount = typeIds.Length;
            //row count write to 2 bytes and col count write to 1 byte.
            tempBytes = BitConverter.GetBytes((short)rowCount);
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);
            tempBytes = new byte[] { (byte)colCount };
            tranToBigEndian(tempBytes);
            resultList.AddRange(tempBytes);

            for (int i = 0; i < rowCount; ++i)
            {
                for (int j = 0; j < colCount; ++j)
                {
                    int typeId = typeIds[j];
                    if (typeId == (int)CellType.TypeId.CharStr_Value ||
                        typeId == (int)CellType.TypeId.UnicodeStr_Value)
                    {
                        string strContent;
                        if (table[i, j] != null)
                        {
                            strContent = table[i, j].ToString();
                        }
                        else
                        {
                            strContent = "";
                        }
                        if (typeId == (int)CellType.TypeId.CharStr_Value)
                        {
                            stringTempBytes = System.Text.Encoding.ASCII.GetBytes(strContent);
                            int maxLength = byte.MaxValue;
                            if (stringTempBytes.Length > maxLength) throw new ArgumentException("Length of cell char[] content of table exceed limit " + maxLength + ".");
                            //write length of bytes of description, it is stored in one bytes.
                            tempBytes = new byte[] { (byte)stringTempBytes.Length };
                            tranToBigEndian(tempBytes);
                            resultList.AddRange(tempBytes);
                            //continue write description to bytes
                            resultList.AddRange(stringTempBytes);
                        }
                        else
                        {
                            stringTempBytes = System.Text.Encoding.UTF8.GetBytes(strContent);
                            int maxLength = byte.MaxValue * 2;
                            if (stringTempBytes.Length > maxLength) throw new ArgumentException("Length of cell unicode string content of table exceed limit " + maxLength + ".");
                            //write length of bytes of description, it is stored in one bytes.
                            tempBytes = BitConverter.GetBytes((short)stringTempBytes.Length);
                            tranToBigEndian(tempBytes);
                            resultList.AddRange(tempBytes);
                            //continue write description to bytes
                            resultList.AddRange(stringTempBytes);
                        }
                    }
                    else if (typeId == (int)CellType.TypeId.Int_Value ||
                        typeId == (int)CellType.TypeId.Float_Value ||
                        typeId == (int)CellType.TypeId.Double_Value)
                    {
                        object content;
                        if (typeId == (int)CellType.TypeId.Int_Value)
                        {
                            content = Convert.ToInt32(table[i, j]);
                        }
                        else if (typeId == (int)CellType.TypeId.Float_Value)
                        {
                            content = Convert.ToSingle(table[i, j]);
                        }
                        else
                        {
                            content = Convert.ToDouble(table[i, j]);
                        }
                        resultList.AddRange(CellIO.Write((CellType.TypeId)typeId, content));
                    }
                    else if (typeId == (int)CellType.TypeId.Bool_Value)
                    {
                        bool content = Convert.ToBoolean(table[i, j]);
                        resultList.AddRange(CellIO.Write((CellType.TypeId)typeId, content));
                    }
                    else  //null type
                    {
                        //no write bytes.
                    }
                }
            }

            return resultList.ToArray();
        }

        private static void tranToSystemEndian(byte[] bytes)
        {
            if (BitConverter.IsLittleEndian)
                Array.Reverse(bytes);
        }

        private static void tranToBigEndian(byte[] bytes)
        {
            if (BitConverter.IsLittleEndian)
                Array.Reverse(bytes);
        }
    }
}
