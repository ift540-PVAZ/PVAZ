# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Designspecifications(models.Model):
    designspecificationid = models.AutoField(db_column='DesignSpecificationID', primary_key=True)  # Field name made lowercase.
    solarpanel_modelid = models.ForeignKey('Solarpanel', models.DO_NOTHING, db_column='SolarPanel_ModelID')  # Field name made lowercase.
    modelnumber = models.IntegerField(db_column='ModelNumber', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    size = models.FloatField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=45, blank=True, null=True)  # Field name made lowercase.
    totalnoofcells = models.IntegerField(db_column='TotalNoOfCells', blank=True, null=True)  # Field name made lowercase.
    encapsulant = models.CharField(db_column='Encapsulant', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frontdesign = models.CharField(db_column='FrontDesign', max_length=45, blank=True, null=True)  # Field name made lowercase.
    backdesign = models.CharField(db_column='BackDesign', max_length=45, blank=True, null=True)  # Field name made lowercase.
    typemodeldesignation = models.CharField(db_column='TypeModelDesignation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    modelmanufacturingdate = models.DateTimeField(db_column='ModelManufacturingDate', blank=True, null=True)  # Field name made lowercase.
    moduletotalarea = models.FloatField(db_column='ModuleTotalArea', blank=True, null=True)  # Field name made lowercase.
    moduleweight = models.FloatField(db_column='ModuleWeight', blank=True, null=True)  # Field name made lowercase.
    individualcellarea = models.FloatField(db_column='IndividualCellArea', blank=True, null=True)  # Field name made lowercase.
    celltechnology = models.CharField(db_column='CellTechnology', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cellmanufacturerandpartno = models.CharField(db_column='CellManufacturerAndPartNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cellmanufacturinglocation = models.CharField(db_column='CellManufacturingLocation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    noofcellsinseries = models.IntegerField(db_column='NoOfCellsInSeries', blank=True, null=True)  # Field name made lowercase.
    noofcellsinparallel = models.IntegerField(db_column='NoOfCellsInParallel', blank=True, null=True)  # Field name made lowercase.
    noofbypassdiodes = models.IntegerField(db_column='NoOfBypassDiodes', blank=True, null=True)  # Field name made lowercase.
    bypassdioderating = models.FloatField(db_column='BypassDiodeRating', blank=True, null=True)  # Field name made lowercase.
    bypassdiodemaxjunctiontemp = models.FloatField(db_column='BypassDiodeMaxJunctionTemp', blank=True, null=True)  # Field name made lowercase.
    seriesfuserating = models.FloatField(db_column='SeriesFuseRating', blank=True, null=True)  # Field name made lowercase.
    interconnectmaterialandsuppliermodelno = models.CharField(db_column='InterconnectMaterialAndSupplierModelNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    superstratetype = models.CharField(db_column='SuperstrateType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    superstratemanufacturerandpartno = models.CharField(db_column='SuperstrateManufacturerAndPartNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    substratetype = models.CharField(db_column='SubstrateType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    substratemanufacturerandpartno = models.CharField(db_column='SubstrateManufacturerAndPartNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frametypematerial = models.CharField(db_column='FrameTypeMaterial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frameadhesive = models.CharField(db_column='FrameAdhesive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    encapsulanttype = models.CharField(db_column='EncapsulantType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    encapsulantmanufacturerandpartno = models.CharField(db_column='EncapsulantManufacturerAndPartNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxtype = models.CharField(db_column='JunctionBoxType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxmanufacturerandpartno = models.CharField(db_column='JunctionBoxManufacturerAndPartNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxplottingmaterial = models.CharField(db_column='JunctionBoxPlottingMaterial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    junctionboxadhesive = models.CharField(db_column='JunctionBoxAdhesive', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cableandconnectortype = models.CharField(db_column='CableAndConnectorType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    maximumsystemvoltage = models.FloatField(db_column='MaximumSystemVoltage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'designspecifications'
        unique_together = (('designspecificationid', 'solarpanel_modelid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manufacturer(models.Model):
    manufacturerid = models.AutoField(db_column='ManufacturerID', primary_key=True)  # Field name made lowercase.
    manufacturername = models.CharField(db_column='ManufacturerName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    authorityname = models.CharField(db_column='AuthorityName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Performanceparameters(models.Model):
    performanceid = models.AutoField(db_column='PerformanceID', primary_key=True)  # Field name made lowercase.
    power = models.FloatField(db_column='Power', blank=True, null=True)  # Field name made lowercase.
    voltage = models.FloatField(db_column='Voltage', blank=True, null=True)  # Field name made lowercase.
    current = models.FloatField(db_column='Current', blank=True, null=True)  # Field name made lowercase.
    temperaturecoefficient = models.FloatField(db_column='TemperatureCoefficient', blank=True, null=True)  # Field name made lowercase.
    testcondition = models.CharField(db_column='TestCondition', max_length=45, blank=True, null=True)  # Field name made lowercase.
    modelid = models.ForeignKey('Solarpanel', models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'performanceparameters'


class Solarpanel(models.Model):
    modelid = models.AutoField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    designspecificationid = models.CharField(db_column='DesignSpecificationID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    manufacturer_manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='Manufacturer_ManufacturerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solarpanel'
        unique_together = (('modelid', 'manufacturer_manufacturerid'),)


class SolarpanelHasTestcondition(models.Model):
    solarpanel_modelid = models.ForeignKey(Solarpanel, models.DO_NOTHING, db_column='SolarPanel_ModelID', primary_key=True)  # Field name made lowercase.
    testcondition_name = models.ForeignKey('Testcondition', models.DO_NOTHING, db_column='TestCondition_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solarpanel_has_testcondition'
        unique_together = (('solarpanel_modelid', 'testcondition_name'),)


class Testcondition(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=45)  # Field name made lowercase.
    irradiance = models.FloatField(db_column='Irradiance', blank=True, null=True)  # Field name made lowercase.
    ambienttemperature = models.FloatField(db_column='AmbientTemperature', blank=True, null=True)  # Field name made lowercase.
    airmass = models.FloatField(db_column='AirMass', blank=True, null=True)  # Field name made lowercase.
    windspeed = models.FloatField(db_column='WindSpeed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testcondition'
