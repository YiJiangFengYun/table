/**
 * Created by YiJiangFengYun on 2017/4/16.
 */
package table
{
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
    }
}
