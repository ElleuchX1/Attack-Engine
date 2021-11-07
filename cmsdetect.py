import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
 ########adazedaze
Hheaders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
CMSnames = ['WordPress' ,'Magento' ,'Blogger By Google' ,'Ghost CMS' ,'LiveJournal' ,'3dCart' ,'Ametys CMS' ,'Apostrophe CMS' ,'AsciiDoc' ,'Drupal' ,'Bolt' ,'BrowserCMS' ,'Bubble' ,'Adobe Business Catalyst' ,'CKAN' ,'CMS Made Simple' ,'CMSimple' ,'XpressEngine' ,'TYPO3 CMS' ,'Textpattern CMS' ,'Joomla' ,'OpenCart' ,'XOOPS' ,'Ushahidi' ,'UMI.CMS' ,'Tiki Wiki CMS Groupware' ,'Wolf CMS' ,'WIX Website Builder' ,'WebsiteBaker CMS' ,'WebGUI' ,'TiddlyWiki' ,'SULU' ,'Subrion CMS' ,'Squiz Matrix' ,'Spin CMS' ,'solodev' ,'sNews' ,'Sitecore' ,'SIMsite' ,'Simplébo' ,'SilverStripe' ,'Silva CMS' ,'Serendipity' ,'SeamlessCMS' ,'Rock RMS' ,'Roadiz CMS' ,'RiteCMS' ,'RCMS' ,'Quick.Cms' ,'Pimcore' ,'phpWind' ,'phpCMS' ,'Percussion CMS' ,'PencilBlue' ,'Ophal' ,'Sitefinity' ,'OpenText WSM' ,'OpenCms' ,'Odoo' ,'Microsoft Sharepoint' ,'October CMS' ,'Mura CMS' ,'Moto CMS' ,'Mono.net' ,'MODX' ,'Methode' ,'Mambo' ,'LiveStreet CMS' ,'LEPTON CMS' ,'Kooboo CMS' ,'Koken' ,'Jimdo' ,'Indexhibit' ,'Webflow CMS' ,'Jalios JCMS' ,'ImpressPages CMS' ,'Hotaru CMS' ,'HIPPO CMS' ,'GravCMS' ,'GetSimple CMS' ,'Fork CMS' ,'PHP Nuke' ,'FlexCMP' ,'eZ Publish' ,'ExpressionEngine' ,'EPiServer' ,'e107' ,'DNN Platform' ,'phpBB' ,'DEDE CMS' ,'Danneo CMS' ,'Craft CMS' ,'CPG Dragonfly' ,'Cotonti' ,'Orchard CMS' ,'ContentBox' ,'Contentful' ,'Contensis CMS' ,'CMS CONTENIDO' ,'Contao CMS' ,'Concrete5 CMS' ,'Arc Forum' ,'Burning Board' ,'Discourse' ,'Discuz!' ,'Flarum' ,'FluxBB' ,'IP.Board community forum' ,'miniBB' ,'MyBB' ,'NodeBB' ,'PunBB' ,'Simple Machines Forum' ,'Vanilla Forums' ,'uKnowva' ,'XenForo' ,'XMB' ,'YaBB (Yet another Bulletin Board)' ,'Advanced Electron Forum' ,'Beehive Forum' ,'FUDforum' ,'Phorum' ,'Yet Another Forum (YAF)' ,'Yazd' ,'UBB.threads' ,'NoNonsense Forum' ,'myUPB' ,'mvnForum' ,'mwForum' ,'MercuryBoard' ,'AspNetForum' ,'JForum' ,'Afosto' ,'Afterbuy' ,'Arastta' ,'BigCommerce' ,'Bigware' ,'Bizweb' ,'Clientexec' ,'CloudCart' ,'ColorMeShop' ,'Moodle' ,'ORKIS Ajaris Websuite' ,'Comandia' ,'Commerce Server' ,'Cosmoshop' ,'CS Cart' ,'CubeCart' ,'Al Mubda' ,'Dynamicweb' ,'EC-CUBE' ,'Elcodi' ,'ePages' ,'eZ Publish' ,'Fortune3' ,'PrestaShop' ,'BigTree CMS' ,'Proximis Omnichannel' ,'Quick.Cart' ,'RBS Change' ,'Salesforce Commerce Cloud' ,'Sazito' ,'Shopatron' ,'Umbraco' ,'Shoper' ,'Shopery' ,'ShopFA' ,'Shopify' ,'Shoptet' ,'Smartstore' ,'Solusquare Commerce Cloud' ,'Spree' ,'Bitrix' ,'Brightspot CMS' ,'Amiro.CMS' ,'Weebly' ,'ekmPowershop' ,'GoDaddy Website Builder' ,'WHMCS' ,'OpenNemas CMS' ,'Zen Cart CMS' ,'IPO CMS' ]


def cmsdetector(url) :
	domain_name = urlparse(url).netloc
	print('[i] Searching for generator in meta tags : ' , end='' )
	soup = BeautifulSoup(requests.get(url).content, "html.parser")	
	metas = soup.findAll("meta")
	for meta in metas :
		if str(meta.get("name")).lower()=="generator" :
			for i in CMSnames :
				if i.lower() in str(meta.get("content")).lower() :
					print('Found')
					return i
	print('Failed')
	print('[i] Searching for CMS in http(s) header : ' , end='' )
	header=requests.get(url).headers
	header_values = list(header.values())
	for H in header_values :
			for i in CMSnames :
				lowH = H.lower()
				if i.lower() in lowH :
					print('Found')
					return i
	print('Failed')				
	#/robots.txt
	print('[i] Searching for CMS in robots.txt : ' , end='' )
	prased_url=urlparse(url)
	try :
		content = requests.get(prased_url.scheme + "://" + prased_url.netloc + '/robots.txt' , headers=Hheaders).content
		content_low=str(content).lower()
		if "/wp-" in content_low :
			print('Found')
			return 'WordPress'
		for i in CMSnames : 
			if i.lower() in content_low :
				print('Found')
				return i	

	except : 
		pass
	print('Failed')
	#/license.txt
	print('[i] Searching for CMS in license.txt : ' , end='' )
	prased_url=urlparse(url)
	try :
		content = requests.get(prased_url.scheme + "://" + prased_url.netloc + '/license.txt' , headers=Hheaders ).content
		content_low=str(content).lower()
		for i in CMSnames : 
			if i.lower() in content_low :
				print('Found')
				return i	
	except : 
		pass
	return None











