from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, TemplateView
from app.models import Employee, Contact, MynumberCard
from django.shortcuts import get_object_or_404
from app.forms import EmployeeForm, ContactForm, MynumberCardForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class EmployeeListView(ListView):
    template_name = 'list.html'
    model = Employee


class EmployeeDetailView(DetailView):
    template_name = "detail.html"
    model = Employee
  
class EmployeeDetailUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'update.html'
    def get_success_url(self):
        """変更対象レコードのPKを取得してreverse_lazyで詳細画面へ戻る"""
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})


class EmployeeDetailUpdateView2(TemplateView):
    template_name = 'update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = get_object_or_404(Employee,pk=self.kwargs['pk'])
        context['employee'] = employee
        context['employee_form'] = EmployeeForm(instance=employee)
        context['contact_form'] = ContactForm(instance=employee.contact)
        context['mynumber_form'] = MynumberCardForm(instance=employee.mynumbercard)

        return context

    def post(self, request, *args, **kwargs):
        # URLに渡されたキーワード引数から主キーpkを取得
        pk = self.kwargs['pk']
  
        # pkに基づいてデータベースから各モデルクラスのインスタンスを取得
        employee = get_object_or_404(Employee, pk=pk)
        contact = get_object_or_404(Contact, employee__pk=pk)
        mynumber = get_object_or_404(MynumberCard, employee__pk=pk)


        # 各モデルクラス用のFormインスタンスを作成
        employee_form = EmployeeForm(instance=employee, data=request.POST)
        mynumber_form = MynumberCardForm(instance=mynumber, data=request.POST)
        contact_form = ContactForm(instance=contact, data=request.POST)
        
        # save_employeeボタンがクリックされた場合
        if 'save_employee' in request.POST:
            if employee_form.is_bound and employee_form.is_valid():
                employee_form.save()
                messages.success(request, '社員情報の更新処理が正常終了しました。')
            
            else:
                messages.error(request, employee_form.errors)
        

        # save_mynumberボタンがクリックされた場合
        elif 'save_mynumber' in request.POST:
            
            if mynumber_form.is_bound and mynumber_form.is_valid():
                mynumber_form.save()
                messages.success(request, 'マイナンバー情報の更新処理が正常終了しました。')
            else:
                messages.error(request, mynumber_form.errors)
        
        # save_contactボタンがクリックされた場合
        elif 'save_contact' in request.POST:
            if contact_form.is_bound and contact_form.is_valid():
                contact_form.save()
                messages.success(request, '連絡先情報の更新処理が正常終了しました。')
            else:
                messages.error(request, contact_form.errors)
      
        return HttpResponseRedirect(reverse('detail', kwargs={'pk': self.kwargs['pk']}))