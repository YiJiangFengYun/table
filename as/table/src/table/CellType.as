/**
 * Created by YiJiangFengYun on 2017/4/16.
 */
package table
{
    import flash.utils.ByteArray;

    public final class CellType
    {
        public static const null_value:int = 0;
        public static const bool_value:int = 1;
        public static const int_value:int = 2;
        public static const float_value:int = 3;
        public static const double_value:int = 4;
        public static const charStr_value:int = 5;
        public static const unicodeStr_value:int = 6;
        public static const typeCount:int = 7;

        public static const typeNames:Vector.<String> = new <String>["null",
                                                                     "bool",
                                                                     "int",
                                                                     "float",
                                                                     "double",
                                                                     "char[]",
                                                                     "string"];
        public static const typeByteLengths:Vector.<int> = new <int>[0, 1, 4, 4, 8, -1, -1];
        public static function getTypeName(id:int):String { return typeNames[id]; }

        /**
         * get number of bytes for specified type.
         * if return -1, means its number of type is unkown in CellType, in other words, its number of bytes is variational.
         */
        public static function getTypeByteLength(id:int):int { return typeByteLengths[id]; }

        /**
         * read value of specified type id from byteArray
         * @param id           type id
         * @param byteArray    origin binary data
         * @param startPos     start pos of byteArray for reading
         * @param length       the number of bytes used when the type is string.
         * @return             value of specified type
         */
        public static function read(id:int, byteArray:ByteArray, startPos:uint = 0, length:uint = 0):Object
        {
            byteArray.position = startPos;
            switch(id)
            {
                case null_value:
                {
                    return null;
                    break;
                }
                case bool_value:
                {
                    return byteArray.readBoolean();
                }
                case int_value:
                {
                    return byteArray.readInt();
                }
                case float_value:
                {
                    return byteArray.readFloat();
                }
                case double_value:
                {
                    return byteArray.readDouble();
                }
                case charStr_value:
                {
                    return byteArray.readMultiByte(length, "us-ascii");
                }
                case unicodeStr_value:
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
         * read value of specified type id to byteArray
         * @param id           type id
         * @param value        type value
         * @param result       target binary data
         * @param startPos     start pos of byteArray for writing
         * @return             result byte stream.
         */
        public static function write(id:int, value:Object, result:ByteArray = null, startPos:int = 0):ByteArray
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

            switch (id)
            {
                case null_value:
                {
                    return null;
                    break;
                }
                case bool_value:
                {
                    result.writeBoolean(value);
                    break;
                }
                case int_value:
                {
                    result.writeInt(value as int);
                    break;
                }
                case float_value:
                {
                    result.writeFloat(value as Number);
                    break;
                }
                case double_value:
                {
                    result.writeDouble(value as Number);
                    break;
                }
                case charStr_value:
                {
                    result.writeMultiByte(value as String, "us-ascii");
                    break;
                }
                case unicodeStr_value:
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
