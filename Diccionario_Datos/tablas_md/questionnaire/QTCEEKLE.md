# questionnaire.QTCEEKLE

> Evaluación Kinésica de Lesiones Encefálicas

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Kinésica de Lesiones Encefálicas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antecedentes clinicos |
| Q02 | bit |  |  | SI | Hemiparesia |
| Q03 | bit |  |  | SI | Hemiplejia |
| Q04 | bit |  |  | SI | Hipertonia |
| Q05 | bit |  |  | SI | Hipotonia |
| Q06 | varchar |  |  | SI | Nivel Cognitivo |
| Q07 | bit |  |  | SI | Giro lado afectado |
| Q08 | bit |  |  | SI | Giro lado afectado Independiente |
| Q09 | bit |  |  | SI | Giro lado afectado con Ayuda |
| Q10 | bit |  |  | SI | Giro lado afectado dependiente |
| Q11 | varchar |  |  | SI | Giro lado afectado observaciones |
| Q12 | bit |  |  | SI | Giro lado sano Independiente |
| Q13 | bit |  |  | SI | Giro lado sano con ayuda |
| Q14 | bit |  |  | SI | Giro lado sano dependiente |
| Q15 | varchar |  |  | SI | Giro lado sano observaciones |
| Q16 | bit |  |  | SI | De supino a sentado borde cama Independiente |
| Q17 | bit |  |  | SI | De supino a sentado borde cama con ayuda |
| Q18 | bit |  |  | SI | De supino a sentado borde cama dependiente |
| Q19 | varchar |  |  | SI | De supino a sentado borde cama Observaciones |
| Q20 | bit |  |  | SI | Equilibrio en sedente Independiente |
| Q21 | bit |  |  | SI | Equilibrio en sedente con ayuda |
| Q22 | bit |  |  | SI | Equilibrio en sedente dependiente |
| Q23 | varchar |  |  | SI | Equilibrio en sedente observaciones |
| Q24 | bit |  |  | SI | Sedente a bípedo Independiente |
| Q25 | bit |  |  | SI | Sedente a bípedo con ayuda |
| Q26 | bit |  |  | SI | Sedente a bípedo dependiente |
| Q27 | varchar |  |  | SI | Sedente a bípedo observaciones |
| Q28 | bit |  |  | SI | Equilibrio en bípedo independiente |
| Q29 | bit |  |  | SI | Equilibrio en bípedo con ayuda |
| Q30 | bit |  |  | SI | Equilibrio en bípedo dependiente |
| Q31 | bit |  |  | SI | Marcha independiente |
| Q32 | bit |  |  | SI | Marcha con ayuda |
| Q33 | bit |  |  | SI | Marcha dependiente |
| Q34 | varchar |  |  | SI | Marcha observaciones |
| Q35 | varchar |  |  | SI | Equilibrio en bípedo observaciones |
| Q36 | bit |  |  | SI | Movimiento de la mano independiente |
| Q37 | bit |  |  | SI | Movimiento de la mano con ayuda |
| Q38 | bit |  |  | SI | Movimiento de la mano dependiente |
| Q39 | varchar |  |  | SI | Movimiento de la mano observaciones |
| Q40 | bit |  |  | SI | Tacto Conservado |
| Q41 | bit |  |  | SI | Tacto Aumentado |
| Q42 | bit |  |  | SI | Tacto Disminuído |
| Q43 | bit |  |  | SI | Tacto Ausente |
| Q44 | bit |  |  | SI | Tacto Alterado |
| Q45 | varchar |  |  | SI | Observación |
| Q46 | varchar |  |  | SI | Ubicación |
| Q47 | varchar |  |  | SI | Intensidad |
| Q48 | varchar |  |  | SI | Tipo de dolor, demostración |
| Q49 | varchar |  |  | SI | Desplazamiento en el hogar |
| Q50 | varchar |  |  | SI | Transferencia entre silla y cama |
| Q51 | varchar |  |  | SI | Subir y bajar escaleras |
| Q52 | varchar |  |  | SI | Usar el baño |
| Q53 | varchar |  |  | SI | Bañarse/ducharse  |
| Q54 | varchar |  |  | SI | Alimentación |
| Q55 | varchar |  |  | SI | Vestirse/Desvestirse |
| Q56 | varchar |  |  | SI | Flexores de MMSS |
| Q57 | varchar |  |  | SI | FM 1IZQ |
| Q58 | varchar |  |  | SI | Extensores de MMSS |
| Q59 | varchar |  |  | SI | Flexores de MMII |
| Q60 | varchar |  |  | SI | ext mmss izq |
| Q61 | varchar |  |  | SI | flex mmii izq |
| Q62 | varchar |  |  | SI | Extensores de MMII |
| Q63 | varchar |  |  | SI | Tronco |
| Q64 | varchar |  |  | SI | ext mmii izq |
| Q65 | varchar |  |  | SI | Observaciones |
| Q66 | bit |  |  | SI | i |
| Q67 | bit |  |  | SI | a |
| Q68 | bit |  |  | SI | d |
| Q69 | varchar |  |  | SI | Antecedentes Clínicos |
| Q70 | varchar |  |  | SI | Tono Muscular |
| Q71 | varchar |  |  | SI | Nivel Cognitivo |
| Q72 | varchar |  |  | SI | Evaluación Funcional |
| Q73 | varchar |  |  | SI | Evaluación Sensorial |
| Q74 | varchar |  |  | SI | Dolor (EVA) |
| Q75 | varchar |  |  | SI | Evolución de las AVD |
| Q76 | varchar |  |  | SI | Independiente (I); con ayuda (A); Dependiente (D) |
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