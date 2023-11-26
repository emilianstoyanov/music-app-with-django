from django import forms


class AlbumBaseForm(forms.Form):
    album_name = forms.CharField(
        label='Album Name:',
        max_length=30,
        required=True,
    )

    image_url = forms.URLField(
        label='Image URL:',
        required=True,
    )

    price = forms.DecimalField(
        label='Price:',
        min_value=0.0,
        required=True,
    )


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    pass
