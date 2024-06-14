from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VowelCountRequestSerializer, SortRequestSerializer
from .utils import count_vowels, sort_words


class VowelCountView(APIView):
    def post(self, request):
        serializer = VowelCountRequestSerializer(data=request.data)
        if serializer.is_valid():
            words = serializer.validated_data['words']
            vowel_counts = count_vowels(words)
            return Response(vowel_counts, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SortView(APIView):
    def post(self, request):
        serializer = SortRequestSerializer(data=request.data)
        if serializer.is_valid():
            words = serializer.validated_data['words']
            order = serializer.validated_data['order']
            sorted_words = sort_words(words, order)
            return Response(sorted_words, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
