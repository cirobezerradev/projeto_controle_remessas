from django.shortcuts import render, redirect
from dom_nfe.dom_nfe import DomNFe
from .models import Shipping, ShippingItem, ShippingStorage

# Create your views here.
def index(request):
    return render(request, 'shippings/pages/index.html')

def abrir_xml(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/xml/':
        if not request.FILES == {}:
            xml = request.FILES.get('xml')   
            
            dom = DomNFe(xml)

            return render(request, 'shippings/pages/cadastrar_remessa.html',
                        {'cliente': dom.cliente, 
                        'nfe': dom.num_nfe,
                        'emission': dom.data_emissao,
                        'volumes': dom.volumes,
                        'peso': dom.peso,
                        'itens': dom.itens})
    
    return redirect('cadastrar_remessa')

def cadastrar_remessa(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/':
        
        lista_remessa = request.POST.getlist('remessa')
                
        shipping = Shipping(*lista_remessa)
        shipping.save()

        lista_post = list(request.POST.lists())

        for i in range(1, len(lista_post)-1):
            lista_itens = request.POST.getlist(f'{i}')
            shipping_item = ShippingItem(codigo=lista_itens[0],
                            descricao=lista_itens[1],
                            un=lista_itens[2],
                            quantidade=lista_itens[3],
                            valor_unit=lista_itens[4],
                            nfe_remessa=Shipping.objects.get(nfe=shipping.nfe))
            
            shipping_storage = ShippingStorage(codigo=lista_itens[0],
                            descricao=lista_itens[1],
                            un=lista_itens[2],
                            quantidade=lista_itens[3],
                            valor_unit=lista_itens[4],
                            nfe_remessa=Shipping.objects.get(nfe=shipping.nfe))
            
            shipping_item.save()
            shipping_storage.save()
   
    return render(request, 'shippings/pages/cadastrar_remessa.html')

def cadastrar_retorno(request):
    lista = range(10)
    return render(request, 'shippings/pages/cadastrar_retorno.html', {'lista': lista})