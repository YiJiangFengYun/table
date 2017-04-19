/**
 * Created by YiJiangFengYun on 2017/4/19.
 */
package table
{
    import flash.utils.ByteArray;
    import flash.utils.Endian;

    import table.CellType;

    public final class CellIO
    {
        /**
         * Read value of specified type id from byteArray.
         * @param id           type id
         * @param byteArray    origin binary data
         * @param startPos     start pos of byteArray for reading
         * @param length       the number of bytes used when the type is string.
         * @return             value of specified type
         */
        public static function read(id:int, byteArray:ByteArray, startPos:uint = 0, length:uint = 0):Object
        {
            byteArray.endian = Endian.BIG_ENDIAN;
            byteArray.position = startPos;
            switch(id)
            {
                case CellType.null_value:
                {
                    return null;
                    break;
                }
                case CellType.bool_value:
                {
                    return byteArray.readBoolean();
                }
                case CellType.int_value:
                {
                    return byteArray.readInt();
                }
                case CellType.float_value:
                {
                    return byteArray.readFloat();
                }
                case CellType.double_value:
                {
                    return byteArray.readDouble();
                }
                case CellType.charStr_value:
                {
                    return byteArray.readMultiByte(length, "us-ascii");
                }
                case CellType.unicodeStr_value:
                {
                    return byteArray.readMultiByte(length, "us-ascii");
                }
                default:
                {
                    throw new ArgumentError("Invalid type id argument when read value from ByteArray.");
                    break;
                }
            }
        }

        /**
         * Write value of specified type id to byteArray
         * @param id           type id
         * @param value        type value
         * @param result       target binary data
         * @param startPos     start pos of byteArray for writing
         * @return             result byte stream.
         */
        public static function write(id:int, value:Object, result:ByteArray = null, startPos:uint = 0):ByteArray
        {
            if(result == null)
            {
                result = new ByteArray();
                result.position = 0;
            }
            else
            {
                result.position = startPos;
            }
            result.endian = Endian.BIG_ENDIAN;

            switch (id)
            {
                case CellType.null_value:
                {
                    return result;
                    break;
                }
                case CellType.bool_value:
                {
                    result.writeBoolean(value);
                    break;
                }
                case CellType.int_value:
                {
                    result.writeInt(value as int);
                    break;
                }
                case CellType.float_value:
                {
                    result.writeFloat(value as Number);
                    break;
                }
                case CellType.double_value:
                {
                    result.writeDouble(value as Number);
                    break;
                }
                case CellType.charStr_value:
                {
                    result.writeMultiByte(value as String, "us-ascii");
                    break;
                }
                case CellType.unicodeStr_value:
                {
                    result.writeMultiByte(value as String, "us-ascii");
                    break;
                }
                default:
                {
                    throw new ArgumentError("Invalid type id argument when write value to ByteArray.");
                    break;
                }
            }
            return result;
        }
    }
}
