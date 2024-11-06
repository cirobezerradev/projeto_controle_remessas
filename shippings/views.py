from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from dom_nfe import DomNFe
from .models import Shipping, ShippingItem, ShippingStorage
from .validators import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'shippings/pages/index.html')

def abrir_xml_remessa(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/xml/':
        if not request.FILES == {}:
            try:
                xml = request.FILES.get('xml')  
                
                validator_extension_file(xml)

                dom = DomNFe(xml)

                validator_cfop_remessa(dom.cfop)

                return render(request, 'shippings/pages/cadastrar_remessa.html',
                            {'cliente': dom.cliente, 
                            'nfe': dom.num_nfe,
                            'emission': dom.data_emissao,
                            'limit' : dom.data_limite,
                            'volumes': dom.volumes,
                            'peso': dom.peso,
                            'itens': dom.itens})
            except ValidationError as e:
                messages.error(request, e)
                return render(request, 'shippings/pages/cadastrar_remessa.html')
            except XMLInvalidError as e:
                messages.error(request, e)
                return render(request, 'shippings/pages/cadastrar_remessa.html')
 
    return redirect('cadastrar_remessa')

def cadastrar_remessa(request):
    if request.method == 'POST' and request.path == '/cadastrar_remessa/':
        try:
            lista_remessa = request.POST.getlist('remessa')
                
            item_exists(Shipping.objects.get(nfe=lista_remessa[1]))

        except ItemExists as e:
            messages.warning(request, e)
            return render(request, 'shippings/pages/cadastrar_remessa.html')

        except Shipping.DoesNotExist:   

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

def retornar_remessa(request):
    remessas_db = Shipping.objects.values().filter(status='PENDENTE')
    lista = list(remessas_db)
    return render(request, 'shippings/pages/retornar_remessa.html', {'remessas': lista})

def abrir_xml_retorno(request):
    pass

def cadastrar_retorno(request, nfe):
    return render(request, 'shippings/pages/cadastrar_retorno.html', {'nfe_remessa': nfe})