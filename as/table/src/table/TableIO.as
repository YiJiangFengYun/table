/**
 * Created by YiJiangFengYun on 2017/4/17.
 */
package table
{
    import flash.utils.ByteArray;

    public final class TableIO
    {
        private static var m_colAttsHelper:Vector.<Column> = new Vector.<Column>();
        public static function read(byteArray:ByteArray, resultTable:Table = null):Table
        {
            byteArray.position = 0;
            ///1.Parse first table, namely, table attributes.
            var lengthTableBytes:int = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes.
            //Now there are only one attribute of table (name attribute). so table parsing has one row and one column.
            //3 means three bytes storage row and column count of table.
            // and 1 means first one byte of cell bytes storage bytes length of cell value.
            var offsetBytes:int = 3 + 1;
            var tableName:String = CellType.read(CellType.charStr_value,
                                                 byteArray,
                                                 byteArray.position + offsetBytes,
                                                 lengthTableBytes - offsetBytes) as String;

            ///2.Parse second table, namely table column attributes.
            lengthTableBytes = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes.
            var rowCount:int = byteArray.readUnsignedShort(); //get table row count;
            var columnCount:int = byteArray.readUnsignedByte(); //get table column count;
            var columnAttributes:Vector.<Column> = m_colAttsHelper;
            if(columnAttributes.length < columnCount)
            {
                columnAttributes.length = columnCount;
            }
            for(var i:int = 0; i < rowCount; ++i)
            {
                //first column of this table storage column name of target table. its type is char[].
                //get column name
                var lengthColumnBytes:int = byteArray.readUnsignedByte();  //get length of bytes of column value stored in one byte
                var colName:String = CellType.read(CellType.charStr_value,
                                                   byteArray, byteArray.position, lengthColumnBytes) as String;
                //get column type id
                var colTypeId:int = CellType.read(CellType.int_value, byteArray) as int;

                //third column of this table storage column description of target table, its type is unicode string.
                //get column description.
                lengthColumnBytes = byteArray.readUnsignedShort(); //get length of bytes of column value stored in two byte
                if(lengthColumnBytes != 0)
                {
                    var colDescription:String = CellType.read(CellType.unicodeStr_value,
                                                              byteArray,
                                                              byteArray.position,
                                                              lengthColumnBytes) as String;
                }
                else
                {
                    colDescription = null;
                }

                var columnAttribute:Column;
                if(columnAttributes[i] == null)
                {
                    columnAttribute = new Column(colName, colTypeId, colDescription);
                    columnAttributes[i] = columnAttribute;
                }
                else
                {
                    columnAttribute = columnAttributes[i];
                    columnAttribute.set(colName, colTypeId, colDescription);
                }
            }

            ///3.Parse third table, its is real target table.
            lengthTableBytes = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes
            rowCount = byteArray.readUnsignedShort(); //get table row count;
            columnCount = byteArray.readUnsignedByte(); //get table column count;
            if(resultTable == null)
            {
                resultTable = new Table(tableName, rowCount, columnCount, columnAttributes); //create table
            }
            else
            {
                resultTable.set(tableName, rowCount, columnCount, columnAttributes);  //reset table.
            }
            for(i = 0; i < rowCount; ++i)
            {
                for(var j:int = 0; j < columnCount; ++j)
                {
                    columnAttribute = columnAttributes[j];
                    var cell:Cell = resultTable.getCell(i, j);
                    if(cell.typeId == CellType.charStr_value)
                    {
                        var lengthColumnBytes:int = byteArray.readUnsignedByte();  //get length of bytes of column value stored in one byte
                        cell.writeWithByteArray(byteArray, byteArray.position, lengthColumnBytes);
                    }
                    else if(cell.typeId == CellType.unicodeStr_value)
                    {
                        lengthColumnBytes = byteArray.readUnsignedShort(); //get length of bytes of column value stored in two byte
                        cell.writeWithByteArray(byteArray, byteArray.position, lengthColumnBytes);
                    }
                    else
                    {
                        if(cell.typeId != CellType.null_value)
                        {
                            cell.writeWithByteArray(byteArray,
                                                    byteArray.position,
                                                    CellType.typeByteLengths[cell.typeId]);
                        }
                    }
                }
            }

            return resultTable;
        }

//        public static function write(table:Table, resultByteArray:ByteArray = null):ByteArray
//        {
//            if(resultByteArray == null)resultByteArray = new ByteArray();
//            var rowCount:int = table.rowCount;
//            var colCount:int = table.colCount;
//            resultByteArray.position = 0;
//
//            var byteArrayHelper:ByteArray = new ByteArray(); //use to calculate length of bytes of table.
//            ///1.Write first table, namely, table attributes.
//            var tableName:String = table.name;
//            //Now there are only one attribute of table (name attribute). so table parsing has one row and one column.
//            //4 means four bytes storage table total length of bytes.
//            ////and 3 means four bytes storage row and column count of table.
//            // and 1 means first one byte of cell bytes storage bytes length of cell value.
//            var lengthTableBytes:int = 4 + 3 + 1 + tableName.length;
//            resultByteArray.writeUnsignedInt(lengthTableBytes); //table total length of bytes to first 4 bytes.
//            resultByteArray.writeShort(1); // table row count.
//            resultByteArray.writeByte(1);  //table column count.
//            CellType.write(CellType.charStr_value, tableName, resultByteArray, resultByteArray.position);
//
//            ///2.Write second table, namely table column attributes.
//            byteArrayHelper.clear();
//            byteArrayHelper.position = 0;
//        }
    }
}
