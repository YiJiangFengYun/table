/**
 * Created by YiJiangFengYun on 2017/4/17.
 */
package table
{
    public class Column
    {
        private var m_name:String;
        private var m_typeId:int;
        private var m_description:String;
        public function Column(name:String = null, typeId:int = 0, description:String = null)
        {
            m_name = name;
            m_typeId = typeId;
            m_description = description;
        }

        public function set(name:String = null, typeId:int = 0, description:String = null):void
        {
            m_name = name;
            m_typeId = typeId;
            m_description = description;
        }

        public function copyFrom(src:Column):void
        {
            //copy don't copy id, because the different instance has different id to identity.
            //m_id = src.m_id;
            m_name = src.m_name;
            m_typeId = src.m_typeId;
            m_description = src.m_description;
        }

        public function clone():Column
        {
            var clone = new Column();
            clone.copyFrom(this);
            return clone;
        }

        public function get name():String { return m_name; }
        public function get typeId():int { return m_typeId; }
        public function get description():String { return m_description; }
    }
}
