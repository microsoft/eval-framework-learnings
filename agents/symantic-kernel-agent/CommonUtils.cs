using AI_Agent_SemanticKernel.Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace AI_Agent_SemanticKernel
{
    public class CommonUtils
    {

        public static async Task<IList<DataSetItem>> ReadFromJsonFile(string jsonFile)
        {
            string jsonString = File.ReadAllText(jsonFile);
            IList<DataSetItem> data = JsonSerializer.Deserialize<IList<DataSetItem>>(jsonString);
            return data;

        }

        public static async Task WriteToFile(IList<DataSetItem> items, string outputFileName)
        {
            string jsonString = JsonSerializer.Serialize(items, new JsonSerializerOptions { WriteIndented = true }); // WriteIndented for pretty-printing
            File.WriteAllText(outputFileName, jsonString);
        }
    }
}
