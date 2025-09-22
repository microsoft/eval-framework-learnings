using AI_Agent_SemanticKernel.Plugins;
using Azure;
using Azure.AI.Agents.Persistent;
using Azure.AI.OpenAI;
using Azure.Core;
using Azure.Identity;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using Microsoft.SemanticKernel.Agents.AzureAI;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using OpenAI.Chat;
using System;
using System.ClientModel;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace AI_Agent_SemanticKernel.Agents
{
    public class AzureAIMovieAgent
    {

        const string AgentDescription = "An AI Movie Information Agent that helps users find accurate details about movies by title. It first searches the OMDB API for verified movie information, and if the required details are not available, it performs an internet search using DuckDuckGo. The agent always prioritizes trusted sources, avoids speculation, and responds with ‘Result not found’ if no relevant information is available.";

        const string AngentInstructions = @"You are movie information agent and can be used to search and know about any movie. Please follow these instructions: 
1. **Primary Source – OMDB API (SearchMovieByTitle_OMDB)**

   * Whenever you receive a question about a movie, first attempt to find the answer by searching the movie by its title using the OMDB API.
   * Parse the OMDB response and use only the retrieved details to answer the user’s query.

2. **Fallback Source – Internet Search (SearchMovieInfo_OnInternet)**

   * If the OMDB API does not return results or the retrieved data does not answer the user’s question, then search using the DuckDuckGo plugin (SearchMovieInfo_OnInternet).
   * Use the search results to answer the user’s query.

3. **Answering Rules**

   * Always prioritize OMDB API results over internet search.
   * Do not mix fabricated or assumed information with results.
   * If neither OMDB nor DuckDuckGo search provides relevant information, respond with:
     **“Result not found.”**

4. **Behavioral Guidelines**

   * Be precise and factual, based only on the retrieved results.
   * Do not hallucinate or speculate.
   * If partial information is available, clearly state what was found and what could not be determined.
";


        public async Task<ChatCompletionAgent> CreateAgentAsync(string modelDeployment, string azureOpenAIEndPoint, string apiKey)
        {


            // Initialize a semantic kernel
            AzureOpenAIClient azureClient = new(new Uri(azureOpenAIEndPoint), new AzureKeyCredential(apiKey));


            ChatClient chatClient = azureClient.GetChatClient(modelDeployment);


            var kernel = Kernel.CreateBuilder()
                .AddAzureOpenAIChatCompletion(modelDeployment, azureClient)
                .Build();
            // Add the tasks CRUD plugin
            kernel.Plugins.AddFromType<SearchMovieOnInternet>();
            kernel.Plugins.AddFromType<SearchMovieOnOmDBIAPI>();


            // Create a chat completion agent
            var agent = new ChatCompletionAgent
            {
                Name = "MovieAgent",
                Instructions = AngentInstructions,
                Description = AgentDescription,
                Kernel = kernel,
                Arguments = new KernelArguments(new OpenAIPromptExecutionSettings()
                {
                    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
                })
            };

            return agent;
        }

        //public async Task<AzureAIAgent> CreateAgentAsync(string tenantId, string apiKey, string endPoint, string clientId)
        //{
        //    // Implementation for creating the Azure AI Movie Agent

        //    KernelPlugin searchMoviesOnInternet = KernelPluginFactory.CreateFromType<SearchMovieOnInternet>();

        //    KernelPlugin searchMoviesOnOMDBAPI = KernelPluginFactory.CreateFromType<SearchMovieOnOmDBIAPI>();

        //    AzureOpenAIClient azureClient = new(new Uri(endPoint), new DefaultAzureCredential());


        //    PersistentAgentsClient agentsClient = AzureAIAgent.CreateAgentsClient(endPoint, new DefaultAzureCredential());

        //    PersistentAgent definition = await agentsClient.Administration.CreateAgentAsync(
        //           "gpt-4.1-mini",
        //            name: "MovieAgent",
        //            description: AgentDescription,
        //            instructions: AngentInstructions);

        //    AzureAIAgent agent = new(definition, agentsClient, plugins: [searchMoviesOnInternet, searchMoviesOnOMDBAPI]);
        //    return agent; 
        //}
    }
}

