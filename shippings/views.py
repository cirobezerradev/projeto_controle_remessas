from django.shortcuts import render
from dom_nfe.dom_nfe import DomNFe
from .models import Shipping

# Create your views here.
def index(request):
    return render(request, 'shippings/pages/index.html')

def abrir_xml(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/xml/':
        xml = request.FILES.get('xml')   
        
        dom = DomNFe(xml)

        return render(request, 'shippings/pages/cadastrar_remessa.html',
                      {'cliente': dom.cliente, 
                       'nfe': dom.num_nfe,
                       'emission': dom.data_emissao,
                       'volumes': dom.volumes,
                       'peso': dom.peso,
                       'itens': dom.itens})
    
    return render(request, 'shippings/pages/cadastrar_remessa.html')

def cadastrar_remessa(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/':
        # model = Shipping(nfe, data_emissao, cliente, volumes, peso)
        pass
        

    return render(request, 'shippings/pages/cadastrar_remessa.html')