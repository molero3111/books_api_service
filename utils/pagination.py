from rest_framework.pagination import PageNumberPagination


class PaginationSettings(PageNumberPagination):
    page_size = 50  # sets the default number of records to retrieve

    # sets the query param name in case the request needs
    # to show fewer records than default value
    page_size_query_param = 'page_size'

    # sets maximum number of records to retrieve if it is
    # specified it on the query param as page_size
    max_page_size = 50
