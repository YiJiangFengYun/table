using System;
using System.Collections.Generic;

namespace table
{
    public class Table : IDisposable
    {
        private string name;
        private List<Column> colAttributes;
        private List<List<Cell>> data;
        private uint rowCount;
        private uint colCount;

        public Table(string name, uint rowCount, uint colCount, List<Column> colAttributes)
        {
            Set(name, rowCount, colCount, colAttributes);
        }

        public void Dispose()
        {
            colAttributes.Clear();
            colAttributes = null;
            data.Clear();
            data = null;
        }

        internal void Set(string name, uint rowCount, uint colCount, List<Column> colAttributes)
        {
            this.name = name;
            this.rowCount = rowCount;
            this.colCount = colCount;
            int i;
            int j;
            List<Column> myColAtts = this.colAttributes;
            if(myColAtts == null)
            {
                this.colAttributes = myColAtts = new List<Column>((int)colCount);
            }
            else if(myColAtts.Capacity < colCount)
            {
                myColAtts.Capacity = (int)colCount;
            }
            for(i = 0; i < colCount; ++i)
            {
                if(myColAtts.Count <= i)
                {
                    myColAtts.Add(colAttributes[i].Clone());
                }
                else
                {
                    myColAtts[i].CopyFrom(colAttributes[i]);
                }
            }

            var data = this.data;
            if(data == null)
            {
                this.data = data = new List<List<Cell>>((int)rowCount);
            }
            else if(data.Capacity < rowCount)
            {
                data.Capacity = (int)rowCount;
            }
            for(i = 0; i < rowCount; ++i)
            {
                if(data.Count <= i)
                {
                    data.Add(new List<Cell>((int)colCount));
                }
                else if(data[i].Capacity < colCount)
                {
                    data[i].Capacity = (int)colCount;
                }
                for(j = 0; j < colCount; ++j)
                {
                    if(data[i].Count <= j)
                    {
                        data[i].Add(new Cell(myColAtts[j].TypeId));
                    }
                    else
                    {
                        data[i][j].SetTypeId(myColAtts[j].TypeId);
                    }
                }
            }
        }

        public string Name
        {
            get { return this.name; }
            set { this.name = value; }
        }

        public Column getColAttribute(uint col)
        {
            return this.colAttributes[(int)col];
        }

        /// <summary>
        /// Get a cell of the table.
        /// </summary>
        public Cell GetCell(uint row, uint col)
        {
            return this.data[(int)row][(int)col];
        }

        /// <summary>
        /// Set (Update) a cell of the table
        /// </summary>
        public void SetCell(uint row, uint col, object value)
        {
            this.data[(int)row][(int)col].Write(value);
        }

        public void SetCellWithByteArray(uint row, uint col, byte[] byteArray, uint offset = 0, uint length = 0)
        {
            this.data[(int)row][(int)col].WriteWithByteArray(byteArray, offset, length);
        }

        public uint RowCount
        {
            get { return this.rowCount; }
        }

        public uint ColCount
        {
            get { return this.colCount; }
        }
    }
}
