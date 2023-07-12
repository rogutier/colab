from django.core.management.base import BaseCommand
from academy.models import Teacher, Student, Course, Subject, Subscription

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--mode", type = str, help = "Mode: load / clear")

    def handle(self, *args, **options):
        print("Data inicial")

        self.seeds_subject(options.get('mode'))
        print("Subjects: ", Subject.objects.all().count())

        self.seeds_student(options.get('mode'))
        print("Students: ", Student.objects.all().count())

        self.seeds_course(options.get('mode'))
        print("Courses: ", Course.objects.all().count())

        self.seeds_teacher(options.get('mode'))
        print("Teachers: ", Teacher.objects.all().count())

    def seeds_subject(self, mode):
        if mode == "load" and Subject.objects.all().count() <= 0:
            self.seeds_course(mode)
            self.seeds_teacher(mode)

            ss = Subject()
            ss.course = Course.objects.get(name = "Cálculo")
            ss.teacher = Teacher.objects.get(first_name = "John")
            ss.start_date = "2023-08-10"
            ss.save()

            ss = Subject()
            ss.course = Course.objects.get(name = "Programación")
            ss.teacher = Teacher.objects.get(first_name = "Ray")
            ss.start_date = "2023-10-15"
            ss.save()
        elif mode == "clear":
            Subject.objects.all().delete()

    def seeds_student(self, mode):
        if mode == "load" and Student.objects.all().count() <= 0:
            s = Student()
            s.first_name = "Juan"
            s.last_name = "Perez"
            s.email = "juan@gmail.com"
            s.save()

            s = Student()
            s.first_name = "Roman"
            s.last_name = "Roy"
            s.email = "roman@gmail.com"
            s.save()
        elif mode == "clear":
            Student.objects.all().delete()

    def seeds_course(self, mode):
        if mode == "load" and Course.objects.all().count() <= 0:
            c = Course()
            c.name = "Cálculo"
            c.description = "Cálculo I"
            c.save()

            c = Course()
            c.name = "Programación"
            c.description = "Lenguajes de programación requeridos en la actualidad."
            c.save()
        elif mode == "clear":
            Course.objects.all().delete()


    def seeds_teacher(self, mode):
        # mode puede ser load o clear
        if mode == "load" and Teacher.objects.all().count() <= 0:
            # Verificamos que solo see creen docentes una sola vez
            t = Teacher()
            t.first_name = "John"
            t.last_name = "Doe"
            t.bio = "Este es un bio del docente"
            t.save()

            t = Teacher()
            t.first_name = "Ray"
            t.last_name = "Rojas"
            t.bio = "Este es un bio del docente"
            t.save()
        elif mode == "clear":
            Teacher.objects.all().delete()

        