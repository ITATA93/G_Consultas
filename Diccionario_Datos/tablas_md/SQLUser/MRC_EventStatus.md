# SQLUser.MRC_EventStatus

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVST_RowId | bigint | PK |  | NO | - |
| EVST_Code | varchar |  |  | NO | Code |
| EVST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EVST_CreatedDate | date |  |  | SI | Created Date |
| EVST_CreatedTime | time |  |  | SI | Created Time |
| EVST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVST_DateFrom | date |  |  | SI | DateFrom |
| EVST_DateTo | date |  |  | SI | DateTo |
| EVST_Desc | varchar |  |  | NO | Description |
| EVST_Owner | varchar |  |  | SI | Owner |
| EVST_UpdatedDate | date |  |  | SI | Updated Date |
| EVST_UpdatedTime | time |  |  | SI | Updated Time |
| EVST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de comienzo de la lesión |
| Q02 | - |  |  | SI | Descripción del Mecanismo |
| Q03 | - |  |  | SI | Cirugía |
| Q04 | - |  |  | SI | Inmovilización |
| Q05 | - |  |  | SI | Ubicación e Intensidad |
| Q06 | - |  |  | SI | Palpación |
| Q07 | - |  |  | SI | Factores que lo inducen |
| Q08 | - |  |  | SI | Factores que lo inducen |
| Q09 | - |  |  | SI | Factores que lo aminora |
| Q10 | - |  |  | SI | Flexión 130-140 al Inicio |
| Q11 | - |  |  | SI | Extensión 10 al Inicio |
| Q12 | - |  |  | SI | Abd 30-50 al Inicio |
| Q13 | - |  |  | SI | Abb 20-30 al Inicio |
| Q14 | - |  |  | SI | Rot.Int 40-50 al Inicio |
| Q15 | - |  |  | SI | Rot. Ext. 30-40 al Inicio |
| Q16 | - |  |  | SI | Flexión 130-140 al Alta |
| Q17 | - |  |  | SI | Extensión 10 al Alta |
| Q18 | - |  |  | SI | Abd 30-50 al Alta |
| Q19 | - |  |  | SI | Abb 20-30 al Alta |
| Q20 | - |  |  | SI | Extensión 5-10 al Alta |
| Q21 | - |  |  | SI | ext |
| Q22 | - |  |  | SI | ab |
| Q23 | - |  |  | SI | ad |
| Q24 | - |  |  | SI | Rot.Int 40-50 al Alta |
| Q25 | - |  |  | SI | Rot. Ext. 30-40 al Alta |
| Q26 | - |  |  | SI | Flexión 130-140 al Inicio |
| Q27 | - |  |  | SI | Extensión 5-10 al Inicio |
| Q28 | - |  |  | SI | rod fle |
| Q29 | - |  |  | SI | rod ext |
| Q30 | - |  |  | SI | Flexión platar 40-50 al Inicio |
| Q31 | - |  |  | SI | Flexión Dorsal 20-30 al Inicio |
| Q32 | - |  |  | SI | Inversión 35 al Inicio |
| Q33 | - |  |  | SI | Flexión IFP I ortejo 45 al Inicio |
| Q34 | - |  |  | SI | Flexión IFD I ortejo 80 al Inicio |
| Q35 | - |  |  | SI | Extensión IFP I ortejo 70 al Inicio |
| Q36 | - |  |  | SI | Flexión IFP dedos 40 al Inicio |
| Q37 | - |  |  | SI | Extensión IFP I dedos 60-80 al Inicio |
| Q38 | - |  |  | SI | Flexión IFD dedos 60 al Inicio |
| Q39 | - |  |  | SI | Extensión IFD dedos 30 al Inicio |
| Q40 | - |  |  | SI | Eversión 15 al Inicio |
| Q41 | - |  |  | SI | Flexión platar 40-50 al Alta |
| Q42 | - |  |  | SI | Flexión Dorsal 20-30 al Alta |
| Q43 | - |  |  | SI | Inversión 35 al Alta |
| Q44 | - |  |  | SI | Eversión 15 al Alta |
| Q45 | - |  |  | SI | Flexión IFP I ortejo 45 al Alta |
| Q46 | - |  |  | SI | Extensión IFP I ortejo 70 al Alta |
| Q47 | - |  |  | SI | Flexión IFD I ortejo 80 al Alta |
| Q48 | - |  |  | SI | Flexión IFP dedos 40 al Alta |
| Q49 | - |  |  | SI | Extensión IFP I dedos 60-80 al Alta |
| Q50 | - |  |  | SI | Flexión IFD dedos 60 al Alta |
| Q51 | - |  |  | SI | Extensión IFD dedos 30 al Alta |
| Q52 | - |  |  | SI | Pruebas Funcionales |
| Q53 | - |  |  | SI | Marcha |
| Q54 | - |  |  | SI | Ortesis y/o Prótesis |
| Q55 | - |  |  | SI | Edema |
| Q56 | - |  |  | SI | Color |
| Q57 | - |  |  | SI | Dolor |
| Q58 | - |  |  | SI | Estadio |
| Q59 | - |  |  | SI | Hipertrófia |
| Q60 | - |  |  | SI | Adherida |
| Q61 | - |  |  | SI | Flexible/Rígida |
| Q62 | - |  |  | SI | Edema |
| Q63 | - |  |  | SI | Extensión 5-10 |
| Q64 | - |  |  | SI | flexx |
| Q65 | - |  |  | SI | Extensión 5-10 al Alta |
| Q66 | - |  |  | SI | Mecanismo de Lesión |
| Q67 | - |  |  | SI | Dolor (EVA) |
| Q68 | - |  |  | SI | Rangos Articulares |
| Q69 | - |  |  | SI | Cadera |
| Q70 | - |  |  | SI | Flexión 130-140 al Alta |
| Q71 | - |  |  | SI | Extensión 5-10 al Alta |
| Q72 | - |  |  | SI | Tobillo |
| Q73 | - |  |  | SI | Rodilla |
| Q74 | - |  |  | SI | Cicatriz |
| Q75 | - |  |  | SI | A/P |
| Q76 | - |  |  | SI | A/P |
| Q77 | - |  |  | SI | A/P |
| Q78 | - |  |  | SI | A/P |
| Q79 | - |  |  | SI | A/P |
| Q80 | - |  |  | SI | A/P |
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