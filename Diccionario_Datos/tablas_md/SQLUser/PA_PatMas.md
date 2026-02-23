# SQLUser.PA_PatMas

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla maestra de **Pacientes** (Patient Master).

Contiene datos demograficos de cada paciente:
- Identificacion (RUT, numero de ficha)
- Datos personales (nombre, fecha nacimiento, sexo)
- Direccion y contacto
- Prevision de salud

**Campos clave:**
- PAPMI_No: Numero de ficha unico
- PAPMI_ID: RUT del paciente
- PAPMI_Name/Name2/Name3: Apellidos y nombre
- PAPMI_DOB: Fecha de nacimiento
- PAPMI_Sex_DR: Sexo (FK a CT_Sex)

**Relaciones:**
- PA_Adm: Admisiones del paciente
- MR_*: Registros medicos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPMI_RowId1 | bigint | PK |  | NO | - |
| PAPMI_Active | varchar |  |  | SI | Is This Patient Usable? |
| PAPMI_Alias | varchar |  |  | SI | Patient Alias |
| PAPMI_Allergy | varchar |  |  | SI | Allergy |
| PAPMI_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAPMI_Batallion | varchar |  |  | SI | Batallion |
| PAPMI_BlackList | varchar |  |  | SI | Black List Flag |
| PAPMI_CHCPatient | varchar |  |  | SI | CHC Patient |
| PAPMI_CT_HCA_DR | bigint |  | FK | SI | Des Ref CT_HCA |
| PAPMI_CT_Province_DR | bigint |  | FK | SI | Des Ref CT_Province |
| PAPMI_CT_Region_DR | bigint |  | FK | SI | Des REf Region |
| PAPMI_CardType_DR | bigint |  | FK | SI | Des Ref CardType |
| PAPMI_CheckConcession | varchar |  |  | SI | Check Concession |
| PAPMI_CheckEPV | varchar |  |  | SI | Enterprise Patient Verification |
| PAPMI_CheckFund | varchar |  |  | SI | Check Health Fund |
| PAPMI_CheckMedicare | varchar |  |  | SI | Check Medicare |
| PAPMI_CityArea_DR | bigint |  | FK | SI | Des Ref CityArea |
| PAPMI_CityBirth_DR | bigint |  | FK | SI | Des Ref CityBirth |
| PAPMI_ConcessionCardExpDate | date |  |  | SI | Concession Card ExpDate |
| PAPMI_ConcessionCardNo | varchar |  |  | SI | ConcessionCardNo |
| PAPMI_ConcessionVerifiedDate | date |  |  | SI | Concession Verified Date |
| PAPMI_CountryOfBirth_DR | bigint |  | FK | SI | Des Ref CountryOfBirth |
| PAPMI_DOB | date |  |  | SI | Patient Date Of Birth |
| PAPMI_DVAnumber | varchar |  |  | SI | DVA number |
| PAPMI_Deceased | varchar |  |  | SI | Deceased Flag |
| PAPMI_DeceasedTime | time |  |  | SI | Deceased Time |
| PAPMI_Deceased_Date | date |  |  | SI | Deceased Date |
| PAPMI_DentistClinic_DR | varchar |  | FK | SI | Des Ref DentistClinic |
| PAPMI_Dentist_DR | bigint |  | FK | SI | Des Ref Dentist |
| PAPMI_EPRDescription | varchar |  |  | SI | EPR Description |
| PAPMI_Email | varchar |  |  | SI | Email |
| PAPMI_EmailValidationStatus_DR | bigint |  | FK | SI | Des Ref PACEmailValidationStatus |
| PAPMI_EstAgeMonth | double |  |  | SI | Estimated Age In Month |
| PAPMI_EstAgeTmStmp | date |  |  | SI | Estimated Age Time Stamp |
| PAPMI_EstAgeYear | double |  |  | SI | Estimated Age In Years |
| PAPMI_EstimatedDeathDate | varchar |  |  | SI | Estimated Death Date |
| PAPMI_ForeignPhoneNo | varchar |  |  | SI | Foreign Phone Number |
| PAPMI_GPOrgAddress | varchar |  |  | SI | GPOrgAddress |
| PAPMI_GPText | varchar |  |  | SI | GP Text |
| PAPMI_GovernCardNo | varchar |  |  | SI | Government Card No_ |
| PAPMI_HealthCardExpiryDate | date |  |  | SI | HealthCardExpiryDate |
| PAPMI_HealthFundNo | varchar |  |  | SI | Health FundNo |
| PAPMI_HomeClinicNo | varchar |  |  | SI | Home Clinic number |
| PAPMI_ID | varchar |  |  | SI | Patient IC/PP/BC No |
| PAPMI_IPNo | varchar |  |  | SI | Inpatient No |
| PAPMI_IndexMark | varchar |  |  | SI | Mark "*" in Index |
| PAPMI_IndigStat_DR | bigint |  | FK | SI | Des Ref IndigStat |
| PAPMI_InsuranceCardHolder | varchar |  |  | SI | InsuranceCardHolder |
| PAPMI_LangPrim_DR | bigint |  | FK | SI | Des Ref to CTLAN |
| PAPMI_LangPrintDR | varchar |  | FK | SI | Not Used Des Ref to CTPTI |
| PAPMI_LangSecondDR | bigint |  | FK | SI | Des Ref to CTLAN (Secondary Language) |
| PAPMI_LookupDisplay | varchar |  |  | SI | Lookup Display |
| PAPMI_Medicare | varchar |  |  | SI | Medicare No |
| PAPMI_MedicareCardType_DR | bigint |  | FK | SI | Des Ref PACMedicareCardType |
| PAPMI_MedicareCode | varchar |  |  | SI | Medicare Code |
| PAPMI_MedicareExpDate | date |  |  | SI | Medicare Expiry Date |
| PAPMI_MedicareString | varchar |  |  | SI | Medicare String |
| PAPMI_MedicareSuffix_DR | bigint |  | FK | SI | Des Ref MedicareSuffix_DR |
| PAPMI_MobPhone | varchar |  |  | SI | MobPhone |
| PAPMI_Mother1_DR | bigint |  | FK | SI | Des Ref Person |
| PAPMI_Mother_DR | bigint |  | FK | SI | Des Ref to PA_Mother |
| PAPMI_Name | varchar |  |  | NO | Patient Name |
| PAPMI_Name2 | varchar |  |  | SI | Patient Name 2 |
| PAPMI_Name3 | varchar |  |  | SI | PAPMI Name3 |
| PAPMI_Name4 | varchar |  |  | SI | Name4 |
| PAPMI_Name5 | varchar |  |  | SI | Name5 |
| PAPMI_Name6 | varchar |  |  | SI | Name6 |
| PAPMI_Name7 | varchar |  |  | SI | Name7 |
| PAPMI_Name8 | varchar |  |  | SI | Name8 |
| PAPMI_No | varchar |  |  | SI | Patient No |
| PAPMI_NxtOPAdmNo | double |  |  | SI | Next OP Encounter No |
| PAPMI_OPNo | varchar |  |  | SI | Outpatient No |
| PAPMI_PAPER_DR | bigint |  | FK | SI | Des Ref to PAPER |
| PAPMI_PatCategory_DR | bigint |  | FK | SI | Des Ref to Pat. Categ |
| PAPMI_PatientFundUPI | double |  |  | SI | Patient Fund UPI |
| PAPMI_PayorVerifiedDate | date |  |  | SI | Payor Verified Date |
| PAPMI_PensionType_DR | bigint |  | FK | SI | Des Ref PensionType |
| PAPMI_PrefLanguage_DR | bigint |  | FK | SI | Des Ref PrefLanguage |
| PAPMI_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| PAPMI_Refund | varchar |  |  | SI | Refund |
| PAPMI_Remark | varchar |  |  | SI | Patient Remark |
| PAPMI_RequireAssistanceMeal | varchar |  |  | SI | RequireAssistanceMeal |
| PAPMI_RequireAssistanceMenu | varchar |  |  | SI | RequireAssistanceMenu |
| PAPMI_ResponsibleForPayment | bigint |  |  | SI | ResponsibleForPayment |
| PAPMI_RowId | bigint |  |  | NO | PAPMI Row ID |
| PAPMI_SafetyNetCardExpDate | date |  |  | SI | Safety Net Card ExpDate |
| PAPMI_SafetyNetCardNo | varchar |  |  | SI | Safety Net Card No |
| PAPMI_SecondPhone | varchar |  |  | SI | SecondPhone |
| PAPMI_Sex_DR | bigint |  | FK | NO | Des Ref to CTSEX |
| PAPMI_Soundex | varchar |  |  | SI | Patient Soundex |
| PAPMI_SurName | varchar |  |  | SI | Computered Surname |
| PAPMI_Title_DR | bigint |  | FK | SI | Des Ref Title |
| PAPMI_TraceStatus_DR | bigint |  | FK | SI | Des Ref TraceOutcome |
| PAPMI_UserUpdate | bigint |  |  | SI | User Update |
| PAPMI_VIPFlag | varchar |  |  | SI | VIP Flag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*