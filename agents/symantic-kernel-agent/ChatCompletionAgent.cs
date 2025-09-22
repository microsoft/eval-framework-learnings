//using Microsoft.SemanticKernel;
//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace AI_Agent_SemanticKernel
//{
//    public class MoveChatCompletionAgent
//    {

//        public ChatCompletionAgent CreateAgent(Kernel kernel, string credential)
//        {
//            var builder = Kernel.CreateBuilder();
//            builder.AddAzureOpenAIChatCompletion(
//                deploymentName: deploymentName,
//                apiKey: credential,
//                endpoint: endpoint,
//                modelId: model
//            );
//            var chatKernel = builder.Build();
//            // Register the movie info tool as a kernel plugin
//            chatKernel.ImportPluginFromObject(new ApiMovieSearchPlugin(), "movie");
//            // Register the internet search skill as a kernel plugin
//            chatKernel.ImportPluginFromObject(new InternetSearchPlugin(), "search");
//            var agent = ChatCompletionAgent.Create(chatKernel);
//            return agent;
//        }
//    }
//}
