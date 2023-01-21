from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers.common import CommentSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Comment


class CommentListView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.data['owner'] = request.user.id
        comment_to_create = CommentSerializer(data=request.data)
        try:
            comment_to_create.is_valid()
            comment_to_create.save()
            return Response(comment_to_create.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({
                "detail": str(e),
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response("Unprocessable Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound(detail="Can't find that album!")

    def put(self, request, pk):
        comment_to_edit = self.get_comment(pk=pk)
        if comment_to_edit.owner != request.user:
            raise PermissionDenied()

        updated_comment = CommentSerializer(comment_to_edit, data=request.data)
        try:
            updated_comment.is_valid()
            updated_comment.save()
            return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        try:
            comment_to_delete = self.get_comment(pk=pk)
            if comment_to_delete.owner != request.user:
                raise PermissionDenied()

            comment_to_delete.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail="Comment not found")


    def delete(self, _request, pk):
        try:
            comment_to_delete = Comment.objects.get(pk=pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail="Comment not found")