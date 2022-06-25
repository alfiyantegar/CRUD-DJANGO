from django.urls import path

# import View dari todo Application
from .views import index_view, detail_view, create_view, update_view, delete_view
from django.urls import path

# import class View
from .views import CustomLoginView, HomeView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
app_name = 'todo'
urlpatterns = [
    # url untuk halaman daftar task
    path('', index_view, name='index'),
    # url untuk halaman detail task
    path('<int:task_id>', detail_view, name='detail'),
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    # url untuk halaman ubah task
    path('update/<int:task_id>', update_view, name='update'),
    # url untuk menghapus task
    path('delete/<int:task_id>', delete_view, name='delete'),
]