
ALL_CARVERS = {

    ('диван',): {     # CARVERS_FOR_FIRNITURE 
            'Описание': '''\t\t\t\t<entry><bean class="SofaFillingCarver"/></entry>
    \t\t\t<entry><bean class="SofaTransformerCarver"/></entry>
    \t\t\t<entry><bean class="SofaMaterialCarver"/></entry>
    \t\t\t<entry><bean class="SofaFeatureCarver"/></entry>'''
        },
        ('стол',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureStolyFormCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyFeatureCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyTransformCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureStolyFormCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyFeatureCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureStolyTransformCarver"/></entry>'''
        },
        ('кресло',): {
            'Описание': '''\t\t\t\t<entry><bean class="ArmchairsSupportCarver"/></entry>
    \t\t\t<entry><bean class="ArmchairsFeatureCarver"/></entry>
    \t\t\t<entry><bean class="ArmchairsMaterialCarver"/></entry>'''
        },
        ('стул',): {
            'Описание': '''\t\t\t\t<entry><bean class="ChairsFrameMaterialCarver"/></entry>
    \t\t\t<entry><bean class="ChairsUpholsteryMaterialCarver"/></entry>
    \t\t\t<entry><bean class="ChairsFeatureCarver"/></entry>'''
        },
        ('кухонный гарнитур',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureKitchenSetsTypeCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureKitchenSetsFeatureCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureKitchenSetsMaterialCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureKitchenSetsTypeCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureKitchenSetsFeatureCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureKitchenSetsMaterialCarver"/></entry>'''
        },
        ('матрас',): {
            'Описание': '''\t\t\t\t<entry><bean class="MattressTypeCarver"/></entry>
    \t\t\t<entry><bean class="MattressFillingCarver"/></entry>
    \t\t\t<entry><bean class="MattressFeatureCarver"/></entry>'''
        },
        ('шкаф',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>'''
        },
        ('стеллаж',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>'''
        },
        ('полка',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureCabinetsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsDoorsCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureCabinetsFeatureCarver"/></entry>'''
        },
        ('комод',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureDressersBoxesCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureDressersMaterialCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="FurnitureDressersBoxesCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureDressersMaterialCarver"/></entry>'''
        },
        ('кровать',): {
            'Описание': '''\t\t\t\t<entry><bean class="FurnitureBedsAreaCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureBedsMaterialCarver"/></entry>
    \t\t\t<entry><bean class="FurnitureBedsFeatureCarver"/></entry>'''
        },

    ('электропила', 'бензопила', 'пила'): {  # Одинаковые 4 из  5 карвера ставлю и в описание и в наименование    CARVERS_FOR_ELECTROBENZO 
        'Наименование': '''\t\t\t\t<entry><bean class="HomeToolsBatteryCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsDiscCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsEngineCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsSawCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPowerCarver"/></entry>''',
    'Описание':'''\t\t\t\t<entry><bean class="HomeToolsDiscCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsEngineCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsSawCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPowerCarver"/></entry>'''
    },

    ('генератор',): # CARVERS_FOR_GENERATORS
        {
            'Описание': '''\t\t\t\t<entry><bean class="GeneratorPowerCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorVoltageCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorFeaturesCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorStartTypeCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorTypeCarver"/></entry>''',
            'Наименование': '''\t\t\t\t<entry><bean class="GeneratorPowerCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorVoltageCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorFeaturesCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorStartTypeCarver"/></entry>
    \t\t\t<entry><bean class="GeneratorTypeCarver"/></entry>'''
        },


        ("смеситель", "душ", "душевой шланг", "душевое оборудование"): # CARVERS_FOR_SANTECHNIKA
    {'Наименование':'''\t\t\t\t<entry><bean class="SanitaryLiquidizerCarver"/></entry>'''},
    ('ванна',):{'Наименование':'''\t\t\t\t<entry><bean class="SanitaryShapeCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>''',
    'Описание':'''\t\t\t\t<entry><bean class="SanitaryShapeCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>
    \t\t\t<entry><bean class="SanitaryBathCarver"/></entry>'''},
    #('ванна','раковина'):{'''\t\t\t\t<entry><bean class="SanitaryColorCarver"/></entry>'''}

    ('sup-доска', 'сап-доска','сап доска','sup доска'): # CARVERS_FOR_SUPDOSKI
    {'Наименование':'''\t\t\t\t<entry><bean class="SupBrandCarver"/></entry>
    \t\t\t<entry><bean class="SupLengthCarver"/></entry>''',
    'Описание':'''\t\t\t\t<entry><bean class="SupBrandCarver"/></entry>
    \t\t\t<entry><bean class="SupLengthCarver"/></entry>'''},


    (  "болторез", "арматурорез", "бормашина", "гравер", "гайковерт",  # CARVERS_FOR_ELECTROINSTRUMENTS
    "винтоверт", "дрель", "заклепочник", "лобзик", "молоток отбойный", 
    "набор электроинструментов", "ножницы", "отвертка", "перфоратор", 
    "пистолет для вязки арматуры", "дрель алмазного бурения", 
    "пистолет для герметика аккумуляторный", "пистолет клеевой", 
    "реноватор", "рубанок", "степлер", "гвоздезабиватель", 
    "труборез электрический", "фен строительный", "фрезер", 
    "шлифмашина", "штроборез", "шуруповерт"):

    {'Наименование':'''\t\t\t\t<entry><bean class="HomeToolsBatteryCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsSquareCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPowerSupplyCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPowerCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsDiscCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsGrinderCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsHammerCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPneumaticCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsDrillCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="HomeToolsPowerSupplyCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPowerCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsDiscCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsGrinderCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsHammerCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsPneumaticCarver"/></entry>
    \t\t\t<entry><bean class="HomeToolsDrillCarver"/></entry>'''},

    ("водонагреватель",): # CARVERS_FOR_WATERHEATER
    {'Наименование':'''\t\t\t\t<entry><bean class="WaterHeaterPowerCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterVolumeCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterHeatCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterTypeCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="WaterHeaterPowerCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterVolumeCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterHeatCarver"/></entry>
    \t\t\t<entry><bean class="WaterHeaterTypeCarver"/></entry>'''},

    ("кондиционер", "сплит-система"): # CARVERS_FOR_CONDITIONERS
    {'Наименование':'''\t\t\t\t<entry><bean class="ConditionersTypeCarver"/></entry>
    \t\t\t<entry><bean class="ConditionerCompressorCarver"/></entry>
    \t\t\t<entry><bean class="ConditionerFormCarver"/></entry>
    \t\t\t<entry><bean class="ConditionersAreaCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="ConditionersTypeCarver"/></entry>
    \t\t\t<entry><bean class="ConditionerCompressorCarver"/></entry>
    \t\t\t<entry><bean class="ConditionersAreaCarver"/></entry>'''},

    ("оперативная память",): # CARVERS_FOR_COMPUTER
    {'Наименование':'''\t\t\t\t<entry><bean class="RamCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="RamCarver"/></entry>'''},

    ("Материнская плата",):
    {'Наименование':'''\t\t\t\t<entry><bean class="MotherBoardCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="MotherBoardCarver"/></entry>'''},

    ("Ноутбук",): # CARVERS_FOR_NOTEBOOK
    {'Наименование':'''\t\t\t\t<entry><bean class="NotebookTypeCarver"/></entry>
    \t\t\t<entry><bean class="NotebookScreenSizeCarver"/></entry>
    \t\t\t<entry><bean class="NotebookFeaturesCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="NotebookTypeCarver"/></entry>
    \t\t\t<entry><bean class="NotebookScreenSizeCarver"/></entry>
    \t\t\t<entry><bean class="NotebookFeaturesCarver"/></entry>'''},

    ("телефон", "смартфон"): # CARVERS_FOR_PHONE
    {'Наименование':
                    '''\t\t\t\t<entry><bean class="PhoneInternalMemoryCarver"/></entry>
                <entry><bean class="PhoneDiagonalCarver"/></entry>
                <entry><bean class="PhoneFormFactorCarver"/></entry>
                <entry><bean class="ColorCarver"/></entry>
                <entry><bean class="PhoneFunctionsCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="PhoneInternalMemoryCarver"/></entry>
    \t\t\t<entry><bean class="PhoneDiagonalCarver"/></entry>
    \t\t\t<entry><bean class="PhoneFormFactorCarver"/></entry>
    \t\t\t<entry><bean class="ColorCarver"/></entry>
    \t\t\t<entry><bean class="PhoneFunctionsCarver"/></entry>'''},

                        ("телевизор",): # CARVERS_FOR_TV
    {'Наименование':'''\t\t\t\t<entry><bean class="TvTypeCarver"/></entry>
    \t\t\t<entry><bean class="TvDiagonalCarver"/></entry>
    \t\t\t<entry><bean class="TvResolutionCarver"/></entry>
    \t\t\t<entry><bean class="SmartTvCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="TvTypeCarver"/></entry>
    \t\t\t<entry><bean class="TvDiagonalCarver"/></entry>
    \t\t\t<entry><bean class="TvResolutionCarver"/></entry>
    \t\t\t<entry><bean class="SmartTvCarver"/></entry>'''},

                        ("монитор",):
    {'Наименование':'''\t\t\t\t<entry><bean class="MatrixTypeCarver"/></entry>
    \t\t\t<entry><bean class="DisplayTypeCarver"/></entry>
    \t\t\t<entry><bean class="ResolutionCarver"/></entry>
    \t\t\t<entry><bean class="SmartTvCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="MatrixTypeCarver"/></entry>
    \t\t\t<entry><bean class="DisplayTypeCarver"/></entry>
    \t\t\t<entry><bean class="ResolutionCarver"/></entry>
    \t\t\t<entry><bean class="SmartTvCarver"/></entry>'''},

                        ("планшет", "ipad"): # CARVERS_FOR_PDA  
    {'Наименование':'''\t\t\t\t<entry><bean class="PdaDiagonalCarver"/></entry>важно, гляди в wiki
    \t\t\t<entry><bean class="PdaOperatingSystemCarver"/></entry>
    \t\t\t<entry><bean class="PhoneInternalMemoryCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="PdaDiagonalCarver"/></entry>важно, гляди в wiki
    \t\t\t<entry><bean class="PdaOperatingSystemCarver"/></entry>
    \t\t\t<entry><bean class="PhoneInternalMemoryCarver"/></entry>'''},


                        ("Стирально-сушильная машина", "Сушильная машина", "Стиральная машина, Центрифуга"): # CARVERS_FOR_WASHER 
    {'Наименование':'''\t\t\t\t<entry><bean class="WasherTypeCarver"/></entry>
    \t\t\t<entry><bean class="WasherLoadingFeatureCarver"/></entry>
    \t\t\t<entry><bean class="WasherInstallationFeatureCarver"/></entry>
    \t\t\t<entry><bean class="WasherMaxLoadCarver"/></entry>''',

    'Описание':'''\t\t\t\t<entry><bean class="WasherTypeCarver"/></entry>
    \t\t\t<entry><bean class="WasherLoadingFeatureCarver"/></entry>
    \t\t\t<entry><bean class="WasherInstallationFeatureCarver"/></entry>
    \t\t\t<entry><bean class="WasherMaxLoadCarver"/></entry>'''}


}



