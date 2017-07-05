using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using Excel = Microsoft.Office.Interop.Excel;


namespace excel_load
{
    public enum TableType
    {
        TABLE_ATTR,
        COL_ATTRS,
        TABLE,
        ENUM_COUNT
    }

    public static class ExcelToBinary
    {
        public static List<List<List<object>>> Parse(string excelFilePath)
        {
            var excelApp = new Excel.Application();
            var excelWorkbooks = excelApp.Workbooks;
            excelApp.Visible = false;
            Excel.Workbook excelWorkBook;
            try
            {
                excelWorkBook = excelWorkbooks.Open(excelFilePath);
            }
            catch (Exception e)
            {
                excelWorkbooks.Close();
                excelApp.Quit();
                Marshal.ReleaseComObject(excelWorkbooks);
                Marshal.ReleaseComObject(excelApp);
                throw e;
            }
            var sheets = excelWorkBook.Sheets;
            const int sheetCount = (int)TableType.ENUM_COUNT;
            Console.WriteLine("excel sheet count: " + sheets.Count);
            if (sheets.Count < sheetCount)
            {
                excelWorkBook.Close();
                excelWorkbooks.Close();
                excelApp.Quit();

                Marshal.ReleaseComObject(sheets);
                Marshal.ReleaseComObject(excelWorkBook);
                Marshal.ReleaseComObject(excelWorkbooks);
                Marshal.ReleaseComObject(excelApp);
                throw new Exception("Count of Excel Sheets is less than " + sheetCount + ".");
            }

            List<List<List<object>>> tables = new List<List<List<object>>>();
            List<int> rowCounts = new List<int>();
            List<int> colCounts = new List<int>();
            for (int i = 1; i <= sheetCount; ++i)
            {
                Excel.Worksheet sheet = sheets[i];
                var table = new List<List<object>>();
                tables.Add(table);
                var usedRange = sheet.UsedRange;
                var rows = usedRange.Rows;
                var columns = usedRange.Columns;
                int rowCount = rows.Count;
                int colCount = columns.Count;
                rowCounts.Add(rowCount - 1); //first row is not useful.
                colCounts.Add(colCount);
                table.Capacity = rowCount - 1;//first row is not useful.
                int rowIndex;
                int colIndex;
                for (rowIndex = 2; rowIndex <= rowCount; ++rowIndex)
                {
                    List<object> row = new List<object>();
                    table.Add(row);
                    row.Capacity = colCount;
                    for (colIndex = 1; colIndex <= colCount; ++colIndex)
                    {
                        var item = usedRange[rowIndex, colIndex];
                        row.Add(item.Value);
                        Marshal.ReleaseComObject(item);
                    }
                }

                Marshal.ReleaseComObject(rows);
                Marshal.ReleaseComObject(columns);
                Marshal.ReleaseComObject(usedRange);
                Marshal.ReleaseComObject(sheet);
            }

            //close excel app
            excelWorkBook.Close();
            excelWorkbooks.Close();
            excelApp.Quit();

            Marshal.ReleaseComObject(sheets);
            Marshal.ReleaseComObject(excelWorkBook);
            Marshal.ReleaseComObject(excelWorkbooks);
            Marshal.ReleaseComObject(excelApp);

            return tables;
        }
    }
}
