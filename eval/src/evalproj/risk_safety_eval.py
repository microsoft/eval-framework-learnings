import os
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation import (
    HateUnfairnessEvaluator,
    SexualEvaluator,
    ViolenceEvaluator,
    SelfHarmEvaluator,
    ContentSafetyEvaluator,
)

class RiskSafetyEval:
    def __init__(self, azure_ai_project: dict = None):
        self.credential = DefaultAzureCredential()
        if azure_ai_project is None:
            # azure_ai_project = {
            #     "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
            #     "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
            #     "project_name": os.environ.get("AZURE_PROJECT_NAME"),
            # }
            azure_ai_project = os.environ.get("AZURE_PROJECT_URL") 
        print("[RiskSafetyEval] Using azure_ai_project config:", azure_ai_project)
        try:
            self.hate = HateUnfairnessEvaluator(azure_ai_project=azure_ai_project, credential=self.credential, threshold=3)
            self.sexual = SexualEvaluator(azure_ai_project=azure_ai_project, credential=self.credential, threshold=3)
            self.violence = ViolenceEvaluator(azure_ai_project=azure_ai_project, credential=self.credential, threshold=3)
            self.self_harm = SelfHarmEvaluator(azure_ai_project=azure_ai_project, credential=self.credential, threshold=3)
            self.composite = ContentSafetyEvaluator(azure_ai_project=azure_ai_project, credential=self.credential, threshold=3)
        except Exception as e:
            print("[RiskSafetyEval] ERROR initializing evaluators:", e)
            raise

    def evaluate(self, query: str, response: str) -> dict:
        result = {}
        result["hate_unfairness"] = self.hate(query=query, response=response)
        result["sexual"] = self.sexual(query=query, response=response)
        result["violence"] = self.violence(query=query, response=response)
        result["self_harm"] = self.self_harm(query=query, response=response)
        result["composite"] = self.composite(query=query, response=response)
        print("Risk/Safety evaluation:", result)
        return result

    def evaluate_batch(self, data: list) -> list:
        results = []
        for item in data:
            query = item.get("question", "")
            response = item.get("actualAnswer", "")
            eval_result = self.evaluate(query, response)
            results.append({**item, "risk_safety": eval_result})
        return results