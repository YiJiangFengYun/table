using System;

namespace table
{
    public class Column : IDisposable
    {
        private string name;
        private CellType.TypeId typeId;
        private string description;

        public Column(string name = null, CellType.TypeId typeId = 0, string description = null)
        {
            this.name = name;
            this.typeId = typeId;
            this.description = description;
        }

        public void Dispose()
        {

        }

        public void Set(string name, CellType.TypeId typeId, string description)
        {
            this.name = name;
            this.typeId = typeId;
            this.description = description;
        }

        public void CopyFrom(Column src)
        {
            this.name = src.name;
            this.typeId = src.typeId;
            this.description = src.description;
        }

        public Column Clone()
        {
            var clone = new Column();
            clone.CopyFrom(this);
            return clone;
        }

        public string Name
        {
            get { return this.name; }
        }

        public CellType.TypeId TypeId
        {
            get { return this.typeId; }
        }

        public string Description
        {
            get { return this.description; }
        }

    }
}
