using Microsoft.SemanticKernel;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace AI_Agent_SemanticKernel.Plugins
{
    internal class SearchMovieOnInternet
    {

        [KernelFunction("SearchMovieInfo_OnInternet")]
        [Description("Search for a movie by title or any query about movies on Internet")]
        public async Task<string> SearchMovieDetails(string query)
        {
            string url = $"https://api.duckduckgo.com/?q={Uri.EscapeDataString(query)}&format=json&no_redirect=1&no_html=1";
            using var http = new HttpClient();
            try
            {
                var response = await http.GetStringAsync(url);
                using var doc = JsonDocument.Parse(response);
                if (doc.RootElement.TryGetProperty("AbstractText", out var abs) && !string.IsNullOrWhiteSpace(abs.GetString()))
                {
                    return abs.GetString()!;
                }
                else if (doc.RootElement.TryGetProperty("RelatedTopics", out var rel) && rel.ValueKind == JsonValueKind.Array && rel.GetArrayLength() > 0)
                {
                    var first = rel[0];
                    if (first.TryGetProperty("Text", out var text))
                        return text.GetString() ?? "No relevant web result found.";
                }
                return "No relevant web result found.";
            }
            catch
            {
                return "Error retrieving web search result.";
            }
        }
    }
}
