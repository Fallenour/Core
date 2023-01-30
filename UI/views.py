from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# from django.http import JsonResponse12
from django.db.models import Q
from django.template import loader
from django.urls import reverse_lazy


from .models import System, Event, Spread


##################################################################################################
#                                 Django REST Framework                                          #
##################################################################################################
from rest_framework import viewsets
from .serializers import SystemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


##################################################################################################
#                                 Backend API Data Calls                                         #
##################################################################################################
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        event_count = Event.objects.all().count()
        ops_team_chart_event_count = Event.objects.all().count()*10
        ops_radar_chart_event_count = Event.objects.all().count()*10
        ops_doughut_chart_event_count = Event.objects.all().count() * 45
        ops_line_chart_event_count = Event.objects.all().count() * 35
        ops_pie_chart_event_count = Event.objects.all().count() * 15
        ops_polar_chart_event_count = Event.objects.all().count() * 15
        ops_sales_chart_event_count = Event.objects.all().count() * 15
        ops_singlebar_chart_event_count = Event.objects.all().count() * 15
        labels = ["Events", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [event_count, 23, 2, 3, 12, 2]
        ops_team_chart_labels = ["2015", "2016", "2017", "2018", "2019", "2020", "2021" ]
        ops_team_chart_default_items = [ops_team_chart_event_count, 2, 3, 12, 2, 4, 7]
        ops_radar_chart_labels = []
        ops_radar_chart_default_items = [ops_radar_chart_event_count, 59, 66, 45, 56, 55, 40 ]
        ops_doughut_chart_labels = []
        ops_doughut_chart_default_items = [ops_doughut_chart_event_count, 25, 20, 10  ]
        ops_line_chart_labels = []
        ops_line_chart_default_items = [ops_line_chart_event_count, 44, 67, 43, 76, 45, 12  ]
        ops_pie_chart_labels = []
        ops_pie_chart_default_items = [ops_pie_chart_event_count, 25, 20, 10 ]
        ops_polar_chart_labels = []
        ops_polar_chart_default_items = [ops_polar_chart_event_count, 18, 9, 6, 19]
        ops_sales_chart_labels = []
        ops_sales_chart_default_items = [ops_sales_chart_event_count, 30, 10, 120, 50, 63, 10]
        ops_singlebar_chart_labels = []
        ops_singlebar_chart_default_items = [ops_singlebar_chart_event_count, 55, 75, 81, 56, 55, 40 ]
        data = {
                "labels": labels,
                "default": default_items,
                "ops_team_chart_labels": ops_team_chart_labels,
                "ops_team_chart_default_items": ops_team_chart_default_items,
                "ops_radar_chart_labels": ops_radar_chart_labels,
                "ops_radar_chart_default_items": ops_radar_chart_default_items,
                "ops_doughut_chart_labels": ops_doughut_chart_labels,
                "ops_doughut_chart_default_items": ops_doughut_chart_default_items,
                "ops_line_chart_labels": ops_line_chart_labels,
                "ops_line_chart_default_items": ops_line_chart_default_items,
                "ops_pie_chart_labels": ops_pie_chart_labels,
                "ops_pie_chart_default_items": ops_pie_chart_default_items,
                "ops_polar_chart_labels": ops_polar_chart_labels,
                "ops_polar_chart_default_items": ops_polar_chart_default_items,
                "ops_sales_chart_labels": ops_sales_chart_labels,
                "ops_sales_chart_default_items": ops_sales_chart_default_items,
                "ops_singlebar_chart_labels": ops_singlebar_chart_labels,
                "ops_singlebar_chart_default_items": ops_singlebar_chart_default_items,
        }
        return Response(data)


class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        event_count = Event.objects.all().count()
        ops_team_chart_event_count = Event.objects.all().count()*10
        ops_radar_chart_event_count = Event.objects.all().count()*10
        ops_doughut_chart_event_count = Event.objects.all().count() * 45
        ops_line_chart_event_count = Event.objects.all().count() * 35
        ops_pie_chart_event_count = Event.objects.all().count() * 15
        ops_polar_chart_event_count = Event.objects.all().count() * 15
        ops_sales_chart_event_count = Event.objects.all().count() * 15
        ops_singlebar_chart_event_count = Event.objects.all().count() * 15
        labels = ["Events", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [event_count, 23, 2, 3, 12, 2]
        ops_team_chart_labels = ["2015", "2016", "2017", "2018", "2019", "2020", "2021" ]
        ops_team_chart_default_items = [ops_team_chart_event_count, 2, 3, 12, 2, 4, 7]
        ops_radar_chart_labels = []
        ops_radar_chart_default_items = [ops_radar_chart_event_count, 59, 66, 45, 56, 55, 40 ]
        ops_doughut_chart_labels = []
        ops_doughut_chart_default_items = [ops_doughut_chart_event_count, 25, 20, 10  ]
        ops_line_chart_labels = []
        ops_line_chart_default_items = [ops_line_chart_event_count, 44, 67, 43, 76, 45, 12  ]
        ops_pie_chart_labels = []
        ops_pie_chart_default_items = [ops_pie_chart_event_count, 25, 20, 10 ]
        ops_polar_chart_labels = []
        ops_polar_chart_default_items = [ops_polar_chart_event_count, 18, 9, 6, 19]
        ops_sales_chart_labels = []
        ops_sales_chart_default_items = [ops_sales_chart_event_count, 30, 10, 120, 50, 63, 10]
        ops_singlebar_chart_labels = []
        ops_singlebar_chart_default_items = [ops_singlebar_chart_event_count, 55, 75, 81, 56, 55, 40 ]
        data = {
                "labels": labels,
                "default": default_items,
                "ops_team_chart_labels": ops_team_chart_labels,
                "ops_team_chart_default_items": ops_team_chart_default_items,
                "ops_radar_chart_labels": ops_radar_chart_labels,
                "ops_radar_chart_default_items": ops_radar_chart_default_items,
                "ops_doughut_chart_labels": ops_doughut_chart_labels,
                "ops_doughut_chart_default_items": ops_doughut_chart_default_items,
                "ops_line_chart_labels": ops_line_chart_labels,
                "ops_line_chart_default_items": ops_line_chart_default_items,
                "ops_pie_chart_labels": ops_pie_chart_labels,
                "ops_pie_chart_default_items": ops_pie_chart_default_items,
                "ops_polar_chart_labels": ops_polar_chart_labels,
                "ops_polar_chart_default_items": ops_polar_chart_default_items,
                "ops_sales_chart_labels": ops_sales_chart_labels,
                "ops_sales_chart_default_items": ops_sales_chart_default_items,
                "ops_singlebar_chart_labels": ops_singlebar_chart_labels,
                "ops_singlebar_chart_default_items": ops_singlebar_chart_default_items,
        }
        return Response(data)


##################################################################################################
#                                      UI Views                                            #
##################################################################################################
class IndexView(TemplateView):
    template_name = 'ui/Focus/templates/ui/Focus/base.html'
    #    model = Products
    #    paginate_by = 50
    #    permissions_required = ('polls.view_choice', 'polls.change_choice')

class PrimaryView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/overview.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')


class ChartsFlotView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chart-flot.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartsKnobView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chart-knob.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartsMorrisView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chart-morris.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartsJSView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chartjs.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartistView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chartist.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartsPeityView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chart-peity.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ChartsSparkleView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/chart-sparkline.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class CalenderView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/app-event-calender.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class AppEmailView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/app-email.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class AppProfileView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/app-profile.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class AppWidgetView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/app-widget-card.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsTypographyView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-typography.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsAlertsView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-alerts.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsButtonView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-button.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsDropdownView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-dropdown.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsListGroupView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-list-group.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIElementsProgressBarView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/ui-progressbar.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentCalendarView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-calendar.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentCarouselView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-carousel.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentWeatherView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-weather.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentDatamapView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-datamap.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentDatamapView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-datamap.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentToDoView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-todo-list.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentSweetAlertView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-sweetalert.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentToastrView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-toastr.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentRangeSliderBasicView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-range-slider-basic.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentRangeSliderAdvancedView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-range-slider-advance.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentNestableView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-nestable.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentBarRatingView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-rating-bar-rating.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentBarRatingView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-rating-bar-rating.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class UIComponentJRateView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/uc-rating-jRate.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class TableBasicView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/table-basic.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class TableDatatableExportView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/table-export.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class TableDatatableRowView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/table-row-select.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class TablejsgridView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/table-jsgrid.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class FontThemifyView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/font-themify.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class MapBasicView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/gmaps.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class MapVectorView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/vector-map.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class BasicFormView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/form-basic.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')

class ValidatorFormView(TemplateView):  # mixin comes first, View is not needed if you have TemplateView that is already child of View
    template_name = "ui/Focus/form-validation.html"
#    model = Products
#    paginate_by = 50
#    permissions_required = ('polls.view_choice', 'polls.change_choice')



##################################################################################################
#                                  UI Data Functions                                       #
##################################################################################################
class UIAPIView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = SystemSerializer


def docops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/docops.html', {
            'event_list': events,
        }) #, context)

def ops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/ops.html', {
            'event_list': events,
        }) #, context)

def mgmtops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        events = Event.objects.all()
        return render(request, 'ui/Focus/mgmtops.html', {
            'event_list': events,
        }) #, context)

def spreadops(request):
#    if not request.user.is_authenticate:
#        return render(request, 'ui/Focus/login.html')
#    else:
        spread = Spread.objects.all()
        return render(request, 'ui/Focus/spreadops.html', {
            'spread_list': spread,
        }) #, context)

def spreads(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'ui/Focus/login.html')
    else:
        try:
            spread_ids = []
            for spread in Spread.objects.filter(spread=request.spread):
                for spread in spread.event_set.all():
                    spread_ids.append(spread.pk)
            spread_events = Spread.objects.filter(pk__in=spread_ids)
            if filter_by == 'processed':
                spread_events = spread_events.filter(is_processed=True)
        except Spread.DoesNotExist:
            spread_events = []
        return render(request, 'ui/Focus/galaxyops.html', {
            'spread_list': spread_events,
            'filter_by': filter_by,
        })

def events(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'ui/Focus/login.html')
    else:
        try:
            event_ids = []
            for System in System.objects.filter(event=request.event):
                for event in system.event_set.all():
                    event_ids.append(event.pk)
            system_events = Event.objects.filter(pk__in=event_ids)
            if filter_by == 'processed':
                system_events = system_events.filter(is_processed=True)
        except System.DoesNotExist:
            system_events = []
        return render(request, 'ui/Focus/galaxyops.html', {
            'event_list': system_events,
            'filter_by': filter_by,
        })

def celery(request):
    if not request.user.is_authenticated():
        return render(request, 'ui/Focus/login.html')
    else:
        return render(request, 'ui/Focus/base.html') #, context)

def celeryfeedback(request):
    if not request.user.is_authenticated():
       return render(request, 'ui/Focus/login.html')
    else:
        return render(request, 'ui/Focus/base.html') #, context)