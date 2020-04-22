from django.shortcuts import render, redirect
from amz_brands.models import Brand
from .forms import BrandForm
from django.http import QueryDict
from .filter import BrandFilter
from django.http import HttpResponse
from amz_brands.resources import BrandResource
from tablib import Dataset


def dashboard(request):
    latest_brand = Brand.objects.all()
    filter_brands = BrandFilter(request.GET, queryset=latest_brand)

    if request.method == 'POST':
        entries = QueryDict(request.POST['content'])
        for index, entry_id in enumerate(entries.getlist('entry[]')):
            entry = Brand.objects.get(id=entry_id)
            entry.order = index
            entry.save()

    context = {
        'latest_brand': 'latest_brand',
        'filter': filter_brands,
    }

    return render(request, 'accounts/dashboard.html', context)


def enroll(request):
    form = BrandForm()
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/dashboard')

    context = {'form': form}
    return render(request, 'pages/enroll.html', context)


def reports(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands
    }
    return render(request, 'pages/reports.html', context)


def export_file(request):
    brand_resource = BrandResource()
    dataset = brand_resource.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="brands.xls"'
    return response


def upload_file(request):
    if request.method == 'POST':
        brand_resource = BrandResource()
        new_brands = request.FILES['myfile']
        print(f"file: {new_brands}")

        imported_data = Dataset().load(new_brands.read().decode('UTF-8'), format='csv')
        print(f"data: {imported_data}")
        result = brand_resource.import_data(imported_data, dry_run=True)

        if not result.has_errors():
            brand_resource.import_data(imported_data, dry_run=False)

    return render(request, 'pages/upload_file.html')


def about(request):
    context = {

    }
    return render(request, 'pages/about.html')
