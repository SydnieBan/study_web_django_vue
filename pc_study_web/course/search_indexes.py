from haystack import indexes
from course.models import Course

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Course
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
        # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())