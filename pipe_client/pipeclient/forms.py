from django import forms

RESOLUTION = [('1280x720', '1280 x 720'), ('1440x1080', '1440 X 1080'), ('960x720', '960 X 720'),
              ('1280x1080', '1280 X 1080'), ('1920x1080', '1920 X 1080'), ('3840x2160', '3840 X 2160'),
              ('2048x1556', '2048 X 1556'), ('4096x3112', '4096 X 3112'), ('720x480', '720 X 480'),
              ('720x576', '720 X 576')]


class CreateProjectForm(forms.Form):

    name = forms.CharField(label='Project Name')
    code = forms.CharField(label='Project Code')
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
    )

    fps = forms.ChoiceField(label='FPS', choices=[('24', '24'), ('25', '25'), ('29', '29'), ('30', '30')],
                            required=False)
    resolution = forms.ChoiceField(label='Resolution',
                                   choices=RESOLUTION, required=False)
    project_type = forms.ChoiceField(choices=[('film', 'Film'), ('series', 'Series')])
    project_path = forms.CharField(label='Project Path')
    active = forms.CharField(label='Active', required=False)
    added_by = forms.CharField(label='Added By', required=False)


class EditProjectForm(forms.Form):

    name = forms.CharField(label='Project Name')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    fps = forms.ChoiceField(label='FPS', choices=[('24', '24'), ('25', '25'), ('29', '29'), ('30', '30')],
                            required=False)
    resolution = forms.ChoiceField(label='Resolution',
                                   choices=RESOLUTION, required=False)
    url = forms.CharField(widget=forms.HiddenInput())


# class DeleteProjectForm(forms.Form):
#     name = forms.CharField(label='Project Name')
#     code = forms.CharField(label='Project Code')
#     url = forms.CharField(widget=forms.HiddenInput())


class CreateAssetForm(forms.Form):
    name = forms.CharField(label='Asset Name')
    asset_type = forms.ChoiceField(label='Asset Type', choices=[('character', 'Character'), ('prop', 'Prop'), ('bg', 'BG'), ('fx', 'FX')])
    project = forms.CharField(label='Project Name')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    description = forms.CharField(label='Description')
    added_by = forms.CharField(label='Added By')
    active = forms.CharField(label='Active')


class CreateSequenceForm(forms.Form):
    name = forms.CharField(label='Sequence Name')
    added_by = forms.CharField(label='Added By')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    project = forms.CharField(label='Project Name')
    description = forms.CharField(label='Description')
    active = forms.CharField(label='Active')


class CreateShotForm(forms.Form):
    name = forms.CharField(label='Sequence Name')
    added_by = forms.CharField(label='Added By')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    sequence = forms.CharField(label='Sequence')
    description = forms.CharField(label='Description')
    active = forms.CharField(label='Active')


class CreateTaskForm(forms.Form):
    artist = forms.CharField(label='Artist')
    task_type = forms.ChoiceField(label='Task Type', choices=[('shot', 'Shot'), ('asset', 'Asset')])
    sub_type = forms.ChoiceField(label='Sub Type', choices=[('animation', 'Animation'), ('modeling', 'Modeling')])
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    finish_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), )
    complexity = forms.IntegerField(min_value=1, label="Complexity", widget=forms.NumberInput(attrs={'size': '10'}))
    shot = forms.CharField(label='Shot')
    asset = forms.CharField(label='Asset')
    status = forms.ChoiceField(label='Status', choices=[('wip', 'WIP'), ('added', 'Added')])
    assigned_by = forms.CharField(label='Assigned By')
    description = forms.CharField(label='Description')
    active = forms.CharField(label='Active')

