/**
 * Created by YiJiangFengYun on 2017/4/16.
 */
package table
{
    import flash.utils.ByteArray;

    public class Table
    {
        private var m_name:String;
        private var m_colAttributes:Vector.<Column>;
        private var m_data:Vector.<Vector.<Cell>>;
        private var m_rowCount:uint;
        private var m_colCount:uint;

        public function Table(name:String,
                              rowCount:uint,
                              colCount:uint,
                              colAttributes:Vector.<Column>)
        {

        }

        internal function set(name:String,
                              rowCount:uint,
                              colCount:uint,
                              colAttributes:Vector.<Column>):void
        {
            m_name = name;
            m_rowCount = rowCount;
            m_colCount = colCount;
            var i:int;
            var j:int;
            var myColAttrs:Vector.<Column> = m_colAttributes;
            if(myColAttrs == null)
            {
                m_colAttributes = myColAttrs = new Vector.<Column>(colCount);
                myColAttrs.fixed = true;
            }
            else if(myColAttrs.length < colCount)
            {
                myColAttrs.fixed = false;
                myColAttrs.length = colCount;
                myColAttrs.fixed = true;
            }
            for(i = 0; i < colCount; ++i)
            {
                if(myColAttrs[i] == null)
                {
                    myColAttrs[i] = colAttributes[i].clone();
                }
                else
                {
                    myColAttrs[i].copyFrom(colAttributes[i]);
                }
            }

            var data:Vector.<Vector.<Cell>> = m_data;
            if(data == null)
            {
                m_data = data = new Vector.<Vector.<Cell>>(rowCount);
                data.fixed = true;
            }
            else if(data.length < rowCount)
            {
                data.fixed = false;
                data.length = rowCount;
                data.fixed = true;
            }
            m_data = data;
            for(i = 0; i < rowCount; ++i)
            {
                if(data[i] == null)
                {
                    data[i] = new Vector.<Cell>(colCount);
                    data[i].fixed = true;
                }
                else if(data[i].length < colCount)
                {
                    data[i].fixed = false;
                    data[i].length = colCount;
                    data[i].fixed = true;
                }
                for(j = 0; j < colCount; ++j)
                {
                    if(data[i][j] == null)
                    {
                        data[i][j] = new Cell(myColAttrs[j].typeId);
                    }
                    else
                    {
                        data[i][j].setTypeId(myColAttrs[j].typeId);
                    }
                }
            }
        }

        public function get name():String { return m_name; }
        public function set name(value:String):void { m_name = value; }

        public function getColAttribute(col:int):Column { return m_colAttributes[col]; }

        /**
         * Get a cell of the table.
         */
        public function getCell(row:uint, col:uint):Cell
        {
            return m_data[row][col];
        }

        /**
         * Set (Update) a cell of the table
         */
        public function setCell(row:uint, col:uint, value:Object):void
        {
            m_data[row][col].write(value);
        }

        /**
         * Set (Update) a cell of the table with ByteArray
         */
        public function setCellWithByteArray(row:uint, col:uint,
                                             byteArray:ByteArray, offset:uint = 0, length:int = 0):void
        {
            m_data[row][col].writeWithByteArray(byteArray, offset, length);
        }

        public function get rowCount():uint { return m_rowCount; }
        public function get colCount():uint { return m_colCount; }
    }
}
