from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import UserViewSet, CategoryViewSet, EventViewSet, OrganizerViewSet, PaymentViewSet, TicketViewSet, \
    EventTicketViewSet, EventReviewViewSet, ReviewReplyViewSet, UserReviewViewSet #, StatisticsViewSet
from . import tests

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'events', EventViewSet, basename='event')
router.register(r'organizers', OrganizerViewSet, basename='organizer')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'events/(?P<event_id>\d+)/tickets', EventTicketViewSet, basename='event-ticket')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'my-reviews', UserReviewViewSet, basename='my-reviews')
# router.register(r'statistics', StatisticsViewSet, basename='statistics')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', tests.home, name='home'),
    path('home/logout/', tests.logout_tests, name='logout'),
    path('payments/ipn/', PaymentViewSet.as_view({
        'get': 'payment_ipn',
        'post': 'payment_ipn'
    }), name='payment_ipn'),
    path('payments/return/', PaymentViewSet.as_view({
        'get': 'payment_return'
    }), name='payment_return'),
    path('events/<int:event_id>/reviews/', EventReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='event-reviews'),

    path('reviews/<int:review_id>/replies/', ReviewReplyViewSet.as_view({
        'post': 'create'
    }), name='review-replies'),
]
