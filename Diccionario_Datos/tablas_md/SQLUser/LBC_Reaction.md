# SQLUser.LBC_Reaction

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCR_RowID | bigint | PK |  | NO | - |
| LBCR_Code | varchar |  |  | NO | Code
Collation exception of upper to support + an... |
| LBCR_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCR_CreatedDate | date |  |  | SI | Created Date |
| LBCR_CreatedTime | time |  |  | SI | Created Time |
| LBCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCR_DateTo | date |  |  | SI | Last day the record is active |
| LBCR_Desc | varchar |  |  | NO | Description
Collation exception of upper to suppo... |
| LBCR_ImplicitValue | varchar |  |  | SI | Implicit value |
| LBCR_Owner | varchar |  |  | SI | Owner |
| LBCR_System | varchar |  |  | SI | System created |
| LBCR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes clinicos |
| Q02 | - |  |  | SI | Hemiparesia |
| Q03 | - |  |  | SI | Hemiplejia |
| Q04 | - |  |  | SI | Hipertonia |
| Q05 | - |  |  | SI | Hipotonia |
| Q06 | - |  |  | SI | Nivel Cognitivo |
| Q07 | - |  |  | SI | Giro lado afectado |
| Q08 | - |  |  | SI | Giro lado afectado Independiente |
| Q09 | - |  |  | SI | Giro lado afectado con Ayuda |
| Q10 | - |  |  | SI | Giro lado afectado dependiente |
| Q11 | - |  |  | SI | Giro lado afectado observaciones |
| Q12 | - |  |  | SI | Giro lado sano Independiente |
| Q13 | - |  |  | SI | Giro lado sano con ayuda |
| Q14 | - |  |  | SI | Giro lado sano dependiente |
| Q15 | - |  |  | SI | Giro lado sano observaciones |
| Q16 | - |  |  | SI | De supino a sentado borde cama Independiente |
| Q17 | - |  |  | SI | De supino a sentado borde cama con ayuda |
| Q18 | - |  |  | SI | De supino a sentado borde cama dependiente |
| Q19 | - |  |  | SI | De supino a sentado borde cama Observaciones |
| Q20 | - |  |  | SI | Equilibrio en sedente Independiente |
| Q21 | - |  |  | SI | Equilibrio en sedente con ayuda |
| Q22 | - |  |  | SI | Equilibrio en sedente dependiente |
| Q23 | - |  |  | SI | Equilibrio en sedente observaciones |
| Q24 | - |  |  | SI | Sedente a bípedo Independiente |
| Q25 | - |  |  | SI | Sedente a bípedo con ayuda |
| Q26 | - |  |  | SI | Sedente a bípedo dependiente |
| Q27 | - |  |  | SI | Sedente a bípedo observaciones |
| Q28 | - |  |  | SI | Equilibrio en bípedo independiente |
| Q29 | - |  |  | SI | Equilibrio en bípedo con ayuda |
| Q30 | - |  |  | SI | Equilibrio en bípedo dependiente |
| Q31 | - |  |  | SI | Marcha independiente |
| Q32 | - |  |  | SI | Marcha con ayuda |
| Q33 | - |  |  | SI | Marcha dependiente |
| Q34 | - |  |  | SI | Marcha observaciones |
| Q35 | - |  |  | SI | Equilibrio en bípedo observaciones |
| Q36 | - |  |  | SI | Movimiento de la mano independiente |
| Q37 | - |  |  | SI | Movimiento de la mano con ayuda |
| Q38 | - |  |  | SI | Movimiento de la mano dependiente |
| Q39 | - |  |  | SI | Movimiento de la mano observaciones |
| Q40 | - |  |  | SI | Tacto Conservado |
| Q41 | - |  |  | SI | Tacto Aumentado |
| Q42 | - |  |  | SI | Tacto Disminuído |
| Q43 | - |  |  | SI | Tacto Ausente |
| Q44 | - |  |  | SI | Tacto Alterado |
| Q45 | - |  |  | SI | Observación |
| Q46 | - |  |  | SI | Ubicación |
| Q47 | - |  |  | SI | Intensidad |
| Q48 | - |  |  | SI | Tipo de dolor, demostración |
| Q49 | - |  |  | SI | Desplazamiento en el hogar |
| Q50 | - |  |  | SI | Transferencia entre silla y cama |
| Q51 | - |  |  | SI | Subir y bajar escaleras |
| Q52 | - |  |  | SI | Usar el baño |
| Q53 | - |  |  | SI | Bañarse/ducharse |
| Q54 | - |  |  | SI | Alimentación |
| Q55 | - |  |  | SI | Vestirse/Desvestirse |
| Q56 | - |  |  | SI | Flexores de MMSS |
| Q57 | - |  |  | SI | FM 1IZQ |
| Q58 | - |  |  | SI | Extensores de MMSS |
| Q59 | - |  |  | SI | Flexores de MMII |
| Q60 | - |  |  | SI | ext mmss izq |
| Q61 | - |  |  | SI | flex mmii izq |
| Q62 | - |  |  | SI | Extensores de MMII |
| Q63 | - |  |  | SI | Tronco |
| Q64 | - |  |  | SI | ext mmii izq |
| Q65 | - |  |  | SI | Observaciones |
| Q66 | - |  |  | SI | i |
| Q67 | - |  |  | SI | a |
| Q68 | - |  |  | SI | d |
| Q69 | - |  |  | SI | Antecedentes Clínicos |
| Q70 | - |  |  | SI | Tono Muscular |
| Q71 | - |  |  | SI | Nivel Cognitivo |
| Q72 | - |  |  | SI | Evaluación Funcional |
| Q73 | - |  |  | SI | Evaluación Sensorial |
| Q74 | - |  |  | SI | Dolor (EVA) |
| Q75 | - |  |  | SI | Evolución de las AVD |
| Q76 | - |  |  | SI | Independiente (I) |
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