#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User,Country,City,Group,Comment,GroupMember
import datetime


class UserFormRe(forms.Form):
    email = forms.EmailField(label='email',max_length=100)
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    firstname = forms.CharField(label='firstname',max_length=30)
    lastname = forms.CharField(label='lastname',max_length=30)

class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

#Register
def regist(req):
    if req.method == 'POST':
        uf = UserFormRe(req.POST)
        if uf.is_valid():
            email = uf.cleaned_data['email']
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            lastname = uf.cleaned_data['lastname']
            firstname = uf.cleaned_data['firstname']
            # add to database
            User.objects.create(username= username,password=password,email=email,firstname=firstname,lastname=lastname)
            return HttpResponseRedirect('/books/Login/')
    else:
        uf = UserFormRe()
        return render(req,'regist.html',{'uf':uf})


# login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # get the username and pw
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # compare it to the database
            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
                #hour = 0
                #dt = datetime.datetime.now() + datetime.timedelta(hours=int(hour))
                # login success, go to /homepage.html
                response = HttpResponseRedirect('/books/')
                response.set_cookie("username", username, 3600)
                return response

            else:
                return HttpResponseRedirect('/Login/')
    else:
        uf = UserForm()
        return render(req,'Login.html',{'uf':uf})


def show_user(request):
    if "username" in request.COOKIES:
        username = request.COOKIES["username"]
        return HttpResponseRedirect('/books/my_group/', {'username': username})
    return HttpResponseRedirect('/books/Login')


# logout
def logout(req):
    response = HttpResponseRedirect('/books/Login')
    response.delete_cookie('username')
    return response


# add comment member
def comment_add(request):

    if request.method == 'POST':

        group_id = request.POST.get('group', '')

        detail = request.POST.get('detail', '')

        if group_id and detail:
            comment = Comment()
            comment.article = Group(id=group_id)
            comment.detail = detail
            comment.save()

        return HttpResponseRedirect('/myGroupDetail_member/%s' % group_id)

    return render_to_response('myGroupDetail_member.html',)


# c_a_o
def comment_add_o(request):

    if request.method == 'POST':

        group_id = request.POST.get('group', '')

        detail = request.POST.get('detail', '')

        if group_id and detail:
            comment = Comment()
            comment.article = Group(id=group_id)
            comment.detail = detail
            comment.save()

        return HttpResponseRedirect('/myGroupDetail_organiser/%s' % group_id)


# index
def homepage(request):

    countries = Country.objects.order_by("-id").all()

    return render_to_response('Homepage.html',{'countries': countries})


def grouplist(request):

    #country = Country.objects.get(id=id)

    #groups = Group.objects.filter(g_country=id).order_by("-id").all()


    groups = Group.objects.order_by("-id").all()

    return render_to_response('groupList.html', {'groups': groups })


def group_detail(request, id):

    group = Group.objects.get(id=id)

    inmembers = GroupMember.objects.filter(group=id)

    mid = inmembers.member.all()

    members = User.objects.filter(id=mid)

    print len(members)

    return render_to_response('group_detail.html', {'group': group, 'members': members})

#
def my_group(request):

    if request.user.is_authenticated():

        current_user = request.user

        #user = User.objects.filter(username=current_user).all()

        #userid = user.id.all()

        #gm_id = GroupMember.objects.filter(gm_member=current_user)

        #m_groups = Group.objects.filter(GroupMember=gm_id).order_by("-id").all()

        groupid = GroupMember.objects.filter(member_username=current_user).values_list("user_group_group")

        m_groups = Group.objects.filter(id=groupid).order_by("-id").all()

        return render_to_response('myGroups.html', {'m_groups': m_groups})
    else:
        # login page
        return HttpResponseRedirect('/books/my_group')


#
def myo_group(request):


    if request.user.is_authenticated():

        current_user = request.user

        o_groups = Group.objects.filter(g_organiser_username=current_user).all()

        return render_to_response('myGroups.html', {'o_groups': o_groups})



#
def group_detail_member(request, id):

    m_group = Group.objects.get(id=id)

    #members = GroupMember.objects.filter(group=id).order_by("-id").all()

    inmembers = GroupMember.objects.filter(group=id)

    mid = inmembers.member.all()

    members = User.objects.filter(id=mid)

    comments = Comment.objects.filter(group=id).order_by("-id").all()

    print len(members)

    print len(comments)
    return render_to_response('group_detail.html', {'m_group': m_group, 'members': members, 'comments':comments})


def group_detail_organiser(request, id):

    o_group = Group.objects.get(id=id)

    inmembers = GroupMember.objects.filter(group=id)

    mid = inmembers.member.all()

    members = User.objects.filter(id=mid)

    #members = GroupMember.objects.filter(group=id).order_by("-id").all()

    comments = Comment.objects.filter(group=id).order_by("-id").all()

    print len(members)
    print len(comments)

    return render_to_response('group_detail.html', {'o_group': o_group, 'members': members, 'comments':comments})


# create a new group ok
def create_new_group(request):

    if request.method == 'POST':

        g_name = request.POST.get('g_name', None)
        g_city = request.POST.get('g_city', None)
        g_place = request.POST.get('g_place', None)
        g_member = request.POST.get('g_member', None)
        g_country = request.POST.get('g_country', None)
        g_organiser = request.POST.get('g_organiser', None)
        g_content = request.POST.get('g_content', None)

        new = Group(g_name=g_name,g_city=g_city,g_place=g_place,g_member=g_member,g_country=g_country,g_organiser=g_organiser,g_content=g_content,g_state="u")
        new.save()

        return HttpResponseRedirect('/books/groupList')

    return render_to_response('create_new_group.html')


def delete_group(request):

    if request.method == 'POST':
        Group.objects.filter(id=id).delete()

        return HttpResponseRedirect('/books/group/delete_group')

    return render_to_response('myGroupDetail_organiser.html')


def complete_group(request):

    if request.method == 'POST':

        state = Group.objects.get(id=id)

        state.g_state = 'c'

        state.save()

        return HttpResponseRedirect('/books/group/complete_group')

    return render_to_response('myGroupDetail_organiser.html')


def quit_group(request):

    if request.method == 'POST':
        # if request.user.is_authenticated():

        #   current_user = request.user

        nomember = Group.objects.get(id=id)

        nomember.g_member = nomember.g_member -1

        nomember.save()

        return HttpResponseRedirect('/books/group/quit_group')

    return render_to_response('myGroupDetail_member.html')


def group_addme(request):

    if request.method == 'POST':

    #if request.user.is_authenticated():

     #   current_user = request.user

        nomember = Group.objects.get(id=id)

        nomember.g_member= nomember.g_member+1

        nomember.save()

        return HttpResponseRedirect('/books/group/addme')

    return render_to_response('group_detail.html')


