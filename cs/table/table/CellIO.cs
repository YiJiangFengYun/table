using System;

namespace table
{
    public static class CellIO
    {
        /// <summary>
        /// Read value of specified type id from byte array.
        /// </summary>
        /// <param name="id">Type id</param>
        /// <param name="byteArray">Origin binary data</param>
        /// <param name="startPos">Start pos of byteArray for reading</param>
        /// <param name="length">The number of bytes used when the type is string.</param>
        /// <returns>Value of specified type</returns>
        public static object read(CellType.TypeId id, byte[] byteArray, uint startPos = 0, uint length = 0)
        {
            switch (id)
            {
                case CellType.TypeId.Null_Value:
                    {
                        return null;
                    }
                case CellType.TypeId.Bool_Value:
                    {
                        byte usedByte = byteArray[startPos];
                        return Convert.ToBoolean(usedByte);
                    }
                case CellType.TypeId.Int_Value:
                case CellType.TypeId.Float_Value:
                case CellType.TypeId.Double_Value:
                    {
                        int byteCount = CellType.TypeByteLengths[(int)id];
                        byte[] usedBytes = new byte[byteCount];
                        for (int i = 0; i < byteCount; ++i)
                        {
                            usedBytes[i] = byteArray[startPos + i];
                        }
                        if (BitConverter.IsLittleEndian)
                        {
                            Array.Reverse(usedBytes); //because binary protocol use BigEndian.
                        }
                        switch (id)
                        {
                            case CellType.TypeId.Int_Value:
                                {
                                    return BitConverter.ToInt32(usedBytes, 0);
                                }
                            case CellType.TypeId.Float_Value:
                                {
                                    return BitConverter.ToSingle(usedBytes, 0);
                                }
                            case CellType.TypeId.Double_Value:
                                {
                                    return BitConverter.ToDouble(usedBytes, 0);
                                }
                        }

                        break;
                    }
                case CellType.TypeId.CharStr_Value:
                    {
                        return System.Text.Encoding.ASCII.GetString(byteArray, (int)startPos, (int)length);
                    }
                case CellType.TypeId.UnicodeStr_Value:
                    {
                        return System.Text.Encoding.UTF8.GetString(byteArray, (int)startPos, (int)length);
                    }
                default:
                    {
                        throw new ArgumentException("Invalid type id argument when write value to ByteArray.");
                    }
            }
            return null;
        }

        /// <summary>
        /// Write value of specified type id to byteArray
        /// </summary>
        /// <param name="id">Type id</param>
        /// <param name="value">Type value</param>
        /// <param name="result">Target binary data</param>
        /// <param name="startPos">Start pos of byteArray for writing</param>
        /// <returns>Result byte stream.</returns>
        public static byte[] write(CellType.TypeId id, object value)
        {
            switch(id)
            {
                case CellType.TypeId.Null_Value:
                    {
                        return new byte[]{};
                    }
                case CellType.TypeId.Bool_Value:
                    {
                        return BitConverter.GetBytes((bool)value);
                    }
                case CellType.TypeId.Int_Value:
                case CellType.TypeId.Float_Value:
                case CellType.TypeId.Double_Value:
                    {
                        byte[] result;
                        switch(id)
                        {
                            case CellType.TypeId.Int_Value:
                                {
                                    result = BitConverter.GetBytes((int)value);
                                    break;
                                }
                            case CellType.TypeId.Float_Value:
                                {
                                    result = BitConverter.GetBytes((float)value);
                                    break;
                                }
                            case CellType.TypeId.Double_Value:
                                {
                                    result = BitConverter.GetBytes((double)value);
                                    break;
                                }
                            default:
                                result = new byte[] { };
                                break;

                        }
                        if (BitConverter.IsLittleEndian)
                        {
                            Array.Reverse(result); //because binary protocol use BigEndian.
                        }
                        return result;
                    }
                case CellType.TypeId.CharStr_Value:
                    {
                        return System.Text.Encoding.ASCII.GetBytes((string)value);
                    }
                case CellType.TypeId.UnicodeStr_Value:
                    {
                        return System.Text.Encoding.UTF8.GetBytes((string)value);
                    }
                default:
                    {
                        throw new ArgumentException("Invalid type id argument when write value to ByteArray.");
                    }
            }
        }
    }
}
