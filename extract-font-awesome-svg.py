#!/usr/bin/env python3

import xml.etree.ElementTree as ET

icon_names_by_codepoint = {
    61440: ['glass'],
    61441: ['music'],
    61442: ['search'],
    61443: ['envelope-o'],
    61444: ['heart'],
    61445: ['star'],
    61446: ['star-o'],
    61447: ['user'],
    61448: ['film'],
    61449: ['th-large'],
    61450: ['th'],
    61451: ['th-list'],
    61452: ['check'],
    61453: ['remove', 'close', 'times'],
    61454: ['search-plus'],
    61456: ['search-minus'],
    61457: ['power-off'],
    61458: ['signal'],
    61459: ['gear', 'cog'],
    61460: ['trash-o'],
    61461: ['home'],
    61462: ['file-o'],
    61463: ['clock-o'],
    61464: ['road'],
    61465: ['download'],
    61466: ['arrow-circle-o-down'],
    61467: ['arrow-circle-o-up'],
    61468: ['inbox'],
    61469: ['play-circle-o'],
    61470: ['rotate-right', 'repeat'],
    61473: ['refresh'],
    61474: ['list-alt'],
    61475: ['lock'],
    61476: ['flag'],
    61477: ['headphones'],
    61478: ['volume-off'],
    61479: ['volume-down'],
    61480: ['volume-up'],
    61481: ['qrcode'],
    61482: ['barcode'],
    61483: ['tag'],
    61484: ['tags'],
    61485: ['book'],
    61486: ['bookmark'],
    61487: ['print'],
    61488: ['camera'],
    61489: ['font'],
    61490: ['bold'],
    61491: ['italic'],
    61492: ['text-height'],
    61493: ['text-width'],
    61494: ['align-left'],
    61495: ['align-center'],
    61496: ['align-right'],
    61497: ['align-justify'],
    61498: ['list'],
    61499: ['dedent', 'outdent'],
    61500: ['indent'],
    61501: ['video-camera'],
    61502: ['photo', 'image', 'picture-o'],
    61504: ['pencil'],
    61505: ['map-marker'],
    61506: ['adjust'],
    61507: ['tint'],
    61508: ['edit', 'pencil-square-o'],
    61509: ['share-square-o'],
    61510: ['check-square-o'],
    61511: ['arrows'],
    61512: ['step-backward'],
    61513: ['fast-backward'],
    61514: ['backward'],
    61515: ['play'],
    61516: ['pause'],
    61517: ['stop'],
    61518: ['forward'],
    61520: ['fast-forward'],
    61521: ['step-forward'],
    61522: ['eject'],
    61523: ['chevron-left'],
    61524: ['chevron-right'],
    61525: ['plus-circle'],
    61526: ['minus-circle'],
    61527: ['times-circle'],
    61528: ['check-circle'],
    61529: ['question-circle'],
    61530: ['info-circle'],
    61531: ['crosshairs'],
    61532: ['times-circle-o'],
    61533: ['check-circle-o'],
    61534: ['ban'],
    61536: ['arrow-left'],
    61537: ['arrow-right'],
    61538: ['arrow-up'],
    61539: ['arrow-down'],
    61540: ['mail-forward', 'share'],
    61541: ['expand'],
    61542: ['compress'],
    61543: ['plus'],
    61544: ['minus'],
    61545: ['asterisk'],
    61546: ['exclamation-circle'],
    61547: ['gift'],
    61548: ['leaf'],
    61549: ['fire'],
    61550: ['eye'],
    61552: ['eye-slash'],
    61553: ['warning', 'exclamation-triangle'],
    61554: ['plane'],
    61555: ['calendar'],
    61556: ['random'],
    61557: ['comment'],
    61558: ['magnet'],
    61559: ['chevron-up'],
    61560: ['chevron-down'],
    61561: ['retweet'],
    61562: ['shopping-cart'],
    61563: ['folder'],
    61564: ['folder-open'],
    61565: ['arrows-v'],
    61566: ['arrows-h'],
    61568: ['bar-chart-o', 'bar-chart'],
    61569: ['twitter-square'],
    61570: ['facebook-square'],
    61571: ['camera-retro'],
    61572: ['key'],
    61573: ['gears', 'cogs'],
    61574: ['comments'],
    61575: ['thumbs-o-up'],
    61576: ['thumbs-o-down'],
    61577: ['star-half'],
    61578: ['heart-o'],
    61579: ['sign-out'],
    61580: ['linkedin-square'],
    61581: ['thumb-tack'],
    61582: ['external-link'],
    61584: ['sign-in'],
    61585: ['trophy'],
    61586: ['github-square'],
    61587: ['upload'],
    61588: ['lemon-o'],
    61589: ['phone'],
    61590: ['square-o'],
    61591: ['bookmark-o'],
    61592: ['phone-square'],
    61593: ['twitter'],
    61594: ['facebook-f', 'facebook'],
    61595: ['github'],
    61596: ['unlock'],
    61597: ['credit-card'],
    61598: ['feed', 'rss'],
    61600: ['hdd-o'],
    61601: ['bullhorn'],
    61602: ['bell-o'],
    61603: ['certificate'],
    61604: ['hand-o-right'],
    61605: ['hand-o-left'],
    61606: ['hand-o-up'],
    61607: ['hand-o-down'],
    61608: ['arrow-circle-left'],
    61609: ['arrow-circle-right'],
    61610: ['arrow-circle-up'],
    61611: ['arrow-circle-down'],
    61612: ['globe'],
    61613: ['wrench'],
    61614: ['tasks'],
    61616: ['filter'],
    61617: ['briefcase'],
    61618: ['arrows-alt'],
    61632: ['group', 'users'],
    61633: ['chain', 'link'],
    61634: ['cloud'],
    61635: ['flask'],
    61636: ['cut', 'scissors'],
    61637: ['copy', 'files-o'],
    61638: ['paperclip'],
    61639: ['save', 'floppy-o'],
    61640: ['square'],
    61641: ['navicon', 'reorder', 'bars'],
    61642: ['list-ul'],
    61643: ['list-ol'],
    61644: ['strikethrough'],
    61645: ['underline'],
    61646: ['table'],
    61648: ['magic'],
    61649: ['truck'],
    61650: ['pinterest'],
    61651: ['pinterest-square'],
    61652: ['google-plus-square'],
    61653: ['google-plus'],
    61654: ['money'],
    61655: ['caret-down'],
    61656: ['caret-up'],
    61657: ['caret-left'],
    61658: ['caret-right'],
    61659: ['columns'],
    61660: ['unsorted', 'sort'],
    61661: ['sort-down', 'sort-desc'],
    61662: ['sort-up', 'sort-asc'],
    61664: ['envelope'],
    61665: ['linkedin'],
    61666: ['rotate-left', 'undo'],
    61667: ['legal', 'gavel'],
    61668: ['dashboard', 'tachometer'],
    61669: ['comment-o'],
    61670: ['comments-o'],
    61671: ['flash', 'bolt'],
    61672: ['sitemap'],
    61673: ['umbrella'],
    61674: ['paste', 'clipboard'],
    61675: ['lightbulb-o'],
    61676: ['exchange'],
    61677: ['cloud-download'],
    61678: ['cloud-upload'],
    61680: ['user-md'],
    61681: ['stethoscope'],
    61682: ['suitcase'],
    61683: ['bell'],
    61684: ['coffee'],
    61685: ['cutlery'],
    61686: ['file-text-o'],
    61687: ['building-o'],
    61688: ['hospital-o'],
    61689: ['ambulance'],
    61690: ['medkit'],
    61691: ['fighter-jet'],
    61692: ['beer'],
    61693: ['h-square'],
    61694: ['plus-square'],
    61696: ['angle-double-left'],
    61697: ['angle-double-right'],
    61698: ['angle-double-up'],
    61699: ['angle-double-down'],
    61700: ['angle-left'],
    61701: ['angle-right'],
    61702: ['angle-up'],
    61703: ['angle-down'],
    61704: ['desktop'],
    61705: ['laptop'],
    61706: ['tablet'],
    61707: ['mobile-phone', 'mobile'],
    61708: ['circle-o'],
    61709: ['quote-left'],
    61710: ['quote-right'],
    61712: ['spinner'],
    61713: ['circle'],
    61714: ['mail-reply', 'reply'],
    61715: ['github-alt'],
    61716: ['folder-o'],
    61717: ['folder-open-o'],
    61720: ['smile-o'],
    61721: ['frown-o'],
    61722: ['meh-o'],
    61723: ['gamepad'],
    61724: ['keyboard-o'],
    61725: ['flag-o'],
    61726: ['flag-checkered'],
    61728: ['terminal'],
    61729: ['code'],
    61730: ['mail-reply-all', 'reply-all'],
    61731: ['star-half-empty', 'star-half-full', 'star-half-o'],
    61732: ['location-arrow'],
    61733: ['crop'],
    61734: ['code-fork'],
    61735: ['unlink', 'chain-broken'],
    61736: ['question'],
    61737: ['info'],
    61738: ['exclamation'],
    61739: ['superscript'],
    61740: ['subscript'],
    61741: ['eraser'],
    61742: ['puzzle-piece'],
    61744: ['microphone'],
    61745: ['microphone-slash'],
    61746: ['shield'],
    61747: ['calendar-o'],
    61748: ['fire-extinguisher'],
    61749: ['rocket'],
    61750: ['maxcdn'],
    61751: ['chevron-circle-left'],
    61752: ['chevron-circle-right'],
    61753: ['chevron-circle-up'],
    61754: ['chevron-circle-down'],
    61755: ['html5'],
    61756: ['css3'],
    61757: ['anchor'],
    61758: ['unlock-alt'],
    61760: ['bullseye'],
    61761: ['ellipsis-h'],
    61762: ['ellipsis-v'],
    61763: ['rss-square'],
    61764: ['play-circle'],
    61765: ['ticket'],
    61766: ['minus-square'],
    61767: ['minus-square-o'],
    61768: ['level-up'],
    61769: ['level-down'],
    61770: ['check-square'],
    61771: ['pencil-square'],
    61772: ['external-link-square'],
    61773: ['share-square'],
    61774: ['compass'],
    61776: ['toggle-down', 'caret-square-o-down'],
    61777: ['toggle-up', 'caret-square-o-up'],
    61778: ['toggle-right', 'caret-square-o-right'],
    61779: ['euro', 'eur'],
    61780: ['gbp'],
    61781: ['dollar', 'usd'],
    61782: ['rupee', 'inr'],
    61783: ['cny', 'rmb', 'yen', 'jpy'],
    61784: ['ruble', 'rouble', 'rub'],
    61785: ['won', 'krw'],
    61786: ['bitcoin', 'btc'],
    61787: ['file'],
    61788: ['file-text'],
    61789: ['sort-alpha-asc'],
    61790: ['sort-alpha-desc'],
    61792: ['sort-amount-asc'],
    61793: ['sort-amount-desc'],
    61794: ['sort-numeric-asc'],
    61795: ['sort-numeric-desc'],
    61796: ['thumbs-up'],
    61797: ['thumbs-down'],
    61798: ['youtube-square'],
    61799: ['youtube'],
    61800: ['xing'],
    61801: ['xing-square'],
    61802: ['youtube-play'],
    61803: ['dropbox'],
    61804: ['stack-overflow'],
    61805: ['instagram'],
    61806: ['flickr'],
    61808: ['adn'],
    61809: ['bitbucket'],
    61810: ['bitbucket-square'],
    61811: ['tumblr'],
    61812: ['tumblr-square'],
    61813: ['long-arrow-down'],
    61814: ['long-arrow-up'],
    61815: ['long-arrow-left'],
    61816: ['long-arrow-right'],
    61817: ['apple'],
    61818: ['windows'],
    61819: ['android'],
    61820: ['linux'],
    61821: ['dribbble'],
    61822: ['skype'],
    61824: ['foursquare'],
    61825: ['trello'],
    61826: ['female'],
    61827: ['male'],
    61828: ['gittip', 'gratipay'],
    61829: ['sun-o'],
    61830: ['moon-o'],
    61831: ['archive'],
    61832: ['bug'],
    61833: ['vk'],
    61834: ['weibo'],
    61835: ['renren'],
    61836: ['pagelines'],
    61837: ['stack-exchange'],
    61838: ['arrow-circle-o-right'],
    61840: ['arrow-circle-o-left'],
    61841: ['toggle-left', 'caret-square-o-left'],
    61842: ['dot-circle-o'],
    61843: ['wheelchair'],
    61844: ['vimeo-square'],
    61845: ['turkish-lira', 'try'],
    61846: ['plus-square-o'],
    61847: ['space-shuttle'],
    61848: ['slack'],
    61849: ['envelope-square'],
    61850: ['wordpress'],
    61851: ['openid'],
    61852: ['institution', 'bank', 'university'],
    61853: ['mortar-board', 'graduation-cap'],
    61854: ['yahoo'],
    61856: ['google'],
    61857: ['reddit'],
    61858: ['reddit-square'],
    61859: ['stumbleupon-circle'],
    61860: ['stumbleupon'],
    61861: ['delicious'],
    61862: ['digg'],
    61863: ['pied-piper-pp'],
    61864: ['pied-piper-alt'],
    61865: ['drupal'],
    61866: ['joomla'],
    61867: ['language'],
    61868: ['fax'],
    61869: ['building'],
    61870: ['child'],
    61872: ['paw'],
    61873: ['spoon'],
    61874: ['cube'],
    61875: ['cubes'],
    61876: ['behance'],
    61877: ['behance-square'],
    61878: ['steam'],
    61879: ['steam-square'],
    61880: ['recycle'],
    61881: ['automobile', 'car'],
    61882: ['cab', 'taxi'],
    61883: ['tree'],
    61884: ['spotify'],
    61885: ['deviantart'],
    61886: ['soundcloud'],
    61888: ['database'],
    61889: ['file-pdf-o'],
    61890: ['file-word-o'],
    61891: ['file-excel-o'],
    61892: ['file-powerpoint-o'],
    61893: ['file-photo-o', 'file-picture-o', 'file-image-o'],
    61894: ['file-zip-o', 'file-archive-o'],
    61895: ['file-sound-o', 'file-audio-o'],
    61896: ['file-movie-o', 'file-video-o'],
    61897: ['file-code-o'],
    61898: ['vine'],
    61899: ['codepen'],
    61900: ['jsfiddle'],
    61901: ['life-bouy', 'life-buoy', 'life-saver', 'support', 'life-ring'],
    61902: ['circle-o-notch'],
    61904: ['ra', 'resistance', 'rebel'],
    61905: ['ge', 'empire'],
    61906: ['git-square'],
    61907: ['git'],
    61908: ['y-combinator-square', 'yc-square', 'hacker-news'],
    61909: ['tencent-weibo'],
    61910: ['qq'],
    61911: ['wechat', 'weixin'],
    61912: ['send', 'paper-plane'],
    61913: ['send-o', 'paper-plane-o'],
    61914: ['history'],
    61915: ['circle-thin'],
    61916: ['header'],
    61917: ['paragraph'],
    61918: ['sliders'],
    61920: ['share-alt'],
    61921: ['share-alt-square'],
    61922: ['bomb'],
    61923: ['soccer-ball-o', 'futbol-o'],
    61924: ['tty'],
    61925: ['binoculars'],
    61926: ['plug'],
    61927: ['slideshare'],
    61928: ['twitch'],
    61929: ['yelp'],
    61930: ['newspaper-o'],
    61931: ['wifi'],
    61932: ['calculator'],
    61933: ['paypal'],
    61934: ['google-wallet'],
    61936: ['cc-visa'],
    61937: ['cc-mastercard'],
    61938: ['cc-discover'],
    61939: ['cc-amex'],
    61940: ['cc-paypal'],
    61941: ['cc-stripe'],
    61942: ['bell-slash'],
    61943: ['bell-slash-o'],
    61944: ['trash'],
    61945: ['copyright'],
    61946: ['at'],
    61947: ['eyedropper'],
    61948: ['paint-brush'],
    61949: ['birthday-cake'],
    61950: ['area-chart'],
    61952: ['pie-chart'],
    61953: ['line-chart'],
    61954: ['lastfm'],
    61955: ['lastfm-square'],
    61956: ['toggle-off'],
    61957: ['toggle-on'],
    61958: ['bicycle'],
    61959: ['bus'],
    61960: ['ioxhost'],
    61961: ['angellist'],
    61962: ['cc'],
    61963: ['shekel', 'sheqel', 'ils'],
    61964: ['meanpath'],
    61965: ['buysellads'],
    61966: ['connectdevelop'],
    61968: ['dashcube'],
    61969: ['forumbee'],
    61970: ['leanpub'],
    61971: ['sellsy'],
    61972: ['shirtsinbulk'],
    61973: ['simplybuilt'],
    61974: ['skyatlas'],
    61975: ['cart-plus'],
    61976: ['cart-arrow-down'],
    61977: ['diamond'],
    61978: ['ship'],
    61979: ['user-secret'],
    61980: ['motorcycle'],
    61981: ['street-view'],
    61982: ['heartbeat'],
    61985: ['venus'],
    61986: ['mars'],
    61987: ['mercury'],
    61988: ['intersex', 'transgender'],
    61989: ['transgender-alt'],
    61990: ['venus-double'],
    61991: ['mars-double'],
    61992: ['venus-mars'],
    61993: ['mars-stroke'],
    61994: ['mars-stroke-v'],
    61995: ['mars-stroke-h'],
    61996: ['neuter'],
    61997: ['genderless'],
    62000: ['facebook-official'],
    62001: ['pinterest-p'],
    62002: ['whatsapp'],
    62003: ['server'],
    62004: ['user-plus'],
    62005: ['user-times'],
    62006: ['hotel', 'bed'],
    62007: ['viacoin'],
    62008: ['train'],
    62009: ['subway'],
    62010: ['medium'],
    62011: ['yc', 'y-combinator'],
    62012: ['optin-monster'],
    62013: ['opencart'],
    62014: ['expeditedssl'],
    62016: ['battery-4', 'battery', 'battery-full'],
    62017: ['battery-3', 'battery-three-quarters'],
    62018: ['battery-2', 'battery-half'],
    62019: ['battery-1', 'battery-quarter'],
    62020: ['battery-0', 'battery-empty'],
    62021: ['mouse-pointer'],
    62022: ['i-cursor'],
    62023: ['object-group'],
    62024: ['object-ungroup'],
    62025: ['sticky-note'],
    62026: ['sticky-note-o'],
    62027: ['cc-jcb'],
    62028: ['cc-diners-club'],
    62029: ['clone'],
    62030: ['balance-scale'],
    62032: ['hourglass-o'],
    62033: ['hourglass-1', 'hourglass-start'],
    62034: ['hourglass-2', 'hourglass-half'],
    62035: ['hourglass-3', 'hourglass-end'],
    62036: ['hourglass'],
    62037: ['hand-grab-o', 'hand-rock-o'],
    62038: ['hand-stop-o', 'hand-paper-o'],
    62039: ['hand-scissors-o'],
    62040: ['hand-lizard-o'],
    62041: ['hand-spock-o'],
    62042: ['hand-pointer-o'],
    62043: ['hand-peace-o'],
    62044: ['trademark'],
    62045: ['registered'],
    62046: ['creative-commons'],
    62048: ['gg'],
    62049: ['gg-circle'],
    62050: ['tripadvisor'],
    62051: ['odnoklassniki'],
    62052: ['odnoklassniki-square'],
    62053: ['get-pocket'],
    62054: ['wikipedia-w'],
    62055: ['safari'],
    62056: ['chrome'],
    62057: ['firefox'],
    62058: ['opera'],
    62059: ['internet-explorer'],
    62060: ['tv', 'television'],
    62061: ['contao'],
    62062: ['500px'],
    62064: ['amazon'],
    62065: ['calendar-plus-o'],
    62066: ['calendar-minus-o'],
    62067: ['calendar-times-o'],
    62068: ['calendar-check-o'],
    62069: ['industry'],
    62070: ['map-pin'],
    62071: ['map-signs'],
    62072: ['map-o'],
    62073: ['map'],
    62074: ['commenting'],
    62075: ['commenting-o'],
    62076: ['houzz'],
    62077: ['vimeo'],
    62078: ['black-tie'],
    62080: ['fonticons'],
    62081: ['reddit-alien'],
    62082: ['edge'],
    62083: ['credit-card-alt'],
    62084: ['codiepie'],
    62085: ['modx'],
    62086: ['fort-awesome'],
    62087: ['usb'],
    62088: ['product-hunt'],
    62089: ['mixcloud'],
    62090: ['scribd'],
    62091: ['pause-circle'],
    62092: ['pause-circle-o'],
    62093: ['stop-circle'],
    62094: ['stop-circle-o'],
    62096: ['shopping-bag'],
    62097: ['shopping-basket'],
    62098: ['hashtag'],
    62099: ['bluetooth'],
    62100: ['bluetooth-b'],
    62101: ['percent'],
    62102: ['gitlab'],
    62103: ['wpbeginner'],
    62104: ['wpforms'],
    62105: ['envira'],
    62106: ['universal-access'],
    62107: ['wheelchair-alt'],
    62108: ['question-circle-o'],
    62109: ['blind'],
    62110: ['audio-description'],
    62112: ['volume-control-phone'],
    62113: ['braille'],
    62114: ['assistive-listening-systems'],
    62115: ['asl-interpreting', 'american-sign-language-interpreting'],
    62116: ['deafness', 'hard-of-hearing', 'deaf'],
    62117: ['glide'],
    62118: ['glide-g'],
    62119: ['signing', 'sign-language'],
    62120: ['low-vision'],
    62121: ['viadeo'],
    62122: ['viadeo-square'],
    62123: ['snapchat'],
    62124: ['snapchat-ghost'],
    62125: ['snapchat-square'],
    62126: ['pied-piper'],
    62128: ['first-order'],
    62129: ['yoast'],
    62130: ['themeisle'],
    62131: ['google-plus-circle', 'google-plus-official'],
    62132: ['fa', 'font-awesome'],
    62133: ['handshake-o'],
    62134: ['envelope-open'],
    62135: ['envelope-open-o'],
    62136: ['linode'],
    62137: ['address-book'],
    62138: ['address-book-o'],
    62139: ['vcard', 'address-card'],
    62140: ['vcard-o', 'address-card-o'],
    62141: ['user-circle'],
    62142: ['user-circle-o'],
    62144: ['user-o'],
    62145: ['id-badge'],
    62146: ['drivers-license', 'id-card'],
    62147: ['drivers-license-o', 'id-card-o'],
    62148: ['quora'],
    62149: ['free-code-camp'],
    62150: ['telegram'],
    62151: ['thermometer-4', 'thermometer', 'thermometer-full'],
    62152: ['thermometer-3', 'thermometer-three-quarters'],
    62153: ['thermometer-2', 'thermometer-half'],
    62154: ['thermometer-1', 'thermometer-quarter'],
    62155: ['thermometer-0', 'thermometer-empty'],
    62156: ['shower'],
    62157: ['bathtub', 's15', 'bath'],
    62158: ['podcast'],
    62160: ['window-maximize'],
    62161: ['window-minimize'],
    62162: ['window-restore'],
    62163: ['times-rectangle', 'window-close'],
    62164: ['times-rectangle-o', 'window-close-o'],
    62165: ['bandcamp'],
    62166: ['grav'],
    62167: ['etsy'],
    62168: ['imdb'],
    62169: ['ravelry'],
    62170: ['eercast'],
    62171: ['microchip'],
    62172: ['snowflake-o'],
    62173: ['superpowers'],
    62174: ['wpexplorer'],
    62176: ['meetup']
}

tree = ET.parse('svg/fontawesome4/fontawesome-webfont.svg')
ET.register_namespace("svg", "http://www.w3.org/2000/svg")

font = tree.find(".//font")
default_horiz_adv_x = font.attrib["horiz-adv-x"]
font_face = tree.find(".//font-face")
size = int(font_face.attrib["units-per-em"])
ascent = int(font_face.attrib["ascent"])

for node in tree.findall(".//glyph[@d][@unicode]"):
    codepoint = ord(node.attrib["unicode"])
    d = node.attrib["d"]
    horiz_adv_x = int(node.attrib.get("horiz-adv-x", default_horiz_adv_x))
    for name in icon_names_by_codepoint[codepoint]:
        doc = ET.Element("svg", attrib={
            "xmlns": "http://www.w3.org/2000/svg",
            "version": "1.1",
            "width": f"{horiz_adv_x/10}",
            "height": f"{size/10}",
        })

        ET.SubElement(doc, "path", attrib={"d": node.attrib["d"],
                                           "transform": f"scale(0.1 -0.1) translate(0 -{ascent})"})

        with open(f"svg/fontawesome4/{name}.svg", mode="w") as outfile:
            print(ET.tostring(element=doc,
                              encoding="unicode"),
                  file=outfile)
