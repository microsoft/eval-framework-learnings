import os
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    IntentResolutionEvaluator,
    ToolCallAccuracyEvaluator,
    TaskAdherenceEvaluator,
)

class AgentEval:
    def __init__(self, model_config: AzureOpenAIModelConfiguration = None):
        if model_config is None:
            model_config = AzureOpenAIModelConfiguration(
                azure_endpoint=os.environ["AZURE_ENDPOINT"],
                api_key=os.environ.get("AZURE_API_KEY"),
                azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
                api_version=os.environ.get("AZURE_API_VERSION"),
            )
        self.intent_resolution = IntentResolutionEvaluator(model_config=model_config, threshold=3)
        self.tool_call_accuracy = ToolCallAccuracyEvaluator(model_config=model_config, threshold=3)
        self.task_adherence = TaskAdherenceEvaluator(model_config=model_config, threshold=3)

    def evaluate(self, query: str, response: str, tool_calls=None, tool_definitions=None) -> dict:
        result = {}
        # Intent Resolution
        result["intent_resolution"] = self.intent_resolution(query=query, response=response)
        # Tool Call Accuracy (only if tool_calls and tool_definitions are provided)
        if tool_calls and tool_definitions:
            result["tool_call_accuracy"] = self.tool_call_accuracy(
                query=query,
                tool_calls=tool_calls,
                tool_definitions=tool_definitions
            )
        # Task Adherence
        result["task_adherence"] = self.task_adherence(query=query, response=response)
        print("Agent evaluation:", result)
        return result

    def evaluate_batch(self, data: list) -> list:
        results = []
        for item in data:
            query = item.get("question", "")
            response = item.get("actualAnswer", "")
            tool_calls = item.get("tool_calls")
            tool_definitions = item.get("tool_definitions")
            eval_result = self.evaluate(query, response, tool_calls, tool_definitions)
            results.append({**item, "agent_eval": eval_result})
        return results
