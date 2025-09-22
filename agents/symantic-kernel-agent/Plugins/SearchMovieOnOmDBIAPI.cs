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
    public class SearchMovieOnOmDBIAPI
    {

        [KernelFunction("SearchMovieByTitle_OMDB")]
        [Description("Search for a movie by title  on omdb api")]
        public async Task<string> SearchMovieByTitle(string movieTitle)
        {
            string omdbApiKey = "f042f260"; // Get a free key from http://www.omdbapi.com/apikey.aspx
            string url = $"http://www.omdbapi.com/?apikey={omdbApiKey}&t={Uri.EscapeDataString(movieTitle)}";
            using var http = new HttpClient();
            try
            {
                var response = await http.GetStringAsync(url);
                using var doc = JsonDocument.Parse(response);
                if (doc.RootElement.TryGetProperty("Response", out var resp) && resp.GetString() == "True")
                {
                    return doc.RootElement.ToString();
                }
                else
                {
                    return "No movie information found.";
                }
            }
            catch
            {
                return "Error retrieving movie information.";
            }
        }
    }
}
