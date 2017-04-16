/**
 * Created by YiJiangFengYun on 2017/4/16.
 */
package table
{
    import flash.utils.ByteArray;

    public class Table
    {
        private var m_data:Vector.<Vector.<ByteArray>>;
        private var m_rowCount:int;
        private var m_colCount:int;
        public function Table(rowCount:int, colCount:int)
        {
            if(rowCount < 0)rowCount = 0;
            if(colCount < 0)colCount = 0;
            m_rowCount = rowCount;
            m_colCount = colCount;
            var data:Vector.<Vector.<ByteArray>> = new Vector.<Vector.<ByteArray>>(rowCount);
            m_data = data;
            for(var i:int = 0; i < rowCount; ++i)
            {
                data[i] = new Vector.<ByteArray>(colCount);
                for(var j:int = 0; j < colCount; ++j)
                {
                    data[i][j] = new ByteArray();
                }
            }
        }
    }
}
