# questionnaire.QTCEFEMISU

> Ficha de Evaluación: Miembro Superior

**Schema:** questionnaire
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha de Evaluación: Miembro Superior

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Comienzo de la lesión |
| Q02 | varchar |  |  | SI | Descripción del mecanismo |
| Q03 | varchar |  |  | SI | Cirugía |
| Q04 | varchar |  |  | SI | Inmovilización |
| Q05 | varchar |  |  | SI | Ubicación e Intensidad |
| Q06 | varchar |  |  | SI | Palpación |
| Q07 | varchar |  |  | SI | Factores que lo Inducen |
| Q08 | varchar |  |  | SI | Factores que lo Aminoran |
| Q09 | varchar |  |  | SI | Flexión 180 al Inicio |
| Q10 | varchar |  |  | SI | Flexión 180 al Alta |
| Q11 | varchar |  |  | SI | Extensión 45 al Inicio |
| Q12 | varchar |  |  | SI | Extensión 45 al Alta |
| Q13 | varchar |  |  | SI | Abd. 160-180 al Inicio |
| Q14 | varchar |  |  | SI | Abd. 160-180 al Alta |
| Q15 | varchar |  |  | SI | Add. 20 al Inicio |
| Q16 | varchar |  |  | SI | Rot. Int. 95 al Inicio |
| Q17 | varchar |  |  | SI | Add. 20 al Alta |
| Q18 | varchar |  |  | SI | Rot. Int. 95 al Alta |
| Q19 | varchar |  |  | SI | Rot. Ext. 70 al Inicio |
| Q20 | varchar |  |  | SI | Rot. Ext. 70 al Alta |
| Q21 | varchar |  |  | SI | Flexión 150 al Inicio |
| Q22 | varchar |  |  | SI | Flexión 150 al Alta |
| Q23 | varchar |  |  | SI | Extensión 0-10 al Inicio |
| Q24 | varchar |  |  | SI | Prono-Supinación 85-90 al Inicio |
| Q25 | varchar |  |  | SI | Prono-Supinación 85-90 al Alta |
| Q26 | varchar |  |  | SI | Extensión 0-10 al Alta |
| Q27 | varchar |  |  | SI | Flexión 60-80 al Inicio |
| Q28 | varchar |  |  | SI | Abducción pulgar 70 al Alta |
| Q29 | varchar |  |  | SI | Extensión 60-90 al Inicio |
| Q30 | varchar |  |  | SI | Extensión 60-90 al Alta |
| Q31 | varchar |  |  | SI | Desviación radial 25-30 al Inicio |
| Q32 | varchar |  |  | SI | Desviación radial 25-30 al Alta |
| Q33 | varchar |  |  | SI | Desviación cubital 30-40 al Inicio |
| Q34 | varchar |  |  | SI | Desviación cubital 30-40 al Alta |
| Q35 | varchar |  |  | SI | Abducción pulgar 70 al Inicio |
| Q36 | varchar |  |  | SI | Abducción pulgar 70 al Alta |
| Q37 | varchar |  |  | SI | Flexión MF pulgar 50 al Inicio |
| Q38 | varchar |  |  | SI | Flexión MF pulgar 50 al Alta |
| Q39 | varchar |  |  | SI | Flexión interfalangica pulgar 80 al Inicio |
| Q40 | varchar |  |  | SI | Flexión IFD 100 al Inicio |
| Q41 | varchar |  |  | SI | Flexión IFP 90 al Inicio |
| Q42 | varchar |  |  | SI | Flexión MF 90 al Inicio |
| Q43 | varchar |  |  | SI | Hiperextensión MF 90 al Inicio |
| Q44 | varchar |  |  | SI | Flexión IFP 90 al Alta |
| Q45 | varchar |  |  | SI | Flexión MF 90 al Alta |
| Q46 | varchar |  |  | SI | Flexión IFD 100 al Alta |
| Q47 | varchar |  |  | SI | Flexión interfalangica pulgar 80 al Alta |
| Q48 | varchar |  |  | SI | Hiperextensión MF 90 al Alta |
| Q49 | varchar |  |  | SI | Pruebas Funcionales |
| Q50 | varchar |  |  | SI | Cicatriz |
| Q51 | varchar |  |  | SI | Ortesis y/o Prótesis |
| Q52 | varchar |  |  | SI | Edema |
| Q53 | varchar |  |  | SI | Color  |
| Q54 | varchar |  |  | SI | Dolor |
| Q55 | varchar |  |  | SI | Estadio |
| Q56 | varchar |  |  | SI | Hipertrófica |
| Q57 | varchar |  |  | SI | Adherida |
| Q58 | varchar |  |  | SI | Flexible/Rígida |
| Q59 | varchar |  |  | SI | Flexión 60-80 al Alta |
| Q60 | varchar |  |  | SI | Mecanismo de Lesión |
| Q61 | varchar |  |  | SI | Dolor (EVA) |
| Q62 | varchar |  |  | SI | Rangos Articulares |
| Q63 | varchar |  |  | SI | Hombro |
| Q64 | varchar |  |  | SI | Muñeca-Mano |
| Q65 | varchar |  |  | SI | Codo |
| Q66 | varchar |  |  | SI | Cicatriz |
| Q67 | varchar |  |  | SI | A/P |
| Q68 | varchar |  |  | SI | A/P |
| Q69 | varchar |  |  | SI | A/P |
| Q70 | varchar |  |  | SI | A//P |
| Q71 | varchar |  |  | SI | A/P |
| Q72 | varchar |  |  | SI | A/P |
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