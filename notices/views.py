from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from .forms import NoticeForm

def is_staff(user):
    return user.is_staff

@login_required
def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notices/notice_list.html', {'notices': notices})

@login_required
@user_passes_test(is_staff)
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notices/notice_create.html', {'form': form})

@login_required
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'notices/notice_detail.html', {'notice': notice})

@login_required
@user_passes_test(is_staff)
def notice_update(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_detail', notice_id=notice.id)
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notices/notice_update.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.delete()
    return redirect('notice_list')