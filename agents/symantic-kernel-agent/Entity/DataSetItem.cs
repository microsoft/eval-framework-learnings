using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace AI_Agent_SemanticKernel.Entity
{
    public class DataSetItem
    {
        [JsonPropertyName("id")]    
        public int Id { get; set; }

        [JsonPropertyName("question")]
        public string Question { get; set; }

        [JsonPropertyName("actualAnswer")]
        public string ActualAnswer { get; set; }

        [JsonPropertyName("expectedAnswer")]
        public string ExpectedAnswer { get; set; }

    }
}
