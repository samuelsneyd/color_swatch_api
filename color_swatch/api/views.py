from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .color_spaces import get_random_color_space, get_color_space

N_COLORS_PARAM = 'n'
N_COLORS_DEFAULT = 5
N_COLORS_MIN = 1
N_COLORS_MAX = 50


class HealthCheck(APIView):
    def get(self, _request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class ColorSwatchView(APIView):
    def get(self, request):
        try:
            n = int(request.query_params.get(N_COLORS_PARAM, N_COLORS_DEFAULT))
            if not (N_COLORS_MIN <= n <= N_COLORS_MAX):
                raise ValueError
        except ValueError:
            return Response(
                {"error": f"'{N_COLORS_PARAM}' must be an int between {N_COLORS_MIN} and {N_COLORS_MAX}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        swatch = [get_random_color_space().random_color() for _ in range(n)]
        return Response(swatch)


class ColorSwatchBySpaceView(APIView):
    def get(self, request, color_space):
        space = get_color_space(color_space)
        if space is None:
            return Response(
                {"error": f"invalid color space '{color_space}'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            n = int(request.query_params.get(N_COLORS_PARAM, N_COLORS_DEFAULT))
            if not (N_COLORS_MIN < n < N_COLORS_MAX):
                raise ValueError
        except ValueError:
            return Response(
                {"error": f"'{N_COLORS_PARAM}' must be an int between {N_COLORS_MIN} and {N_COLORS_MAX}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        swatch = [space.random_color() for _ in range(n)]
        return Response(swatch)
