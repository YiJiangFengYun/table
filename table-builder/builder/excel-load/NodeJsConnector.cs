using System;
using System.IO;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace excel_load
{
    /// <summary>
    /// Excel build conntector used to port interface to nodeJs, so that nodejs call excel build feature
    /// </summary>
    public class NodeJsConnector
    {

        public class Result
        {
            public bool isComplete;
            public string msg;
            public List<List<List<object>>> tables;
        }

        /// <summary>
        /// This interface method called by external nodejs.
        /// External javascript should pass some params to input object.
        /// Param:
        ///    excelPath: excel file path
        ///    outPath: output binary path
        /// </summary>
        /// <param name="input"></param>
        /// <returns></returns>
        public async Task<object> Excecute(dynamic input)
        {
            Result result;
            try
            {
                string excelPath = (string)input.excelPath;
                if (excelPath == null) throw new ArgumentException("Excel path is not specified.");
                //excel path
                if (Path.IsPathRooted(excelPath) == false)
                {
                    excelPath = Path.Combine(Environment.CurrentDirectory, excelPath);
                }

                var tables = ExcelToBinary.Parse(excelPath);

                result = new Result();
                result.isComplete = true;
                result.msg = "excel build success.";
                result.tables = tables;
            }
            catch(Exception e)
            {
                result = new Result();
                result.isComplete = false;
                result.msg = e.Message;
            }
            return result;
        }
    }
}
