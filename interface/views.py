from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Centris
from django.http import JsonResponse
from functools import reduce
from operator import __or__ as OR

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
    keys = ["pid", "centris_title", "centris_title_business", "centris_title_for", "address", "price", "workscore", "beds_baths", "geo_cordinates", "description",
            "agent_name", "built_year", "construction_year", "available_area", "lot_area",
            "operation_type",
            "fireplace_stove", "additional_features", "potential_gross_revenue", "main_unit", "residential_units",
            "unit_number", "parking", "building_area", "use_property", "zoning",
            "residential_unit",
            "business_type", "intergenerational", "building_style", "pool", "condominium", "gross_area",
            "net_area", "property_current_active"]

    if request.method == 'POST':
        item_list = {}
        for key in keys:
            item_list[key] = request.POST.getlist(key)
        # if (item_list['centris_title'] is []):
        # if (item_list['centris_title_business'][0] == "Commercial"):
        #     centris = Centris.objects.filter(reduce(lambda x, y: x & y, [Q(centris_title__contains='Commercial') | Q(centris_title__contains='Industrial') & Q(centris_title__contains=item_list['centris_title_for'][0])]))
                # if item_list:
                #     request.session['item_list'] = item_list
                # paginator = Paginator(centris, 15)
                # page = request.GET.get('page')
                #
                # centris = paginator.get_page(page)
                # context = {
                #     'centris': centris
                # }

                # return render(request, 'interface/index.html', context=context)
        # else:
        #     centris = Centris.objects.filter(reduce(lambda x, y: x & y, [~Q(centris_title__contains='Commercial') & ~Q(centris_title__contains='Industrial') & Q(centris_title__contains=item_list['centris_title_for'][0])]))
                # if item_list:
                #     request.session['item_list'] = item_list
                # paginator = Paginator(centris, 15)
                # page = request.GET.get('page')
                #
                # centris = paginator.get_page(page)
                # context = {
                #     'centris': centris
                # }
                #
                # return render(request, 'interface/index.html', context=context)
        # else:

        if (item_list['centris_title_business'][0] == "Commercial"):
            centris = Centris.objects.filter(reduce(lambda x, y: x & y, [
                Q(centris_title__contains='Commercial') | Q(centris_title__contains='Industrial') & Q(
                    centris_title__contains=item_list['centris_title_for'][0])]))
        else:
            centris = Centris.objects.filter(reduce(lambda x, y: x & y, [
                ~Q(centris_title__contains='Commercial') & ~Q(centris_title__contains='Industrial') & Q(
                    centris_title__contains=item_list['centris_title_for'][0])]))

        # centris_res = centris.filter(reduce(OR, [Q(centris_title__contains=title) for title in item_list['centris_title']]))
        # if item_list:
        #     request.session['item_list'] = item_list
        # paginator = Paginator(centris_res, 15)
        # page = request.GET.get('page')
        #
        # centris_res = paginator.get_page(page)
        # context = {
        #     'centris': centris_res
        # }
        #
        #     return render(request, 'interface/index.html', context=context)
            queries = [Q(pid__contains=pid) for pid in item_list['pid']] + \
                      [Q(address__contains=address) for address in item_list['address']] + \
                      [Q(price__contains=price) for price in item_list['price']] + \
                      [Q(workscore__contains=workscore) for workscore in item_list['workscore']] + \
                      [Q(beds_baths__contains=beds_baths) for beds_baths in item_list['beds_baths']] + \
                      [Q(geo_cordinates__contains=geo_cordinates) for geo_cordinates in
                       item_list['geo_cordinates']] + \
                      [Q(description__contains=description) for description in item_list['description']] + \
                      [Q(agent_name__contains=agent_name) for agent_name in item_list['agent_name']] + \
                      [Q(built_year__contains=built_year) for built_year in item_list['built_year']] + \
                      [Q(construction_year__contains=construction_year) for construction_year in
                       item_list['construction_year']] + \
                      [Q(available_area__contains=available_area) for available_area in
                       item_list['available_area']] + \
                      [Q(lot_area__contains=lot_area) for lot_area in item_list['lot_area']] + \
                      [Q(operation_type__contains=operation_type) for operation_type in
                       item_list['operation_type']] + \
                      [Q(fireplace_stove__contains=fireplace_stove) for fireplace_stove in
                       item_list['fireplace_stove']] + \
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
                      [Q(building_style__contains=building_style) for building_style in
                       item_list['building_style']] + \
                      [Q(pool__contains=pool) for pool in item_list['pool']] + \
                      [Q(condominium__contains=condominium) for condominium in item_list['condominium']] + \
                      [Q(gross_area__contains=gross_area) for gross_area in item_list['gross_area']] + \
                      [Q(net_area__contains=net_area) for net_area in item_list['net_area']] + \
                      [Q(property_current_active__contains=property_current_active) for property_current_active in
                       item_list['property_current_active']]

        # query = reduce(lambda x, y: x & y, queries)

        queries = [Q(centris_title__contains=title) for title in item_list['centris_title']]

        #
        centris_res = centris.filter(reduce(OR, queries))

        if item_list:
            request.session['item_list'] = item_list

        if len(centris_res) > 1:

            response_str = 'There are {count} centris.'.format(count=len(centris))

        paginator = Paginator(centris_res, 15)
        page = request.GET.get('page')

        centris_res = paginator.get_page(page)
        context = {
            'centris': centris_res
        }

        return render(request, 'interface/index.html', context=context)
    else:
        item_list = request.session.get('item_list')
        if (item_list['centris_title_business'][0] == "Commercial"):
            centris = Centris.objects.filter(reduce(lambda x, y: x & y, [
                Q(centris_title__contains='Commercial') | Q(centris_title__contains='Industrial') & Q(
                    centris_title__contains=item_list['centris_title_for'][0])]))
            paginator = Paginator(centris, 15)
            page = request.GET.get('page')

            centris = paginator.get_page(page)
            context = {
                'centris': centris
            }

            return render(request, 'interface/index.html', context=context)
        else:
            centris = Centris.objects.filter(reduce(lambda x, y: x & y, [
                ~Q(centris_title__contains='Commercial') & ~Q(centris_title__contains='Industrial') & Q(
                    centris_title__contains=item_list['centris_title_for'][0])]))
            paginator = Paginator(centris, 15)
            page = request.GET.get('page')

            centris = paginator.get_page(page)
            context = {
                'centris': centris
            }

            return render(request, 'interface/index.html', context=context)
        if (item_list['centris_title'][0] is not []):
            centris_res = centris.filter(
                reduce(OR, [Q(centris_title__contains=title) for title in item_list['centris_title']]))
            paginator = Paginator(centris_res, 15)
            page = request.GET.get('page')

            centris_res = paginator.get_page(page)
            context = {
                'centris': centris_res
            }

            return render(request, 'interface/index.html', context=context)

        queries = [Q(pid__contains=pid) for pid in item_list['pid']] + \
                  [Q(address__contains=address) for address in item_list['address']] + \
                  [Q(price__contains=price) for price in item_list['price']] + \
                  [Q(workscore__contains=workscore) for workscore in item_list['workscore']] + \
                  [Q(beds_baths__contains=beds_baths) for beds_baths in item_list['beds_baths']] + \
                  [Q(geo_cordinates__contains=geo_cordinates) for geo_cordinates in
                   item_list['geo_cordinates']] + \
                  [Q(description__contains=description) for description in item_list['description']] + \
                  [Q(agent_name__contains=agent_name) for agent_name in item_list['agent_name']] + \
                  [Q(built_year__contains=built_year) for built_year in item_list['built_year']] + \
                  [Q(construction_year__contains=construction_year) for construction_year in
                   item_list['construction_year']] + \
                  [Q(available_area__contains=available_area) for available_area in
                   item_list['available_area']] + \
                  [Q(lot_area__contains=lot_area) for lot_area in item_list['lot_area']] + \
                  [Q(operation_type__contains=operation_type) for operation_type in
                   item_list['operation_type']] + \
                  [Q(fireplace_stove__contains=fireplace_stove) for fireplace_stove in
                   item_list['fireplace_stove']] + \
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
                  [Q(building_style__contains=building_style) for building_style in
                   item_list['building_style']] + \
                  [Q(pool__contains=pool) for pool in item_list['pool']] + \
                  [Q(condominium__contains=condominium) for condominium in item_list['condominium']] + \
                  [Q(gross_area__contains=gross_area) for gross_area in item_list['gross_area']] + \
                  [Q(net_area__contains=net_area) for net_area in item_list['net_area']] + \
                  [Q(property_current_active__contains=property_current_active) for property_current_active in
                   item_list['property_current_active']]

        queries_title = [Q(centris_title__contains=title) for title in item_list['centris_title']]
        # # query = reduce(lambda x, y: x & y, queries)
        centris_res = centris.filter(reduce(OR, queries_title))
        #
        # centris.filter(reduce(lambda x, y: x & y, queries))

        paginator = Paginator(centris_res, 15)
        page = request.GET.get('page')

        centris_res = paginator.get_page(page)
        context = {
            'centris': centris_res
        }
        return render(request, 'interface/index.html', context=context)


def delete(request):
    id = int(request.GET.get('id'))
    centris = Centris.objects.get(pk=id)
    centris.delete()
    return JsonResponse({'success': 'success'})
