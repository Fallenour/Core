from django.conf import settings
from django.views.generic import TemplateView
from django.urls import path, include
from UI import views
from UI.views import IndexView, TemplateView




###Django Framework

from rest_framework import routers


router = routers.DefaultRouter()
router.register('UI', views.UIAPIView)

### Chart Data ###

from .views import ChartData
from .views import ChartData2

urlpatterns = [

    # API Call for Chart View for ChartData
    path('api/chart/data/', ChartData.as_view()),

    # API Call for Chart View for Overview Dashboard
    path('api/chart/data2/', ChartData2.as_view()),

    # /ui/

    # Indexes
    path('', TemplateView.as_view(template_name='ui/Focus/base.html'), name='index1'),  # this one is OK with '' it means end of the string

    # Dashboards
    path('docops/', views.docops, name='docops'),
    path('ops/', views.ops, name='ops'),
    path('mgmtops/', views.mgmtops, name='mgmtops'),
    path('spreadops/', views.spreadops, name='spreadops'),
    path('overview/', TemplateView.as_view(template_name='ui/Focus/overview.html'), name='primary'),

    # Charts
    path('charts-flot/', TemplateView.as_view(template_name='ui/Focus/chart-flot.html'), name='chartsflot'),
    path('charts-knob/', TemplateView.as_view(template_name='ui/Focus/chart-knob.html'), name='chartsknob'),
    path('charts-morris/', TemplateView.as_view(template_name='ui/Focus/chart-morris.html'), name='chartsmorris'),
    path('charts-js/', TemplateView.as_view(template_name='ui/Focus/chartjs.html'), name='chartsjs'),
    path('chartist/', TemplateView.as_view(template_name='ui/Focus/chartist.html'), name='chartist'),
    path('charts-peity/', TemplateView.as_view(template_name='ui/Focus/chart-peity.html'), name='chartspeity'),
    path('charts-sparkle/', TemplateView.as_view(template_name='ui/Focus/chart-sparkline.html'), name='chartssparkline'),

    # UI Elements
    path('ui-elements-typography/', TemplateView.as_view(template_name='ui/Focus/ui-typography.html'), name='uielementstypography'),
    path('ui-elements-alerts/', TemplateView.as_view(template_name='ui/Focus/ui-alerts.html'), name='uielementsalerts'),
    path('ui-elements-button/', TemplateView.as_view(template_name='ui/Focus/ui-button.html'), name='uielementsbutton'),
    path('ui-elements-dropdown/', TemplateView.as_view(template_name='ui/Focus/ui-dropdown.html'), name='uielementsdropdown'),
    path('ui-elements-list-group/', TemplateView.as_view(template_name='ui/Focus/ui-list-group.html'), name='uielementslistgroup'),
    path('ui-elements-progressbar/', TemplateView.as_view(template_name='ui/Focus/ui-progressbar.html'), name='uielementsprogressbar'),

    # UI Components
    path('ui-components-calendar/', TemplateView.as_view(template_name='ui/Focus/uc-calendar.html'), name='uicomponentscalendar'),
    path('ui-components-carousel/', TemplateView.as_view(template_name='ui/Focus/uc-carousel.html'), name='uicomponentscarousel'),
    path('ui-components-weather/', TemplateView.as_view(template_name='ui/Focus/uc-weather.html'), name='uicomponentsweather'),
    path('ui-components-datamap/', TemplateView.as_view(template_name='ui/Focus/uc-datamap.html'), name='uicomponentsdatamap'),
    path('ui-components-todo-list/', TemplateView.as_view(template_name='ui/Focus/uc-todo-list.html'), name='uicomponentstodo'),
    path('ui-components-sweetalert/', TemplateView.as_view(template_name='ui/Focus/uc-sweetalert.html'), name='uicomponentssweetalert'),
    path('ui-components-toastr/', TemplateView.as_view(template_name='ui/Focus/uc-toastr.html'), name='uicomponentstoastr'),
    path('ui-components-rangesliderbasic/', TemplateView.as_view(template_name='ui/Focus/uc-range-slider-basic.html'), name='uicomponentsrangesliderbasic'),
    path('ui-components-rangeslideradvance/', TemplateView.as_view(template_name='ui/Focus/uc-range-slider-advance.html'), name='uicomponentsrangeslideradvance'),
    path('ui-components-nestable/', TemplateView.as_view(template_name='ui/Focus/uc-nestable.html'), name='uicomponentsnestable'),
    path('ui-components-bar-rating/', TemplateView.as_view(template_name='ui/Focus/uc-rating-bar-rating.html'), name='uicomponentsbarrating'),
    path('ui-components-jRate/', TemplateView.as_view(template_name='ui/Focus/uc-rating-jRate.html'), name='uicomponentsjrate'),

    # Tables
    path('ui-tables-basic/', TemplateView.as_view(template_name='ui/Focus/table-basic.html'), name='tablebasic'),
    path('ui-tables-datatableexport/', TemplateView.as_view(template_name='ui/Focus/table-export.html'), name='tableexport'),
    path('ui-tables-datatablerowselect/', TemplateView.as_view(template_name='ui/Focus/table-row-select.html'), name='tablerow'),
    path('ui-tables-datatablejsgrid/', TemplateView.as_view(template_name='ui/Focus/table-jsgrid.html'), name='tablejsgrid'),

    # Icons
    path('ui-icons-themify/', TemplateView.as_view(template_name='ui/Focus/font-themify.html'), name='icons-themify'),

    # Maps
    path('ui-maps-vector/', TemplateView.as_view(template_name='ui/Focus/vector-map.html'), name='maps-vector'),

    # Forms
    path('ui-forms-basic/', TemplateView.as_view(template_name='ui/Focus/form-basic.html'), name='forms-basic'),
    path('ui-forms-validation/', TemplateView.as_view(template_name='ui/Focus/form-validation.html'), name='forms-validation'),

    # Tasks
    path('calender/', TemplateView.as_view(template_name='ui/Focus/app-event-calender.html'), name='calender'),
    path('email/', TemplateView.as_view(template_name='ui/Focus/app-email.html'), name='appemail'),

    # Django Rest Framework API path
    path('api/', include(router.urls)),

    # Misc
    path('profile/', TemplateView.as_view(template_name='ui/Focus/app-profile.html'), name='appprofile'),
    path('widgets/', TemplateView.as_view(template_name='ui/Focus/app-widget-card.html'), name='appwidget'),

    # Celery Testing
#   path('cel/', PhotoView.as_view(), name="celeryhome"),
#   path('feedback/', FeedbackView.as_view(), name="celeryfeedback"),
]