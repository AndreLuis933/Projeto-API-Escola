from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet , MatriculaCurso, MatriculaEstudante
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename= 'Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',MatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',MatriculaCurso.as_view()),
]
