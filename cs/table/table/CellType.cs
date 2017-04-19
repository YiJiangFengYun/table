using System;

namespace table
{
    public class CellType
    {
        public enum TypeId
        {
            null_value,
            bool_value,
            int_value,
            float_value,
            double_value,
            charStr_value,
            unicodeStr_value,
            typeCount
        }

        public static readonly string[] typeNames = {"null", "bool", "int", "float", "double", "char[]", "string" };
        public static readonly int[] typeByteLengths = {0, 1, 4, 4, 8, -1, -1 };
        public static string getTypeName(int id)
        {
            return typeNames[id];
        }

        /**
         * get number of bytes for specified type.
         * if return -1, means its number of type is unkown in CellType, 
         * in other words, its number of bytes is variational.
         */
        public static int getTypeByteLength(int id)
        {
            return typeByteLengths[id];
        }
    }
}
