# SQLUser.ARC_SurchInsSubType

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| INS_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INS_CreatedDate | date |  |  | SI | Created Date |
| INS_CreatedTime | time |  |  | SI | Created Time |
| INS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INS_DateFrom | date |  |  | SI | Date From |
| INS_DateTo | date |  |  | SI | Date To |
| INS_FixedAmt | double |  |  | SI | Fixed Amt |
| INS_InsSub_DR | bigint |  | FK | SI | Des Ref InsSub |
| INS_Name | varchar |  |  | SI | Description |
| INS_Perc | double |  |  | SI | % Charge |
| INS_RowId | varchar |  |  | NO | - |
| INS_UpdatedDate | date |  |  | SI | Updated Date |
| INS_UpdatedTime | time |  |  | SI | Updated Time |
| INS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INS_VisitType | varchar |  |  | SI | Visit Type |
| Q01 | - |  |  | SI | Solicitud de Postergación |
| Q02 | - |  |  | SI | Identificación del Solicitante de Postergación |
| Q03 | - |  |  | SI | Nombre |
| Q04 | - |  |  | SI | Con Fecha |
| Q05 | - |  |  | SI | RUN |
| Q06 | - |  |  | SI | Parentesco Vinculo |
| Q07 | - |  |  | SI | Por Motivo de |
| Q08 | - |  |  | SI | Condiciones |
| Q09 | - |  |  | SI | Captación de la Postergación |
| Q10 | - |  |  | SI | Solicito postergar mi atención |
| Q11 | - |  |  | SI | ID Local |
| Q12 | - |  |  | SI | ID SIGTE |
| Q13 | - |  |  | SI | Fecha Acordada de Postergación |
| Q14 | - |  |  | SI | Fecha de Próximo Contacto |
| Q15 | - |  |  | SI | Datos de Contacto |
| Q16 | - |  |  | SI | Teléfono |
| Q17 | - |  |  | SI | Dirección |
| Q18 | - |  |  | SI | Establecimiento |
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