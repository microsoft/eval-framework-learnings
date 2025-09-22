import os
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    RetrievalEvaluator,
    DocumentRetrievalEvaluator,
    GroundednessEvaluator,
    GroundednessProEvaluator,
    RelevanceEvaluator,
    ResponseCompletenessEvaluator,
)

class RAGEval:
    def __init__(self, model_config: AzureOpenAIModelConfiguration = None, azure_ai_project: dict = None):
        if model_config is None:
            model_config = AzureOpenAIModelConfiguration(
                azure_endpoint=os.environ["AZURE_ENDPOINT"],
                api_key=os.environ.get("AZURE_API_KEY"),
                azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
                api_version=os.environ.get("AZURE_API_VERSION"),
            )
        self.retrieval = RetrievalEvaluator(model_config=model_config, threshold=3)
        self.groundedness = GroundednessEvaluator(model_config=model_config, threshold=3)
        self.relevance = RelevanceEvaluator(model_config=model_config, threshold=3)
        self.response_completeness = ResponseCompletenessEvaluator(model_config=model_config, threshold=3)
        self.document_retrieval = None
        self.groundedness_pro = None
        if azure_ai_project:
            self.document_retrieval = DocumentRetrievalEvaluator(azure_ai_project=azure_ai_project)
            self.groundedness_pro = GroundednessProEvaluator(azure_ai_project=azure_ai_project)

    def evaluate_retrieval(self, query: str, context: str) -> dict:
        result = self.retrieval(query=query, context=context)
        print("RetrievalEvaluator result:", result)
        return result

    def evaluate_groundedness(self, query: str, context: str, response: str) -> dict:
        result = self.groundedness(query=query, context=context, response=response)
        print("GroundednessEvaluator result:", result)
        return result

    def evaluate_relevance(self, query: str, response: str) -> dict:
        result = self.relevance(query=query, response=response)
        print("RelevanceEvaluator result:", result)
        return result

    def evaluate_response_completeness(self, response: str, ground_truth: str) -> dict:
        result = self.response_completeness(response=response, ground_truth=ground_truth)
        print("ResponseCompletenessEvaluator result:", result)
        return result

    def evaluate_document_retrieval(self, retrieval_ground_truth: list, retrieved_documents: list, ground_truth_label_min: int, ground_truth_label_max: int) -> dict:
        if not self.document_retrieval:
            raise ValueError("DocumentRetrievalEvaluator requires azure_ai_project config.")
        result = self.document_retrieval(
            retrieval_ground_truth=retrieval_ground_truth,
            retrieved_documents=retrieved_documents,
            ground_truth_label_min=ground_truth_label_min,
            ground_truth_label_max=ground_truth_label_max
        )
        print("DocumentRetrievalEvaluator result:", result)
        return result

    def evaluate_groundedness_pro(self, query: str, context: str, response: str) -> dict:
        if not self.groundedness_pro:
            raise ValueError("GroundednessProEvaluator requires azure_ai_project config.")
        result = self.groundedness_pro(query=query, context=context, response=response)
        print("GroundednessProEvaluator result:", result)
        return result