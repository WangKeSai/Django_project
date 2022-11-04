import random
from jobapp.models import Jobs


def recommend_data(n, jobname):
    sample = random.sample(range(Jobs.objects.filter(job_name__contains=jobname).count()), n)
    result = [Jobs.objects.filter(job_name__contains=jobname).all()[i] for i in sample]
    return result


def stu_data(n):
    sample = random.sample(range(Jobs.objects.filter(attribute__contains="应届生").count()), n)
    result = [Jobs.objects.filter(attribute__contains="应届生").all()[i] for i in sample]
    return result


def random_all(n):
    sample = random.sample(range(Jobs.objects.count()), n)
    result = [Jobs.objects.all()[i] for i in sample]
    return result
