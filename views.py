from django.shortcuts import render
from django.http import HttpResponse

def mission(request):
    msg = "The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence."
    return HttpResponse(msg)

def vision(request): 
    msg = "The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education."
    return HttpResponse(msg)

def objectives(request): 
    msg = """
    Increase faculty performance by obtaining a minimum rating of 4.00 in the semestral faculty evaluation of each faculty for the next five years. 
    Maintain competent faculty line-up by sending all permanent fulltime faculty to at least one (1) IT related training, conference, or seminar annually for the next five years. 
    Conduct a minimum of two (2) researches, IT projects or production of instructional materials annually for the next five years. 
    Achieve a minimum of 50 student passing percentage in the IT certification annually for the next five years. 
    Maintain state-of-the-art information technology learning environment through annual procurement or upgrading of hardware or software licenses for at least one computer laboratory for the next five years. 
    Set up minimum of two (2) academe-industry partnership projects and commercialization initiatives or research publication and presentation annually in preparation for the next CHED COD/COE application. 
    Strengthen promotion program to increase freshman enrollees to a minimum of three (3) class sections annually for the next five years
    """
    return HttpResponse(msg)