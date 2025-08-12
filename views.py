from django.shortcuts import render,redirect
from .models import User,Teacher,NotApproved,Student
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def Home(request):
    return render(request,'Home.html')

def Userlogin(request):
    if request.method=="POST":
        usr=request.POST['usern']
        pwd=request.POST['password']
        x=authenticate(request,username=usr,password=pwd)
        if x is not None and x.is_superuser==1:
            login(request,x)
            request.session['adm_id']=x.id
            return redirect(Admin_home)
        elif x is not None and x.usertype=="teacher":
            login(request,x)
            request.session['teach_id']=x.id
            return redirect(Teacher_home)
        elif x is not None and x.usertype=="student":
            login(request,x)
            request.session['stud_id']=x.id
            return redirect(Student_home)
    else:
        return render(request,'login.html')

@login_required
def Admin_home(request):
    session_id=request.session['adm_id']
    obj=User.objects.get(id=session_id)
    return render(request,'Admin_Dashboard.html',{'adm_obj':obj})

def Admin_Teacher_Register(request):
    if request.method=="POST":
        usr=request.POST['usern']
        pwd=request.POST['pswd']
        cpwd=request.POST['cpswd']
        na=request.POST['name']
        pro=request.FILES['profile_Pic']
        ph=request.POST['phone']
        em=request.POST['email']
        ag=request.POST['age']
        qua=request.POST['qualify']
        dept=request.POST['depart']
        if pwd==cpwd:
            user_obj=User.objects.create_user(username=usr,password=pwd,first_name=na,email=em,usertype="teacher")
            teacher_obj=Teacher.objects.create(usrname=user_obj,passd=pwd,phone=ph,profile_Pic=pro,email=em,name=na,qualification=qua,dep=dept,age=ag)
            teacher_obj.save()
            return redirect(Admin_home)
    else:
        return render(request,'TeacherRegister.html')   
    
def Admin_ViewTeacher(request):
    obj=Teacher.objects.all()
    return render(request,'ViewTeacher.html',{'view':obj})

def Admin_DeleteTeacher(request,id):    # teacherid
    teach_obj = Teacher.objects.get(id=id)
    obj=User.objects.get(id=teach_obj.usrname_id)
    print(obj)
    obj.delete()
    return redirect(Admin_ViewTeacher)

def Admin_EditTeacher(request,id):
    if request.method=="POST":
        e_obj=Teacher.objects.get(id=id)
        usr_obj=User.objects.get(id=e_obj.usrname_id)
     
        usr=request.POST['usrname']
        na=request.POST['name']
        psd=request.POST['passwd']
        ph=request.POST['phone']
        em=request.POST['email']
        ag=request.POST['age']
        q=request.POST['qualify']
        d=request.POST['dept']
        img = request.FILES['prof']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    
        file = Teacher.objects.get(id=id).profile_Pic
        Teacher.objects.filter(id=id).update( profile_Pic=file)
        usr_obj.username=usr
        usr_obj.first_name=na
        usr_obj.set_password(psd)
        usr_obj.email=em
        usr_obj.save()

        e_obj.name=na
        e_obj.profile_Pic=img
        e_obj.passd=psd
        e_obj.phone=ph
        e_obj.email=em
        e_obj.age=ag
        e_obj.qualification=q
        e_obj.dep=d
        e_obj.save()
        return redirect(Admin_ViewTeacher)
    else:
        obj=Teacher.objects.get(id=id)
        return render(request,'EditTeacher.html',{"edit":obj})

def Teacher_home(request):
    session_id=request.session['teach_id']
    obj=Teacher.objects.get(usrname=session_id)
    return render(request,'Teacher_dashboard.html',{'teach':obj})


def Teacher_ViewTeacher(request):
    session_id=request.session['teach_id']
    obj=Teacher.objects.get(usrname=session_id)
    return render(request,'TeacherviewTeacher.html',{'view':obj})


def Teacher_EditTeacher(request,id):
    if request.method=="POST":
        e_obj=Teacher.objects.get(id=id)
        obj=User.objects.get(id=e_obj.usrname_id)
        usr=request.POST['usrname']
        na=request.POST['name']
        psd=request.POST['passwd']
        ph=request.POST['phone']
        em=request.POST['email']
        ag=request.POST['age']
        q=request.POST['qualify']
        d=request.POST['dept']
        img = request.FILES['prof']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    
        file = Teacher.objects.get(id=id).profile_Pic
        Teacher.objects.filter(id=id).update( profile_Pic=file)
        obj.username=usr
        obj.first_name=na
        obj.set_password(psd)
        obj.email=em
        obj.save()
        
        e_obj.name=na
        e_obj.profile_Pic=img
        e_obj.passd=psd
        e_obj.phone=ph
        e_obj.email=em
        e_obj.age=ag
        e_obj.qualification=q
        e_obj.dep=d
        e_obj.save()
        return redirect(Teacher_home)
    else:
        obj=Teacher.objects.get(id=id)
        return render(request,'TeacherEditTeacher.html',{"edit":obj})
    


def StudentRequest(request):
    if request.method=="POST":
        usr=request.POST['usern']
        pwd=request.POST['pswd']
        cpwd=request.POST['cpswd']
        na=request.POST['name']
        pro=request.FILES['profile_Pic']
        ph=request.POST['phone']
        em=request.POST['email']
        dept=request.POST['depart']
        ag=request.POST['age']
        if pwd==cpwd:
            Student_obj=NotApproved.objects.create(usrname=usr,passd=pwd,phone=ph,profile_Pic=pro,email=em,name=na,dep=dept,age=ag)
            Student_obj.save()
            return redirect(Home)

    else:
            return render(request,'StudentRegister.html')
        

def Student_Accept_Reject(request):
    obj=NotApproved.objects.all()
    return render(request,'admin_accept_reject.html',{'view':obj})



def Admin_AcceptRequest(request, id):
    not_aprv_obj = NotApproved.objects.get(id=id)
    user_obj = User.objects.create_user(      #auto save
            username=not_aprv_obj.usrname, 
            password=not_aprv_obj.passd,
            usertype="student"
        )
    stud_obj=Student.objects.create(
            usrname=user_obj,
            passd=not_aprv_obj.passd,
            phone=not_aprv_obj.phone,
            profile_Pic=not_aprv_obj.profile_Pic,
            email=not_aprv_obj.email,
            name=not_aprv_obj.name,
            dep=not_aprv_obj.dep,
            age=not_aprv_obj.age
        )
    stud_obj.save()
    not_aprv_obj.delete()
    return redirect('Student_Accept_Reject')
 

def Admin_RejectRequest(request,id):
    obj=NotApproved.objects.get(id=id)
    obj.delete()
    return redirect(Student_Accept_Reject) 


def Student_home(request):
    session_id=request.session['stud_id']
    obj=Student.objects.get(usrname=session_id)
    return render(request,'Student_Dashboard.html',{'stud':obj})

def Admin_ViewStudent(request):
    obj=Student.objects.all()
    return render(request,"AdminViewStudent.html",{'view':obj})


def Admin_StudentDelete(request,id):
    obj=Student.objects.get(id=id)
    d_obj=User.objects.get(id=obj.usrname_id)
    d_obj.delete()
    return redirect(Admin_ViewStudent)

def Admin_StudentEdit(request,id):
    if request.method=="POST":
        e_obj=Student.objects.get(id=id)
        usr_obj=User.objects.get(id=e_obj.usrname_id)
     
        na=request.POST['name']
        ph=request.POST['phone']
        em=request.POST['email']
        ag=request.POST['age']
        d=request.POST['dept']
        img = request.FILES['prof']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    
        file = Student.objects.get(id=id).profile_Pic
        Student.objects.filter(id=id).update( profile_Pic=file)
        usr_obj.first_name=na
        usr_obj.email=em
        usr_obj.save()

        e_obj.name=na
        e_obj.profile_Pic=img
        e_obj.phone=ph
        e_obj.email=em
        e_obj.age=ag
        e_obj.dep=d
        e_obj.save()
        return redirect(Admin_ViewStudent)
    else:
        obj=Student.objects.get(id=id)
        return render(request,'AdminEditStudent.html',{"edit":obj})



def Teacher_ViewStudent(request): 
        d_obj=Student.objects.values_list('dep',flat=True).distinct()  
        selected_department=request.GET.get('depart')       
        session_id=request.session['teach_id']
        t_obj=Teacher.objects.get(usrname=session_id)
        if selected_department:
            obj=Student.objects.filter(dep=selected_department)
            print(selected_department)
        else:
            obj=Student.objects.all()
        return render(request,"TeacherViewStudent.html",{'view':obj, 'departments':d_obj, 'selected_department':selected_department,'teach':t_obj})




def Student_ViewStudent(request):
    session_id=request.session['stud_id']
    obj=Student.objects.get(usrname=session_id)
    return render(request,'StudentViewStudent.html',{'view':obj})


def StudentEditStudent(request,id):
    if request.method=="POST":
        e_obj=Student.objects.get(id=id)
        obj=User.objects.get(id=e_obj.usrname_id)
        usr=request.POST['usrname']
        na=request.POST['name']
        psd=request.POST['passwd']
        ph=request.POST['phone']
        em=request.POST['email']
        ag=request.POST['age']
        d=request.POST['dept']
        img = request.FILES['prof']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    
        file = Student.objects.get(id=id).profile_Pic
        Student.objects.filter(id=id).update( profile_Pic=file)
        obj.username=usr
        obj.first_name=na
        obj.set_password(psd)
        obj.email=em
        obj.save()
        
        e_obj.name=na
        e_obj.profile_Pic=img
        e_obj.passd=psd
        e_obj.phone=ph
        e_obj.email=em
        e_obj.age=ag
        e_obj.dep=d
        e_obj.save()
        return redirect(Student_home)
    else:
        obj=Student.objects.get(id=id)
        return render(request,'StudentEditStudent.html',{"edit":obj})

def StudentViewTeacher(request):
    d_obj=Teacher.objects.values_list('dep',flat=True).distinct()    # unique dept   : [....]
    selected_department=request.GET.get('depart')                    # user chose : value
    session_id=request.session['stud_id']
    s_obj=Student.objects.get(usrname=session_id)
    if selected_department:
        obj=Teacher.objects.filter(dep=selected_department)
        print(selected_department)
    else:
        obj=Teacher.objects.all()
    return render(request,"StudentViewTeacher.html",{'view':obj, 'departments':d_obj, 'selected_department':selected_department,'stud':s_obj})


def logouts(request):
    logout(request)
    return redirect(Home)
