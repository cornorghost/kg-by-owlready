from owlready2 import *
import datetime

onto = get_ontology("http://Device.org/onto.owl")

with onto:
    #设备类
    class 电力设备(Thing):
        pass
    #设备子类
    class DTU(电力设备):
        pass
    class FTU(电力设备):
        pass
    class LCT(电力设备):
        pass
    class Charger(电力设备):
        pass
    '''
    **********************************************************
    '''
    #设备根属性
    class topObjectProperty(PropertyClass):
        namespace = onto

    #----------------------------------设备名称
    #属性类
    class 设备名称(Thing):
        namespace = onto
    #属性
    class 有设备名称(ObjectProperty):
        domain=[DTU,FTU,LCT,Charger]
        range=[设备名称]
    #数据类型
    class 设备名称类型(DataProperty):
        namespace=onto
        domain=[设备名称]
        range=[str]
    ''''''
    #----------------------------------电压等级
    class 电压等级(Thing):
        pass

    class 有电压等级(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT]
        range=[电压等级]

    class 电压等级类型(DataProperty):
        pass
        domain=[电压等级]
        range=[str]
    ''''''
    #----------------------------------型号
    class 型号(Thing):
        pass

    class 有型号(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT,Charger]
        range=[型号]
        
    class 型号类型(DataProperty):
        pass
        domain=[型号]
        range=[str]
    ''''''
    #----------------------------------批次
    class 批次(Thing):
        ontology = onto

    class 有批次(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT,Charger]
        range=[批次]

    class 批次类型(DataProperty):
        pass
        domain=[批次]
        range=[int]
    ''''''
    #----------------------------------厂商名
    class 生产厂家制造商名称(Thing):
        ontology = onto

    class 有生产厂家制造商名称(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT,Charger]
        range=[生产厂家制造商名称]

    class 生产厂家制造商名称类型(DataProperty):
        pass
        domain=[生产厂家制造商名称]
        range=[str]
    ''''''
    #----------------------------------出厂日期
    class 出厂日期(Thing):
        ontology = onto

    class 有出厂日期(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT,Charger]
        range=[出厂日期]

    class 出厂日期类型(DataProperty):
        pass
        domain=[出厂日期]
        range=[datetime.datetime]
    ''''''
    #----------------------------------使用的操作系统
    class 使用的操作系统(Thing):
        ontology = onto

    class 有使用的操作系统(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT]
        range=[使用的操作系统]

    class 使用的操作系统类型(DataProperty):
        pass
        domain=[使用的操作系统]
        range=[str]
    ''''''
    #----------------------------------操作系统版本
    class 操作系统版本(Thing):
        ontology = onto

    class 有操作系统版本(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT]
        range=[操作系统版本]

    class 操作系统版本类型(DataProperty):
        pass
        domain=[操作系统版本]
        range=[str]
    ''''''
    #----------------------------------固件主程序版本
    class 固件主程序版本(Thing):
        ontology = onto

    class 有固件主程序版本(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT]
        range=[固件主程序版本]

    class 固件主程序版本类型(DataProperty):
        pass
        domain=[固件主程序版本]
        range=[str]
    ''''''
    #----------------------------------使用规约及版本
    class 使用的规约及版本(Thing):
        ontology = onto

    class 有使用的规约及版本(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT]
        range=[使用的规约及版本]

    class 使用的规约及版本类型(DataProperty):
        pass
        domain=[使用的规约及版本]
        range=[str]
    ''''''
    #----------------------------------安全问题
    class 中国电科院入网测试报告中写明的安全问题(Thing):
        ontology = onto

    class 有中国电科院入网测试报告中写明的安全问题(ObjectProperty):
        pass
        domain=[DTU,FTU,LCT,Charger]
        range=[中国电科院入网测试报告中写明的安全问题]

    class 中国电科院入网测试报告中写明的安全问题类型(DataProperty):
        pass
        domain=[中国电科院入网测试报告中写明的安全问题]
        range=[str]
    #----------------------------------控制单元计费厂商
    class 充电桩计费控制单元厂商(Thing):
        pass

    class 有充电桩计费控制单元厂商(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元厂商]

    class 充电桩计费控制单元厂商类型(DataProperty):
        pass
        domain=[充电桩计费控制单元厂商]
        range=[str]
    ''''''
    #----------------------------------控制单元计费型号
    class 充电桩计费控制单元型号(Thing):
        pass

    class 有充电桩计费控制单元型号(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元型号]

    class 充电桩计费控制单元型号类型(DataProperty):
        pass
        domain=[充电桩计费控制单元型号]
        range=[str]
    ''''''
    #----------------------------------控制单元计费操作系统
    class 充电桩计费控制单元使用的操作系统(Thing):
        pass

    class 有充电桩计费控制单元使用的操作系统(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元使用的操作系统]

    class 充电桩计费控制单元使用的操作系统类型(DataProperty):
        pass
        domain=[充电桩计费控制单元使用的操作系统]
        range=[str]
    #----------------------------------控制单元计费操作系统版本
    class 充电桩计费控制单元的操作系统版本(Thing):
        pass

    class 有充电桩计费控制单元的操作系统版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元的操作系统版本]

    class 充电桩计费控制单元的操作系统版本类型(DataProperty):
        pass
        domain=[充电桩计费控制单元的操作系统版本]
        range=[str]
    #----------------------------------固控制单元计费固件主程序版本
    class 充电桩计费控制单元的固件主程序版本(Thing):
        ontology = onto

    class 有充电桩计费控制单元的固件主程序版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元的固件主程序版本]

    class 充电桩计费控制单元的固件主程序版本类型(DataProperty):
        pass
        domain=[充电桩计费控制单元的固件主程序版本]
        range=[str]
    ''''''
    #----------------------------------固控制单元计费使用规约及版本
    class 充电桩计费控制单元使用的规约及版本(Thing):
        ontology = onto

    class 有充电桩计费控制单元使用的规约及版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩计费控制单元的固件主程序版本]

    class 充电桩计费控制单元使用的规约及版本类型(DataProperty):
        pass
        domain=[充电桩计费控制单元的固件主程序版本]
        range=[str]
    ''''''
    #----------------------------------控制单元控制厂商
    class 充电桩充电控制单元厂商(Thing):
        pass

    class 有充电桩充电控制单元厂商(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元厂商]

    class 充电桩充电控制单元厂商类型(DataProperty):
        pass
        domain=[充电桩充电控制单元厂商]
        range=[str]
    ''''''
    #----------------------------------控制单元控制型号
    class 充电桩充电控制单元型号(Thing):
        pass

    class 有充电桩充电控制单元型号(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元型号]

    class 充电桩充电控制单元型号类型(DataProperty):
        pass
        domain=[充电桩充电控制单元型号]
        range=[str]
    ''''''
    #----------------------------------控制单元控制操作系统
    class 充电桩充电控制单元使用的操作系统(Thing):
        pass

    class 有充电桩充电控制单元使用的操作系统(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元使用的操作系统]

    class 充电桩充电控制单元使用的操作系统类型(DataProperty):
        pass
        domain=[充电桩充电控制单元使用的操作系统]
        range=[str]
    #----------------------------------控制单元控制操作系统版本
    class 充电桩充电控制单元的操作系统版本(Thing):
        pass

    class 有充电桩充电控制单元的操作系统版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元的操作系统版本]

    class 充电桩充电控制单元的操作系统版本类型(DataProperty):
        pass
        domain=[充电桩充电控制单元的操作系统版本]
        range=[str]
    #----------------------------------固控制单元控制固件主程序版本
    class 充电桩充电控制单元的固件主程序版本(Thing):
        ontology = onto

    class 有充电桩充电控制单元的固件主程序版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元的固件主程序版本]

    class 充电桩充电控制单元的固件主程序版本类型(DataProperty):
        pass
        domain=[充电桩充电控制单元的固件主程序版本]
        range=[str]
    ''''''
    #----------------------------------固控制单元控制使用规约及版本
    class 充电桩充电控制单元使用的规约及版本(Thing):
        ontology = onto

    class 有充电桩充电控制单元使用的规约及版本(ObjectProperty):
        pass
        domain=[Charger]
        range=[充电桩充电控制单元使用的规约及版本]

    class 充电桩充电控制单元使用的规约及版本类型(DataProperty):
        pass
        domain=[充电桩充电控制单元使用的规约及版本]
        range=[str]
    ''''''
    '''
    *********************************************************************
    '''

    # #----------------------------------设备名称
    # #属性类
    # class Name(Thing):
    #     ontology = onto
    # #属性
    # class hasName(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[Name]
    # #数据类型
    # class NameType(Property):
    #     pass
    #     domain=[Name]
    #     range=[str]
    # ''''''
    # #----------------------------------电压等级
    # class Voltage(Thing):
    #     ontology = onto

    # class hasVoltage(Property):
    #     pass
    #     domain=[DTU,FTU,LCT]
    #     range=[Voltage]

    # class VoltageType(Property):
    #     pass
    #     domain=[Voltage]
    #     range=[str]
    # ''''''
    # #----------------------------------型号
    # class Model(Thing):
    #     pass

    # class hasModel(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[Model]
        
    # class ModelType(Property):
    #     pass
    #     domain=[Model]
    #     range=[str]
    # ''''''
    # #----------------------------------批次
    # class Num(Thing):
    #     ontology = onto

    # class hasNum(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[Num]

    # class NumType(Property):
    #     pass
    #     domain=[Num]
    #     range=[int]
    # ''''''
    # #----------------------------------厂商名
    # class ProduceName(Thing):
    #     ontology = onto

    # class hasProduceName(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[ProduceName]

    # class ProduceNameType(Property):
    #     pass
    #     domain=[ProduceName]
    #     range=[str]
    # ''''''
    # #----------------------------------出厂日期
    # class ProduceDate(Thing):
    #     ontology = onto

    # class hasProduceDate(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[ProduceDate]

    # class ProduceDateType(Property):
    #     pass
    #     domain=[ProduceDate]
    #     range=[datetime.datetime]
    # ''''''
    # #----------------------------------使用的操作系统
    # class System(Thing):
    #     ontology = onto

    # class hasSystem(Property):
    #     pass
    #     domain=[DTU,FTU,LCT]
    #     range=[System]

    # class SystemType(Property):
    #     pass
    #     domain=[System]
    #     range=[str]
    # ''''''
    # #----------------------------------操作系统版本
    # class SysVersion(Thing):
    #     ontology = onto

    # class hasSysVersion(Property):
    #     pass
    #     domain=[DTU,FTU,LCT]
    #     range=[SysVersion]

    # class SysVersionType(Property):
    #     pass
    #     domain=[SysVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------固件主程序版本
    # class SofVersion(Thing):
    #     ontology = onto

    # class hasSofVersion(Property):
    #     pass
    #     domain=[DTU,FTU,LCT]
    #     range=[SofVersion]

    # class SofVersionType(Property):
    #     pass
    #     domain=[SofVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------使用规约及版本
    # class RegVersion(Thing):
    #     ontology = onto

    # class hasRegVersion(Property):
    #     pass
    #     domain=[DTU,FTU,LCT]
    #     range=[RegVersion]

    # class RegVersionType(Property):
    #     pass
    #     domain=[RegVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------安全问题
    # class Problem(Thing):
    #     ontology = onto

    # class hasProblem(Property):
    #     pass
    #     domain=[DTU,FTU,LCT,Charger]
    #     range=[Problem]

    # class ProblemType(Property):
    #     pass
    #     domain=[ProduceName]
    #     range=[str]
    # #----------------------------------控制单元计费厂商
    # class billProducer(Thing):
    #     pass

    # class hasBillProducer(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billProducer]

    # class billProducertYPE(Property):
    #     pass
    #     domain=[billProducer]
    #     range=[str]
    # ''''''
    # #----------------------------------控制单元计费型号
    # class billModel(Thing):
    #     pass

    # class hasBillModel(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billModel]

    # class billModelType(Property):
    #     pass
    #     domain=[billModel]
    #     range=[str]
    # ''''''
    # #----------------------------------控制单元计费操作系统
    # class billSystem(Thing):
    #     pass

    # class hasBillSystem(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billSystem]

    # class billSystemType(Property):
    #     pass
    #     domain=[billSystem]
    #     range=[str]
    # #----------------------------------控制单元计费操作系统版本
    # class billSysversion(Thing):
    #     pass

    # class hasBillSysversion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billSysversion]

    # class billSysversionType(Property):
    #     pass
    #     domain=[billSysversion]
    #     range=[str]
    # #----------------------------------固控制单元计费固件主程序版本
    # class billSofVersion(Thing):
    #     ontology = onto

    # class hasBillSofVersion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billSofVersion]

    # class billSofVersionType(Property):
    #     pass
    #     domain=[billSofVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------固控制单元计费使用规约及版本
    # class billRegVersion(Thing):
    #     ontology = onto

    # class hasBillRegVersion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[billRegVersion]

    # class billRegVersionType(Property):
    #     pass
    #     domain=[billRegVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------控制单元控制厂商
    # class controlProducer(Thing):
    #     pass

    # class hasControlProducer(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlProducer]

    # class controlProducerType(Property):
    #     pass
    #     domain=[controlProducer]
    #     range=[str]
    # ''''''
    # #----------------------------------控制单元控制型号
    # class controlModel(Thing):
    #     pass

    # class hasControlModel(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlModel]

    # class controlModelType(Property):
    #     pass
    #     domain=[controlModel]
    #     range=[str]
    # ''''''
    # #----------------------------------控制单元控制操作系统
    # class controlSystem(Thing):
    #     pass

    # class hasControlSystem(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlSystem]

    # class controlSystemType(Property):
    #     pass
    #     domain=[controlSystem]
    #     range=[str]
    # #----------------------------------控制单元控制操作系统版本
    # class controlSysversion(Thing):
    #     pass

    # class hasControlSysversion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlSysversion]

    # class controlSysversionType(Property):
    #     pass
    #     domain=[controlSysversion]
    #     range=[str]
    # #----------------------------------固控制单元控制固件主程序版本
    # class controlSofVersion(Thing):
    #     ontology = onto

    # class hasControlSofVersion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlSofVersion]

    # class controlSofVersionType(Property):
    #     pass
    #     domain=[controlSofVersion]
    #     range=[str]
    # ''''''
    # #----------------------------------固控制单元控制使用规约及版本
    # class controlRegVersion(Thing):
    #     ontology = onto

    # class hasControlRegVersion(Property):
    #     pass
    #     domain=[Charger]
    #     range=[controlRegVersion]

    # class controlRegVersionType(Property):
    #     pass
    #     domain=[controlRegVersion]
    #     range=[str]