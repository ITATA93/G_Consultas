# SQLUser.CT_Province

**Schema:** SQLUser
**Columnas:** 164
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROV_RowId | bigint | PK |  | NO | - |
| PROV_Code | varchar |  |  | NO | Code |
| PROV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROV_CreatedDate | date |  |  | SI | Created Date |
| PROV_CreatedTime | time |  |  | SI | Created Time |
| PROV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROV_DateFrom | date |  |  | SI | Date From |
| PROV_DateTo | date |  |  | SI | Date To |
| PROV_Desc | varchar |  |  | NO | Description |
| PROV_NationalCode | varchar |  |  | SI | NationalCode |
| PROV_Owner | varchar |  |  | SI | Owner |
| PROV_Region_DR | bigint |  | FK | SI | Des Ref Region |
| PROV_TimeZone | varchar |  |  | SI | Time Zone 
Used as a default for all locations wi... |
| PROV_UpdatedDate | date |  |  | SI | Updated Date |
| PROV_UpdatedTime | time |  |  | SI | Updated Time |
| PROV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Are you |
| Q10 | - |  |  | SI | Are you pregnant ? |
| Q100 | - |  |  | SI | Extra label |
| Q101 | - |  |  | SI | Date |
| Q102 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | When is the last date of menstrual period: date |
| Q12 | - |  |  | SI | Are you currently lactating? |
| Q13 | - |  |  | SI | Medical history questionnnaire |
| Q14 | - |  |  | SI | Are you taking any medications: |
| Q15 | - |  |  | SI | Currently taking antibiotics? |
| Q16 | - |  |  | SI | Other medications? |
| Q17 | - |  |  | SI | Notes |
| Q18 | - |  |  | SI | Do you have a history of fainting or dizziness dur... |
| Q19 | - |  |  | SI | Do you have hematological disease (e.g. anemias, b... |
| Q2 | - |  |  | SI | Feeling healthy and well today? |
| Q20 | - |  |  | SI | Do you have history of other malignancy? |
| Q21 | - |  |  | SI | Do you have history of immunological disease? |
| Q22 | - |  |  | SI | Do you have history of cardio-vascular disease (ca... |
| Q23 | - |  |  | SI | Do you have history of respiratory disease? |
| Q24 | - |  |  | SI | Do you have history of neurological disease (epile... |
| Q25 | - |  |  | SI | Do you have a skin disease (especially on the site... |
| Q26 | - |  |  | SI | Do you have renal and urinary tract diseases? |
| Q27 | - |  |  | SI | In the past 48 hours? |
| Q28 | - |  |  | SI | Have you taken aspirin or anything that has aspiri... |
| Q29 | - |  |  | SI | In the past 16 weeks, have you |
| Q3 | - |  |  | SI | Are you familiar with autologous donation, benefit... |
| Q30 | - |  |  | SI | Donated blood, platelets or plasma? |
| Q31 | - |  |  | SI | Medical and surgical intervention (for last 12 mon... |
| Q32 | - |  |  | SI | Have you been under a doctors care, undergone surg... |
| Q33 | - |  |  | SI | Signatures |
| Q34 | - |  |  | SI | Donor name |
| Q35 | - |  |  | SI | Donor signature |
| Q35UDt | - |  |  | SI | Donor signature Last Updated Date |
| Q35UTm | - |  |  | SI | Donor signature Last Updated Time |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Time |
| Q38 | - |  |  | SI | Time |
| Q39 | - |  |  | SI | Nurse name |
| Q4 | - |  |  | SI | In the last 4 hours, have you had a meal or snack? |
| Q40 | - |  |  | SI | Nurse signature |
| Q40UDt | - |  |  | SI | Nurse signature Last Updated Date |
| Q40UTm | - |  |  | SI | Nurse signature Last Updated Time |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q43 | - |  |  | SI | Attending physician assessment |
| Q44 | - |  |  | SI | Date of next assessment |
| Q45 | - |  |  | SI | Reason for deferral |
| Q46 | - |  |  | SI | Additional notes |
| Q47 | - |  |  | SI | Attending physician name |
| Q48 | - |  |  | SI | Signature |
| Q48UDt | - |  |  | SI | Signature Last Updated Date |
| Q48UTm | - |  |  | SI | Signature Last Updated Time |
| Q49 | - |  |  | SI | Date |
| Q5 | - |  |  | SI | Have you got a chesty cough, sore throat or active... |
| Q50 | - |  |  | SI | Time |
| Q51 | - |  |  | SI | Extra label |
| Q52 | - |  |  | SI | Extra label |
| Q53 | - |  |  | SI | Extra label |
| Q54 | - |  |  | SI | Extra label |
| Q55 | - |  |  | SI | Extra label |
| Q56 | - |  |  | SI | Extra label |
| Q57 | - |  |  | SI | Extra label |
| Q58 | - |  |  | SI | Extra label |
| Q59 | - |  |  | SI | Extra label |
| Q6 | - |  |  | SI | In the last 7 days, have you seen a doctor, dentis... |
| Q60 | - |  |  | SI | Extra label |
| Q61 | - |  |  | SI | Extra label |
| Q62 | - |  |  | SI | Extra label |
| Q63 | - |  |  | SI | Extra label |
| Q64 | - |  |  | SI | Extra label |
| Q65 | - |  |  | SI | Extra label |
| Q66 | - |  |  | SI | Extra label |
| Q67 | - |  |  | SI | Extra label |
| Q68 | - |  |  | SI | Extra label |
| Q69 | - |  |  | SI | Extra label |
| Q7 | - |  |  | SI | (except for routine screening) |
| Q70 | - |  |  | SI | Extra label |
| Q71 | - |  |  | SI | Extra label |
| Q72 | - |  |  | SI | Extra label |
| Q73 | - |  |  | SI | Extra label |
| Q74 | - |  |  | SI | Extra label |
| Q75 | - |  |  | SI | Extra label |
| Q76 | - |  |  | SI | Extra label |
| Q77 | - |  |  | SI | Extra label |
| Q78 | - |  |  | SI | Extra label |
| Q79 | - |  |  | SI | Extra label |
| Q8 | - |  |  | SI | For female donor only |
| Q80 | - |  |  | SI | Extra label |
| Q81 | - |  |  | SI | Extra label |
| Q82 | - |  |  | SI | Extra label |
| Q83 | - |  |  | SI | Extra label |
| Q84 | - |  |  | SI | Extra label |
| Q85 | - |  |  | SI | Extra label |
| Q86 | - |  |  | SI | Extra label |
| Q87 | - |  |  | SI | Extra label |
| Q88 | - |  |  | SI | Extra label |
| Q89 | - |  |  | SI | Extra label |
| Q9 | - |  |  | SI | Have you been pregnant ? |
| Q90 | - |  |  | SI | Extra label |
| Q91 | - |  |  | SI | Extra label |
| Q92 | - |  |  | SI | Extra label |
| Q93 | - |  |  | SI | Extra label |
| Q94 | - |  |  | SI | Extra label |
| Q95 | - |  |  | SI | Extra label |
| Q96 | - |  |  | SI | Extra label |
| Q97 | - |  |  | SI | Extra label |
| Q98 | - |  |  | SI | Extra label |
| Q99 | - |  |  | SI | Extra label |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*