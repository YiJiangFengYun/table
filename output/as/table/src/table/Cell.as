/**
 * Created by YiJiangFengYun on 2017/4/17.
 */
package table
{
    import flash.utils.ByteArray;

    public class Cell
    {
        private var m_typeId:int;
        private var m_content:ByteArray;
        public function Cell(typeId:int = 0)
        {
            m_typeId = typeId;
            m_content = new ByteArray();
        }

        public function dispose():void
        {
            m_content.clear();
            m_content = null;
        }

        public function get typeId():int { return m_typeId; }
        internal function setTypeId(value:int):void { m_typeId = value; }

        public function copyFrom(src:Cell):void
        {
            m_typeId = src.m_typeId;
            m_content.clear();
            m_content.writeBytes(src.m_content);
        }

        public function clone():Cell
        {
            var clone:Cell = new Cell();
            clone.copyFrom(this);
            return clone;
        }

        public function getValue():Object
        {
            return read();
        }

        public function setValue(value:Object):void
        {
            write(value);
        }

        public function read():Object
        {
            return CellIO.read(m_typeId, m_content, 0, m_content.length);
        }

        public function write(value:Object):void
        {
            CellIO.write(m_typeId, value, m_content, 0);
        }

        public function writeWithByteArray(value:ByteArray, offset:uint = 0, length:uint = 0):void
        {
            var content:ByteArray = m_content;
            content.clear();
            content.position = 0;
            value.position = offset;
            if(length === 0)length = value.bytesAvailable;
            content.writeBytes(value, offset, length);
        }
    }
}
