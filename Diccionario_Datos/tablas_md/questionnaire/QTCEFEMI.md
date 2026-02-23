# questionnaire.QTCEFEMI

> Ficha de Evaluación: Miembro Inferior

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha de Evaluación: Miembro Inferior

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de comienzo de la lesión  |
| Q02 | varchar |  |  | SI | Descripción del Mecanismo |
| Q03 | varchar |  |  | SI | Cirugía |
| Q04 | varchar |  |  | SI | Inmovilización |
| Q05 | varchar |  |  | SI | Ubicación e Intensidad |
| Q06 | varchar |  |  | SI | Palpación |
| Q07 | varchar |  |  | SI | Factores que lo inducen |
| Q08 | varchar |  |  | SI | Factores que lo inducen |
| Q09 | varchar |  |  | SI | Factores que lo aminora |
| Q10 | varchar |  |  | SI | Flexión 130-140 al Inicio |
| Q11 | varchar |  |  | SI | Extensión 10 al Inicio |
| Q12 | varchar |  |  | SI | Abd 30-50 al Inicio |
| Q13 | varchar |  |  | SI | Abb 20-30 al Inicio |
| Q14 | varchar |  |  | SI | Rot.Int 40-50 al Inicio |
| Q15 | varchar |  |  | SI | Rot. Ext. 30-40 al Inicio |
| Q16 | varchar |  |  | SI | Flexión 130-140 al Alta |
| Q17 | varchar |  |  | SI | Extensión 10 al Alta |
| Q18 | varchar |  |  | SI | Abd 30-50 al Alta |
| Q19 | varchar |  |  | SI | Abb 20-30 al Alta |
| Q20 | varchar |  |  | SI | Extensión 5-10 al Alta |
| Q21 | varchar |  |  | SI | ext |
| Q22 | varchar |  |  | SI | ab |
| Q23 | varchar |  |  | SI | ad |
| Q24 | varchar |  |  | SI | Rot.Int 40-50 al Alta |
| Q25 | varchar |  |  | SI | Rot. Ext. 30-40 al Alta |
| Q26 | varchar |  |  | SI | Flexión 130-140 al Inicio |
| Q27 | varchar |  |  | SI | Extensión 5-10 al Inicio |
| Q28 | varchar |  |  | SI | rod fle |
| Q29 | varchar |  |  | SI | rod ext  |
| Q30 | varchar |  |  | SI | Flexión platar 40-50 al Inicio |
| Q31 | varchar |  |  | SI | Flexión Dorsal 20-30 al Inicio |
| Q32 | varchar |  |  | SI | Inversión 35 al Inicio |
| Q33 | varchar |  |  | SI | Flexión IFP I ortejo 45 al Inicio |
| Q34 | varchar |  |  | SI | Flexión IFD I ortejo 80 al Inicio |
| Q35 | varchar |  |  | SI | Extensión IFP I ortejo 70 al Inicio |
| Q36 | varchar |  |  | SI | Flexión IFP dedos 40 al Inicio |
| Q37 | varchar |  |  | SI | Extensión IFP I dedos 60-80 al Inicio |
| Q38 | varchar |  |  | SI | Flexión IFD dedos 60 al Inicio |
| Q39 | varchar |  |  | SI | Extensión IFD dedos 30 al Inicio |
| Q40 | varchar |  |  | SI | Eversión 15 al Inicio |
| Q41 | varchar |  |  | SI | Flexión platar 40-50 al Alta |
| Q42 | varchar |  |  | SI | Flexión Dorsal 20-30 al Alta |
| Q43 | varchar |  |  | SI | Inversión 35 al Alta |
| Q44 | varchar |  |  | SI | Eversión 15 al Alta |
| Q45 | varchar |  |  | SI | Flexión IFP I ortejo 45 al Alta |
| Q46 | varchar |  |  | SI | Extensión IFP I ortejo 70 al Alta |
| Q47 | varchar |  |  | SI | Flexión IFD I ortejo 80 al Alta |
| Q48 | varchar |  |  | SI | Flexión IFP dedos 40 al Alta |
| Q49 | varchar |  |  | SI | Extensión IFP I dedos 60-80 al Alta |
| Q50 | varchar |  |  | SI | Flexión IFD dedos 60 al Alta |
| Q51 | varchar |  |  | SI | Extensión IFD dedos 30 al Alta |
| Q52 | varchar |  |  | SI | Pruebas Funcionales |
| Q53 | varchar |  |  | SI | Marcha |
| Q54 | varchar |  |  | SI | Ortesis y/o Prótesis |
| Q55 | varchar |  |  | SI | Edema  |
| Q56 | varchar |  |  | SI | Color |
| Q57 | varchar |  |  | SI | Dolor |
| Q58 | varchar |  |  | SI | Estadio |
| Q59 | varchar |  |  | SI | Hipertrófia |
| Q60 | varchar |  |  | SI | Adherida |
| Q61 | varchar |  |  | SI | Flexible/Rígida |
| Q62 | varchar |  |  | SI | Edema |
| Q63 | varchar |  |  | SI | Extensión 5-10 |
| Q64 | varchar |  |  | SI | flexx |
| Q65 | varchar |  |  | SI | Extensión 5-10 al Alta |
| Q66 | varchar |  |  | SI | Mecanismo de Lesión |
| Q67 | varchar |  |  | SI | Dolor (EVA) |
| Q68 | varchar |  |  | SI | Rangos Articulares |
| Q69 | varchar |  |  | SI | Cadera |
| Q70 | varchar |  |  | SI | Flexión 130-140 al Alta |
| Q71 | varchar |  |  | SI | Extensión 5-10 al Alta |
| Q72 | varchar |  |  | SI | Tobillo |
| Q73 | varchar |  |  | SI | Rodilla |
| Q74 | varchar |  |  | SI | Cicatriz |
| Q75 | varchar |  |  | SI | A/P |
| Q76 | varchar |  |  | SI | A/P |
| Q77 | varchar |  |  | SI | A/P |
| Q78 | varchar |  |  | SI | A/P |
| Q79 | varchar |  |  | SI | A/P |
| Q80 | varchar |  |  | SI | A/P |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*