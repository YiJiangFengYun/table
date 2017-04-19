using System;

namespace table
{
    public static class CellType
    {
        public enum TypeId
        {
            Null_Value,
            Bool_Value,
            Int_Value,
            Float_Value,
            Double_Value,
            CharStr_Value,
            UnicodeStr_Value,
            TypeCount
        }

        public static readonly string[] TypeNames = {"null", "bool", "int", "float", "double", "char[]", "string" };
        public static readonly int[] TypeByteLengths = {0, 1, 4, 4, 8, -1, -1 };
        public static string GetTypeName(int id)
        {
            return TypeNames[id];
        }

        /// <summary>
        /// Get number of bytes for specified type.
        /// If return -1, means its number of type is unkown in CellType, in other words, its number of bytes is variational.
        /// </summary>
        /// <param name="id"> type id </param>
        /// <returns></returns>
        public static int GetTypeByteLength(int id)
        {
            return TypeByteLengths[id];
        }
    }
}
