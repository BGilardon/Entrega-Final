from django.test import TestCase

from .models import Curso

# Create your tests here.
class CursosTest(TestCase):
    
    def setUp(self):
        Curso.objects.create(nombre="Curso de Django", comision=2)
        
    def test_curso_nombre(self):
        curso = Curso.objects.get(comision=2)
        self.assertEqual(curso.nombre, "Curso de Django")
    
    def test_curso_creado(self):
        curso = Curso.objects.get(comision=2)
        self.assertNotEquals(curso, None)


# def eliminar_posteo(request,posteo_id):

#     posteo = Posteo.objects.get(id=posteo_id)
#     posteo.delete()

#     return redirect("posteos")

# def editar_posteo(request,posteo_id):

#     posteo = Posteo.objects.get(id=posteo_id)

#     if request.method == "POST":

#         formulario = posteoCrear(request.POST)

#         if formulario.is_valid():
            
#             info_posteo = formulario.cleaned_data

#             posteo.titulo=info_posteo["titulo"]
#             posteo.cuerpo=info_posteo["cuerpo"]
#             posteo.fecha = info_posteo["fecha"]
#             posteo.imagen = info_posteo["imagen"]
            
#             posteo.save()

#             return redirect("posteos")

#     # get
#     formulario = posteoCrear(initial={'titulo':posteo.titulo,'cuerpo':posteo.cuerpo, 'fecha':posteo.fecha,'imagen':posteo.imagen})
    
#     return render(request,"ProyectoCoderApp/crearPosteos.html",{"form":formulario})