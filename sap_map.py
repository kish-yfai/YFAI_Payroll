def sap_company(input_cc):
    sap_dict = {
        '19299999': '9952',
        '19310010': '9952',
        '19310011': '9952',
        '19310014': '9952',
        '19310015': '9952',
        '19310015': '9952',
        '19310020': '9952',
        '19310020': '9952',
        '19310034': '9952',
        '19310034': '9952',
        '19310035': '9952',
        '19310035': '9952',
        '19310109': '9952',
        '19310185': '9952',
        '19310185': '9952',
        '19310281': '9952',
        '19310400': '9952',
        '19310400': '9952',
        '19310411': '9952',
        '19310411': '9952',
        '19310423': '9952',
        '19310427': '9952',
        '19310427': '9952',
        '19310440': '9952',
        '19310484': '9952',
        '19310535': '9952',
        '19310570': '9952',
        '19310575': '9952',
        '19310657': '9952',
        '19310690': '9952',
        '19310740': '9952',
        '19310753': '9952',
        '19310770': '9952',
        '19310792': '9952',
        '19310830': '9952',
        '19310882': '9952',
        '19310882': '9952',
        '19311060': '9952',
        '19311080': '9952',
        '19311220': '9952',
        '19311340': '9952',
        '19311500': '9952',
        '19311500': '9952',
        '19311635': '9952',
        '19311700': '9952',
        '19311701': '9952',
        '19311702': '9952',
        '19311703': '9952',
        '19311704': '9952',
        '19311705': '9952',
        '19311709': '9952',
        '19311710': '9952',
        '19312815': '9952',
        '19319999': '9952',
        '19321900': '9952',
        '19322200': '9952',
        '19322300': '9952',
        '19322400': '9952',
        '19323010': '9952',
        '19323030': '9952',
        '19323050': '9952',
        '19323060': '9952',
        '19323080': '9952',
        '19323090': '9952',
        '19323100': '9952',
        '19323200': '9952',
        '19328000': '9952',
        '19329000': '9952',
        '19329999': '9952',
        '19331102': '9951',
        '19331202': '9951',
        '19331212': '9951',
        '19331402': '9951',
        '19331501': '9951',
        '19331611': '9951',
        '19331702': '9951',
        '19331822': '9951',
        '19331832': '9951',
        '19331841': '9951',
        '19332204': '9951',
        '19332306': '9951',
        '19332407': '9951',
        '19333011': '9951',
        '19333014': '9951',
        '19333035': '9951',
        '19333066': '9951',
        '19333113': '9951',
        '19333210': '9951',
        '19338001': '9951',
        '19339002': '9951',
        '19339999': '9951',
        '19355001': '9952',
        '19359999': '9952',
        '19370700': '9952',
        '19371030': '9952',
        '19371031': '9952',
        '19371032': '9952',
        '19371033': '9952',
        '19371034': '9952',
        '19371035': '9952',
        '19371036': '9952',
        '19371037': '9952',
        '19371038': '9952',
        '19371066': '9952',
        '19371067': '9952',
        '19371068': '9952',
        '19371700': '9952',
        '19371701': '9952',
        '19371702': '9952',
        '19371704': '9952',
        '19371705': '9952',
        '19379999': '9952',
        '19380000': '9951',
        '19380001': '9951',
        '19380002': '9951',
        '19380003': '9951',
        '19380004': '9951',
        '19380005': '9951',
        '19380006': '9951',
        '19380007': '9951',
        '19380008': '9951',
        '19380009': '9951',
        '19380010': '9951',
        '19380011': '9951',
        '19380012': '9951',
        '19380013': '9951',
        '19380014': '9951',
        '19389000': '9951',
        '19389001': '9951',
        '19389999': '9951',
        '19390000': '9951',
        '19390001': '9951',
        '19390002': '9951',
        '19390003': '9951',
        '19390004': '9951',
        '19390005': '9951',
        '19390006': '9951',
        '19390007': '9951',
        '19390008': '9951',
        '19390009': '9951',
        '19390010': '9951',
        '19390011': '9951',
        '19399000': '9951',
        '19399001': '9951',
        '19399999': '9951',
        '19400000': '9951',
        '19400001': '9951',
        '19400002': '9951',
        '19400003': '9951',
        '19400004': '9951',
        '19400005': '9951',
        '19400006': '9951',
        '19400007': '9951',
        '19400008': '9951',
        '19400009': '9951',
        '19400010': '9951',
        '19400011': '9951',
        '19400012': '9951',
        '19400013': '9951',
        '19400014': '9951',
        '19409000': '9951',
        '19409999': '9951',
        '19420000': '9951',
        '19420001': '9951',
        '19420002': '9951',
        '19420003': '9951',
        '19420004': '9951',
        '19420005': '9951',
        '19420006': '9951',
        '19420007': '9951',
        '19420008': '9951',
        '19420009': '9951',
        '19420010': '9951',
        '19420011': '9951',
        '19420012': '9951',
        '19420013': '9951',
        '19420014': '9951',
        '19420017': '9951',
        '19429000': '9951',
        '19429001': '9951',
        '19429999': '9951',
        '19430000': '9951',
        '19430001': '9951',
        '19430002': '9951',
        '19430003': '9951',
        '19430004': '9951',
        '19430005': '9951',
        '19430006': '9951',
        '19430007': '9951',
        '19430008': '9951',
        '19430009': '9951',
        '19430010': '9951',
        '19430011': '9951',
        '19430012': '9951',
        '19430013': '9951',
        '19430014': '9951',
        '19439000': '9951',
        '19439001': '9951',
        '19439999': '9951',
        '19440000': '9951',
        '19440001': '9951',
        '19440002': '9951',
        '19440003': '9951',
        '19440004': '9951',
        '19440005': '9951',
        '19440006': '9951',
        '19440007': '9951',
        '19440008': '9951',
        '19440009': '9951',
        '19440010': '9951',
        '19440011': '9951',
        '19440012': '9951',
        '19440013': '9951',
        '19440014': '9951',
        '19449000': '9951',
        '19449001': '9951',
        '19449999': '9951',
        '19450000': '9951',
        '19450001': '9951',
        '19450002': '9951',
        '19450003': '9951',
        '19450004': '9951',
        '19450005': '9951',
        '19450006': '9951',
        '19450007': '9951',
        '19450008': '9951',
        '19450009': '9951',
        '19450010': '9951',
        '19450011': '9951',
        '19450012': '9951',
        '19450013': '9951',
        '19450014': '9951',
        '19459000': '9951',
        '19459001': '9951',
        '19459999': '9951',
        '19460011': '9951',
        '19460012': '9951',
        '19460012': '9951',
        '19460014': '9951',
        '19460014': '9951',
        '19460015': '9951',
        '19460016': '9951',
        '19460017': '9951',
        '19460018': '9951',
        '19460019': '9951',
        '19460020': '9951',
        '19460020': '9951',
        '19460022': '9951',
        '19460025': '9951',
        '19460025': '9951',
        '19460026': '9951',
        '19460027': '9951',
        '19460028': '9951',
        '19460028': '9951',
        '19460029': '9951',
        '19460029': '9951',
        '19460031': '9951',
        '19460032': '9951',
        '19460033': '9951',
        '19460033': '9951',
        '19460034': '9951',
        '19460034': '9951',
        '19460035': '9951',
        '19460035': '9951',
        '19460037': '9951',
        '19460038': '9951',
        '19460040': '9951',
        '19460041': '9951',
        '19460041': '9951',
        '19460042': '9951',
        '19460043': '9951',
        '19460044': '9951',
        '19460097': '9951',
        '19460098': '9951',
        '19460099': '9951',
        '19460100': '9951',
        '19460200': '9951',
        '19460201': '9951',
        '19460300': '9951',
        '19460400': '9951',
        '19460500': '9951',
        '19460501': '9951',
        '19460600': '9951',
        '19460701': '9951',
        '19460800': '9951',
        '19460801': '9951',
        '19460802': '9951',
        '19460803': '9951',
        '19460804': '9951',
        '19460805': '9951',
        '19460806': '9951',
        '19460807': '9951',
        '19467000': '9951',
        '19468000': '9951',
        '19468900': '9951',
        '19469000': '9951',
        '19469999': '9951',
        '19474000': '9952',
        '19479000': '9952',
        '19479999': '9952',
        '19480000': '9952',
        '19480001': '9952',
        '19480002': '9952',
        '19480003': '9952',
        '19480004': '9952',
        '19480005': '9952',
        '19480006': '9952',
        '19480007': '9952',
        '19480008': '9952',
        '19480009': '9952',
        '19480010': '9952',
        '19480011': '9952',
        '19480012': '9952',
        '19480013': '9952',
        '19480014': '9952',
        '19489000': '9952',
        '19489001': '9952',
        '19489999': '9952',
        '19490100': '9952',
        '19490200': '9952',
        '19490300': '9952',
        '19490504': '9952',
        '19490505': '9952',
        '19492000': '9952',
        '19493000': '9952',
        '19494000': '9952',
        '19499999': '9952',
        '19499999': '9952',
        '19511401': '9952',
        '19511402': '9952',
        '19511403': '9952',
        '19511601': '9952',
        '19511602': '9952',
        '19511603': '9952',
        '19511604': '9952',
        '19511605': '9952',
        '19511606': '9952',
        '19511607': '9952',
        '19511608': '9952',
        '19511609': '9952',
        '19511610': '9952',
        '19511611': '9952',
        '19511612': '9952',
        '19511613': '9952',
        '19511614': '9952',
        '19511615': '9952',
        '19511616': '9952',
        '19511617': '9952',
        '19511618': '9952',
        '19511619': '9952',
        '19511620': '9952',
        '19511621': '9952',
        '19511622': '9952',
        '19511623': '9952',
        '19511624': '9952',
        '19511625': '9952',
        '19511626': '9952',
        '19511627': '9952',
        '19511628': '9952',
        '19511629': '9952',
        '19511630': '9952',
        '19511631': '9952',
        '19511632': '9952',
        '19512100': '9952',
        '19512200': '9952',
        '19512300': '9952',
        '19512400': '9952',
        '19513010': '9952',
        '19513020': '9952',
        '19513030': '9952',
        '19513040': '9952',
        '19513050': '9952',
        '19513060': '9952',
        '19513070': '9952',
        '19513080': '9952',
        '19513090': '9952',
        '19513100': '9952',
        '19513110': '9952',
        '19513120': '9952',
        '19513130': '9952',
        '19513140': '9952',
        '19513150': '9952',
        '19513160': '9952',
        '19513170': '9952',
        '19513180': '9952',
        '19513200': '9952',
        '19514000': '9952',
        '19514200': '9952',
        '19514300': '9952',
        '19514400': '9952',
        '19514500': '9952',
        '19514900': '9952',
        '19519999': '9952',
        '19520700': '9952',
        '19521269': '9952',
        '19521709': '9952',
        '19521720': '9952',
        '19521721': '9952',
        '19521722': '9952',
        '19521723': '9952',
        '19521724': '9952',
        '19521726': '9952',
        '19521727': '9952',
        '19521730': '9952',
        '19521731': '9952',
        '19521732': '9952',
        '19529999': '9952',
        '19540000': '9952',
        '19540001': '9952',
        '19540002': '9952',
        '19540003': '9952',
        '19540004': '9952',
        '19540005': '9952',
        '19540006': '9952',
        '19540007': '9952',
        '19540008': '9952',
        '19540009': '9952',
        '19540010': '9952',
        '19540011': '9952',
        '19540012': '9952',
        '19540013': '9952',
        '19540014': '9952',
        '19540015': '9952',
        '19540016': '9952',
        '19540017': '9952',
        '19540018': '9952',
        '19540019': '9952',
        '19540020': '9952',
        '19540021': '9952',
        '19540022': '9952',
        '19540023': '9952',
        '19540024': '9952',
        '19540025': '9952',
        '19540026': '9952',
        '19549000': '9952',
        '19549001': '9952',
        '19549999': '9952',
        '19699999': '9952',
        '20180011': '9952',
        '20180012': '9952',
        '20180014': '9952',
        '20180015': '9952',
        '20180016': '9952',
        '20180017': '9952',
        '20180018': '9952',
        '20180019': '9952',
        '20180020': '9952',
        '20180022': '9952',
        '20180025': '9952',
        '20180026': '9952',
        '20180027': '9952',
        '20180028': '9952',
        '20180029': '9952',
        '20180031': '9952',
        '20180032': '9952',
        '20180033': '9952',
        '20180034': '9952',
        '20180035': '9952',
        '20180037': '9952',
        '20180038': '9952',
        '20180040': '9952',
        '20180041': '9952',
        '20180042': '9952',
        '20180043': '9952',
        '20180044': '9952',
        '20180097': '9952',
        '20180098': '9952',
        '20180099': '9952',
        '20180100': '9952',
        '20180200': '9952',
        '20180201': '9952',
        '20180300': '9952',
        '20180400': '9952',
        '20180500': '9952',
        '20180501': '9952',
        '20180600': '9952',
        '20180701': '9952',
        '20180800': '9952',
        '20180801': '9952',
        '20180802': '9952',
        '20180803': '9952',
        '20180804': '9952',
        '20180805': '9952',
        '20180806': '9952',
        '20180807': '9952',
        '20187000': '9952',
        '20188000': '9952',
        '20188900': '9952',
        '20189000': '9952',
        '20189999': '9952',
        '21030011': '9952',
        '21030012': '9952',
        '21030014': '9952',
        '21030015': '9952',
        '21030020': '9952',
        '21030034': '9952',
        '21030035': '9952',
        '21030185': '9952',
        '21030281': '9952',
        '21030400': '9952',
        '21030423': '9952',
        '21030427': '9952',
        '21030440': '9952',
        '21030441': '9952',
        '21030484': '9952',
        '21030657': '9952',
        '21030750': '9952',
        '21030753': '9952',
        '21030882': '9952',
        '21031080': '9952',
        '21031100': '9952',
        '21031111': '9952',
        '21031211': '9952',
        '21031220': '9952',
        '21031311': '9952',
        '21031340': '9952',
        '21031500': '9952',
        '21031510': '9952',
        '21031520': '9952',
        '21031530': '9952',
        '21031635': '9952',
        '21032815': '9952',
        '21039999': '9952',
        '99519999': '9951',
        '99529999': '9952'
    }

    try:
        return sap_dict[input_cc]
    except KeyError:
        return 'Not Found'


def sap_accounts(line_code,
                 account_code,
                 employee_type):
    account_indicator = account_code[:5]
    direct = False
    indirect = False
    exception = False
    salary = False
    if account_indicator == '53010':
        direct = True
    elif account_indicator == '54000' or account_indicator == '54030':
        indirect = True
    elif account_indicator == '55000':
        if employee_type == 'E':
            exception = True
        else:
            salary = True
    direct_dict = {
        '1003': 'NA',
        '2000': account_indicator,
        '2006': '56080',
        '2109': '54310',
        '2110': '54310',
        '2115': '54310',
        '2120': '54310',
        '2206': '54330',
        '2207': '54330',
        '2211': '54330',
        '2214': '54330',
        '2217': '54330',
        '2220': '54330',
        '2221': '54330',
        '2222': '54330',
        '2236': '54330',
        '2306': '54310',
        '2307': '54310',
        '2311': '54310',
        '2314': '54310',
        '2317': '54310',
        '2406': '54310',
        '2407': '54310',
        '2411': '54310',
        '2414': '54310',
        '2417': '54310',
        '2500': '56020',
        '2501': '56010',
        '2502': '56060',
        '2504': '56080',
        '2507': account_indicator,
        '2509': '56080',
        '2517': '56080',
        '2600': '56080',
        '2613': '56070',
        '2801': '56010',
        '2806': '56010',
        '2B15': '54310',
        '2B20': '54310',
        '2P15': '54310',
        '2P20': '54310',
        '3004': '58060',
        '3005': '58060',
        '3021': '56290',
        '3029': '54350',
        '3033': account_indicator,
        '3037': '57480',
        '3039': '21295',
        '3042': '58020',
        '3076': '56390',
        '3078': '56390',
        '3079': '56390',
        '3080': '56390',
        '3092': account_indicator,
        '3108': account_indicator,
        '3120': 'NA',
        '3121': 'NA',
        '3125': 'NA',
        '3150': account_indicator,
        '3151': '54070',
        '3152': '54350',
        '3153': '54330',
        '3205': 'NA',
        '3210': 'NA',
        '3212': 'NA',
        '3213': 'NA',
        '336S': '56370',
        '33BS': 'NA',
        '352S': '54350',
        '356S': 'NA',
        '3599': '21290 (Company Code)',
        '3626': account_indicator,
        '3628': account_indicator,
        '3634': '54350',
        '3640': '54350',
        '3643': '54350',
        '3644': '54340',
        '3651': '54340',
        '3655': '54350',
        '3656': '54350',
        '5002': '56240',
        '5003': account_indicator,
        '5004': '56240',
        '5005': '56240',
        '7500': 'NA',
        '7505': '22640',
        '7511': '58250',
        '7512': '58250',
        '7522': '57480',
        '7524': '22630',
        '7526': '22630',
        '7527': '21290 (Company Code)',
        '7546': '56280',
        '7699': '22630',
        '7700': '22630',
        '7701': '22630',
        '7702': '22630',
        '7705': '22630',
        '7706': '22630',
        '7707': '22630',
        '7721': '22630',
        '7731': '22630',
        '7800': '21290 (Company Code)',
        '7801': '21290 (Company Code)',
        '7802': '21290 (Company Code)',
        '7803': '21290 (Company Code)',
        '7804': '21290 (Company Code)',
        '7805': '21290 (Company Code)',
        '7806': '21290 (Company Code)',
        '7820': '21290 (Company Code)',
        '7831': '21290 (Company Code)',
        '7833': '21290 (Company Code)',
        '7834': '21290 (Company Code)',
        '8100': '21290 (Company Code)',
        '8101': '21290 (Company Code)',
        '8102': '21290 (Company Code)',
        '8113': '21290 (Company Code)',
        '8117': '21290 (Company Code)',
        '8132': '21290 (Company Code)',
        '8140': '21290 (Company Code)',
        '8300': '56510',
        '8301': '56510',
        '8304': '56510',
        '8332': '56510',
        '8340': '56510',
        '8400': '22640',
        '8598': '21290 (Company Code)',
        '8599': '21290 (Company Code)',
        '9559': '21290 (Company Code)',
        '9900': 'NA',
        '9993': '21290 (Company Code)',
        '/401': '21290 (Company Code)',
        '/403': '21290 (Company Code)',
        '/404': '56210',
        '/405': '21290 (Company Code)',
        '/406': '56210',
        '/410': '56230',
        '/441': '21290 (Company Code)',
        '/450': '21290 (Company Code)',
        '/451': '21290 (Company Code)',
        '/453': '21290 (Company Code)',
        '333G': account_indicator,
        '333S': account_indicator,
        '33BG': '55040',
        '33BS': 'NA',
        '33EG': '54350',
        '33ES': '54350',
        '33ET': 'NA',
        '352G': '54350',
        '352S': '54350',
        '702D': '57450',
        '707G': 'NA',
        '719D': '57450',
        '719G': 'NA',
        '719T': 'NA',
        '720E': '56390',
        '722D': '57450',
        '722E': '56390',
        '723E': '56200',
        '724E': '56390',
        '724G': 'NA',
        '724T': 'NA',
        '725E': '56200',
        '727E': '56390',
        '728E': '56390',
        '731A': '56390',
        '739A': '56390',
        '740A': '56390',
        '742A': '56390',
        '771G': 'NA',
        '771T': 'NA',
        '773D': '22630',
        '773G': 'NA',
        '773T': 'NA',
        '779A': '22630',
        '779P': '22630',
        '779Q': '22630',
        '779R': '22630',
        '77G1': 'NA',
        '77T1': 'NA',
        '79AD': '22630',
        '79AG': 'NA',
        '79AT': 'NA',
        '818A': '21290',
        '819A': '21290',
        '834E': '22300 (Company Code)',
        '835E': '22300 (Company Code)',
        '839E': '21290',
        '840E': '21290',
        '901A': '21290',
        '901B': '21290',
        '901C': '21290',
        '910A': '56210',
        '910B': '56210',
        '9L02': '22389',
        '9M03': 'NA',
        '9M04': 'NA',
        '9S01': 'NA',
        '9T01': 'NA'
    }

    indirect_dict = {
        '1003': 'NA',
        '2000': account_indicator,
        '2006': '56080',
        '2109': '54320',
        '2110': '54320',
        '2115': '54320',
        '2120': '54320',
        '2206': '54330',
        '2207': '54330',
        '2211': '54330',
        '2214': '54330',
        '2217': '54330',
        '2220': '54330',
        '2221': '54330',
        '2222': '54330',
        '2236': '54330',
        '2306': '54320',
        '2307': '54320',
        '2311': '54320',
        '2314': '54320',
        '2317': '54320',
        '2406': '54320',
        '2407': '54320',
        '2411': '54320',
        '2414': '54320',
        '2417': '54320',
        '2500': '56020',
        '2501': '56010',
        '2502': '56060',
        '2504': '56080',
        '2507': account_indicator,
        '2509': '56080',
        '2517': '56080',
        '2600': '56080',
        '2613': '56070',
        '2801': '56010',
        '2806': '56010',
        '2B15': '54320',
        '2B20': '54320',
        '2P15': '54320',
        '2P20': '54320',
        '3004': '58060',
        '3005': '58060',
        '3021': '56290',
        '3029': '54350',
        '3033': account_indicator,
        '3037': '57480',
        '3039': '21295',
        '3042': '58020',
        '3076': '56390',
        '3078': '56390',
        '3079': '56390',
        '3080': '56390',
        '3092': account_indicator,
        '3108': account_indicator,
        '3120': 'NA',
        '3121': 'NA',
        '3125': 'NA',
        '3150': account_indicator,
        '3151': '54070',
        '3152': '54350',
        '3153': '54330',
        '3205': 'NA',
        '3210': 'NA',
        '3212': 'NA',
        '3213': 'NA',
        '336S': '56370',
        '33BS': 'NA',
        '352S': '54350',
        '356S': 'NA',
        '3599': '21290 (Company Code)',
        '3626': account_indicator,
        '3628': account_indicator,
        '3634': '54350',
        '3640': '54350',
        '3643': '54350',
        '3644': '54340',
        '3651': '54340',
        '3655': '54350',
        '3656': '54350',
        '5002': '56240',
        '5003': account_indicator,
        '5004': '56240',
        '5005': '56240',
        '7500': 'NA',
        '7505': '22640',
        '7511': '58250',
        '7512': '58250',
        '7522': '57480',
        '7524': '22630',
        '7526': '22630',
        '7527': '21290 (Company Code)',
        '7546': '56280',
        '7699': '22630',
        '7700': '22630',
        '7701': '22630',
        '7702': '22630',
        '7705': '22630',
        '7706': '22630',
        '7707': '22630',
        '7721': '22630',
        '7731': '22630',
        '7800': '21290 (Company Code)',
        '7801': '21290 (Company Code)',
        '7802': '21290 (Company Code)',
        '7803': '21290 (Company Code)',
        '7804': '21290 (Company Code)',
        '7805': '21290 (Company Code)',
        '7806': '21290 (Company Code)',
        '7820': '21290 (Company Code)',
        '7831': '21290 (Company Code)',
        '7833': '21290 (Company Code)',
        '7834': '21290 (Company Code)',
        '8100': '21290 (Company Code)',
        '8101': '21290 (Company Code)',
        '8102': '21290 (Company Code)',
        '8113': '21290 (Company Code)',
        '8117': '21290 (Company Code)',
        '8132': '21290 (Company Code)',
        '8140': '21290 (Company Code)',
        '8300': '56510',
        '8301': '56510',
        '8304': '56510',
        '8332': '56510',
        '8340': '56510',
        '8400': '22640',
        '8598': '21290 (Company Code)',
        '8599': '21290 (Company Code)',
        '9559': '21290 (Company Code)',
        '9900': 'NA',
        '9993': '21290 (Company Code)',
        '/401': '21290 (Company Code)',
        '/403': '21290 (Company Code)',
        '/404': '56210',
        '/405': '21290 (Company Code)',
        '/406': '56210',
        '/410': '56230',
        '/441': '21290 (Company Code)',
        '/450': '21290 (Company Code)',
        '/451': '21290 (Company Code)',
        '/453': '21290 (Company Code)',
        '333G': account_indicator,
        '333S': account_indicator,
        '33BG': '55040',
        '33BS': 'NA',
        '33EG': '54350',
        '33ES': '54350',
        '33ET': 'NA',
        '352G': '54350',
        '352S': '54350',
        '702D': '57450',
        '707G': 'NA',
        '719D': '57450',
        '719G': 'NA',
        '719T': 'NA',
        '720E': '56390',
        '722D': '57450',
        '722E': '56390',
        '723E': '56200',
        '724E': '56390',
        '724G': 'NA',
        '724T': 'NA',
        '725E': '56200',
        '727E': '56390',
        '728E': '56390',
        '731A': '56390',
        '739A': '56390',
        '740A': '56390',
        '742A': '56390',
        '771G': 'NA',
        '771T': 'NA',
        '773D': '22630',
        '773G': 'NA',
        '773T': 'NA',
        '779A': '22630',
        '779P': '22630',
        '779Q': '22630',
        '779R': '22630',
        '77G1': 'NA',
        '77T1': 'NA',
        '79AD': '22630',
        '79AG': 'NA',
        '79AT': 'NA',
        '818A': '21290',
        '819A': '21290',
        '834E': '22300 (Company Code)',
        '835E': '22300 (Company Code)',
        '839E': '21290',
        '840E': '21290',
        '901A': '21290',
        '901B': '21290',
        '901C': '21290',
        '910A': '56210',
        '910B': '56210',
        '9L02': '22389',
        '9M03': 'NA',
        '9M04': 'NA',
        '9S01': 'NA',
        '9T01': 'NA'
    }

    exception_dict = {
        '1003': 'NA',
        '2000': account_indicator,
        '2006': '56080',
        '2109': '55030',
        '2110': '55030',
        '2115': '55030',
        '2120': '55030',
        '2206': '54330',
        '2207': '54330',
        '2211': '54330',
        '2214': '54330',
        '2217': '54330',
        '2220': '54330',
        '2221': '54330',
        '2222': '54330',
        '2236': '54330',
        '2306': '55030',
        '2307': '55030',
        '2311': '55030',
        '2314': '55030',
        '2317': '55030',
        '2406': '55030',
        '2407': '55030',
        '2411': '55030',
        '2414': '55030',
        '2417': '55030',
        '2500': '56020',
        '2501': '56010',
        '2502': '56060',
        '2504': '56080',
        '2507': account_indicator,
        '2509': '56080',
        '2517': '56080',
        '2600': '56080',
        '2613': '56070',
        '2801': '56010',
        '2806': '56010',
        '2B15': '55030',
        '2B20': '55030',
        '2P15': '55030',
        '2P20': '55030',
        '3004': '58060',
        '3005': '58060',
        '3021': '56290',
        '3029': '54350',
        '3033': account_indicator,
        '3037': '57480',
        '3039': '21295',
        '3042': '58020',
        '3076': '56390',
        '3078': '56390',
        '3079': '56390',
        '3080': '56390',
        '3092': account_indicator,
        '3108': account_indicator,
        '3120': 'NA',
        '3121': 'NA',
        '3125': 'NA',
        '3150': account_indicator,
        '3151': '54070',
        '3152': '54350',
        '3153': '54330',
        '3205': 'NA',
        '3210': 'NA',
        '3212': 'NA',
        '3213': 'NA',
        '336S': '56370',
        '33BS': 'NA',
        '352S': '54350',
        '356S': 'NA',
        '3599': '21290 (Company Code)',
        '3626': account_indicator,
        '3628': account_indicator,
        '3634': '54350',
        '3640': '54350',
        '3643': '54350',
        '3644': '54340',
        '3651': '54340',
        '3655': '54350',
        '3656': '54350',
        '5002': '56240',
        '5003': account_indicator,
        '5004': '56240',
        '5005': '56240',
        '7500': 'NA',
        '7505': '22640',
        '7511': '58250',
        '7512': '58250',
        '7522': '57480',
        '7524': 'NA',
        '7526': '22630',
        '7527': '21290 (Company Code)',
        '7546': '56280',
        '7699': '22630',
        '7700': '22630',
        '7701': '22630',
        '7702': '22630',
        '7705': '22630',
        '7706': '22630',
        '7707': '22630',
        '7721': '22630',
        '7731': '22630',
        '7800': '21290 (Company Code)',
        '7801': '21290 (Company Code)',
        '7802': '21290 (Company Code)',
        '7803': '21290 (Company Code)',
        '7804': '21290 (Company Code)',
        '7805': '21290 (Company Code)',
        '7806': '21290 (Company Code)',
        '7820': '21290 (Company Code)',
        '7831': '21290 (Company Code)',
        '7833': '21290 (Company Code)',
        '7834': '21290 (Company Code)',
        '8100': '21290 (Company Code)',
        '8101': '21290 (Company Code)',
        '8102': '21290 (Company Code)',
        '8113': '21290 (Company Code)',
        '8117': '21290 (Company Code)',
        '8132': '21290 (Company Code)',
        '8140': '21290 (Company Code)',
        '8300': '56510',
        '8301': '56510',
        '8304': '56510',
        '8332': '56510',
        '8340': '56510',
        '8400': '22640',
        '8598': '21290 (Company Code)',
        '8599': '21290 (Company Code)',
        '9559': '21290 (Company Code)',
        '9900': 'NA',
        '9993': '21290 (Company Code)',
        '/401': '21290 (Company Code)',
        '/403': '21290 (Company Code)',
        '/404': '56210',
        '/405': '21290 (Company Code)',
        '/406': '56210',
        '/410': '56230',
        '/441': '21290 (Company Code)',
        '/450': '21290 (Company Code)',
        '/451': '21290 (Company Code)',
        '/453': '21290 (Company Code)',
        '333G': account_indicator,
        '333S': account_indicator,
        '33BG': '55040',
        '33BS': 'NA',
        '33EG': '54350',
        '33ES': '54350',
        '33ET': 'NA',
        '352G': '54350',
        '352S': '54350',
        '702D': '57450',
        '707G': 'NA',
        '719D': '57450',
        '719G': 'NA',
        '719T': 'NA',
        '720E': '56390',
        '722D': '57450',
        '722E': '56390',
        '723E': '56200',
        '724E': '56390',
        '724G': 'NA',
        '724T': 'NA',
        '725E': '56200',
        '727E': '56390',
        '728E': '56390',
        '731A': '56390',
        '739A': '56390',
        '740A': '56390',
        '742A': '56390',
        '771G': 'NA',
        '771T': 'NA',
        '773D': '22630',
        '773G': 'NA',
        '773T': 'NA',
        '779A': '22630',
        '779P': '22630',
        '779Q': '22630',
        '779R': '22630',
        '77G1': 'NA',
        '77T1': 'NA',
        '79AD': '22630',
        '79AG': 'NA',
        '79AT': 'NA',
        '818A': '21290',
        '819A': '21290',
        '834E': '22300 (Company Code)',
        '835E': '22300 (Company Code)',
        '839E': '21290',
        '840E': '21290',
        '901A': '21290',
        '901B': '21290',
        '901C': '21290',
        '910A': '56210',
        '910B': '56210',
        '9L02': '22389',
        '9M03': 'NA',
        '9M04': 'NA',
        '9S01': 'NA',
        '9T01': 'NA'
    }

    salary_dict = {
        '1003': account_indicator,
        '2000': account_indicator,
        '2006': 'NA',
        '2109': '55030',
        '2110': '55030',
        '2115': '55030',
        '2120': '55030',
        '2206': 'NA',
        '2207': 'NA',
        '2211': 'NA',
        '2214': 'NA',
        '2217': 'NA',
        '2220': 'NA',
        '2221': 'NA',
        '2222': 'NA',
        '2236': 'NA',
        '2306': 'NA',
        '2307': 'NA',
        '2311': 'NA',
        '2314': 'NA',
        '2317': 'NA',
        '2406': 'NA',
        '2407': 'NA',
        '2411': 'NA',
        '2414': 'NA',
        '2417': 'NA',
        '2500': 'NA',
        '2501': 'NA',
        '2502': 'NA',
        '2504': 'NA',
        '2507': account_indicator,
        '2509': 'NA',
        '2517': 'NA',
        '2600': 'NA',
        '2613': '56070',
        '2801': '55000',
        '2806': '55000',
        '2B15': '55030',
        '2B20': '55030',
        '2P15': '55030',
        '2P20': '55030',
        '3004': '58060',
        '3005': '58060',
        '3021': '56290',
        '3029': 'NA',
        '3033': account_indicator,
        '3037': 'NA',
        '3039': '21295',
        '3042': '58020',
        '3076': '56390',
        '3078': '56390',
        '3079': '56390',
        '3080': '56390',
        '3092': account_indicator,
        '3108': account_indicator,
        '3120': '55000',
        '3121': '55000',
        '3125': '55000',
        '3150': account_indicator,
        '3151': 'NA',
        '3152': '54350',
        '3153': '55000',
        '3205': '55000',
        '3210': '56070',
        '3212': '56070',
        '3213': '56070',
        '336S': '56370',
        '33BS': 'NA',
        '352S': '54350',
        '356S': 'NA',
        '3599': '21290 (Company Code)',
        '3626': account_indicator,
        '3628': account_indicator,
        '3634': '55040',
        '3640': '54350',
        '3643': '54350',
        '3644': '54340',
        '3651': '54340',
        '3655': '54350',
        '3656': '54350',
        '5002': '56240',
        '5003': account_indicator,
        '5004': '56240',
        '5005': '56240',
        '7500': 'NA',
        '7505': '22640',
        '7511': '58250',
        '7512': '58250',
        '7522': 'NA',
        '7524': 'NA',
        '7526': 'NA',
        '7527': '21290 (Company Code)',
        '7546': '56280',
        '7699': 'NA',
        '7700': 'NA',
        '7701': 'NA',
        '7702': 'NA',
        '7705': 'NA',
        '7706': 'NA',
        '7707': 'NA',
        '7721': 'NA',
        '7731': 'NA',
        '7800': '21290 (Company Code)',
        '7801': '21290 (Company Code)',
        '7802': '21290 (Company Code)',
        '7803': '21290 (Company Code)',
        '7804': '21290 (Company Code)',
        '7805': '21290 (Company Code)',
        '7806': '21290 (Company Code)',
        '7820': '21290 (Company Code)',
        '7831': '21290 (Company Code)',
        '7833': '21290 (Company Code)',
        '7834': '21290 (Company Code)',
        '8100': '21290 (Company Code)',
        '8101': '21290 (Company Code)',
        '8102': '21290 (Company Code)',
        '8113': '21290 (Company Code)',
        '8117': '21290 (Company Code)',
        '8132': '21290 (Company Code)',
        '8140': '21290 (Company Code)',
        '8300': '56510',
        '8301': '56510',
        '8304': '56510',
        '8332': '56510',
        '8340': '56510',
        '8400': '22640',
        '8598': '21290 (Company Code)',
        '8599': '21290 (Company Code)',
        '9559': '21290 (Company Code)',
        '9900': 'NA',
        '9993': '21290 (Company Code)',
        '/401': '21290 (Company Code)',
        '/403': '21290 (Company Code)',
        '/404': '56210',
        '/405': '21290 (Company Code)',
        '/406': '56210',
        '/410': '56230',
        '/441': '21290 (Company Code)',
        '/450': '21290 (Company Code)',
        '/451': '21290 (Company Code)',
        '/453': '21290 (Company Code)',
        '333G': account_indicator,
        '333S': account_indicator,
        '33BG': '55040',
        '33BS': 'NA',
        '33EG': '54350',
        '33ES': '54350',
        '33ET': 'NA',
        '352G': '54350',
        '352S': '54350',
        '702D': '57450',
        '707G': 'NA',
        '719D': 'NA',
        '719G': 'NA',
        '719T': 'NA',
        '720E': '56390',
        '722D': 'NA',
        '722E': '56390',
        '723E': '56200',
        '724E': '56390',
        '724G': 'NA',
        '724T': 'NA',
        '725E': '56200',
        '727E': '56390',
        '728E': '56390',
        '731A': '56390',
        '739A': '56390',
        '740A': '56390',
        '742A': '56390',
        '771G': 'NA',
        '771T': 'NA',
        '773D': 'NA',
        '773G': 'NA',
        '773T': 'NA',
        '779A': 'NA',
        '779P': 'NA',
        '779Q': 'NA',
        '779R': 'NA',
        '77G1': 'NA',
        '77T1': 'NA',
        '79AD': 'NA',
        '79AG': 'NA',
        '79AT': 'NA',
        '818A': '21290',
        '819A': '21290',
        '834E': '22300 (Company Code)',
        '835E': '22300 (Company Code)',
        '839E': '21290',
        '840E': '21290',
        '901A': '21290',
        '901B': '21290',
        '901C': '21290',
        '910A': '56210',
        '910B': '56210',
        '9L02': '22389',
        '9M03': 'NA',
        '9M04': 'NA',
        '9S01': 'NA',
        '9T01': 'NA'
    }

    try:
        if direct is True:
            return direct_dict[line_code]
        elif indirect is True:
            return indirect_dict[line_code]
        elif exception is True:
            return exception_dict[line_code]
        elif salary is True:
            return salary_dict[line_code]
        else:
            return "Not Found"
    except KeyError:
        return "Not Found"
