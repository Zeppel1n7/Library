from abc import ABC, abstractmethod

from django.db import transaction


class FileUploadMixin(ABC):
    file_field_name = 'reviews'

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save()
        for file in self.request.FILES.getlist(self.file_field_name):
            self.create_related_object(file)

        return super().form_valid(form)

    @abstractmethod
    def create_related_object(self, file):
        raise NotImplementedError("Необходимо переопределить метод create_related_object.")
