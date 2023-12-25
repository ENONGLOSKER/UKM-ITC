from django import forms
from .models import Anggota, Sertifikat,Program,Pengurus,Bidang


class SertifikatForm(forms.ModelForm): 
    class Meta:
        model = Sertifikat
        fields = '__all__'

class ProgramForm(forms.ModelForm): 
    class Meta:
        model = Program
        fields = '__all__'
        
class PengurusForm(forms.ModelForm): 
    class Meta:
        model = Pengurus
        fields = '__all__'
        widgets = {
             'status': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Masukkan Nama Status'}),
             'nama_pengurus': forms.Select(attrs={'class':'form-control', 'placeholder': 'Masukkan Nama Pengurus'}),
             'bidang': forms.Select(attrs={'class':'form-control', 'placeholder': 'Masukkan Nama Bidang/Devisi'}),
        }

class BidangForm(forms.ModelForm): 
    class Meta:
        model = Bidang
        fields = '__all__'
        widgets = {
             'nama_bidang': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Masukkan Nama Bidang'}),
             'deskripsi': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Masukkan Deskripsi'}),
        }
 
class AnggotaForm(forms.ModelForm):
    GENDER_CHOICES = [("L", "Laki-Laki"), ("P", "Perempuan")]
    PD_CHOICES = [("TI", "Teknik Informatika"), ("SI", "Sistem Informasi")]
    SM_CHOICES = [('1','Satu (1)'),('2','Dua (2)'),('3','Tiga (3)'),('4','Empat (4'),('5','Lima (5)'),('6','Enam (6)'),('7','Tujuh (7)'),('8','Delapan (8)'),]

    jk = forms.ChoiceField(label='Jenis Kelamin', choices=GENDER_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    prodi = forms.ChoiceField(choices=PD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    semester = forms.ChoiceField(choices=SM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Anggota
        fields = ['nama', 'jk', 'alamat', 'nim', 'prodi', 'semester', 'nomor', 'email']
        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Masukkan Nama Lengkap'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Masukkan Alamat'}),
            'nim': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NIM'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Semester'}),
            'nomor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nomor Telepon'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Email'}),
        }
