import java.io.*;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;



import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Excel_Write {
    public static void main(String[] args)  throws IOException {

    XSSFWorkbook workbook = new XSSFWorkbook();

    XSSFSheet sheet = workbook.createSheet("Employee Data");

    Map<String, Object[]> data = new TreeMap<String, Object[]>();
    data.put("1", new Object[] {"ID", "NAME", "LASTNAME"});
    data.put("2", new Object[] {101, "Ved", "Patel"});
    data.put("3", new Object[] {102, "Milap", "Prajapati"});
    data.put("4", new Object[] {103, "Devansh", "Patel"});
    data.put("5", new Object[] {104, "Keyur", "Patel"});
    

    Set<String> keyset = data.keySet();
    int rownum = 0;
    for (String key : keyset)
    {
    Row row = sheet.createRow(rownum++);
    Object [] objArr = data.get(key);
    int cellnum = 0;
    for (Object obj : objArr)
    {
    Cell cell = row.createCell(cellnum++);
    if(obj instanceof String)
    cell.setCellValue((String)obj);
    else if(obj instanceof Integer)
    cell.setCellValue((Integer)obj);
    }
    }
    try
    {
    //Write the workbook in file system
    FileOutputStream out = new FileOutputStream(new File("excel_demo.xlsx"));
    workbook.write(out);
    out.close();
    System.out.println("excel_demo.xlsx written successfully on disk.");
    }
    catch (Exception e)
    {
    e.printStackTrace();
    }
        
    }
    
}
