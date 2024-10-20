from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.models import LLMOpinionModel
from api.serializers import LLMOpinionModelSerializer

import requests

INSIDE_DOCKER = False
online_models = {'gpt-3', 'gpt4-mini'}


class LLMOpinionModelView(APIView):
    serializer_class = LLMOpinionModelSerializer

    @swagger_auto_schema(
        operation_description='Fetches all historic LLM questions and answers.'
    )
    def get(self, request):
        LLMOpinionValue = LLMOpinionModel.objects.all()

        if LLMOpinionValue:
            model_serializer = self.serializer_class(LLMOpinionValue, many=True)
            return Response(model_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No responses found'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['question', 'model'],
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING),
                'model': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        operation_description='Ask a model a question'
    )
    def post(self, request):
        print(f"Request:{request.data}")
        question = request.data.get('question', None)
        model = request.data.get('model', None)
        host = 'localhost'
        port = '8090'
        endpoint = 'model-response'

        if INSIDE_DOCKER:
            host = 'llm-ai'
        if model in online_models:
            port = '8091'

        url = f"http://{host}:{port}/{endpoint}"
        if model not in online_models:
            response = requests.get(url, params={"prompt": question, "model": model})
        else:
            response = requests.get(url, params={"prompt": question})

        response_json = response.json()

        answer = response_json[0]['generated_text']

        post_data = {
            'question': question,
            'model': model,
            'answer': answer
        }
        print(f"Response:{post_data}")
        serializer = self.serializer_class(data=post_data)
        if serializer.is_valid(raise_exception=True):
            model_used = serializer.save()

            if model_used:
                return Response({'message': f'{answer}'}, status=status.HTTP_200_OK)
        return Response({'message': 'unable answer question'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id'],
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        operation_description='Deletes a LLM question and answer.'
    )
    def delete(self, request):
        model_id = request.data.get('id', None)
        if model_id:
            model = LLMOpinionModel.objects.filter(id=model_id)
            if model:
                model.delete()
                response = {'message': f'Successfully deleted {model_id}'}
                return Response(response, status=status.HTTP_200_OK)
        response = {'message': f'unable to delete {model_id}'}
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id', 'question', 'answer'],
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'question': openapi.Schema(type=openapi.TYPE_STRING),
                'answer': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        operation_description='Updates a LLM question and answer.'
    )
    def put(self, request):
        model_id = request.data.get('id', None)
        question = request.data.get('question', None)
        answer = request.data.get('answer', None)

        model = LLMOpinionModel.objects.get(id=model_id)
        if model:
            model.question = question
            model.answer = answer
            model.save()
            if model:
                return Response({'message': 'Successfully updated model name'}, status=status.HTTP_200_OK)
            return Response({'message': 'Something went wrong during name update'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Model not found'}, status=status.HTTP_400_BAD_REQUEST)


class RunningDevice(APIView):
    serializer_class = LLMOpinionModelSerializer

    @swagger_auto_schema(
        operation_description='What are the device details that are being run'
    )
    def get(self, request):
        host = 'localhost'
        port = '8090'
        endpoint = 'using-device'
        if INSIDE_DOCKER:
            host = 'llm-ai'

        url = f"http://{host}:{port}/{endpoint}"
        response = requests.get(url)

        response_json = response.json()
        return Response(response_json, status=status.HTTP_200_OK)


class DeviceUsage(APIView):
    serializer_class = LLMOpinionModelSerializer

    @swagger_auto_schema(
        operation_description='GPU details'
    )
    def get(self, request):
        host = 'localhost'
        port = '8090'
        endpoint = 'gpu-details'
        if INSIDE_DOCKER:
            host = 'llm-ai'

        url = f"http://{host}:{port}/{endpoint}"
        response = requests.get(url)

        response_json = response.json()
        return Response(response_json, status=status.HTTP_200_OK)
