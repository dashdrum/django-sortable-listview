from sortable_listview import SortableListView
from .models import Article

class ArticleListView(SortableListView):
    allowed_sort_fields = {'title': {'default_direction': '',
                                     'verbose_name': 'Title',
                                     'order': 1},
                           'published_date': {'default_direction': '-',
                                              'verbose_name': 'Published On',
                                              'order': 2}}
    default_sort_field = 'published_date'
    paginate_by = 5
    template_name = 'list.html'
    model = Article
