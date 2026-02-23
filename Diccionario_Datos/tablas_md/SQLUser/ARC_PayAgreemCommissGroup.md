# SQLUser.ARC_PayAgreemCommissGroup

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMGRP_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| COMGRP_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| COMGRP_Childsub | double |  |  | NO | Childsub |
| COMGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMGRP_CreatedDate | date |  |  | SI | Created Date |
| COMGRP_CreatedTime | time |  |  | SI | Created Time |
| COMGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMGRP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| COMGRP_Priority | double |  |  | SI | Priority |
| COMGRP_RowId | varchar |  |  | NO | - |
| COMGRP_UpdatedDate | date |  |  | SI | Updated Date |
| COMGRP_UpdatedTime | time |  |  | SI | Updated Time |
| COMGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Hombro Izquierdo |
| Q02 | - |  |  | SI | Hombro Derecho |
| Q03 | - |  |  | SI | Codo Izquierdo |
| Q04 | - |  |  | SI | Codo Derecho |
| Q05 | - |  |  | SI | Muñeca Izquierda |
| Q06 | - |  |  | SI | Muñeca Derecha |
| Q07 | - |  |  | SI | Dedos Mano Izquierda |
| Q08 | - |  |  | SI | Dedos Mano Derecha |
| Q09 | - |  |  | SI | Cadera Izquierda |
| Q10 | - |  |  | SI | Cadera Derecha |
| Q11 | - |  |  | SI | Rodilla izquierda |
| Q12 | - |  |  | SI | Rodilla Derecha |
| Q13 | - |  |  | SI | Tobillo Izquierdo |
| Q14 | - |  |  | SI | Tobillo Derecho |
| Q15 | - |  |  | SI | Pie Izquierdo |
| Q16 | - |  |  | SI | Pie Derecho |
| Q17 | - |  |  | SI | Comentarios |
| Q18 | - |  |  | SI | Escala de Disfuncion Motora (Sensibilida) |
| Q19 | - |  |  | SI | Resultado |
| Q20 | - |  |  | SI | Profesional de Salud |
| Q21 | - |  |  | SI | M0: Sin pruebas de contractilidad, espasmo o espas... |
| Q22 | - |  |  | SI | M1: Manisfestaciones ligeras de contractilidad |
| Q23 | - |  |  | SI | M2: Movimiento en toda su amplitud al suprimir la ... |
| Q24 | - |  |  | SI | M3: Arco completo de movimiento contra la acción d... |
| Q25 | - |  |  | SI | M4: Arco completo de Movimiento contra la acción d... |
| Q26 | - |  |  | SI | M5: Arco completo de movimiento contra la acción d... |
| Q27 | - |  |  | SI | 0: Inmovilidad |
| Q28 | - |  |  | SI | 1: Vestigios |
| Q29 | - |  |  | SI | 2: Malo |
| Q30 | - |  |  | SI | 3: Regular |
| Q31 | - |  |  | SI | 4: Bueno |
| Q32 | - |  |  | SI | 5: Normal |
| Q33 | - |  |  | SI | Puntaje |
| Q34 | - |  |  | SI | Resultado |
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