from django.urls import path,include
from rest_framework import routers
from . import views
from django.contrib.auth.decorators import login_required
router = routers.DefaultRouter()
router.register(r'hostel', views.HostelView)
router.register(r'mess', views.MessView)
router.register(r'student', views.StudentView)
router.register(r'hostel-student', views.HostelStudentView)
router.register(r'attendance', views.AttendanceView)
router.register(r'year',views.YearView)
# router.register(r'application-setting',views.ApplicationSettingsView)
# router.register(r'log-entry',views.LogEntryView)
# router.register(r'level',views.LevelView)
# router.register(r'organization-division-location-department',views.OrganizationDivisionLocationDepartmentView)
# router.register(r'organization-division',views.OrganizationDivisionView)
# router.register(r'organization-designation-level',views.OrganizationDesignationLevelView)
# router.register(r'user-organization',views.UserOrganizationView)
# router.register(r'organization-division-location',views.OrganizationDivisionLocationView)
# router.register(r'subscribed-apps',views.SubscribedAppsView)
# router.register(r'roles-user',views.OrganizationRolesUserView)
urlpatterns = [
	path(r'', include(router.urls)),
	path(r'save-attendance/',views.SaveAttendance.as_view()),
   
]
