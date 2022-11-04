from django.db.models import Q

from jobapp.models import Jobs


def query_for_name(key, val, sort_info, educa, work_year):
    if educa == 'edu所有':
        educa = ''
    if work_year == 'wor所有':
        work_year = ''
    if key == "query":
        if not val:
            result = Jobs.objects.filter(attribute__icontains=educa).filter(attribute__icontains=work_year).order_by("-" + str(sort_info))
            return result
        result = Jobs.objects.filter(Q(job_name__icontains=val) |
                                 Q(company_name__icontains=val) |
                                 Q(work_area__icontains=val) |
                                 Q(provide_salary__icontains=val) |
                                 Q(company_type__icontains=val) |
                                 Q(job_welf__icontains=val) |
                                 Q(company_ind__icontains=val)).filter(attribute__icontains=educa).filter(attribute__icontains=work_year).order_by("-" + str(sort_info))
        return result
    if key == "work_name":
        result = Jobs.objects.filter(job_name__icontains=val).filter(attribute__icontains=educa).filter(attribute__icontains=work_year).order_by("-" + str(sort_info))
        return result
    elif key == "city_name":
        result = Jobs.objects.filter(work_area__icontains=val).filter(attribute__icontains=educa).filter(attribute__icontains=work_year).order_by("-" + str(sort_info))
        return result
    elif key == "stu_work":
        result = Jobs.objects.filter(attribute__contains=val).filter(attribute__icontains=educa).filter(attribute__icontains=work_year).order_by("-" + str(sort_info))
        return result

