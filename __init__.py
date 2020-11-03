# Use 'alpha', 'beta', 'rc' or 'final' as the 4th element to indicate release type.
VERSION = (2, 1, 0, 'final')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        version = '%s%s' % (version, mapping[VERSION[3]])
        if len(VERSION) == 5:
            version = '%s%s' % (version, VERSION[4])
    return version


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'oscar.config.Shop',
    'apps.analytics.apps.AnalyticsConfig',
    'apps.checkout.apps.CheckoutConfig',
    'apps.address.apps.AddressConfig',
    'apps.shipping.apps.ShippingConfig',
    'apps.catalogue.apps.CatalogueConfig',
    'apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'apps.communication.apps.CommunicationConfig',
    'apps.partner.apps.PartnerConfig',
    'apps.basket.apps.BasketConfig',
    'apps.payment.apps.PaymentConfig',
    'offer.apps.OfferConfig',
    'apps.order.apps.OrderConfig',
    'apps.customer.apps.CustomerConfig',
    'apps.search.apps.SearchConfig',
    'apps.voucher.apps.VoucherConfig',
    'apps.wishlists.apps.WishlistsConfig',
    'qpps.dashboard.apps.DashboardConfig',
    'apps.dashboard.reports.apps.ReportsDashboardConfig',
    'apps.dashboard.users.apps.UsersDashboardConfig',
    'apps.dashboard.orders.apps.OrdersDashboardConfig',
    'apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'apps.dashboard.offers.apps.OffersDashboardConfig',
    'apps.dashboard.partners.apps.PartnersDashboardConfig',
    'apps.dashboard.pages.apps.PagesDashboardConfig',
    'apps.dashboard.ranges.apps.RangesDashboardConfig',
    'apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'django_tables2',
]


default_app_config = 'oscar.config.Shop'
