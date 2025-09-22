# AI Agent with Semantic Kernel

This is a C# console application project template for building an AI agent using Microsoft Semantic Kernel.

## Prerequisites
- [.NET 8.0 SDK](https://dotnet.microsoft.com/download)
- Internet connection to restore NuGet packages

## Setup Instructions

1. **Restore dependencies:**
   ```pwsh
   dotnet restore
   ```
2. Update AppConfig.cs with your Azure OpenAI credentials:
   ```csharp
   public const string AzureAI_APIKEY = "<your_api_key>";
   public const string AzureAI_EndPoint = "<your_endpoint>";
   public const string AzureAI_DeploymentName = "<your_deployment_name>";
   ```
3. **Build the project:**
   ```pwsh
   dotnet build
   ```
4. **Run the project:**
   ```pwsh
   dotnet run
   ```

## Project Structure
- `Program.cs`: Entry point with example Semantic Kernel usage
- `AI_Agent_SemanticKernel.csproj`: Project file with dependencies

## Example Usage
The default code demonstrates initializing Semantic Kernel and running a simple prompt.

---

Replace the example code with your own agent logic as needed.
