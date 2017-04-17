/**
 * Created by YiJiangFengYun on 2017/4/17.
 */
package table
{
    import flash.utils.ByteArray;

    public final class TableIO
    {
        private static var m_colAttsHelper:Vector.<Column> = new Vector.<Column>();
        public static function createFromBinary(byteArray:ByteArray):void
        {
            byteArray.position = 0;
            ///1.Parse first table, namely, table attributes.
            var lengthTableBytes:int = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes.
            //Now there are only one attribute of table (name attribute). so table parsing has one row and one column.
            //So the bytes of table is the bytes of column.
            var tableName:String = CellType.read(CellType.charStr_value,
                                                 byteArray,
                                                 //1 means first one byte of cell bytes storage bytes length of cell value
                                                 byteArray.position + 1,
                                                 lengthTableBytes - 1) as String;

            ///2.Parse second table, namely table column attributes.
            lengthTableBytes = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes
            var columnAttributes:Vector.<Column> = m_colAttsHelper;
            var columnCount:int = 0;
            while(lengthTableBytes)
            {
                ++columnCount;
                //first column of this table storage column name of target table. its type is char[].
                //get column name
                var lengthColumnBytes:int = byteArray.readUnsignedByte();  //get length of bytes of column value stored in one byte
                lengthTableBytes -= 1;
                var colName:String = CellType.read(CellType.charStr_value,
                                                     byteArray, byteArray.position, lengthColumnBytes) as String;
                lengthTableBytes -= lengthColumnBytes;
                //get column type id
                var colTypeId:int = CellType.read(CellType.int_value, byteArray) as int;
                lengthTableBytes -= CellType.typeByteLengths[CellType.int_value];

                //third column of this table storage column description of target table, its type is unicode string.
                //get column description.
                lengthColumnBytes = byteArray.readUnsignedShort(); //get length of bytes of column value stored in two byte
                lengthTableBytes -= 2;
                if(lengthColumnBytes != 0)
                {
                    var colDescription:String = CellType.read(CellType.unicodeStr_value,
                                                              byteArray,
                                                              byteArray.position,
                                                              lengthColumnBytes) as String;
                    lengthTableBytes -= lengthColumnBytes;
                }
                else
                {
                    colDescription = null;
                }

                var columnAttribute:Column;
                if(columnAttributes.length < columnCount)
                {
                    columnAttributes.length = columnCount;
                    columnAttribute = new Column(colName, colTypeId, colDescription);
                    columnAttributes[columnCount - 1] = columnAttribute;
                }
                else
                {
                    columnAttribute = columnAttributes[columnCount - 1];
                    columnAttribute.set(colName, colTypeId, colDescription);
                }
            }

            ///3.Parse third table, its is real target table.
            lengthTableBytes = byteArray.readUnsignedInt(); //get table total length of bytes from first 4 bytes
            while(lengthTableBytes)
            {
                
            }
        }
    }
}
