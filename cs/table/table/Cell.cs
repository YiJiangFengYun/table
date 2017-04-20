using System;
using System.Collections.Generic;

namespace table
{
    public class Cell : IDisposable
    {
        private CellType.TypeId typeId;
        private byte[] content;

        public Cell(CellType.TypeId typeId = 0)
        {
            this.typeId = typeId;
        }

        public virtual void Dispose()
        {
            content = null;
        }

        public CellType.TypeId TypeId
        {
            get
            {
                return typeId;
            }
        }

        internal void SetTypeId(CellType.TypeId value) { typeId = value; }

        public void CopyFrom(Cell src)
        {
            typeId = src.typeId;
            content = src.content.Clone() as byte[];
        }

        public Cell Clone()
        {
            var clone = new Cell();
            clone.CopyFrom(this);
            return clone;
        }

        public object GetValue()
        {
            return Read();
        }

        public void SetValue(object value)
        {
            Write(value);
        }

        public object Read()
        {
            return CellIO.Read(typeId, content);
        }

        public void Write(object value)
        {
            content = CellIO.Write(typeId, value);
        }

        public void WriteWithByteArray(byte[] value, uint offset, uint length)
        {
            if (length == 0) length = (uint)value.Length;
            content = new byte[length];
            for (var i = 0; i < length; ++i)
            {
                content[i] = value[(int)offset + i];
            }
        }
    }
}
