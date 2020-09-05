from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Movieapp.models import GetImage 


import pymysql

db=pymysql.Connect("localhost","root","","moviedb")
c=db.cursor()
strval=""



# Create your views here.
def home(request):
    
    
       
        return render(request,"home.html")

def index(request):
    if(request.POST):
        search=request.POST.get("search")
        search=request.session['search']=search
        if(request.session['search']):
            return render(request,"search.html",{"search":request.session['search']})
    return render(request,"index.html")



def search(request):
    if(request.POST):
        search=request.POST.get("search")
        s="select * from movietab where moviename='"+search+"'"
        t="select name,rev from revtab where moviename='"+search+"'"
        u="select round(avg(rate),1) from ratetab where mnane='"+search+"'"
        c.execute(s)
        d=c.fetchall()
        c.execute(t)
        d1=c.fetchall()
        c.execute(u)
        d2=c.fetchall()
        m="incorrect Moviename"
        if(d):
            return render(request,"search.html",{"d":d , "d1":d1 ,"d2":d2})
        else:
            return render(request,"index.html",{"m":m})
    return render(request,"search.html")




def sign(request):
    if(request.POST):
        uname=request.POST.get("uname") 
        pwd=request.POST.get("pwd")
        if(uname=="admin@gmail.com" and pwd=="admin@moviehut"):
            request.session['aduname']=uname
            
            return render(request,"adminpanel.html",{"username":request.session['aduname'],"pass":request.session['adpwd']})
        else:
            
            m="Incorrect Username or Password!"
            s="select email,password from usertab where email='"+uname+"' and password='"+pwd+"'"
            d=c.execute(s)
            if(d):
                request.session['uname']=uname
                return render(request,"userpanel.html",{"user":request.session['uname']})
            else:
                return render(request,"signup.html",{"msg":m})
    return render(request,"signup.html")

def adminpanel(request):
    return render(request,"adminpanel.html")


def addmovie(request):
    if(request.POST):
        mname=request.POST.get("moviename")
        dirt=request.POST.get("director")
        pro=request.POST.get("producer")
        cast=request.POST.get("cast")
        writer=request.POST.get("writer")
        music=request.POST.get("music")
        rdate=request.POST.get("rdate")
        duration=request.POST.get("duration")
        lang=request.POST.get("lang")
        image=request.POST.get("image")
        # if(pwd==cpwd):
        c.execute("insert into movietab values('"+mname+"','"+dirt+"','"+pro+"','"+cast+"','"+writer+"','"+music+"','"+rdate+"','"+duration+"','"+lang+"','"+image+"')")
        # c.execute(s)
        return HttpResponseRedirect("/adminpanel")
    return render(request,"moviedetails.html",{"username":request.session['aduname']})


def viewmovie(request):
    
    s="select * from movietab"
    c.execute(s)
    d=c.fetchall()
    if(d):
        return render(request,"viewmovie.html",{"d":d,"username":request.session['aduname']})
        if(request.POST):
            if(request.session['aduname']):
                new=request.POST.get("movie")
                t="select name,rev from revtab where moviename='"+new+"'"
                u="select round(avg(rate),1) from ratetab where mnane='"+new+"'"
                c.execute(t)
                d1=c.fetchall()
                c.execute(u)
                d2=c.fetchall()
                if(d1 and d2):
                    return render(request,"viewmovie.html",{"d1":d1,"d2":d2})
                else:
                    return HttpResponse("kjk")

    return render(request,"viewmovie.html",{"username":request.session['aduname']})


def viewreviewrate(request):
    if(request.POST):
        search=request.POST.get("search")
        
        t="select name,rev from revtab where moviename='"+search+"'"
        u="select round(avg(rate),1) from ratetab where mnane='"+search+"'"
        
        c.execute(t)
        d1=c.fetchall()
        c.execute(u)
        d2=c.fetchall()
        
        if( d1 and d2):
            return render(request,"viewmovie.html",{ "d1":d1 ,"d2":d2})
        
    return render(request,"viewmovie.html",{"username":request.session['aduname']})     


def editmovie(request):
    if(request.POST):
        movie=request.POST.get("name")
        request.session['name']=movie
        s="select * from movietab where moviename='"+movie+"'"
        c.execute(s)
        d=c.fetchall()
        if(d):
            return render(request,"edit.html",{"d":d,"movie":request.session['name']})
    return render(request,"edit.html",{"username":request.session['aduname']})
def edit(request):

        if(request.POST.get):
            mname=request.POST.get("mname")
            dirt=request.POST.get("director")
            pro=request.POST.get("producer")
            cast=request.POST.get("cast")
            writer=request.POST.get("writer")
            rdate=request.POST.get("rdate")
            music=request.POST.get("music")
            rdate=request.POST.get("rdate")
            duration=request.POST.get("duration")
            lang=request.POST.get("lang")
            #image=request.POST.get("image")
                    
            # if(pwd==cpwd):
            c.execute("update movietab set moviename='"+mname+"', director='"+dirt+"',producer='"+pro+"', cast='"+cast+"',writer='"+writer+"',rdate='"+rdate+"', music='"+music+"', duration='"+duration+"',lang='"+lang+"' where moviename='"+request.session['name']+"'")
            # c.execute(s)
            return render(request,"edit.html",{"movie":request.session['name']})
        return render(request,"edit.html",{"username":request.session['aduname'],"movie":request.session['name']})
def deletemovie(request):
    if(request.POST):
        movie=request.POST.get("moviename")
        c.execute("DELETE FROM movietab WHERE moviename ='"+movie+"'")
        return render(request,"delete.html")
    return render(request,"delete.html",{"username":request.session['aduname']})


#user
def userpanel(request):
     return render(request,"userpanel.html")
def reguser(request):
    if(request.POST):
        email=request.POST.get("email")
        pwd=request.POST.get("pwd")
        cpwd=request.POST.get("cpwd")
        request.session['uname']=email
        request.session['upass']=pwd
        m="Enter Same Password!"
       
        if(pwd==cpwd):
            c.execute("insert into usertab values('"+email+"','"+pwd+"')")
        else:
            return render(request,"register.html",{"m":m,"user":request.session['uname']})

        # c.execute(s)
        return HttpResponseRedirect("/sign")
    return render(request,"register.html")
def moviereview(request):
    s="select * from movietab"
    c.execute(s)
    d=c.fetchall()
    
    if(d):
        return render(request,"moviereview.html",{"d":d,"user":request.session['uname']})
        
        
    return render(request,"moviereview.html",{"user":request.session['uname']})
def addreview(request):
    if(request.POST):
        if(request.session['uname']):
                review=request.POST.get("review")
                new=request.POST.get("new1")
                s="insert into revtab values('"+request.session['uname']+"','"+review+"','"+new+"')"
                c.execute(s)
                return HttpResponseRedirect("/moviereview")
        else:
                return HttpResponse("cannot")   
    return render(request,"moviereview.html",{"user":request.session['uname'],"new":request.session['new']})



def addrate(request):
    if(request.POST):
        if(request.session['uname']):
                star=request.POST.get("demo")
                new=request.POST.get("new")
                s="insert into ratetab values('"+request.session['uname']+"','"+star+"','"+new+"')"
                c.execute(s)
                return HttpResponseRedirect("/moviereview")
        else:
                return HttpResponse("cannot")   
    return render(request,"moviereview.html",{"user":request.session['uname'],"new":request.session['new']})

def logout(request):
    if(request.POST.get("logout")=="LOGOUT"):
        request.session['aduname']=""
        request.session['adpwd']=""
        request.session['uname']=""
        request.session['upass']=""
    return HttpResponseRedirect("/index")