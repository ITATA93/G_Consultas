# SQLUser.LB_RequestTestSetSpecialHandling

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQTSSH_ParRef | bigint | PK |  | NO | - |
| LBRQTSSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBRQTSSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBRQTSSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBRQTSSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBRQTSSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBRQTSSH_RowID | varchar |  |  | NO | - |
| LBRQTSSH_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| Q01 | - |  |  | SI | Evaluación Mano |
| Q02 | - |  |  | SI | Prensión |
| Q03 | - |  |  | SI | Gruesa Mano Derecha |
| Q04 | - |  |  | SI | Gruesa Mano Izquierda |
| Q05 | - |  |  | SI | Fina Mano Derecha |
| Q06 | - |  |  | SI | Fina Mano Izquierda |
| Q07 | - |  |  | SI | Esférica Mano Derecha |
| Q08 | - |  |  | SI | Esférica Mano Izquierda |
| Q09 | - |  |  | SI | Tripode Mano Derecha |
| Q10 | - |  |  | SI | Tripode Mano Izquierda |
| Q11 | - |  |  | SI | Cilíndrica Mano Derecha |
| Q12 | - |  |  | SI | Cilíndrica Mano Izquierda |
| Q13 | - |  |  | SI | Lateral Mano Derecha |
| Q14 | - |  |  | SI | Lateral Mano Izquierda |
| Q15 | - |  |  | SI | Pinza Índice Mano Derecha |
| Q16 | - |  |  | SI | Pinza Índice Mano Izquierda |
| Q17 | - |  |  | SI | Extensión Mano Derecha |
| Q18 | - |  |  | SI | Extensión Mano Izquierda |
| Q19 | - |  |  | SI | Ejecución Motora |
| Q20 | - |  |  | SI | Postura |
| Q21 | - |  |  | SI | Movilidad Gruesa |
| Q22 | - |  |  | SI | Coordinación Bimanual |
| Q23 | - |  |  | SI | Coordinación Ojo-Mano |
| Q24 | - |  |  | SI | Evaluación Sensibilidad |
| Q25 | - |  |  | SI | Sensibilidad Superficial Derecha |
| Q26 | - |  |  | SI | Sensibilidad Superficial Izquierda |
| Q27 | - |  |  | SI | Sensibilidad Propioceptiva Derecha |
| Q28 | - |  |  | SI | Sensibilidad Propioceptiva Izquierda |
| Q29 | - |  |  | SI | Sensibilidad Térmica Derecha |
| Q30 | - |  |  | SI | Sensibilidad Térmica Izquierda |
| Q31 | - |  |  | SI | Algesia Derecha |
| Q32 | - |  |  | SI | Algesia Izquierda |
| Q33 | - |  |  | SI | Patrones de Desempeño |
| Q34 | - |  |  | SI | Rutinas |
| Q35 | - |  |  | SI | Roles |
| Q36 | - |  |  | SI | Intereses |
| Q37 | - |  |  | SI | Evaluación AVD |
| Q38 | - |  |  | SI | AVD Básicas |
| Q39 | - |  |  | SI | Actividad |
| Q40 | - |  |  | SI | Comer |
| Q41 | - |  |  | SI | Higiene |
| Q42 | - |  |  | SI | Vestirse |
| Q43 | - |  |  | SI | Lavarse |
| Q44 | - |  |  | SI | Uso de WC |
| Q45 | - |  |  | SI | Traslado |
| Q46 | - |  |  | SI | Deambulación |
| Q47 | - |  |  | SI | Escalones |
| Q48 | - |  |  | SI | AVD Instrumentales |
| Q49 | - |  |  | SI | Labores del Hogar |
| Q50 | - |  |  | SI | Manejo de Dinero |
| Q51 | - |  |  | SI | Medicación |
| Q52 | - |  |  | SI | Transporte |
| Q53 | - |  |  | SI | Evaluación Cognitiva y Estado de Ánimo |
| Q54 | - |  |  | SI | Apreciación Diagnóstica de Terapia Ocupacional |
| Q55 | - |  |  | SI | Gruesa Mano Derecha Obs |
| Q56 | - |  |  | SI | Gruesa Mano Izquierda Obs |
| Q57 | - |  |  | SI | Fina Mano Derecha Obs |
| Q58 | - |  |  | SI | Fina Mano Izquierda Obs |
| Q59 | - |  |  | SI | Esférica Mano Derecha Obs |
| Q60 | - |  |  | SI | Esférica Mano Izquierda Obs |
| Q61 | - |  |  | SI | Tripode Mano Derecha Obs |
| Q62 | - |  |  | SI | Tripode Mano Izquierda Obs |
| Q63 | - |  |  | SI | Cilíndrica Mano Derecha Obs |
| Q64 | - |  |  | SI | Cilíndrica Mano Izquierda Obs |
| Q65 | - |  |  | SI | Pinza Índice Mano Derecha Obs |
| Q66 | - |  |  | SI | Pinza Índice Mano Izquierda Obs |
| Q67 | - |  |  | SI | Extensión Mano Derecha Obs |
| Q68 | - |  |  | SI | Extensión Mano Izquierda Obs |
| Q69 | - |  |  | SI | Postura Obs |
| Q70 | - |  |  | SI | Movilidad Gruesa Obs |
| Q71 | - |  |  | SI | Coordinación Bimanual Obs |
| Q72 | - |  |  | SI | Coordinación Ojo-Mano Obs |
| Q73 | - |  |  | SI | Sensibilidad Superficial Derecha Obs |
| Q74 | - |  |  | SI | Sensibilidad Superficial Izquierda Obs |
| Q75 | - |  |  | SI | Sensibilidad Propioceptiva Derecha  Obs |
| Q76 | - |  |  | SI | Sensibilidad Propioceptiva Izquierda Obs |
| Q77 | - |  |  | SI | Sensibilidad Térmica Derecha Obs |
| Q78 | - |  |  | SI | Sensibilidad Térmica Izquierda Obs |
| Q79 | - |  |  | SI | Algesia Derecha Obs |
| Q80 | - |  |  | SI | Algesia Izquierda Obs |
| Q89 | - |  |  | SI | Lateral Mano Derecha Obs |
| Q90 | - |  |  | SI | Lateral Mano Izquierda Obs |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*