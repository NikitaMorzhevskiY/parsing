import re

CARVERS_FOR_AUTO = {
    "Наименование": {
        "synonyms": re.compile(r"\b(наименовани[ея]\s*(товар[а|ов]|запчасти)?|запчасть)\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <!--<entry>
                    <bean class="dataRegexpCarver">
                        <constructor-arg>
                            <list>
                                <entry value="all"/>
                                <entry value="post"/>
                                <entry value="name"/>
                            </list>
                        </constructor-arg>
                        <constructor-arg value="@(?i)(.*?)\(?([a-z]*[а-яё]{3,}.*)@"/>
                    </bean>
                </entry>-->
                <entry><bean class="dataSimpleCarver"><constructor-arg value="name"/></bean></entry>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="note0"/></bean></entry>
                <entry><bean class="AutoDiscTireMixedCarver"/></entry>
                <entry><bean class="AutoTyreSeasonCarver"/></entry>
                <entry><bean class="AutoTyreSpikeCarver"/></entry>
                <entry><bean class="AutoDiscTypeCarver"/></entry>
                <entry><bean class="OilTypeDataCarver"/></entry>
                <entry><bean class="MotorOilApiCarver"/></entry>
                <entry><bean class="MotorOilAceaCarver"/></entry>
                <entry><bean class="OilVolumeDataCarver"/></entry>
                <entry><bean class="MotorOilFuelCarver"/></entry>
                <entry><bean class="MotorOilEngineCarver"/></entry>
                <entry><bean class="OilTransportDataCarver"/></entry>
                <entry><bean class="OilViscosityDataCarver"/></entry>
                <entry><bean class="GearOilFunctionCarver"/></entry>
                <entry><bean class="GearOilApiCarver"/></entry>
                <entry><bean class="OtherOilFunctionCarver"/></entry>
                <entry><bean class="OilViscosityIsoDataCarver"/></entry>
                <entry><bean class="BatteryTypeCarver"/></entry>
                <entry><bean class="BatteryCapacityCarver"/></entry>
                <entry><bean class="BatteryFixingCarver"/></entry>
                <entry><bean class="TypeBodyCarver"/></entry>
                <entry><bean class="StartingCurrentCarver"/></entry>
                <entry><bean class="SpeakerSystemTypeCarver"/></entry>
                <entry><bean class="SpeakerTypeCarver"/></entry>
                <entry><bean class="SpeakerSubwooferTypeCarver"/></entry>
                <entry><bean class="SpeakerSubwooferBodyCarver"/></entry>
                <entry><bean class="AmplifierChannelsCarver"/></entry>
                <entry><bean class="AudioRadioDimCarver"/></entry>    
                <entry><bean class="AutoPartsPositionCarver"/></entry>    
                <!--<entry><bean class="BikeFrameSizeCarver"/></entry>
                <entry><bean class="BikeTypeCarver"/></entry>
                <entry><bean class="BikeFrameCarver"/></entry>
                <entry><bean class="BikeWheelsCarver"/></entry>-->
            </list>
        </constructor-arg>
    </bean>
</entry>"""                    
 },
    "Цена": {
        "synonyms": re.compile(r"\bцена|стоимость\b", re.IGNORECASE),
        "xml": """<entry><bean class="PriceCarver"/></entry>"""
    },
    "Артикул":{
        "synonyms": re.compile(r"\bартикул|код\b", re.IGNORECASE),
        "xml": """<entry><bean class="dataSimpleCarver"><constructor-arg value="std.art"/></bean></entry>"""
    },
    "Производитель":{
        "synonyms": re.compile(r"\bпроизводитель\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="maker"/></bean></entry>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="autoParts.manufacturer.text"/></bean></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Состояние":{
        "synonyms": re.compile(r"\bсостояние|новый\/б\.у\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="sell.condition"/>
                        <constructor-arg>
                            <list>
                                <entry key="used" value="@(?i)\\bб[\.\/\\]?у\\b|подержан|контр@"/>
                                <entry key="new" value="@(?i)нов@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="autoParts.authenticity"/>
                        <constructor-arg>
                            <list>
                                <entry key="original" value="@(?i)контр@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="condition"/></bean></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Марка":{
        "synonyms": re.compile(r"\bмарка|фирма\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="firma"/></bean></entry>
                <entry><bean class="dataSimpleNameCarver"><constructor-arg value="auto.firm"/></bean></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Модель":{
        "synonyms": re.compile(r"\bмодель\b", re.IGNORECASE),
        "xml":
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="model1"/></bean></entry>
                <entry><bean class="dataSimpleNameCarver"><constructor-arg value="auto.model"/></bean></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Кузов":{
        "synonyms": re.compile(r"\bкузов\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="body"/></bean></entry>
                <entry><bean class="AutoBodyCarver"/></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Номер":{
        "synonyms": re.compile(r"\bномер\s*(запчасти)?|oem\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="number"/></bean></entry>
                <entry>
                    <bean class="dataPregReplaceFormatCarver">
                        <constructor-arg>
                            <bean class="dataPregReplaceFormatCarver">
                                <constructor-arg>
                                    <bean class="dataSimpleCarver"><constructor-arg value="autoParts.partNumberOem"/></bean>
                                </constructor-arg>
                                <constructor-arg value="@[\/\\;\+]@"/>
                                <constructor-arg value=","/>
                            </bean>
                        </constructor-arg>
                        <constructor-arg value="@[\s\.\-]@"/>
                        <constructor-arg value=""/>
                    </bean>
                </entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Замены":{
        "synonyms": re.compile(r"\bномер\s*(замены)?|кросс\s*(номера?)?\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataPregReplaceFormatCarver">
        <constructor-arg>
                <bean class="dataPregReplaceFormatCarver">
                    <constructor-arg>
                        <bean class="dataSimpleCarver"><constructor-arg value="autoParts.partNumberSubstitutes"/></bean>
                    </constructor-arg>
                    <constructor-arg value="@[\/\\;\+]@"/>
                    <constructor-arg value=","/>
                </bean>
            </constructor-arg>
            <constructor-arg value="@[\s\.\-]@"/>
            <constructor-arg value=""/>
        </bean>
</entry>"""
    },
    "Двигатель":{
        "synonyms": re.compile(r"\bдвигатель\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry><bean class="dataSimpleCarver"><constructor-arg value="engine"/></bean></entry>
                <entry><bean class="AutoEngineCarver"/></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Год":{
        "synonyms": re.compile(r"\bгод\b", re.IGNORECASE),
        "xml": """<entry><bean class="dataSimpleCarver"><constructor-arg value="year"/></bean></entry>"""
    },
    "Сторона":{
        "synonyms": re.compile(r"\bсторона|l\-r\b", re.IGNORECASE),
        "xml": """<entry><bean class="AutoPartsLRCarver"/></entry>"""
    },
    "Положение":{
        "synonyms": re.compile(r"\bположение|f\-r\b", re.IGNORECASE),
        "xml": """<entry><bean class="AutoPartsFRCarver"/></entry>"""
    },
    "UD":{
        "synonyms": re.compile(r"\bu\-d\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="tb"/>
                        <constructor-arg>
                            <list>
                                <entry key="Верх" value="@(?i)\\bвер|\\bup\s|\\bu\\b@"/>
                                <entry key="Низ" value="@(?i)\\bниж|\\bниз|\\bdown\s|\\bd\\b@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
                <entry><bean class="AutoPartsTBCarver"/></entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Цвет":{
        "synonyms": re.compile(r"\bцвет\b", re.IGNORECASE),
        "xml": """<entry><bean class="dataSimpleCarver"><constructor-arg value="color"/></bean></entry>"""
    },
    "Описание":{
        "synonyms": re.compile(r"\bописание|примечание\b", re.IGNORECASE),
        "xml": """<entry><bean class="dataSimpleCarver"><constructor-arg value="note1"/></bean></entry>"""
    },
    "Количество":{
        "synonyms": re.compile(r"\bколичество\b", re.IGNORECASE),
        "xml": """<entry><bean class="QuantityCarver"/></entry>"""
    },
    "Валюта":{
        "synonyms": re.compile(r"\bвалюта\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="DataClassifyingRegexpCarver">
        <constructor-arg value="std.currency"/>
        <constructor-arg>
            <list>
                <entry key="usd" value="@(?i)Доллары|usd|\$@"/>
                <entry key="rur" value="@(?i)руб|ru[rb]@"/>
                <entry key="eur" value="@(?i)Евро|eur@"/>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Статус":{
        "synonyms": re.compile(r"\bналичие|статус\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="DataClassifyingRegexpCarver">
        <constructor-arg value="sell.onDemand"/>
        <constructor-arg>
            <list>
                <entry key="1" value="@(?i)заказ@"/>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Срок доставки":{
        "synonyms": re.compile(r"\bсроки?\s*(доставки)?\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry>
                    <bean class="dataRegexpCarver">
                        <constructor-arg>
                            <list>
                                <entry value="all"/>
                                <entry value="day"/>
                                </list>
                            </constructor-arg>
                        <constructor-arg value="@(?i)(\\b[1-9]\d?\s?\-\s?\d{1,2}|\\b[2-9]\\b|\\b[1-9]\d\\b)@"/>
                    </bean>
                </entry>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="day"/>
                        <constructor-arg>
                            <list>
                                <entry key="" value="@(?i)^\s*дня\s*$|\\b1\sдень|один\sдень|в\s*течени[ие]\s*1?\s*дня?|^\s*1\s*$|час|^\s*0\s*$@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="zakaz"/>
                        <constructor-arg>
                            <list>
                                <entry key="1 дня" value="@(?i)сегодня|\s*\\b0\\b\s?\-\s?\\b1\\b\s*$|^\s*дня?\s*$|^\s*\\b1\s*день|один\sдень|в\s*течени[ие]\s*1?\s*дня|^\s*1\s*$|час|^\s*0\s*$@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Фото":{
        "synonyms": re.compile(r"\bфото(графи[яи])?\b", re.IGNORECASE),
        "xml":
"""<entry>
    <bean class="DataSplittedUrisCarver">
        <constructor-arg>
            <list>
                <entry value="image1"/>
                <entry value="image2"/>
                <entry value="image3"/>
                <entry value="image4"/>
                <entry value="image5"/>
                <entry value="image6"/>
                <entry value="image7"/>
                <entry value="image8"/>
                <entry value="image9"/>
                <entry value="image10"/>
                <entry value="image11"/>
                <entry value="image12"/>
                <entry value="image13"/>
                <entry value="image14"/>
                <entry value="image15"/>
                <entry value="image16"/>
                <entry value="image17"/>
                <entry value="image18"/>
                <entry value="image19"/>
                <entry value="image20"/>
            </list>
        </constructor-arg>
        <constructor-arg value="@[\s\,\;]+@"/>
    </bean>
</entry>"""
    }
}

CARVERS_FOR_UKV = { "Наименование": {
        "synonyms": re.compile(r"\b(наименовани[ея]\s*(товар[а|ов])?|Номенклатура\,\sУпаковка|название)\b", re.IGNORECASE),
        "xml": 
"""\t\t\t\t<entry><bean class="dataSimpleCarver"><constructor-arg value="name"/></bean></entry>
\t\t\t\t<entry><bean class="dataSimpleCarver"><constructor-arg value="note0"/></bean></entry>"""
            },
        "Цена": {
        "synonyms": re.compile(r"\bцена|стоимость\b", re.IGNORECASE),
        "xml": """<entry><bean class="PriceCarver"/></entry>"""
    },
    "Артикул":{
        "synonyms": re.compile(r"\bартикул|код\b", re.IGNORECASE),
        "xml": """<entry><bean class="dataSimpleCarver"><constructor-arg value="std.art"/></bean></entry>"""
    },
    "Состояние":{
        "synonyms": re.compile(r"\bсостояние|новый\/б\.у\b", re.IGNORECASE),
        "xml": 
"""
<entry>
    <bean class="DataClassifyingRegexpCarver">
        <constructor-arg value="sell.condition"/>
        <constructor-arg>
            <list>
                <entry key="used" value="@(?i)\\bб[\.\/\\]?у\\b|подержан|контр@"/>
                <entry key="new" value="@(?i)нов@"/>
            </list>
        </constructor-arg>
    </bean>
</entry>"""},
    "Количество":{
        "synonyms": re.compile(r"\bколичество|остаток\b", re.IGNORECASE),
        "xml": """<entry><bean class="QuantityCarver"/></entry>"""
    },
    "Валюта":{
        "synonyms": re.compile(r"\bвалюта\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="DataClassifyingRegexpCarver">
        <constructor-arg value="currency"/>
        <constructor-arg>
            <list>
                <entry key="usd" value="@(?i)Доллары|usd|\$@"/>
                <entry key="rur" value="@(?i)руб|ru[rb]@"/>
                <entry key="eur" value="@(?i)Евро|eur@"/>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Статус":{
        "synonyms": re.compile(r"\bналичие|статус\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="DataClassifyingRegexpCarver">
        <constructor-arg value="sell.onDemand"/>
        <constructor-arg>
            <list>
                <entry key="1" value="@(?i)заказ@"/>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Срок доставки":{
        "synonyms": re.compile(r"\bсроки?\s*(доставки)?\b", re.IGNORECASE),
        "xml": 
"""<entry>
    <bean class="dataCompositeCarver">
        <constructor-arg>
            <list>
                <entry>
                    <bean class="dataRegexpCarver">
                        <constructor-arg>
                            <list>
                                <entry value="all"/>
                                <entry value="day"/>
                                </list>
                            </constructor-arg>
                        <constructor-arg value="@(?i)(\b[1-9]\d?\s?\-\s?\d{1,2}|\b[2-9]\b|\b[1-9]\d\b)@"/>
                    </bean>
                </entry>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="day"/>
                        <constructor-arg>
                            <list>
                                <entry key="" value="@(?i)^\s*дня\s*$|\b1\sдень|один\sдень|в\s*течени[ие]\s*1?\s*дня?|^\s*1\s*$|час|^\s*0\s*$@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
                <entry>
                    <bean class="DataClassifyingRegexpCarver">
                        <constructor-arg value="zakaz"/>
                        <constructor-arg>
                            <list>
                                <entry key="1 дня" value="@(?i)сегодня|\s*\b0\b\s?\-\s?\b1\b\s*$|^\s*дня?\s*$|^\s*\b1\s*день|один\sдень|в\s*течени[ие]\s*1?\s*дня|^\s*1\s*$|час|^\s*0\s*$@"/>
                            </list>
                        </constructor-arg>
                    </bean>
                </entry>
            </list>
        </constructor-arg>
    </bean>
</entry>"""
    },
    "Фото":{
        "synonyms": re.compile(r"\bфото(графи[яи])?\b", re.IGNORECASE),
        "xml":
"""<entry>
    <bean class="DataSplittedUrisCarver">
        <constructor-arg>
            <list>
                <entry value="image1"/>
                <entry value="image2"/>
                <entry value="image3"/>
                <entry value="image4"/>
                <entry value="image5"/>
                <entry value="image6"/>
                <entry value="image7"/>
                <entry value="image8"/>
                <entry value="image9"/>
                <entry value="image10"/>
                <entry value="image11"/>
                <entry value="image12"/>
                <entry value="image13"/>
                <entry value="image14"/>
                <entry value="image15"/>
                <entry value="image16"/>
                <entry value="image17"/>
                <entry value="image18"/>
                <entry value="image19"/>
                <entry value="image20"/>
            </list>
        </constructor-arg>
        <constructor-arg value="@[\s\,\;]+@"/>
    </bean>
</entry>"""
    },
    "Описание":{
        "synonyms": re.compile(r"\bописание|примечание\b", re.IGNORECASE),
        "xml": """\t\t\t\t<entry><bean class="dataSimpleCarver"><constructor-arg value="note1"/></bean></entry>"""}}



CARVERS_FOR_AVITO = {
    "Артикул":{
        "synonyms": re.compile(r"\bid\b", re.IGNORECASE),
        "xml":
"""                                <entry><bean class="dataSimpleCarver"><constructor-arg value="std.art"/></bean></entry>"""},

        "Наименование": {
        "synonyms": re.compile(r"\btitle\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <!--<entry>
                                                    <bean class="dataRegexpCarver">
                                                        <constructor-arg>
                                                            <list>
                                                                <entry value="all"/>
                                                                <entry value="post"/>
                                                                <entry value="name"/>
                                                            </list>
                                                        </constructor-arg>
                                                        <constructor-arg value="@(?i)(.*?)\(?([a-z]*[а-яё]{3,}.*)@"/>
                                                    </bean>
                                                </entry>-->
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="name"/></bean></entry>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="note0"/></bean></entry>
                                                <entry><bean class="AutoDiscTireMixedCarver"/></entry>
                                                <entry><bean class="AutoTyreSeasonCarver"/></entry>
                                                <entry><bean class="AutoTyreSpikeCarver"/></entry>
                                                <entry><bean class="AutoDiscTypeCarver"/></entry>
                                                <entry><bean class="OilTypeDataCarver"/></entry>
                                                <entry><bean class="MotorOilApiCarver"/></entry>
                                                <entry><bean class="MotorOilAceaCarver"/></entry>
                                                <entry><bean class="OilVolumeDataCarver"/></entry>
                                                <entry><bean class="MotorOilFuelCarver"/></entry>
                                                <entry><bean class="MotorOilEngineCarver"/></entry>
                                                <entry><bean class="OilTransportDataCarver"/></entry>
                                                <entry><bean class="OilViscosityDataCarver"/></entry>
                                                <entry><bean class="GearOilFunctionCarver"/></entry>
                                                <entry><bean class="GearOilApiCarver"/></entry>
                                                <entry><bean class="OtherOilFunctionCarver"/></entry>
                                                <entry><bean class="OilViscosityIsoDataCarver"/></entry>
                                                <entry><bean class="BatteryTypeCarver"/></entry>
                                                <entry><bean class="BatteryCapacityCarver"/></entry>
                                                <entry><bean class="BatteryFixingCarver"/></entry>
                                                <entry><bean class="TypeBodyCarver"/></entry>
                                                <entry><bean class="StartingCurrentCarver"/></entry>
                                                <entry><bean class="SpeakerSystemTypeCarver"/></entry>
                                                <entry><bean class="SpeakerTypeCarver"/></entry>
                                                <entry><bean class="SpeakerSubwooferTypeCarver"/></entry>
                                                <entry><bean class="SpeakerSubwooferBodyCarver"/></entry>
                                                <entry><bean class="AmplifierChannelsCarver"/></entry>
                                                <entry><bean class="AudioRadioDimCarver"/></entry>    
                                                <entry><bean class="AutoPartsPositionCarver"/></entry>    
                                                <!--<entry><bean class="BikeFrameSizeCarver"/></entry>
                                                <entry><bean class="BikeTypeCarver"/></entry>
                                                <entry><bean class="BikeFrameCarver"/></entry>
                                                <entry><bean class="BikeWheelsCarver"/></entry>-->
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""   
},
    "Описание":{
        "synonyms": re.compile(r"\bdescription\b", re.IGNORECASE),
        "xml": 
"""                                <entry><bean class="DataRawCarver"><constructor-arg value="note1"/><constructor-arg value="true"/></bean></entry>"""},


        "Номер":{
        "synonyms": re.compile(r"\boem\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="number"/></bean></entry>
                                                <entry>
                                                    <bean class="dataPregReplaceFormatCarver">
                                                        <constructor-arg>
                                                            <bean class="dataPregReplaceFormatCarver">
                                                                <constructor-arg>
                                                                    <bean class="dataSimpleCarver"><constructor-arg value="autoParts.partNumberOem"/></bean>
                                                                </constructor-arg>
                                                                <constructor-arg value="@[\/\\;\+]@"/>
                                                                <constructor-arg value=","/>
                                                            </bean>
                                                        </constructor-arg>
                                                        <constructor-arg value="@[\s\.\-]@"/>
                                                        <constructor-arg value=""/>
                                                    </bean>
                                                </entry>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""
    },

    "Состояние":{
        "synonyms": re.compile(r"\bcondition\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <entry>
                                                    <bean class="DataClassifyingRegexpCarver">
                                                        <constructor-arg value="sell.condition"/>
                                                        <constructor-arg>
                                                            <list>
                                                                <entry key="used" value="@(?i)\\bб[\.\/\\]?у\\b|подержан|контр@"/>
                                                                <entry key="new" value="@(?i)нов@"/>
                                                            </list>
                                                        </constructor-arg>
                                                    </bean>
                                                </entry>
                                                <entry>
                                                    <bean class="DataClassifyingRegexpCarver">
                                                        <constructor-arg value="autoParts.authenticity"/>
                                                        <constructor-arg>
                                                            <list>
                                                                <entry key="original" value="@(?i)контр@"/>
                                                            </list>
                                                        </constructor-arg>
                                                    </bean>
                                                </entry>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="condition"/></bean></entry>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""
    },

    "Количество":{
        "synonyms": re.compile(r"\bquantity\b", re.IGNORECASE),
        "xml": 
"""                                <entry><bean class="QuantityCarver"/></entry>"""
    },
    "Фото": {
        "synonyms": re.compile(r"\bimageurls\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="dataStrReplaceFormatCarver">
                                        <constructor-arg>
                                            <bean class="DataSplittedUrisCarver">
                                                <constructor-arg>
                                                    <list>
                                                        <entry value="image1"/>
                                                        <entry value="image2"/>
                                                        <entry value="image3"/>
                                                        <entry value="image4"/>
                                                        <entry value="image5"/>
                                                        <entry value="image6"/>
                                                        <entry value="image7"/>
                                                        <entry value="image8"/>
                                                        <entry value="image9"/>
                                                        <entry value="image10"/>
                                                        <entry value="image11"/>
                                                        <entry value="image12"/>
                                                        <entry value="image13"/>
                                                        <entry value="image14"/>
                                                        <entry value="image15"/>
                                                        <entry value="image16"/>
                                                        <entry value="image17"/>
                                                        <entry value="image18"/>
                                                        <entry value="image19"/>
                                                        <entry value="image20"/>
                                                    </list>
                                                </constructor-arg>
                                                <constructor-arg value="@[\s\,\;]+@"/>
                                            </bean>
                                        </constructor-arg>
                                        <constructor-arg value="http://avito.ru/autoload/1/items-to-feed/images?imageSlug="/>
                                        <constructor-arg value="https://50.img.avito.st"/>
                                    </bean>												
                                </entry>"""
    },
    "Статус":{
        "synonyms": re.compile(r"\bAvailability\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="DataClassifyingRegexpCarver">
                                        <constructor-arg value="sell.onDemand"/>
                                        <constructor-arg>
                                            <list>
                                                <entry key="1" value="@(?i)заказ@"/>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""

        },
    "Производитель":{
        "synonyms": re.compile(r"\bbrand\b", re.IGNORECASE),
        "xml": 
                             
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="maker"/></bean></entry>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="autoParts.manufacturer.text"/></bean></entry>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""},

    "Индекс нагрузки": 
                    {"synonyms": re.compile(r"\bloadindex\b", re.IGNORECASE),
                    "xml": 
"""<!-- LoadIndex -->			    <entry><bean class="dataSimpleCarver"><constructor-arg value="in"/></bean></entry>"""},

    "Количество болтов": 
                    {"synonyms": re.compile(r"\brimbolts\b", re.IGNORECASE),
                    "xml": 
"""<!--RimBolts-->    			    <entry><bean class="dataSimpleCarver"><constructor-arg value="spcd"/></bean></entry>"""},                

    
    "Аутентичность":{
        "synonyms": re.compile(r"\boriginality\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="DataClassifyingRegexpCarver">
                                        <constructor-arg value="autoParts.authenticity"/>
                                        <constructor-arg>
                                            <list>
                                                <entry key="original" value="@(?i)контр|оригинал@"/>
                                                <entry key="analog" value="@(?i)аналог@"/>													
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""

},

    "Расстояние болтов": {"synonyms": re.compile(r"\brimboltsdiameter\b", re.IGNORECASE),
                    "xml": 
"""<!--RimBoltsDiameter-->         <entry><bean class="dataSimpleCarver"><constructor-arg value="lpcd"/></bean></entry>"""},

    "Диаметр центрального отверстия": {"synonyms": re.compile(r"\brimdia\b", re.IGNORECASE),
                    "xml": 
"""<!--RimDIA-->    		        <entry><bean class="dataSimpleCarver"><constructor-arg value="wheel.diskHoleDiameter"/></bean></entry>"""},

    "Диаметр шины": {"synonyms": re.compile(r"\brimdiameter\b", re.IGNORECASE),
                    "xml": 
"""<!--RimDiameter--> 			    <entry><bean class="dataSimpleCarver"><constructor-arg value="wheel.diameter"/></bean></entry>"""},      

    "Вылет": {"synonyms": re.compile(r"\brimoffset\b", re.IGNORECASE),
                    "xml": 
"""<!--RimOffset--> 			    <entry><bean class="dataSimpleCarver"><constructor-arg value="wheel.et"/></bean></entry>"""},         

    "Тип диска": {"synonyms": re.compile(r"\brimtype\b", re.IGNORECASE),
                    "xml": 
"""<!--RimType-->                  <entry><bean class="AutoDiscTypeCarver"/></entry>	"""},      

    "Ширина шины": {"synonyms": re.compile(r"\bRimWidth\b", re.IGNORECASE),
                    "xml": 
"""<!--RimWidth-->     			<entry><bean class="dataSimpleCarver"><constructor-arg value="wheel.width"/></bean></entry>"""},     

    "Ранфлэт": {"synonyms": re.compile(r"\bRunFlat\b", re.IGNORECASE),
                    "xml": 
"""<!--RunFlat-->     		        <entry>
                                    <bean class="DataClassifyingRegexpCarver">
                                        <constructor-arg value="tire.runFlat"/>
                                        <constructor-arg>
                                            <list>
                                                <entry key="1" value="@(?i)да|есть@"/>	
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""},                 

    "Индекс скорости": {"synonyms": re.compile(r"\bSpeedIndex\b", re.IGNORECASE),
                    "xml": 
"""<!--SpeedIndex-->     		    <entry><bean class="dataSimpleCarver"><constructor-arg value="is"/></bean></entry>"""},     

    "Высота диска": {"synonyms": re.compile(r"\bTireAspectRatio\b", re.IGNORECASE),
                    "xml": 
"""<!--TireAspectRatio-->     	    <entry><bean class="dataSimpleCarver"><constructor-arg value="tire.height"/></bean></entry>"""},              

    "Ширина диска": {"synonyms": re.compile(r"\bTireSectionWidth\b", re.IGNORECASE),
                    "xml": 
"""<!--TireSectionWidth-->     	<entry><bean class="dataSimpleCarver"><constructor-arg value="tire.width"/></bean></entry>"""},      

    "Сезнность шины": {"synonyms": re.compile(r"\bTireType\b", re.IGNORECASE),
                    "xml": 
"""<!--TireType-->     			<entry><bean class="AutoTyreSeasonCarver"/></entry>	"""},

    "Марка":{
        "synonyms": re.compile(r"\bmake\b", re.IGNORECASE),
        "xml": 
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="firma"/></bean></entry>
                                                <entry><bean class="dataSimpleNameCarver"><constructor-arg value="auto.firm"/></bean></entry>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""
    },
    "Модель":{
        "synonyms": re.compile(r"\bmodel\b", re.IGNORECASE),
        "xml":
"""                                <entry>
                                    <bean class="dataCompositeCarver">
                                        <constructor-arg>
                                            <list>
                                                <entry><bean class="dataSimpleCarver"><constructor-arg value="model1"/></bean></entry>
                                                <entry><bean class="dataSimpleNameCarver"><constructor-arg value="auto.model"/></bean></entry>
                                            </list>
                                        </constructor-arg>
                                    </bean>
                                </entry>"""
    },
    "Цена": {
        "synonyms": re.compile(r"\bprice\b", re.IGNORECASE),
        "xml": 
"""                                <entry><bean class="PriceCarver"/></entry>"""
    },     

    "Год шины": {"synonyms": re.compile(r"\btireyear\b", re.IGNORECASE),
                    "xml": 
"""<!--TireYear-->     		    <entry>
                                    <bean class="dataRegexpCarver">
										<constructor-arg>
											<list>
												<entry value="tire.year"/>
											</list>
										</constructor-arg>
										<constructor-arg value="@(?i)\d{4}@"/>
									</bean>
								</entry>"""}
















































































}

