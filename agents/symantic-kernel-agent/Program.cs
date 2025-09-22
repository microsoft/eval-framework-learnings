using AI_Agent_SemanticKernel;
using AI_Agent_SemanticKernel.Agents;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using Microsoft.SemanticKernel.ChatCompletion;

class Program
{
    const string DatasetInputFileName = "SyntheticDataSet.json";
    const string OutputFileName = "SyntheticDataSet_Output.json"; 
    static async Task Main(string[] args)
    {
    
        AzureAIMovieAgent movieAgent = new AzureAIMovieAgent();
        var agent = await movieAgent.CreateAgentAsync(
            modelDeployment: AppConfig.AzureAI_DeploymentName,
            azureOpenAIEndPoint: AppConfig.AzureAI_EndPoint,
            apiKey: AppConfig.AzureAI_APIKEY
        );

        await GetActualResponse(agent);
        

        Console.WriteLine("\n\nProcesing completed. Press ENTER to exit");
        Console.ReadLine();
        
    }

    static async Task GetActualResponse(ChatCompletionAgent agent)
        
    {
        string currentDirectory = Directory.GetCurrentDirectory();
        string filePath = Path.Combine(currentDirectory, DatasetInputFileName);
        var dataItems = await CommonUtils.ReadFromJsonFile(filePath); 
        foreach(var item in dataItems)
        {
            var response = string.Empty; 
            await foreach (var responseItem in agent.InvokeStreamingAsync(new ChatMessageContent(AuthorRole.User, item.Question)))
            {
                var streamingContent = responseItem.Message;
                response += streamingContent; 
            }

            item.ActualAnswer = response;

        }
        await CommonUtils.WriteToFile(dataItems, OutputFileName); 
        

    }

   
}


