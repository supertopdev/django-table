from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Centris
from django.http import JsonResponse
from functools import reduce

# Create your views here.


def index(request):
    centris = Centris.objects.all()
    paginator = Paginator(centris, 15)
    page = request.GET.get('page')

    centris = paginator.get_page(page)
    context = {
        'centris': centris
    }

    return render(request, 'interface/index.html', context=context)


def search(request):
    keys = ["pid", "centris_title", "address", "price", "workscore", "beds_baths", "geo_cordinates", "description",
            "agent_name", "built_year", "construction_year", "available_area", "lot_area",
            "operation_type",
            "fireplace_stove", "additional_features", "potential_gross_revenue", "main_unit", "residential_units",
            "unit_number", "parking", "building_area", "use_property", "zoning",
            "residential_unit",
            "business_type", "intergenerational", "building_style", "pool", "condominium", "gross_area",
            "net_area", "property_current_active"]

    if request.method == 'POST':
        # centris_items = Centris.objects.all()
        item_list = {}
        for key in keys:
            # if item_list[key] is not None:
            item_list[key] = request.POST.getlist(key)

        queries = [Q(pid__contains=pid) for pid in item_list['pid']] + \
                  [Q(centris_title__contains=title) for title in item_list['centris_title']] + \
                  [Q(address__contains=address) for address in item_list['address']] + \
                  [Q(price__contains=price) for price in item_list['price']] + \
                  [Q(workscore__contains=workscore) for workscore in item_list['workscore']] + \
                  [Q(beds_baths__contains=beds_baths) for beds_baths in item_list['beds_baths']] + \
                  [Q(geo_cordinates__contains=geo_cordinates) for geo_cordinates in item_list['geo_cordinates']] + \
                  [Q(description__contains=description) for description in item_list['description']] + \
                  [Q(agent_name__contains=agent_name) for agent_name in item_list['agent_name']] + \
                  [Q(built_year__contains=built_year) for built_year in item_list['built_year']] + \
                  [Q(construction_year__contains=construction_year) for construction_year in item_list['construction_year']] + \
                  [Q(available_area__contains=available_area) for available_area in item_list['available_area']] + \
                  [Q(lot_area__contains=lot_area) for lot_area in item_list['lot_area']] + \
                  [Q(operation_type__contains=operation_type) for operation_type in item_list['operation_type']] + \
                  [Q(fireplace_stove__contains=fireplace_stove) for fireplace_stove in item_list['fireplace_stove']] + \
                  [Q(additional_features__contains=additional_features) for additional_features in item_list['additional_features']] + \
                  [Q(potential_gross_revenue__contains=potential_gross_revenue) for potential_gross_revenue in item_list['potential_gross_revenue']] + \
                  [Q(main_unit__contains=main_unit) for main_unit in item_list['main_unit']] + \
                  [Q(residential_units__contains=residential_units) for residential_units in item_list['residential_units']] + \
                  [Q(unit_number__contains=unit_number) for unit_number in item_list['unit_number']] + \
                  [Q(parking__contains=parking) for parking in item_list['parking']] + \
                  [Q(building_area__contains=building_area) for building_area in item_list['building_area']] + \
                  [Q(use_property__contains=use_property) for use_property in item_list['use_property']] + \
                  [Q(zoning__contains=zoning) for zoning in item_list['zoning']] + \
                  [Q(residential_unit__contains=residential_unit) for residential_unit in item_list['residential_unit']] + \
                  [Q(business_type__contains=business_type) for business_type in item_list['business_type']] + \
                  [Q(intergenerational__contains=intergenerational) for intergenerational in item_list['intergenerational']] + \
                  [Q(building_style__contains=building_style) for building_style in item_list['building_style']] + \
                  [Q(pool__contains=pool) for pool in item_list['pool']] + \
                  [Q(condominium__contains=condominium) for condominium in item_list['condominium']] + \
                  [Q(gross_area__contains=gross_area) for gross_area in item_list['gross_area']] + \
                  [Q(net_area__contains=net_area) for net_area in item_list['net_area']] + \
                  [Q(property_current_active__contains=property_current_active) for property_current_active in item_list['property_current_active']]

        query = reduce(lambda x, y: x & y, queries)

        if item_list:
            request.session['item_list'] = item_list
        centris = Centris.objects.filter(query)
        if len(centris) > 1:

            response_str = 'There are {count} centris.'.format(count=len(centris))

        # for centris_item in centris_items:
        #     centris = centris_item

        # return HttpResponse(response_str)
        paginator = Paginator(centris, 15)
        page = request.GET.get('page')

        centris = paginator.get_page(page)
        context = {
            'centris': centris
        }

        return render(request, 'interface/index.html', context=context)
    else:
        item_list = request.session.get('item_list')
        queries = [Q(pid__contains=pid) for pid in item_list['pid']] + \
                  [Q(centris_title__contains=title) for title in item_list['centris_title']] + \
                  [Q(address__contains=address) for address in item_list['address']] + \
                  [Q(price__contains=price) for price in item_list['price']] + \
                  [Q(workscore__contains=workscore) for workscore in item_list['workscore']] + \
                  [Q(beds_baths__contains=beds_baths) for beds_baths in item_list['beds_baths']] + \
                  [Q(geo_cordinates__contains=geo_cordinates) for geo_cordinates in item_list['geo_cordinates']] + \
                  [Q(description__contains=description) for description in item_list['description']] + \
                  [Q(agent_name__contains=agent_name) for agent_name in item_list['agent_name']] + \
                  [Q(built_year__contains=built_year) for built_year in item_list['built_year']] + \
                  [Q(construction_year__contains=construction_year) for construction_year in
                   item_list['construction_year']] + \
                  [Q(available_area__contains=available_area) for available_area in item_list['available_area']] + \
                  [Q(lot_area__contains=lot_area) for lot_area in item_list['lot_area']] + \
                  [Q(operation_type__contains=operation_type) for operation_type in item_list['operation_type']] + \
                  [Q(fireplace_stove__contains=fireplace_stove) for fireplace_stove in item_list['fireplace_stove']] + \
                  [Q(additional_features__contains=additional_features) for additional_features in
                   item_list['additional_features']] + \
                  [Q(potential_gross_revenue__contains=potential_gross_revenue) for potential_gross_revenue in
                   item_list['potential_gross_revenue']] + \
                  [Q(main_unit__contains=main_unit) for main_unit in item_list['main_unit']] + \
                  [Q(residential_units__contains=residential_units) for residential_units in
                   item_list['residential_units']] + \
                  [Q(unit_number__contains=unit_number) for unit_number in item_list['unit_number']] + \
                  [Q(parking__contains=parking) for parking in item_list['parking']] + \
                  [Q(building_area__contains=building_area) for building_area in item_list['building_area']] + \
                  [Q(use_property__contains=use_property) for use_property in item_list['use_property']] + \
                  [Q(zoning__contains=zoning) for zoning in item_list['zoning']] + \
                  [Q(residential_unit__contains=residential_unit) for residential_unit in
                   item_list['residential_unit']] + \
                  [Q(business_type__contains=business_type) for business_type in item_list['business_type']] + \
                  [Q(intergenerational__contains=intergenerational) for intergenerational in
                   item_list['intergenerational']] + \
                  [Q(building_style__contains=building_style) for building_style in item_list['building_style']] + \
                  [Q(pool__contains=pool) for pool in item_list['pool']] + \
                  [Q(condominium__contains=condominium) for condominium in item_list['condominium']] + \
                  [Q(gross_area__contains=gross_area) for gross_area in item_list['gross_area']] + \
                  [Q(net_area__contains=net_area) for net_area in item_list['net_area']] + \
                  [Q(property_current_active__contains=property_current_active) for property_current_active in
                   item_list['property_current_active']]

        query = reduce(lambda x, y: x & y, queries)

        centris = Centris.objects.filter(query)
        paginator = Paginator(centris, 15)
        page = request.GET.get('page')

        centris = paginator.get_page(page)
        context = {
            'centris': centris
        }
        return render(request, 'interface/index.html', context=context)


def delete(request):
    id = int(request.GET.get('id'))
    centris = Centris.objects.get(pk=id)
    centris.delete()
    return JsonResponse({'success': 'success'})
