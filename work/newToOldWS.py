import fileinput
import re
import pprint
import fnmatch
import os
from collections import defaultdict

d = {

"http://infadf.telecom.ba/e_racun_WS/e_rac_zahSoapHttpPort" : "http://192.168.133.144/We_racun_WS/proxy/PS_e_racun_WS",

"http://infadf.telecom.ba/lnet-WS/getLnetDetSoapHttpPort" : "http://192.168.133.144/Wlnet-WS/proxy/PS_lnet-WS",

"http://infadf.telecom.ba/lnet-WS/getLnetFiksniDetSoapHttpPort" : "http://192.168.133.144/Wlnet-WS/proxy/PS_lnet-WS_1",

"http://infadf.telecom.ba/lnet-WS/getLnetFiksniSumeSoapHttpPort" : "http://192.168.133.144/Wlnet-WS/proxy/PS_lnet-WS_2",

"http://infadf.telecom.ba/lnet-WS/getLnetSumeSoapHttpPort" : "http://192.168.133.144/Wlnet-WS/proxy/PS_lnet-WS_3",

"http://infadf.telecom.ba/Portal_skladiste-WS_novi/postoji_aparat_prod_noviSoapHttpPort" : "http://192.168.133.144/WPortal_skladiste-WS/proxy/PS_postoji_aparat_prod_novi",

"http://192.168.133.144/WPORTAL_AUTH-PORTAL/proxy/PS_PORTAL_AUTH-PORTAL" : "http://192.168.133.144/WPORTAL_AUTH-PORTAL/proxy/PS_PORTAL_AUTH-PORTAL",

"http://infadf.telecom.ba/FiksGSMDetaljni0605/getTicketDetSoapHttpPort" : "http://192.168.133.144/WFiksGSMDetaljni/proxy/PS_FiksGSMDetaljni",

"http://infadf.telecom.ba/BihDet0906/BihDet0906SoapHttpPort" : "http://192.168.133.144/WBihDet0906/proxy/PS_BihDet0906",

"http://infadf.telecom.ba/ACS-WS/get_jpp_usrSoapHttpPort" : "http://192.168.133.144/WACS-WS/proxy/PS_get_jpp_usr",

"http://infadf.telecom.ba/JRKJPPWS-Server-context-root/SalesCommonSoapHttpPort" : "http://192.168.133.144/JRKJPPWS-Server/proxy/PS_SalesCommon",

"http://infadf.telecom.ba/JRKJPPWS-Server-context-root/SalesAdditionalSoapHttpPort" : "http://192.168.133.144/JRKJPPWS-Server/proxy/PS_SalesAdditional",

"http://infadf.telecom.ba/JRKJPPWS-Server-context-root/SalesSoapHttpPort" : "http://192.168.133.144/JRKJPPWS-Server/proxy/PS_Sales",

"http://192.168.133.144/JRKJPPWS-Server/proxy/PS_PortalServices" : "http://192.168.133.144/JRKJPPWS-Server/proxy/PS_PortalServices",

"http://infadf.telecom.ba/JRKJPPWS-Server-context-root/PortalServicesDBSoapHttpPort" : "http://192.168.133.144/WJRKJPPWS-Server/proxy/PS_PortalServicesDB",

"http://infadf.telecom.ba/kopija_racuna_jrk-WS/kopija_racSoapHttpPort" : "http://192.168.133.144/Wkopija_racuna_jrk-WS/proxy/PS_kopija_racuna_jrk-WS",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getARItemsSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getARItems",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getARItemsBIHNETSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getARItemsBIHNET",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getARItemsGSMSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getARItemsGSM",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getInvoiceItemsSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getInvoiceItems",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getInvoiceItemsBIHNETSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getInvoiceItemsBIHNET",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getInvoiceItemsGSMSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getInvoiceItemsGSM",

"http://infadf.telecom.ba/JPP_JRK_WS_PROD/getInvoiceStateSoapHttpPort" : "http://192.168.133.144/WJPP_JRK_WS_PROD/proxy/PS_getInvoiceState",

"http://infvm115.telecom.ba/PORTAL_AUTH-PORTAL-WS/PORTAL_AUTH_WSSoapHttpPort" : "http://192.168.133.149/WPORTAL_AUTH-PORTAL/proxy/PS_PORTAL_AUTH-PORTAL",

"http://infvm115.telecom.ba/JRKJPPWS-Server-context-root/SalesCommonSoapHttpPort" : "http://192.168.133.149/JRKJPPWS-Server/proxy/PS_SalesCommon",

"http://infvm115.telecom.ba/JRKJPPWS-Server-context-root/PortalServicesSoapHttpPort" : "http://192.168.133.149/JRKJPPWS-Server/proxy/PS_PortalServies"

}

all_php_files = []
for root, dirnames, filenames in os.walk(os.getcwd()):
  for filename in fnmatch.filter(filenames, '*.php'):
      all_php_files.append(os.path.join(root, filename))

for file_name in all_php_files:
	for line in fileinput.input(file_name, inplace=True):
		for k, v in d.iteritems():
			line = line.replace(v,k)
		print line,
